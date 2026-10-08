---
name: planlaeg-time
description: "Planlægger en tre-faset time med lektietjek, arbejdsspørgsmål i par eller grupper og afsluttende diskussion, med Bloom-progression og arbejdsformer. Brug når læreren siger \"planlæg en time\", \"klasseflow\", \"lektionsstruktur\", \"tre faser\", \"hvad skal vi lave i timen\" ud fra en fagtekst. Brug ikke til rollespil, gruppearbejdsdagsordener eller et sæt spørgsmål uden timeplan (spoergsmaal-til-tekst)."
argument-hint: "[fagtekst, emne eller tidsramme]"
allowed-tools:
  - Read
  - Glob
---

# Klasseflow: tre-faset undervisningsstruktur

Planlæg en hel undervisningstime med lektietjek, gruppearbejde og afsluttende diskussion.

## Standardstruktur

| Fase | Tid | Indhold | Bloom-niveau | Arbejdsform |
|------|-----|---------|--------------|-------------|
| 1. Lektietjek | 5-7 min | 3 spørgsmål | Huske/Forstå | Plenum |
| 2. Arbejde | 15-20 min | 3-4 spørgsmål | Anvende/Analysere | Par/grupper |
| 3. Diskussion | 5-10 min | 1 spørgsmål | Evaluere/Skabe | Klasse |

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../spoergsmaalsregler/SKILL.md`.

### Gate 1: Afklar kontekst — VENT på svar

Re-ground: "Vi planlægger en time med Bloom-progression. Jeg har et par spørgsmål om rammerne."

Stil disse spørgsmål (spring over dem læreren allerede har besvaret):

1. **Tid:** Hvor lang tid har du? (30, 45, 90 min?)
2. **Energi:** Er det en frisk klasse eller fredag eftermiddag?
3. **Forberedelse:** Har eleverne læst noget hjemme?
4. **Fokus:** Er der et bestemt læringsmål eller begreb du prioriterer?

**VENT** på svar.

### Gate 2: Præsentér struktur — VENT på OK

Re-ground: "Vi er ved **Gate 2** — her er mit forslag til timestruktur baseret på dine rammer."

Tilpas standardstrukturen til konteksten:
- **Kort tid (30 min):** Reducér fase 2 til 2 spørgsmål
- **Helt modul (90 min):** Udvider fase 2 + tilføjer aktivitet
- **Fredag/lav energi:** Gør fase 2 mere aktiverende (case, debat, design)

Præsentér den tilpassede struktur som tabel:

| Fase | Tid | Aktivitet | Bloom | Arbejdsform |
|------|-----|-----------|-------|-------------|
| 1 | [X] min | [Beskrivelse] | [Niveau] | [Form] |
| 2 | [X] min | [Beskrivelse] | [Niveau] | [Form] |
| 3 | [X] min | [Beskrivelse] | [Niveau] | [Form] |

Giv en anbefaling: "Jeg anbefaler denne fordeling fordi [begrundelse — fx balancerer tid/energi, passer til forberedelsesniveau]."

Spørg: "Passer strukturen? Skal nogen faser have mere/mindre tid, eller skal arbejdsformen ændres?"

**VENT** på OK.

### Generér spørgsmål

2. **Fase 1:** 3 spørgsmål på Huske/Forstå der afdækker om eleverne har læst.
3. **Fase 2:** 3-4 spørgsmål på Anvende/Analysere til par/gruppearbejde.
4. **Fase 3:** 1 åbent spørgsmål på Evaluere/Skabe til klassediskussion.
5. **Kvalitetstjek:** Bygger faserne logisk på hinanden? Er Bloom-progressionen tydelig?

Afslut med: "Vil du justere noget — fx et bestemt spørgsmål, tidsfordelingen, eller arbejdsformen?"

---

## Completion Status

- **DONE** — Tre-faset timestruktur med spørgsmål leveret
- **DONE_WITH_CONCERNS** — Leveret, men tidsrammen er stram for alle tre faser
- **NEEDS_CONTEXT** — Mangler information om tid eller elevernes forberedelse
