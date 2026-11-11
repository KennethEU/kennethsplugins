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
- kan besvares på 5 til 7 minutter samlet, når der er 3. Beder læreren om flere, så regn med ca. 2 minutter pr. spørgsmål
- har Bloom-niveau og videnstype angivet

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/SKILL.md` for spørgsmålsregler.
2. **Find kernestoffet:** Hvad skal eleven mindst have forstået for at kunne følge timen? Vælg de tre vigtigste begreber eller pointer.
3. **Formulér 3 spørgsmål** (eller det antal, læreren beder om) på Huske/Forstå med konkrete spørgeord.
4. **Angiv metadata** (Bloom-niveau og videnstype) for hvert spørgsmål.
5. **Afprøv spørgsmålene på teksten,** jf. "Afprøvning på teksten" i reglerne. Afprøvningen er ikke stille: den efterlader facit og en udfaldslinje i svaret. Lektiespørgsmål får alle tre tests: facit-test, elevtest og ikke-læst-test. Eleven sidder alene med teksten, så et spørgsmål, der kun er rigtigt formuleret, er ikke nok. Ret det, der falder, før du afleverer. Finder du ikke et Forstå-spørgsmål, eleven kan svare på alene uden at skrive af, så aflever Huske-spørgsmål, og sig det i én linje.

Beder læreren bagefter om færre spørgsmål, en omformulering eller en sammenlægning, så afprøv de nye spørgsmål igen, før du svarer.

## Sådan afleverer du

Der er ingen gate, og du spørger ikke, om det skal være hurtigt eller grundigt. Tre spørgsmål er hurtigere at rette bagefter end at godkende på forhånd.

- Én linje øverst: "Fokus: [X, Y og Z]. Lektien: ca. [N] min. læsning og [M] min. til spørgsmålene." Regn tiden efter "Tid: arbejdsregler" i reglerne. Kan du ikke tælle ordene i teksten, så skriv kun tiden til spørgsmålene.
- Spørgsmålene, hvert med facit og sted i teksten under sig: "Svar: ... (side 3)". Læreren bruger facit til lektietjekket.
- Udfaldslinjen fra afprøvningen, jf. "Afprøvningen efterlader et spor" i reglerne.
- Én linje til sidst: "Sig til, hvis fokus skal flyttes, eller du vil have flere eller elevernes typiske svar."

Beder læreren om sparring om, hvad lektietjekket skal teste, så vis de 3 til 5 vigtigste begreber med din anbefaling, og **VENT** på svar, før du skriver spørgsmålene.

## Eksempel på output

Fokus: de fire friheder, tekniske handelshindringer og arbejdskraftens frie bevægelighed. Lektien: ca. 12 min. læsning og 6 min. til spørgsmålene.

**1. Hvilke fire friheder bygger EU's indre marked på?**
*(Huske, faktuel viden)*
Svar: fri bevægelighed for varer, tjenesteydelser, kapital og arbejdskraft (første afsnit).

**2. Hvorfor var det ikke nok at fjerne tolden for at få et fungerende indre marked?**
*(Forstå, konceptuel viden)*
Svar: forskellige nationale krav til varer virkede som handelshindringer, selv uden told (afsnittet om tekniske handelshindringer).

**3. Hvilken fordel ved arbejdskraftens frie bevægelighed fremhæver teksten mest?**
*(Huske, faktuel viden)*
Svar: virksomheder kan lettere få den arbejdskraft, de mangler (sidste afsnit).

Afprøvet som middelmådig elev: 1 holder, 2 rettet (kunne skrives af), 3 holder, men er Huske og ikke Forstå.

Sig til, hvis fokus skal flyttes, eller du vil have flere eller elevernes typiske svar.

---

## Completion Status

- **DONE**: Lektiespørgsmål leveret med metadata og afprøvet på teksten
- **DONE_WITH_CONCERNS**: Leveret, men kernestoffet var svært at afgrænse, eller et svar kunne ikke afgøres sikkert ud fra teksten
- **NEEDS_CONTEXT**: Mangler teksten
