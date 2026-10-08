---
name: rollespil-sprogkvalitet-da
description: "Dansk sproglig kvalitetssikring for undervisningsmaterialer. Brug denne skill ved ENHVER produktion af danske dokumenter — rollekort, lærerguider, elevintroduktioner, opgaveformuleringer, quizzer, artikeludklip eller andre materialer til dansk gymnasieundervisning. Trigger ved 'sprogcheck', 'retskrivning', 'korrektur', 'dansk tekst', eller automatisk som sidste trin i materialeproduktion. Skillen fanger de fejl der oftest slipper igennem: sammensatte ord, person-perspektiv, æøå, forkert genus, og fagterm-inkonsistens."
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Dansk sproglig kvalitetssikring

**Projektregler:** `rollespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill er en systematisk tjekliste for danske undervisningsmaterialer. Kør den som sidste trin FØR levering.

## Kendte faldgruber (fejl der slipper igennem igen og igen)

### 1. Æ, Ø, Å

Claude erstatter ofte danske specialtegn med ASCII-approximationer. Tjek ALTID:

| Forkert | Korrekt |
|---------|---------|
| "ae" | "æ" |
| "oe" | "ø" |
| "aa" (i moderne dansk) | "å" |
| "vaere" | "være" |
| "naaede" | "nåede" |
| "raekke" | "række" |
| "oekonomisk" | "økonomisk" |
| "foerste" | "første" |

### 2. Sammensatte ord

Dansk sammensætter ord UDEN mellemrum. Hyppige fejl:

| Forkert | Korrekt |
|---------|---------|
| "fattigdoms grænse" | "fattigdomsgrænse" |
| "klima forandringer" | "klimaforandringer" |
| "budget forhandling" | "budgetforhandling" |
| "stemme vægt" | "stemmevægt" |
| "rolle kort" | "rollekort" |
| "gruppe arbejde" | "gruppearbejde" |
| "arbejds løshed" | "arbejdsløshed" |
| "velfærds stat" | "velfærdsstat" |
| "forhandlings runde" | "forhandlingsrunde" |

**Regel:** Hvis to substantiver danner ét begreb, skrives de som ét ord.

### 3. Person-perspektiv i rollekort

| Felt | Skal være | Eksempel |
|------|-----------|----------|
| Baggrund | 2. person | "Du er afdelingsdirektør..." |
| Argumenter | 1. person | "Mine data viser..." |
| Dilemmaer | 2. person | "Skal du støtte Henrik...?" |
| Tip | 2. person imperativ | "Brug din vetoret..." |
| Skjult info | 2. person | "Du ved at budgettet..." |

**Tjek:** Scan hvert felt for perspektiv-blanding. Det er den hyppigste strukturfejl i rollekort.

### 4. Genus og artikel

| Forkert | Korrekt | Regel |
|---------|---------|-------|
| "et gruppe" | "en gruppe" | Fælleskøn |
| "en budget" | "et budget" | Intetkøn |
| "din budget" | "dit budget" | Intetkøn possessiv |
| "en forslag" | "et forslag" | Intetkøn |
| "et krise" | "en krise" | Fælleskøn |

### 5. Bestemt artikel ved institutioner

| Forkert | Korrekt |
|---------|---------|
| "finansministeriet har besluttet" | "Finansministeriet har besluttet" |
| "EU kommissionen" | "EU-Kommissionen" |
| "folketinget" (i sætningsstart) | "Folketinget" |

### 6. Specifikke termer

| Forkert | Korrekt | Note |
|---------|---------|------|
| "max." | "maks." | Dansk forkortelse |
| "a 4-5 elever" | "à 4-5 elever" | Accent grave |
| "iflg." | "ifølge" eller "iflg." | Konsistens |
| "dvs" | "dvs." | Punktum efter forkortelse |
| "f.eks" | "fx" eller "f.eks." | Vælg én form og hold fast |
| "%" uden mellemrum | "%" med mellemrum før | "60 %" ikke "60%" |

### 7. Ufuldstændige sætninger

Scan for sætninger der mangler verbum eller subjekt — især i bullet points og tabeller. Hvert punkt i et rollekort skal være en fuldstændig sætning (undtagen i stærk-versionen, der bevidst bruger stikord).

### 8. Fagterm-konsistens

Vælg én term og hold fast HELE vejen:

| Inkonsistent | Konsistent |
|-------------|-----------|
| "deliberation" / "deliberativ samtale" / "deliberativt demokrati" | Vælg én — og brug den alle steder |
| "Phillips-kurven" / "Phillipskurven" | Vælg én stavemåde |
| "stakeholder" / "interessent" | Vælg dansk eller engelsk — ikke begge |

## Kør scriptet først

`scripts/sprogtjek.py` finder de mekaniske fejl deterministisk (tankestreger, ae/oe/aa, delte sammensatte ord, ritualsætninger, `maks.`, `à`, `60 %`, minuttal, blandede fagtermer). Det læser .docx, .md og .html uden ekstra pakker:

```
python3 scripts/sprogtjek.py <fil-eller-mappe>
```

Når scriptet er kørt og fejlene rettet, gennemgår du selv det, en regel ikke kan afgøre: person-perspektiv, genus, ufuldstændige sætninger og valg af fagterm.

## Systematisk tjek-rækkefølge

1. **Æ, ø, å** — søg efter kendte ASCII-erstatninger
2. **Sammensatte ord** — scan for substantiver med mellemrum
3. **Person-perspektiv** — tjek hvert felt i rollekort separat
4. **Genus** — tjek artikel + possessiv for hvert substantiv
5. **Institutionsnavne** — tjek stort begyndelsesbogstav + bindestreg
6. **Specifikke termer** — maks., à, fx, %
7. **Fuldstændige sætninger** — scan alle bullet points
8. **Fagterm-konsistens** — vælg én form pr. begreb

## Output

Rapportér som:

```
SPROGCHECK: [Dokumentnavn]

✅ Æ, ø, å: OK
❌ Sammensatte ord: "budget forhandling" (s. 2), "rolle kort" (s. 3)
✅ Person-perspektiv: OK
⚠️ Genus: "din budget" → "dit budget" (rollekort 3)
✅ Institutionsnavne: OK
❌ Termer: "max." → "maks." (3 forekomster)
✅ Fuldstændige sætninger: OK
⚠️ Konsistens: "stakeholder" (s. 1) vs. "interessent" (s. 4)

RETTELSER: [antal] fejl fundet
```

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Sprogcheck gennemført, ingen fejl fundet (eller alle fejl rettet)
- **DONE_WITH_CONCERNS** — Sprogcheck gennemført, men med advarsler (fx: fagterm-inkonsistens der kræver lærerens valg)
- **BLOCKED** — Kan ikke gennemføre sprogcheck (fx: materiale mangler eller er i forkert format)
- **NEEDS_CONTEXT** — Mangler information (fx: "Hvilken form vil du bruge — 'stakeholder' eller 'interessent'?")
