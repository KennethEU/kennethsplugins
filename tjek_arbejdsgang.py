#!/usr/bin/env python3
"""Tjekker, at afsnittet "Arbejdsgang" er ens i alle principfiler.

Afsnittene "Hurtig eller grundig" og "Kort som standard" skal stå ordret ens i de
fem plugins, så skillene opfører sig ens. Kør: python3 tjek_arbejdsgang.py
"""
import glob, sys

START, SLUT = "### Hurtig eller grundig", "### Forløbsmappen"
filer = sorted(
    f for f in glob.glob("plugins/*/skills/*/SKILL.md")
    if "## Arbejdsgang: hurtigt, kort og samlet" in open(f, encoding="utf-8").read()
)
udsnit = {}
for f in filer:
    t = open(f, encoding="utf-8").read()
    udsnit[f] = t[t.index(START):t.index(SLUT)]

if len(filer) < 5:
    sys.exit(f"FEJL: fandt kun afsnittet i {len(filer)} filer, forventede 5")
reference = udsnit[filer[0]]
afvigere = [f for f in filer if udsnit[f] != reference]
if afvigere:
    sys.exit("FEJL: afsnittet afviger fra " + filer[0] + " i:\n  " + "\n  ".join(afvigere))
print(f"OK: Arbejdsgang er ens i {len(filer)} filer")
