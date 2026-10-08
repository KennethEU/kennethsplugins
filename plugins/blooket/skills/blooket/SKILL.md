---
name: blooket
description: Generér en Blooket-quiz fra undervisningsmateriale som importklar CSV-fil. Brug når læreren siger "lav en Blooket", "quiz til Blooket", "multiple choice", "quizspørgsmål", eller uploader materiale og vil have det omdannet til en importklar Blooket-quiz.
argument-hint: "[emne eller materiale]"
allowed-tools:
  - Read
  - Glob
  - Bash
  - Write
---

# Blooket-quiz

Lav en Blooket-quiz. Brug din `blooket-quiz` skill til at følge det korrekte format.

**Input:** $ARGUMENTS

## Trin

1. Hvis brugeren har uploadet materiale (billeder, PDF, tekst, slides), læs det og identificér de centrale begreber, fakta og sammenhænge.
2. Hvis brugeren kun har angivet et emne, brug din faglige viden til at formulere spørgsmål.

### Gate 1: Bekræft begreber — VENT på OK

Re-ground: "Jeg har læst materialet og fundet de centrale begreber. Her er hvad jeg vil teste i quizzen."

Præsentér de identificerede begreber:

- **Centrale begreber:** [8-10 nøglebegreber fra materialet]
- **Foreslået antal spørgsmål:** [10-15]
- **Sværhedsgrad:** [Let / medium / svær]

Spørg: "Er det de rigtige begreber at teste? Skal sværhedsgraden op eller ned?"

Giv en anbefaling: "Jeg anbefaler [X] spørgsmål på [niveau] fordi [begrundelse — fx passer til pensum og Blooket-formatet]."

**VENT** på svar.

### Gate 2: Preview — VENT på OK

Re-ground: "Vi er ved **Gate 2** — her er et par eksempelspørgsmål så du kan vurdere stil og sværhedsgrad."

Vis **3-4 eksempelspørgsmål** med svarmuligheder, så læreren kan vurdere format og sværhedsgrad.

Spørg: "Passer stilen? Skal spørgsmålene være mere/mindre detaljerede?"

**VENT** på OK.

### Generér og levér

3. Formulér alle spørgsmål med 2-4 svarmuligheder. Randomisér placeringen af det korrekte svar. Bland viden-, forståelses- og anvendelsesspørgsmål.
4. Generér en Blooket-importklar CSV-fil ved at bruge `${CLAUDE_SKILL_DIR}/../blooket-quiz/references/generate_csv.py`.
5. Gem filen og levér den til brugeren.

Svar på dansk.

---

## Completion Status

- **DONE** — Blooket-quiz genereret som CSV-fil
- **DONE_WITH_CONCERNS** — Genereret, men nogle spørgsmål har kun 2 svarmuligheder
- **NEEDS_CONTEXT** — Mangler materiale eller emne at lave quiz fra
