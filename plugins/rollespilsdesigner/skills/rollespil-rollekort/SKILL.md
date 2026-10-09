---
name: rollespil-rollekort
description: "Producerer rollekort, livskort, beslutningskort og elevintroduktioner til rollespil som printklare Word-dokumenter (.docx) med Node.js. Brug når læreren siger rollekort, elevintroduktion, \"til printeren\", print, word eller docx i forbindelse med rollespil eller simulation. Normalversionen er standard; støtte og stærk laves kun efter ønske. Brug ikke til lærerguider (rollespil-laererguide), cheatsheets (rollespil-cheatsheet) eller dokumenter uden for rollespil."
allowed-tools:
  - Read
  - Glob
  - Bash
  - Write
---

# Rollekort & Lærerguide — Docx-generering

**Projektregler:** `rollespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill styrer *hvordan* du genererer Word-dokumenter til rollespil. Den faglige designviden (hvilke roller, dilemmaer, formater) styres af `rollespil-designprincipper`-skillen med dens reference-filer.

## Fase 0: Saml kontekst (automatisk — FØR alt andet)

1. Læs CLAUDE.md for at forstå lærerens fag og hold
2. Scan projektmappen for eksisterende rollespilsmaterialer (indhold, roller, dilemmaer)
3. Læs `rollespil-designprincipper`-skillen — rollekortene SKAL overholde de 10 principper
4. Hvis `/mnt/skills/public/docx/SKILL.md` findes, så læs den for den nyeste docx-vejledning

Hav rollekortenes indhold færdigt, før du begynder at kode. Rettes teksten først bagefter i scriptet, giver det dobbeltarbejde og tekstfejl i de genererede filer.

---

## Workflow

### Før du koder

1. Læs `rollespil-designprincipper`-skillen (den skal allerede være trigget) for at sikre at rollekortene overholder de 10 principper
2. Hvis `/mnt/skills/public/docx/SKILL.md` findes, så læs den for den nyeste docx-vejledning (den opdateres løbende)
3. Hav rollekortenes indhold klar FØR du begynder at kode — skriv aldrig kode og indhold samtidig

### Generering

1. Installér pakken: `npm install docx` (v9.5.1+)
2. Byg scriptet med konstanter og hjælpefunktioner fra `references/template-kode.md`
3. Generér .docx-filen
4. Validér: hvis docx-skillen findes, kør `python3 /mnt/skills/public/docx/scripts/office/validate.py output.docx`. Ellers åbn filen igen med `python-docx` eller konvertér den i trin 5, og stop ved fejl.
5. Preview: Konvertér til PDF med `soffice --headless --convert-to pdf output.docx`, derefter `pdftoppm -jpeg -r 200` og se billederne
6. Kør konsistenstjek (se `rollespil-konsistenstjek`-skillen)

### Vigtigt

- Brug `references/template-kode.md` som udgangspunkt for genbrugelig kode
- Tilpas aldrig margener eller farvepalet uden god grund — standarderne er testet

---

## Farvepalet

| Navn | Hex | Brug |
|------|-----|------|
| PRIMARY | `1A3A6B` | Overskrifter, rollekort-header baggrund |
| SECONDARY | `2A4A8B` | Underoverskrifter, sektionstitler |
| ACCENT | `C0392B` | Advarsler, skjult information, dilemmaer |
| LIGHT | `E8EEF8` | Info-bokse, baggrund |
| YELLOW | `FFF3CC` | Nødhjælpsbokse (støtteversion) |
| GREEN | `E8F5E8` | Forhandlingssætninger (støtteversion), tip-bokse |
| GREEN_TEXT | `1A6B1A` | Tekst i grønne bokse |
| WHITE | `FFFFFF` | Header-tekst |

---

## Sideopsætning (DXA-enheder)

```
A4: PAGE_W = 11906, PAGE_H = 16838

Rollekort (kompakte margener, 1 side pr. kort):
  MH = 1008  (top/bund)
  MV = 640   (venstre/højre)

Lærerguide (standard margener):
  MH = 1440  (top/bund)
  MV = 1008  (venstre/højre)

Elevintroduktion (medium margener):
  MH = 1200
  MV = 900
```

---

## Rollekort-versioner

**Normalversionen er standard og nok i de fleste tilfælde.** Læreren vil ofte have en simpel model, og nogle gange en AI-rådgiver som støtte til de svage elever. Lav kun støtte- og stærkversion, hvis læreren beder om det. Spørg gerne kort, om der skal være flere versioner, men antag ikke, at der skal.

### Normal (1 A4-side)

Standardversion for hovedparten af klassen. Indeholder:
- Farvet header med navn, titel, organisation, stemmer + evt. beføjelse og evt. rådgiverkode (se Rådgiverkode)
- MÅL (1-2 sætninger)
- BAGGRUND (2. person: "Du er...")
- HOLDNING (rollens faglige position)
- VÆRDIER (2 stk.)
- ARGUMENTER (3 stk., 1. person: "Mine data viser...")
- DILEMMAER (3 stk., 2. person: "Skal du...?", med krydsreferencer til andre roller)
- SÆRLIG BEFØJELSE (hvis relevant)
- TIP (2. person imperativ)
- FASEGUIDE-TABEL (2 kolonner, farvet header, INGEN minuttal). Spilfaserne har samme navne, numre og rækkefølge som i elevintroduktion og lærerguide og, hvis de findes, webside og rådgiver. Intro og Debriefing må stå som før- og eftertrin uden fasenummer

### Støtte (2 A4-sider, kun hvis ønsket)

Alt fra normal-versionen PLUS:
- **"Sig f.eks."** ved HVERT argument — konkret sætning eleven kan sige højt
- **Alliancetabel** — Hvem? | Hvorfor? | Sig dette til dem
- **Ordliste** — 3-4 fagbegreber med forklaring i dagligsprog
- **Nødhjælpsboks** (GUL baggrund) — "HVIS DU ER I TVIVL:" + 2-3 universelle sætninger
- **Forhandlingssætninger** (GRØN baggrund) — 3 nummererede sætninger
- Faseguide med mere detalje

### Stærk (1 A4-side, kompakt, kun hvis ønsket)

Slankere version:
- Stikord i stedet for fuldtekst-argumenter
- **Teori-tags** ved hvert argument (fx [NEO], [REAL], [LIB])
- INGEN faseguide
- Tom noteboks til egen strategi
- Ingen "sig f.eks." eller alliancetabel

---

## Person-perspektiv (KRITISK)

| Felt | Perspektiv | Eksempel |
|------|-----------|----------|
| Baggrund | 2. person | "Du er afdelingsdirektør i..." |
| Argumenter | 1. person | "Mine data viser at..." |
| Dilemmaer | 2. person | "Skal du støtte Henrik og..." |
| Tip | 2. person imperativ | "Brug din vetoret strategisk..." |
| Skjult info | 2. person | "Du ved at budgettet..." |

Bland ALDRIG perspektiver inden for samme felt.

---

## Rådgiverkode (kun hvis spillet har en AI-rådgiver)

- Hver rolle har en 4-cifret kode. Den trykkes på forsiden af rollekortet i topbjælkens undertitel, fx "Fjord Outdoors bestyrelse | Leder mødet | Rådgiverkode: 2481".
- Koden står **ikke** under en overskrift og er ikke en ny sektion. Rådgiveren læser kortets faste overskrifter, så sektionerne ændres ikke (se `rollespil-digitale-tillaeg`).
- Koderne kommer fra rådgiverens kodeliste. Rollekortene laves ofte, før rådgiveren findes: tilføj koden, når rådgiveren er bygget, og generér kortene igen. Koden på kortet, i lærervinduet og (som hash) i rådgiveren skal være den samme.
- Koden står kun på sin egen rolles kort, aldrig i elevintroduktion eller fælles bilag. Rådgiverens fejlbesked og webtekster må kun skrive "fra dit kort", hvis koden står der.

---

## Filproduktion

Producér altid som separate .docx-filer:

1. `Elevintroduktion_[Navn].docx` — Scenarie + regler + overblik (1 side)
2. `Rollekort_[Navn]_Normal.docx` — Alle normale rollekort
3. (kun hvis ønsket) `Rollekort_[Navn]_Stoette.docx` — Alle støtte-rollekort
4. (kun hvis ønsket) `Rollekort_[Navn]_Staerk.docx` — Alle stærke rollekort
5. `Laererguide_[Navn].docx` — Komplet lærerguide

Alternativt, hvis brugeren foretrækker: Alle rollekort i ét dokument med page breaks.

---

## Template-kode

Se `references/template-kode.md` for komplet genbrugelig kodebase med:
- Konstanter og borders
- Hjælpefunktioner (empty, divider, colorRow, sectionTitle, bodyText, numberedItem, bold, accentBox)
- Rollekort-header-funktion
- Faseguide-tabel-funktion
- Støtteversion-specifikke funktioner (alliancetabel, nødhjælpsboks, forhandlingsboks, ordliste)
- Lærerguide-specifikke funktioner

Kopiér aldrig hele template-koden blindt — tilpas altid til det specifikke rollespils behov.

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Alle rollekort (normalversionen, og støtte/stærk hvis det er ønsket) genereret som .docx og klar til print
- **DONE_WITH_CONCERNS** — Rollekort leveret, men med forbehold (fx: en ønsket støtteversion mangler, eller farvepalet er tilpasset uden godkendelse)
- **BLOCKED** — Kan ikke generere rollekort (fx: rollernes indhold er ikke defineret, designprincipper-skill ikke tilgængelig)
- **NEEDS_CONTEXT** — Mangler information (fx: "Hvor mange roller skal der være? Skal der laves differentierede versioner?")
