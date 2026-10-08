---
name: bloom-lektie
description: "Laver 3 overkommelige lektiespørgsmål på Huske/Forstå-niveau til en fagtekst, så eleverne kan forberede sig hjemme og læreren kan lave et lektietjek. Brug når læreren siger \"lektiespørgsmål\", \"lektietjek\", \"hvad skal de forberede\", \"lav lige 3 nemme spørgsmål til i morgen\". Brug ikke til et fuldt sæt arbejdsspørgsmål (bloom-bloom), åbne diskussionsspørgsmål eller quizzer (blooket)."
argument-hint: "[fagtekst eller emne]"
allowed-tools:
  - Read
  - Glob
---

# Lektiespørgsmål

Lav overkommelige lektiespørgsmål som eleverne kan forberede hjemme og som kan bruges som lektietjek i starten af timen.

## Brug

Giv mig en tekst og eventuelt ønsket antal (default: 3). Jeg laver spørgsmål der:

- Ligger på **Huske/Forstå**-niveau
- Dækker tekstens vigtigste indhold
- Kan besvares på 5-7 minutter samlet
- Har Bloom-niveau og videnstype angivet

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../bloom-arbejdsspoergsmaal/SKILL.md` for spørgsmålsregler.
2. **Identificér kernestof:** Hvad skal eleven mindst have forstået for at kunne følge timen?

### Gate: Bekræft kernestof — VENT på OK

Re-ground: "Jeg har læst teksten og identificeret de vigtigste begreber. Her er hvad jeg vil teste i lektietjekket."

Præsentér de 3-5 vigtigste begreber/pointer fra teksten og spørg:
"Er det disse begreber du vil teste i lektietjekket? Eller vil du prioritere anderledes?"

**VENT** på svar.

Giv en anbefaling: "Jeg anbefaler at vi fokuserer på [X, Y, Z] fordi det er de begreber der er mest centrale for tekstens hovedpointe."

3. **Formulér spørgsmål** på Huske/Forstå-niveau med konkrete spørgeord.
4. **Angiv metadata** (Bloom-niveau + videnstype) for hvert spørgsmål.

## Eksempel output

**1. Hvad er de fire friheder i EU's indre marked?**
*(Huske, faktuel viden)*

**2. Hvorfor var afskaffelsen af de tekniske handelshindringer særligt vigtig for et fungerende indre marked?**
*(Forstå, konceptuel viden)*

**3. Hvilken fordel ved arbejdskraftens frie bevægelighed fremhæver teksten mest?**
*(Forstå, faktuel viden)*

---

## Completion Status

- **DONE** — Lektiespørgsmål leveret med metadata
- **DONE_WITH_CONCERNS** — Leveret, men kernestoffet var svært at afgrænse
- **NEEDS_CONTEXT** — Mangler information om hvad eleverne har arbejdet med før
