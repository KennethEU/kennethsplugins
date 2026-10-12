---
name: casespil-rollekort
description: "Producerer to adskilte elevpakker (Uden AI og Med AI-rådgiver) med elevintroduktion, bilag, dobbeltsidede rollekort og beslutningsskema, og en samlet lærerpakke, til casespil (også kaldet rollespil) som printklare Word-dokumenter (.docx) med Node.js. Brug når læreren siger rollekort, elevintroduktion, \"til printeren\", print, word eller docx i forbindelse med casespil, rollespil eller simulation. Normalversionen er standard; støtte og stærk laves kun efter ønske. Brug ikke til lærerguider (casespil-laererguide), cheatsheets (casespil-cheatsheet) eller dokumenter uden for casespil og rollespil."
allowed-tools:
  - Read
  - Glob
  - Bash
  - Write
---

# Rollekort & Lærerguide — Docx-generering

**Projektregler:** `casespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill styrer *hvordan* du genererer Word-dokumenter til casespil. Den faglige designviden (hvilke roller, dilemmaer, formater) styres af `casespil-designprincipper`-skillen med dens reference-filer.

## Fase 0: Saml kontekst (automatisk — FØR alt andet)

1. Læs CLAUDE.md for at forstå lærerens fag og hold
2. Scan projektmappen for eksisterende casespilsmaterialer (indhold, roller, dilemmaer)
3. Læs `casespil-designprincipper`-skillen — rollekortene SKAL overholde de 10 principper
4. Hvis `/mnt/skills/public/docx/SKILL.md` findes, så læs den for den nyeste docx-vejledning

Hav rollekortenes indhold færdigt, før du begynder at kode. Rettes teksten først bagefter i scriptet, giver det dobbeltarbejde og tekstfejl i de genererede filer.

---

## Workflow

### Før du koder

1. Læs `casespil-designprincipper`-skillen (den skal allerede være trigget) for at sikre at rollekortene overholder de 10 principper
2. Hvis `/mnt/skills/public/docx/SKILL.md` findes, så læs den for den nyeste docx-vejledning (den opdateres løbende)
3. Hav rollekortenes indhold klar FØR du begynder at kode — skriv aldrig kode og indhold samtidig

### Generering

1. Installér pakken: `npm install docx` (v9.5.1+)
2. Byg scriptet med konstanter og hjælpefunktioner fra `references/template-kode.md`
3. Generér .docx-filen
4. Validér: hvis docx-skillen findes, kør `python3 /mnt/skills/public/docx/scripts/office/validate.py output.docx`. Ellers åbn filen igen med `python-docx` eller konvertér den i trin 5, og stop ved fejl.
5. Preview: Konvertér til PDF med `soffice --headless --convert-to pdf output.docx`, derefter `pdftoppm -jpeg -r 200` og se billederne
6. Kør konsistenstjek (se `casespil-konsistenstjek`-skillen)

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

**Normalversionen er standard og nok i de fleste tilfælde.** Lav kun støtte- og stærkversion, hvis læreren beder om det. Spørg gerne kort, om der skal være flere versioner, men antag ikke, at der skal.

### Normal: dobbeltsidet A4 (forside og bagside)

Et rollekort er altid 2 sider, trykt dobbeltsidet. Spillet foregår fysisk i klasselokalet med papir, dialog og forhandling, og bagsiden er arbejdsarket, eleven har foran sig under forhandlingen.

**Forside (Rolle og mandat):**
- Topbanner med navn, titel, organisation og evt. beføjelse. I varianten Med AI står rådgiverkoden i bannerets undertitel (se Rådgiverkode)
- Nøgletalsbjælke (KPI-bar) med 3 felter: pulje, stemmer eller beføjelser, flertalskrav
- MÅL (1 til 2 sætninger)
- BAGGRUND (2. person: "Du er...")
- HOLDNING OG VÆRDIER (rollens faglige position og 2 værdier)
- INITIATIVKRAV OG MULIGHEDER
- ARGUMENTER, nummereret (3 stk., 1. person: "Mine data viser...")
- DILEMMAER (3 stk., 2. person: "Skal du...?", med krydsreferencer til andre roller)
- SÆRLIG BEFØJELSE (hvis relevant) og evt. TIP (2. person imperativ)
- **FORTROLIGT NOTAT:** en tydelig boks med skjult information (2. person: "Du ved at...")

**Bagside (Taktik og arbejdsark):**
- FAGBEGREBER I SPILLET (fx Eastons model, BCG, Ansoff) med en forklaring i dagligsprog
- FASEGUIDE: opgaver i fase 1, 2 og 3 (2 kolonner, INGEN minuttal). Spilfaserne har samme navne, numre og rækkefølge som i elevintroduktion og lærerguide og, hvis de findes, webside og rådgiver. Intro og Debriefing må stå som før- og eftertrin uden fasenummer
- DINE FORHANDLINGSNOTER med fysiske notelinjer til elevens blyant. Linjerne er rækker i en tabel med bundkant, ikke tomme afsnit (de smelter sammen til én linje)

Hvert rollekort fylder præcis 2 sider. Tjek det i preview og med sidetælling (se Template-kode).

### Støtte (kun hvis ønsket)

Samme forside og bagside som normalversionen, plus på bagsiden (og om nødvendigt en ekstra side):
- **"Sig f.eks."** ved HVERT argument: en konkret sætning eleven kan sige højt
- **Alliancetabel:** Hvem? | Hvorfor? | Sig dette til dem
- **Nødhjælpsboks** (GUL baggrund): "HVIS DU ER I TVIVL:" og 2 til 3 universelle sætninger
- **Forhandlingssætninger** (GRØN baggrund): 3 nummererede sætninger

### Stærk (kun hvis ønsket)

Kompakt version: stikord i stedet for fuldtekst-argumenter, **teori-tags** ved hvert argument (fx [NEO], [REAL], [LIB]), ingen "sig f.eks." og ingen alliancetabel. Bagsiden bruges til notelinjer og fagbegreber. Stærk er den eneste version, der må være på 1 side, og kun hvis læreren beder om det.

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

## Rådgiverkode (kun varianten Med AI)

- Hver rolle har en 4-cifret kode. Den trykkes **kun i elevpakken Med AI** på forsiden af rollekortet i bannerets undertitel, fx "Fjord Outdoors bestyrelse | Leder mødet | Rådgiverkode: 2481".
- **Elevpakken Uden AI indeholder ingen koder og ingen henvisninger til AI, rådgiver eller app.** Den er til 100 % skærmfrie lektioner. Ordene "rådgiver" og "AI" står ikke i filen, og ingen 4-cifret kode står på kortene.
- Koden står **ikke** under en overskrift og er ikke en ny sektion. Rådgiveren læser kortets faste overskrifter, så sektionerne ændres ikke (se `casespil-digitale-tillaeg`).
- Koderne kommer fra rådgiverens kodeliste. Rollekortene laves ofte, før rådgiveren findes: tilføj koden, når rådgiveren er bygget, og generér varianten Med AI igen. Koden på kortet, i lærervinduet og (som hash) i rådgiveren skal være den samme.
- Koden står kun på sin egen rolles kort, aldrig i elevintroduktion, bilag eller lærerpakke. Rådgiverens fejlbesked og webtekster må kun skrive "fra dit kort", hvis koden står der (altså i varianten Med AI).

---

## Filproduktion

Producér altid disse tre Word-filer, og kun disse som standard (`[Spil]` er spillets navn):

1. **`Elevpakke_[Spil]_Uden_AI.docx`:** alt samlet i én fil (elevintroduktion, bilag, rollekort og beslutningsskema), helt uden koder eller AI-henvisninger. Til 100 % skærmfrie lektioner.
2. **`Elevpakke_[Spil]_Med_AI.docx`:** nøjagtig samme indhold, men med den 4-cifrede rådgiverkode trykt på rollekortene ("Rådgiverkode: XXXX") til lærere, der vil lade eleverne sparre med AI på mobilen.
3. **`Laererpakke_[Spil]_Samlet.docx`:** lærerguide og cheatsheet samlet i ét dokument, så læreren kun printer ét hæfte til eget brug.

Regler for de to elevpakker:
- Navnene er "Uden AI" og "Med AI-rådgiver", ikke "Analog" og "Digital". Spillet foregår altid fysisk med papir, dialog og forhandling, og AI er en støtte ved siden af.
- De to varianter ligger altid som to separate Word-filer og blandes aldrig i samme fil, så læreren undgår fejlprint og ikke skal vælge sidetal.
- De bygges af samme data og samme kode med ét flag (`medAI`), så de ikke kan glide fra hinanden. Eneste forskel er rådgiverkoden på rollekortene.
- Støtte- og stærkversion laves kun efter ønske og som egne filer i samme to varianter (fx `Elevpakke_[Spil]_Uden_AI_Stoette.docx`).
- Antal rollekort at printe følger gruppeplanen (se nedenfor). Kortene i pakken er ét pr. rolle, og læreren printer det antal, planen viser.

---

## Gruppeplanlægning og printliste

Antallet af rollekort at printe følger gruppeplanen og ikke et løst overslag. Gruppeplan og printliste bygges af samme plan (se `casespil-digitale-tillaeg` og lærerassistenten), og tallene stemmer for alle elevtal fra 4 til 60.

- **Summen af elever på roller er altid klassens elevtal (Σ elever = N).** Intet bord må have flere pladser end elever, og ingen elev står uden rolle.
- **Stemmende roller har altid et fysisk kort:** antal kort pr. rolle og bord er `max(elever, 1)`. Det betyder, at antal kort kan være højere end antal elever.
- **Små borde (under 5 elever) ved bordbaserede spil** (fx Kommunebudget): eleverne tildeles 1 pr. rolle efter en fast prioritet. De roller, der ikke får en elev, deles af en naborolle, men de modtager alligevel et rollekort, så alle bordets stemmer er repræsenteret i forhandlingen og afstemningen.
- **Større borde:** de største roller dubleres (to elever deler ét kort og afgiver ét fælles svar uden at ændre stemmetallet). Der printes ét kort pr. elev på en delt rolle, så de kan læse hver sit.
- **Printlisten viser begge tal:** elever på roller (N) og rollekort at printe. Den skriver aldrig faste intervaller, men udleder dem af planen.
- Et kort kan ende hos en elev, der også har sin egen rolle (rollen uden egen elev deles af en nabo), eller deles af to elever. Skriv derfor kortets tekst og skjulte information, så den kan bruges af en elev med to hatte, uden at ændre rollens stemmer.

## Template-kode

Se `references/template-kode.md` for komplet genbrugelig kodebase med:
- Konstanter og borders
- Hjælpefunktioner (empty, divider, colorRow, sectionTitle, bodyText, numberedItem, bold, accentBox)
- Rollekort-header-funktion
- Faseguide-tabel-funktion
- Støtteversion-specifikke funktioner (alliancetabel, nødhjælpsboks, forhandlingsboks, ordliste)
- Lærerguide-specifikke funktioner

Kopiér aldrig hele template-koden blindt — tilpas altid til det specifikke casespils behov.

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Alle rollekort (normalversionen, og støtte/stærk hvis det er ønsket) genereret som .docx og klar til print
- **DONE_WITH_CONCERNS** — Rollekort leveret, men med forbehold (fx: en ønsket støtteversion mangler, eller farvepalet er tilpasset uden godkendelse)
- **BLOCKED** — Kan ikke generere rollekort (fx: rollernes indhold er ikke defineret, designprincipper-skill ikke tilgængelig)
- **NEEDS_CONTEXT** — Mangler information (fx: "Hvor mange roller skal der være? Skal der laves differentierede versioner?")
