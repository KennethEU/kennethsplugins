---
name: bloom-lektiespoergsmaal
description: "Laver 3 overkommelige lektiespørgsmål på Huske/Forstå-niveau til en fagtekst, så eleverne kan forberede sig hjemme og læreren kan lave et lektietjek. Brug når læreren siger \"lektiespørgsmål\", \"lektietjek\", \"hvad skal de forberede\", \"lav lige 3 nemme spørgsmål til i morgen\". Brug ikke til et fuldt sæt arbejdsspørgsmål (bloom-spoergsmaal-til-tekst), åbne diskussionsspørgsmål eller quizzer (pluginet blooket)."
argument-hint: "[fagtekst eller emne]"
allowed-tools:
  - Read
  - Glob
  - Write
---

# Lektiespørgsmål

Lav overkommelige lektiespørgsmål, som eleverne kan forberede hjemme, og som kan bruges som lektietjek i starten af timen.

**Skal kendes:** teksten. Har du den ikke, så bed om den eller om et kort resumé, og stop. Følg "Arbejdsgang" i `bloom-spoergsmaalsregler`.

Spørgsmålene:

- ligger på **Huske/Forstå**
- dækker tekstens vigtigste indhold
- kan besvares på 5 til 7 minutter samlet
- har Bloom-niveau og videnstype angivet

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/SKILL.md` for spørgsmålsregler.
2. **Find kernestoffet:** Hvad skal eleven mindst have forstået for at kunne følge timen? Vælg de tre vigtigste begreber eller pointer.
3. **Formulér 3 spørgsmål** (eller det antal, læreren beder om) på Huske/Forstå med konkrete spørgeord.
4. **Angiv metadata** (Bloom-niveau og videnstype) for hvert spørgsmål.
5. **Afprøv spørgsmålene på teksten** stille, jf. "Afprøvning på teksten" i reglerne. Lektiespørgsmål får alle tre tests: facit-test, elevtest og ikke-læst-test. Eleven sidder alene med teksten, så et spørgsmål, der kun er rigtigt formuleret, er ikke nok. Ret det, der falder, før du afleverer.

Beder læreren bagefter om færre spørgsmål, en omformulering eller en sammenlægning, så afprøv de nye spørgsmål igen, før du svarer.

## Sådan afleverer du

Der er ingen gate, og du spørger ikke, om det skal være hurtigt eller grundigt. Tre spørgsmål er hurtigere at rette bagefter end at godkende på forhånd.

- Én linje øverst: "Fokus: [X, Y og Z]."
- Spørgsmålene.
- Kun hvis afprøvningen efterlod en tvivl, du ikke kunne afgøre: én linje om den, fx et antal, der afhænger af, hvordan teksten læses.
- Én linje til sidst: "Sig til, hvis fokus skal flyttes, eller du vil have flere eller facit til lektietjekket."

Beder læreren om sparring om, hvad lektietjekket skal teste, så vis de 3 til 5 vigtigste begreber med din anbefaling, og **VENT** på svar, før du skriver spørgsmålene.

## Eksempel på output

Fokus: de fire friheder, tekniske handelshindringer og arbejdskraftens frie bevægelighed.

**1. Hvad er de fire friheder i EU's indre marked?**
*(Huske, faktuel viden)*

**2. Hvorfor var afskaffelsen af de tekniske handelshindringer særligt vigtig for et fungerende indre marked?**
*(Forstå, konceptuel viden)*

**3. Hvilken fordel ved arbejdskraftens frie bevægelighed fremhæver teksten mest?**
*(Forstå, faktuel viden)*

---

## Completion Status

- **DONE**: Lektiespørgsmål leveret med metadata og afprøvet på teksten
- **DONE_WITH_CONCERNS**: Leveret, men kernestoffet var svært at afgrænse, eller et svar kunne ikke afgøres sikkert ud fra teksten
- **NEEDS_CONTEXT**: Mangler teksten
