#!/usr/bin/env python3
"""Deterministisk sprogtjek af casespilsmaterialer (kun standardbiblioteket).

Brug:
    python3 sprogtjek.py <fil-eller-mappe> [<fil-eller-mappe> ...]

Læser .docx, .md, .txt og .html. Rapporterer fejl (F) og advarsler (A) med
filnavn, linjenummer og forslag. Afslutter med kode 1, hvis der er fejl.

Dækker kun det, en regel kan afgøre sikkert. Person-perspektiv, genus,
ufuldstændige sætninger og fagterm-valg kræver stadig et menneskeligt/modelblik.
"""
import re
import sys
import zipfile
from pathlib import Path

EXTS = {".docx", ".md", ".txt", ".html", ".htm"}

# (regex, forslag, niveau)  F = fejl, A = advarsel
RULES = [
    (r"[—–]", "tankestreg: brug komma, kolon, punktum eller parentes", "F"),
    (r"\b(?:vaer\w*|vaere\w*|oekonom\w*|foerst\w*|raekke\w*|naaed\w*|hoej\w*|stoerr\w*|"
     r"soeg\w*|loes\w*|bl[aå]aa\w*|maaske|baade|paa|saa|faar|gaar|staar|laerer\w*|skoele\w*)\b",
     "ASCII i stedet for æ, ø, å", "F"),
    (r"\bmax\.", "skriv 'maks.'", "F"),
    (r"\b[Gg]rupper? a \d", "skriv 'à' (accent grave)", "F"),
    (r"\d+%", "skriv mellemrum før %: '60 %'", "F"),
    (r"\bdvs\b(?!\.)", "skriv 'dvs.'", "F"),
    (r"\bf\.eks\b(?!\.)", "skriv 'fx' eller 'f.eks.'", "F"),
    (r"\bI spiller en rolle\b|\btræd ud af rollen\b|\bI er nu jer selv\b|\bsig dem højt\b",
     "ritualsætning (projektregel 1)", "F"),
    (r"\b\d+\s*(?:min\.?|minutter|minut)\b", "fast minuttal (projektregel 3). OK kun hvis det er en forklaring og ikke en tidsangivelse til eleverne", "A"),
    (r"\b(?:finansministeriet|folketinget|kommissionen|statsministeriet)\b",
     "institutionsnavn med småt: stort begyndelsesbogstav, hvis det er et egennavn", "A"),
]

SPLIT_COMPOUNDS = [
    "fattigdoms grænse", "klima forandringer", "budget forhandling", "stemme vægt",
    "rolle kort", "gruppe arbejde", "arbejds løshed", "velfærds stat",
    "forhandlings runde", "lærer guide", "elev introduktion", "rolle spil",
]

TERM_PAIRS = [("stakeholder", "interessent"), ("Phillips-kurven", "Phillipskurven")]


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", "replace")
        xml = re.sub(r"</w:p>", "\n", xml)
        xml = re.sub(r"<w:tab/>", " ", xml)
        text = re.sub(r"<[^>]+>", "", xml)
        for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'")):
            text = text.replace(a, b)
        return text
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in {".html", ".htm"}:
        text = re.sub(r"<(script|style)\b.*?</\1>", "", text, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", "", text)
    return text


def check(path: Path):
    findings = []
    text = read_text(path)
    for n, line in enumerate(text.splitlines(), 1):
        line = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)  # kode og filnavne i backticks er ikke prosa
        for pattern, hint, level in RULES:
            for m in re.finditer(pattern, line, flags=re.I if level == "F" and "ASCII" in hint else 0):
                findings.append((level, n, m.group(0), hint))
        for comp in SPLIT_COMPOUNDS:
            if comp in line.lower():
                findings.append(("F", n, comp, f"sammensat ord: skriv '{comp.replace(' ', '')}'"))
    low = text.lower()
    for a, b in TERM_PAIRS:
        if a.lower() in low and b.lower() in low:
            findings.append(("A", 0, f"{a} / {b}", "begge former bruges: vælg én"))
    return findings


def collect(args):
    for a in args:
        p = Path(a)
        if p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.suffix.lower() in EXTS and "_arkiv" not in f.parts and not f.name.startswith("~$"):
                    yield f
        elif p.suffix.lower() in EXTS:
            yield p


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    errors = warnings = files = 0
    for f in collect(sys.argv[1:]):
        files += 1
        try:
            findings = check(f)
        except Exception as e:  # ødelagt eller ulæselig fil
            print(f"{f}: kunne ikke læses ({e})")
            errors += 1
            continue
        for level, n, hit, hint in findings:
            loc = f"linje {n}" if n else "hele filen"
            print(f"{'FEJL' if level == 'F' else 'ADVARSEL'}  {f}  ({loc})  \"{hit}\"  {hint}")
            errors += level == "F"
            warnings += level == "A"
    print(f"\n{files} fil(er) tjekket: {errors} fejl, {warnings} advarsler")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
