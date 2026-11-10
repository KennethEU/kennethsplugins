---
name: bloom-skabe-opgaver
description: "Laver kreative skabe-spørgsmål (Bloom niveau 6) til en fagtekst, 6 som standard og op til 12 på opfordring: design, planlægning, generering, produktion og integration. Brug når læreren siger \"skabe-spørgsmål\", \"kreative opgaver\", \"niveau 6\", \"projektopgaver\", \"eleverne skal producere noget\". Brug ikke til et komplet sæt på alle niveauer (bloom-spoergsmaal-til-tekst) eller til lektiespørgsmål (bloom-lektiespoergsmaal)."
argument-hint: "[fagtekst eller emne]"
allowed-tools:
  - Read
  - Glob
  - Write
---

# Skabe-spørgsmål (Bloom niveau 6)

Lav kreative spørgsmål, der kræver, at eleverne designer, planlægger og producerer noget nyt. Velegnet til projektarbejde, større opgaver og eksamensforberedelse.

**Skal kendes:** teksten. Har du den ikke, så bed om den, og stop. Følg "Arbejdsgang" i `bloom-spoergsmaalsregler`: i hurtig-tilstand springer du gaten over.

## Kategorier

- **Design/Konstruktion**: byg en model, kampagne, regelsæt
- **Planlægning**: lav en strategi eller handlingsplan
- **Generering**: udvikl hypoteser eller alternativer
- **Produktion**: skriv et scenarie, debatindlæg, interview
- **Integration**: kombinér elementer fra flere dele af teksten

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/SKILL.md`.
2. **Læs Skabe-verberne** i `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/references/bloom-verber.md` (Niveau 6-sektionen).
3. **Find det kreative potentiale** i teksten: hvad kan redesignes, planlægges eller genereres? Vælg de to til tre kategorier, teksten bærer bedst.

### Gate: Bekræft fokus (kun uden for hurtig-tilstand, VENT på svar)

Bruges, når læreren beder om sparring om, hvad opgaverne skal bruges til.

Vis 3 til 4 muligheder fra teksten og de kategorier, der passer bedst, og giv en anbefaling: "Jeg anbefaler, at vi fokuserer på [kategori], fordi [begrundelse]."

Spørg: "Skal de bruges til gruppearbejde, individuelt projekt eller eksamensforberedelse?"

**VENT** på svar.

### Generér

4. **Formulér spørgsmålene** i de valgte kategorier med dansk kontekst og videnstype angivet.
5. **Kvalitetstjek** stille: Kræver hvert spørgsmål, at eleven skaber noget nyt? Ret dem, der kun er Evaluere.
6. **Prøv hver opgave som en middelmådig elev,** der skal i gang alene: Ved eleven, hvad produktet er, og hvor stort det skal være? Giver teksten stof nok at bygge på? Kan opgaven løses uden at bruge teksten, så bind den til et begreb eller et eksempel derfra.

## Sådan afleverer du

**Kort version (standard):**

- Én linje øverst: de valgte kategorier og antagelsen om brugen, fx "Kategorier: Design og Planlægning. Antaget: gruppearbejde."
- 6 spørgsmål med kategori og videnstype.
- Én linje til sidst: "Sig til, hvis du vil have flere (op til 12), en anden kategori eller et andet ambitionsniveau."

Beder læreren om et bestemt antal eller om alle kategorier, så lever det.

---

## Completion Status

- **DONE**: Skabe-spørgsmål leveret
- **DONE_WITH_CONCERNS**: Leveret, men nogle spørgsmål er tæt på Evaluere-niveau
- **NEEDS_CONTEXT**: Mangler teksten
