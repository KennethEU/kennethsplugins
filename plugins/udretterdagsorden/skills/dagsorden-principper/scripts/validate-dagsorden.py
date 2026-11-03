#!/usr/bin/env python3
"""
validate-dagsorden.py

Validerer en udretterdagsorden i JSON-format mod kvalitetskriterierne.
Returnerer exit 0 ved OK, exit 2 ved fejl (kompatibelt med Cowork hooks).

Brug:
  python3 validate-dagsorden.py dagsorden.json
"""

import json
import sys


def normalize(data):
    """Normaliser fra nyt (engelsk) eller gammelt (dansk) format til internt format."""
    roles = data.get("roles") or data.get("roller", [])
    steps = data.get("steps") or data.get("trin", [])
    normalized_steps = []
    for i, t in enumerate(steps):
        instruction = t.get("instruction") or t.get("instruktion") or t.get("hvordan", "")
        doc_instr = t.get("docInstruction") or t.get("docInstruktion", "")
        if doc_instr and not t.get("hvordan"):
            instruction += '\n\n' + doc_instr
        normalized_steps.append({
            "nr": t.get("nr", i + 1),
            "type": t.get("type", "normal"),
            "hvad": t.get("heading") or t.get("overskrift") or t.get("hvad", ""),
            "hvordan": instruction,
            "obs": t.get("note") or t.get("obs", ""),
            "docInstruktion": doc_instr if t.get("hvordan") else "",
            "tid": t.get("duration") or t.get("tid", 0),
        })
    return {
        "emne": data.get("title") or data.get("topic") or data.get("titel") or data.get("emne", ""),
        "fag": data.get("subject") or data.get("fag", ""),
        "klasse": data.get("klasse", ""),
        "total_tid": data.get("totalTime") or data.get("totalTid") or data.get("total_tid", 0),
        "roller": roles,
        "trin": normalized_steps,
    }


def validate(raw_data):
    data = normalize(raw_data)
    errors = []
    warnings = []

    # ── Obligatoriske topfelter ──
    for field in ["emne", "fag", "total_tid", "roller", "trin"]:
        if not data.get(field):
            errors.append(f"Mangler obligatorisk felt: '{field}'")

    if errors:
        return errors, warnings  # Kan ikke validere videre

    # ── Roller ──
    if len(data["roller"]) != 3:
        errors.append(f"Der skal være præcis 3 roller, fandt {len(data['roller'])}")

    rollenavne = [r.get("navn", "") for r in data["roller"]]
    for expected in ["Pas-på-tur", "Pas-på-tid", "Pas-på-doc"]:
        if expected not in rollenavne:
            errors.append(f"Mangler rolle: {expected}")

    for rolle in data["roller"]:
        if not rolle.get("beskrivelse"):
            errors.append(f"Rolle '{rolle.get('navn', '?')}' mangler beskrivelse")

    # ── Trin-validering ──
    trin = data["trin"]
    if not trin:
        errors.append("Ingen trin i dagsordenen")
        return errors, warnings

    # Trin 1 skal være rollevalg
    if trin[0].get("hvad", "").lower().find("roller") == -1:
        warnings.append("Trin 1 er normalt rollevalg — overvej om det mangler")

    if trin[0].get("tid", 0) > 4:
        errors.append(f"Rollevalg bruger {trin[0]['tid']} min — max 4 min")

    # ── Tidsvalidering ──
    total_declared = data["total_tid"]
    total_actual = sum(t.get("tid", 0) for t in trin)

    if total_actual != total_declared:
        errors.append(
            f"Tider stemmer ikke: trin summer til {total_actual} min, "
            f"men total_tid er {total_declared} min"
        )

    # Hele minutter
    for t in trin:
        tid = t.get("tid", 0)
        if tid != int(tid):
            errors.append(f"Trin {t.get('nr', '?')}: tid skal være hele minutter (fandt {tid})")

    # ── Pause ──
    has_pause = any(t.get("type") == "pause" for t in trin)
    if total_declared > 25 and not has_pause:
        errors.append(f"Dagsorden er {total_declared} min men mangler pause (påkrævet over 25 min)")

    if has_pause:
        pause_trin = [t for t in trin if t.get("type") == "pause"]
        for p in pause_trin:
            if p.get("tid", 0) != 5:
                warnings.append(f"Pause er {p['tid']} min — standard er 5 min")

    # ── Individuel fase før gruppefase ──
    found_individual = False
    found_group_before_individual = False
    individual_keywords = ["tavshed", "individuel", "skim", "læs i", "tavs", "stilhed", "eget dokument"]
    group_keywords = ["præsenter", "på tur", "fælles", "diskuter", "sammenlign"]

    for t in trin[1:]:  # Spring rollevalg over
        if t.get("type") == "pause":
            continue
        hvordan = t.get("hvordan", "").lower()
        is_individual = any(kw in hvordan for kw in individual_keywords)
        is_group = any(kw in hvordan for kw in group_keywords)

        if is_individual:
            found_individual = True
        if is_group and not found_individual:
            found_group_before_individual = True
            break

    if found_group_before_individual:
        warnings.append("Gruppefase før individuel fase — overvej individuel tænketid først")

    # ── Pas-på-doc nævnt ──
    for t in trin:
        if t.get("type") == "pause":
            continue
        if t.get("nr", 0) == 1:
            continue  # Rollevalg

        hvordan = t.get("hvordan", "").lower()
        doc_instruktion = t.get("docInstruktion", "")
        has_doc_ref = (
            "pas-på-doc" in hvordan
            or "doc" in hvordan
            or bool(doc_instruktion)
        )

        # Trin med præsentation eller fælles arbejde bør nævne doc
        needs_doc = any(kw in hvordan for kw in ["præsenter", "på tur", "fælles", "sammenlign", "skriv"])
        if needs_doc and not has_doc_ref:
            warnings.append(
                f"Trin {t.get('nr', '?')} ('{t.get('hvad', '')}') "
                f"involverer gruppeproduktion men nævner ikke pas-på-doc"
            )

    # ── Nr-sekvens (kun check at numre er sekventielle) ──
    nrs = [t.get("nr", 0) for t in trin]
    expected_nrs = list(range(1, len(trin) + 1))
    if nrs != expected_nrs:
        errors.append(f"Trinumre er ikke sekventielle: {nrs} (forventet: {expected_nrs})")

    # ── Type-felt ──
    for t in trin:
        if t.get("type") not in ("normal", "pause", "individuel"):
            errors.append(f"Trin {t.get('nr', '?')}: ukendt type '{t.get('type', 'MANGLER')}'")

    # ── OBS prefix ──
    for t in trin:
        obs = t.get("obs", "") or ""
        if obs.startswith("OBS:") or obs.startswith("OBS "):
            warnings.append(
                f"Trin {t.get('nr', '?')}: note-feltet starter med 'OBS:' — "
                f"prefix tilføjes automatisk af scriptet, fjern det fra JSON"
            )

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Brug: python3 validate-dagsorden.py <fil.json>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"❌ Kunne ikke læse {path}: {e}", file=sys.stderr)
        sys.exit(2)

    errors, warnings = validate(data)

    # Output
    if warnings:
        for w in warnings:
            print(f"⚠️  {w}")

    if errors:
        for e in errors:
            print(f"❌ {e}", file=sys.stderr)
        print(f"\n{len(errors)} fejl, {len(warnings)} advarsler", file=sys.stderr)
        sys.exit(2)
    else:
        normalized = normalize(data)
        total = normalized.get("total_tid", "?")
        trin_count = len(normalized.get("trin", []))
        print(f"✅ OK: {trin_count} trin, {total} min, {len(warnings)} advarsler")
        sys.exit(0)


if __name__ == "__main__":
    main()
