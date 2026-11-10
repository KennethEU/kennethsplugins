---
name: bloom-spoergsmaal-til-tekst
description: "Laver et sæt arbejdsspørgsmål til en fagtekst efter Blooms taksonomi: som standard ét sæt i taksonomisk progression, og på opfordring også tekstnær version afsnit for afsnit og taxonomy table. Brug når læreren siger \"lav arbejdsspørgsmål\", \"spørgsmål til denne tekst\", \"Bloom-spørgsmål\", \"analyser teksten med Bloom\", eller uploader en fagtekst og vil have spørgsmål. Brug ikke til kun lektiespørgsmål (bloom-lektiespoergsmaal), kun skabe-spørgsmål (bloom-skabe-opgaver), vurdering af eksisterende spørgsmål (bloom-vurder-spoergsmaal), timeplanlægning (bloom-planlaeg-time), quizzer (pluginet blooket) eller eksamensspørgsmål med bilag."
argument-hint: "[fagtekst eller emne]"
allowed-tools:
  - Read
  - Glob
  - Write
---

# Arbejdsspørgsmål til en tekst

Lav et sæt arbejdsspørgsmål til en fagtekst efter Blooms reviderede taksonomi.

**Skal kendes:** teksten. Har du den ikke, så bed om den, og stop. Følg "Arbejdsgang" i `bloom-spoergsmaalsregler`: i hurtig-tilstand springer du Gate 1 over.

## Leverancer

**Kort version (standard):**

1. Én linje øverst med fokus og antagelser, fx "Fokus: X, Y og Z. Antaget: klassearbejde i samfundsfag A."
2. **Version 1: Taksonomisk progression.** 10 til 14 spørgsmål på de niveauer, teksten bærer, med niveauet som overskrift, og 1 til 2 brede hovedspørgsmål til sidst.
3. Balancen i én linje, fx "Tungest i Forstå og Analysere. Teksten bærer ikke Skabe."
4. Kun hvis afprøvningen på teksten efterlod en tvivl, du ikke kunne afgøre: én linje om den.
5. Én afsluttende linje: "Sig til, hvis du vil have den tekstnære version afsnit for afsnit, taxonomy table, facit, flere spørgsmål på et niveau eller basis og udvidet."

**På opfordring:**

- **Version 2: Tekstnær struktur.** Spørgsmål efter tekstens afsnit med overordnede, uddybende og detaljespørgsmål.
- **Taxonomy table** med kommentar til balancen og anbefalinger til klasserummet.
- Det fulde antal pr. niveau fra "Output-struktur" i reglerne.

Beder læreren om "det fulde sæt" eller "begge versioner", så lever alle dele.

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/SKILL.md`, og forstå reglerne.
2. **Analysér teksten** stille: hovedemne, fagbegreber, afsnitsstruktur og teksttype.

### Gate 1: Bekræft analyse (kun uden for hurtig-tilstand, VENT på svar)

Bruges, når læreren beder om sparring om fokus, eller når teksten kan læses på flere måder, og et forkert fokus ville koste et helt sæt.

Vis en kort analyse:

- **Hovedemne:** [emnet]
- **Teksttype:** [argumenterende, informerende eller analyserende]
- **Centrale begreber:** [4 til 6 nøglebegreber fra teksten]
- **Forventet Bloom-fordeling:** [fx "tung i Forstå og Anvende, fordi teksten er informerende"]

Giv en anbefaling: "Jeg anbefaler, at vi fokuserer på [begreber] med vægt på [niveau], fordi [begrundelse]."

Spørg: "Passer det med dit fokus?"

**VENT** på svar.

### Generér

3. **Generér Version 1.** Læs `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/references/bloom-verber.md` for korrekte verber.
4. **Kvalitetstjek** stille mod reglerne: ét spørgsmål ad gangen, ingen forbudte verber, besvarligt fra teksten. Læs `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/references/forbudte-formuleringer.md` ved tvivl. Ret det, der fejler, før du afleverer.
5. **Afprøv spørgsmålene på teksten** stille, jf. "Afprøvning på teksten" i reglerne: facit-test og elevtest på Huske til Anvende, og på de høje niveauer et tjek af, at teksten giver stof nok, og at et tomt svar ikke slipper igennem. Er sættet til lektie, får alle spørgsmål også ikke-læst-testen. Ret det, der falder. Afprøv igen, når læreren beder om ændringer.
6. **Kun på opfordring: Version 2,** der følger tekstens kronologi med Bloom-niveau i parentes.
7. **Kun på opfordring: Taxonomy table.** Læs `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/references/taxonomy-table-template.md`, og udfyld med antal og kommentar.

---

## Completion Status

- **DONE**: Sæt leveret i kort eller fuld udgave
- **DONE_WITH_CONCERNS**: Leveret, men taksonomisk balance er skæv, eller begreber mangler
- **BLOCKED**: Teksten er for kort eller uklar til meningsfulde spørgsmål
- **NEEDS_CONTEXT**: Mangler teksten
