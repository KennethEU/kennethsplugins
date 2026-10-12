---
name: casespil-cheatsheet
description: "Producerer lærercheatsheets med spørgsmål og modelbesvarelser som printvenligt Word-dokument. Brug ved cheatsheet, facitliste, modelsvar, lærersvar, \"facit til gruppeopgaven\", hvad skal eleverne svare, eller teacher guide med svar til gruppeaktiviteter. Fagneutral og til både casespil og rollespil. Brug ikke til selve lærerguiden til et casespil eller rollespil (casespil-laererguide) eller til eksamens- og Bloom-spørgsmål."
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Write
---

# Lærermateriale — Cheatsheet og modelbesvarelser

**Projektregler:** `casespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill styrer workflow for at producere lærervejledninger med spørgsmål og modelbesvarelser. Den er fag-agnostisk og bruges til samfundsfag, erhvervsøkonomi, mediefag og andre fag.

## Hvornår bruges denne skill?

- Læreren har lavet gruppeaktiviteter, casespil eller øvelser med spørgsmål
- Læreren vil have et dokument med spørgsmål + forventede/modelbesvarelser
- Læreren vil have et debriefing-cheatsheet til at facilitere opsamling
- Læreren vil have en facitliste til en quiz eller arbejdsark

## Fase 0: Saml kontekst (automatisk — FØR alt andet)

1. Læs CLAUDE.md for at forstå lærerens fag, hold og arbejdsgange
2. Scan projektmappen for eksisterende elevmaterialer, rollekort eller arbejdsspørgsmål der skal bruges som input
3. Identificér faget og læringsmålene ud fra konteksten

Spørg ikke om fag, niveau eller spørgsmål, der kan læses i de eksisterende materialer. Læreren har allerede givet dem, og gentagne spørgsmål koster tid.

---

## Dialog med læreren: ét spørgsmål ad gangen

Når du skal afklare noget, brug dette mønster:

1. **Re-ground:** Hvad arbejder vi på? (1 sætning)
2. **Forklar simpelt:** Hvad er valget?
3. **Anbefaling:** "Jeg foreslår X fordi [grund]"
4. **Muligheder:** A) ... B) ... C) ...

**Eksempel:**
> Jeg laver et cheatsheet til debriefingen af dit EU-casespil.
>
> Casespillet har 12 spørgsmål fordelt på RAS-faserne. Skal
> cheatsheettet dække alle 12, eller kun de 5 analysespørgsmål
> der kræver fagbegreber?
>
> ANBEFALING: Vælg B — kun analysespørgsmålene. R- og S-spørgsmål
> er åbne og har ikke faste modelsvar, så de fylder bare.
>
> A) Alle 12 spørgsmål med modelsvar
> B) Kun de 5 analysespørgsmål (med fagbegreber i fed)
> C) Analysespørgsmål + 2-3 sammenfatningsspørgsmål

Stil kun ét spørgsmål ad gangen, så læreren kan svare kort uden at miste tråden.

---

## Workflow

### Fase 1: Identificér input

Hvad har Fase 0 fundet? Saml overblikket:
- Opgaveformulering / arbejdsspørgsmål (fundet i projektmappen eller givet af læreren)
- Fagligt indhold (tekster, slides, bilag eleverne har arbejdet med)
- Rollekort / aktivitetsbeskrivelser (hvis det er til et casespil)
- Læringsmål (identificeret i Fase 0 eller givet af læreren)

### Fase 2: Skriv modelbesvarelser

For hvert spørgsmål, skriv:
1. **Kernesvar** — det centrale svar læreren forventer (2-4 sætninger)
2. **Fagbegreber** — hvilke termer SKAL eleverne bruge? Markér med fed.
3. **Uddybning** — yderligere pointer stærke elever kan nævne
4. **Typiske fejl** — hvad siger elever ofte forkert? (valgfrit, men værdifuldt)

### Fase 3: Producér Word-dokument

Brug `casespil-rollekort`-skillens farvepalet og hjælpefunktioner.

**Standard layout: Two-table format**

Hvert spørgsmål-svar-par er en tabel med to rækker:
- Række 1 (farvet header): Spørgsmålet
- Række 2 (hvid): Modelbesvarelsen

```
┌─────────────────────────────────────────────┐
│ SPØRGSMÅL 1: [Spørgsmålstekst]             │  ← PRIMARY baggrund, hvid tekst
├─────────────────────────────────────────────┤
│ Kernesvar: [Svar med **fagbegreber** i fed] │  ← Hvid baggrund
│                                             │
│ Uddybning: [Ekstra pointer]                 │
│ Typiske fejl: [Hvad elever siger forkert]   │  ← Kursiv, grå tekst
└─────────────────────────────────────────────┘
```

**Header på dokumentet:**
- Titel: "LÆRERVEJLEDNING: [Aktivitetsnavn]"
- Undertitel: "Spørgsmål og modelbesvarelser — KUN TIL LÆREREN"
- Fag, niveau, forløb

**Alternativt layout: Debriefing-flow**

For casespils-debriefing følger layoutet RAS-modellen:
- Sektion R: Reaktionsspørgsmål (ingen modelsvar — kun faciliterings-noter)
- Sektion A: Analysespørgsmål med modelsvar og fagbegreber
- Sektion S: Sammenfatningsspørgsmål med teori-kobling

### Fase 4: Kvalitetstjek

- [ ] Er ALLE spørgsmål fra elevmaterialet dækket?
- [ ] Er fagbegreber markeret med fed?
- [ ] Er svarene realistiske — dvs. noget en gymnasieelev faktisk kan formulere?
- [ ] Er der konsistens med de faglige slides/tekster eleverne har læst?
- [ ] Er sproget korrekt dansk? (brug `casespil-sprogtjek` hvis tilgængelig)

## Vigtige principper

**Modelbesvarelser er ikke perfekte svar.** De er det læreren bruger som rettesnor. Skriv dem på det niveau en stærk elev ville formulere — ikke som en akademisk afhandling.

**Fagbegreber er nøglen.** Hele pointen med cheatsheettet er at læreren hurtigt kan se: "Nævnte eleven X-begrebet? Ja/nej." Markér derfor altid de centrale fagbegreber med fed.

**Typiske fejl er guld værd.** Læreren kan bruge dem proaktivt: "Mange tror at... men faktisk..."

**Print-venligt.** Dokumentet skal fungere som ét A4-ark (eller få sider) læreren har ved siden af sig under opsamling. Undgå lange tekstvægge.

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Lærermateriale genereret med spørgsmål, modelbesvarelser og fagbegreber markeret
- **DONE_WITH_CONCERNS** — Materiale leveret, men med forbehold (fx: nogle spørgsmål mangler modelbesvarelser, eller fagbegreber var uklare)
- **BLOCKED** — Kan ikke generere materiale (fx: ingen spørgsmål eller fagligt indhold at arbejde ud fra)
- **NEEDS_CONTEXT** — Mangler information (fx: "Hvilke spørgsmål skal der laves modelsvar til?")
