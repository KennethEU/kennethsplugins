# Rollespilsdesigner

Et Cowork-plugin til design af rollespil og simuleringer i dansk gymnasieundervisning (STX). Bygger på evidensbaseret pædagogik med 10 designprincipper, 8 rollespilsformater og struktureret debriefing.

## Hvad pluginet gør

- **Designer rollespil** baseret på fagligt emne, elevgruppe og praktisk ramme
- **Genererer Word-dokumenter** med rollekort (normalversion som standard, støtte/stærk efter ønske), lærerguider, elevintroduktioner og cheatsheats
- **Laver miniversioner** (10-20 min) af eksisterende rollespil eller fra bunden
- **Bygger digitale værktøjer** (AI-rådgiver, facit-beregner, lærershow, webside, spilintro med voiceover, video) ud fra en teknisk reference med afprøvede mønstre
- **Kører kvalitetssikring** — konsistenstjek + dansk sprogcheck — før levering
- **Understøtter 8 formater:** Forhandling, krisehåndtering, lev-et-liv, konsekvens-kredsløb, retssag, bestyrelse, parlamentarisk lovproces, interaktiv virksomhedssimulation

## Struktur

```
rollespilsdesigner/
├── .claude-plugin/plugin.json
├── README.md
└── skills/
    ├── rollespil-nyt/              ← Start nyt rollespilsdesign
    ├── rollespil-miniversion/      ← Miniversion (forløb og metode samlet)
    ├── rollespil-designprincipper/ ← Faglig rygrad: 10 principper + 8 formater
    ├── rollespil-rollekort/        ← Docx-produktion: farver, margener, layout
    │   └── references/template-kode.md
    ├── rollespil-laererguide/      ← Lærerguide: 12 obligatoriske sektioner + RAS
    ├── rollespil-cheatsheet/       ← Cheatsheets: spørgsmål + modelbesvarelser
    ├── rollespil-sprogtjek/        ← Dansk retskrivning + QA-tjekliste
    │   └── scripts/sprogtjek.py
    ├── rollespil-projektregler/    ← Ingen ritualer, normalversion nok, beregner-tjek
    ├── rollespil-digitale-tillaeg/ ← Digitale værktøjer: designregler
    │   └── references/teknik.md
    └── rollespil-konsistenstjek/   ← Kvalitetssikring af materialer
```

I `evals/` ligger automatiske triggertests (`claude plugin eval plugins/rollespilsdesigner`) og en plan for de tests, der skal køres i Cowork. Se `evals/README.md`.

## Pipeline

Skillsene kører i en fast rækkefølge — du behøver kun starte med en command, resten sker automatisk.

**Fuldt rollespil** (`/rollespilsdesigner:rollespil-nyt`):
```
rollespil-nyt → design → rollekort → lærerguide → materiale → (digitale tillæg) → sprogtjek → konsistenstjek → levér
```

`rollespil-projektregler` gælder hele vejen og overstyrer de øvrige skills.

**Hvem kender hvem:** `rollespil-nyt` har en oversigtstabel over alle skills. Alle produktionsskills peger på projektreglerne, og `rollespil-digitale-tillaeg` peger på designprincipper, projektregler og konsistenstjek, som også har et tjek af beregner og digitale dele.

**Miniversion** (`/rollespilsdesigner:rollespil-miniversion`):
```
miniversion → rollekort → sprogtjek → konsistenstjek → levér
```

## Skills

Kommandoerne skrives med plugin-navnet foran, fx `/rollespilsdesigner:rollespil-rollekort`.

| Skill | Type | Trigger |
|-------|------|---------|
| `rollespil-nyt` | Indgang | "nyt rollespil", "design et rollespil" |
| `rollespil-miniversion` | Indgang | "miniversion", "kort version", "simplificér", "kan vi lave det kortere" |
| `rollespil-designprincipper` | Auto | Design-beslutninger, format-valg, brainstorming |
| `rollespil-rollekort` | Auto | Docx-generering af rollekort og materialer |
| `rollespil-laererguide` | Auto | Produktion af lærerguider |
| `rollespil-cheatsheet` | Auto | Cheatsheats, modelbesvarelser, facitlister |
| `rollespil-sprogtjek` | Auto | Sprogcheck, korrektur, dansk tekst |
| `rollespil-projektregler` | Auto | Regler der overstyrer de øvrige skills (ritualer, versioner) |
| `rollespil-digitale-tillaeg` | Auto | AI-rådgiver, facit-beregner, lærershow, webside, spilintro, video |
| `rollespil-konsistenstjek` | Auto | Kvalitetssikring, "er det færdigt", "klar til print" |

## Anbefalet mappestruktur (Cowork)

```
min-rollespilsmappe/
├── materialer/
│   ├── eu-reformkonference/
│   ├── fattigdomskommission/
│   └── overophedningen/
├── elevtekster/
├── fakta/
│   └── velfaerd_fakta_2026.md    ← Verificerede tal der ellers genslås op
└── MASTERGUIDE_(...).md          ← VALGFRI ekstra reference (pluginet er selvstændigt)
```

## Folder instructions (anbefalet)

```
Du er rollespilsdesigner til dansk gymnasieundervisning.
Skriv altid på dansk med korrekt retskrivning (æøå).
Brug aldrig faste minuttal i materialer — læreren styrer tempoet.
Brug "du" til læreren.
```

## Installation

I Claude: tilføj en marketplace med adressen `KennethEU/kennethsplugins` (se hovedsiden i repositoryet), og installér pluginet `rollespilsdesigner` (installationsnavn `rollespilsdesigner@kennethsplugins`). Alternativt kan zip-filen med pluginets indhold uploades direkte.

## Kompatibilitet

- **Claude Cowork** (primært) — fuld funktionalitet med filsystem-adgang
- **Claude Code** — fungerer som plugin
- **Claude.ai** — skills kan uploades individuelt via Settings > Skills

## Changelog

### v1.9.0 (oktober 2026)
- `rollespil-digitale-tillaeg`: popup på forsiden er erstattet af en selvstændig rollespilsside (hub) med indlejret spilintro, knap til AI-rådgiveren, spilfaser samt roller og regler. Forsiden har kun ét menupunkt og en hero-knap, intet link til rådgiveren, og gamle `#intro`-links sendes videre. Afspilleren bor i én fil, og død kode fjernes, når et format udgår
- Hubben er offentlig: ingen BCG- eller Ansoff-svar og ingen beskrivelser af rollernes holdninger. Roller, stemmetal og beløb hentes fra rollekort og bilag og opfindes ikke
- Spilfaserne har samme navne og numre overalt; rådgiver og webside viser kun faser, hvor eleverne agerer. Ny regel i `rollespil-rollekort` og nyt punkt i `rollespil-konsistenstjek`
- Rådgiverkode (4 cifre) trykkes i rollekortets topbjælke-undertitel, og kodetjek er tilføjet i konsistenstjekket
- Voiceover og scenetekster tjekkes mod bilagene, før stemmen indtales
- `rollespil-projektregler`: offentlige sider afslører ikke svar, og backup gælder også ved gennemgang og små rettelser
- Omdirigering af gamle intro-links er afprøvet i Chromium

### v1.8.0 (oktober 2026)
- `rollespil-digitale-tillaeg` har fået fem nye områder fra Fjord Outdoor: spilintro (popup og selvstændig side, synkroniseret lyd, scener og undertekster), voiceover med ElevenLabs (stemningsmærker, pauser, længde), grafisk stil uden generisk AI-look og med kontrastregler, mobil- og Safari-fejl (usynlig modal, menulukning, Tilbage-knap, layout) og arkitektur for popup mod selvstændig side
- Kontrasttal i skillen er regnet efter: marineblå mærke med hvid tekst er 12,9 til 1 og skovgrøn 7,5 til 1, mens rav med marineblå tekst er 4,4 til 1 og derfor kun godkendt til stor tekst
- Tilbage-knappen lukker nu popup'en: mønstret med `pushState` er afprøvet i Chromium, fordi en `popstate`-lytter alene ikke virker, når linket åbner popup'en med `preventDefault()`
- Ny triggertest `trigger-intro-1`

### v1.7.0 (oktober 2026)
- Skillene har fået gruppenavnet `rollespil-` foran det beskrivende navn, så de står samlet i kommandomenuen i Cowork, hvor plugin-navnet ikke vises: `rollespil-nyt`, `rollespil-miniversion`, `rollespil-rollekort`, `rollespil-laererguide`, `rollespil-cheatsheet`, `rollespil-sprogtjek`, `rollespil-konsistenstjek`, `rollespil-digitale-tillaeg`, `rollespil-designprincipper` og `rollespil-projektregler`.

### v1.6.0 (oktober 2026)
- Skillene er omdøbt, så kommandoerne ikke gentager `rollespil` og forklarer sig selv, fx `/rollespilsdesigner:nyt-rollespil` og `/rollespilsdesigner:miniversion`. Gamle navn og nyt: `rollespil-nyt` er `nyt-rollespil`, `rollespil-mini` er `miniversion`, `rollespil-designprincipper` er `designprincipper`, `rollespil-rollekort-docx` er `rollekort`, `rollespil-laererguide-docx` er `laererguide`, `rollespil-laerermateriale` er `cheatsheet`, `rollespil-sprogkvalitet-da` er `sprogtjek`, `rollespil-konsistenstjek` er `konsistenstjek`, `rollespil-projektregler` er `projektregler` og `rollespil-digitale-tillaeg` er `digitale-tillaeg`.

### Marketplace omdøbt (oktober 2026)
- Repository og marketplace hedder nu `kennethsplugins` (før `rollespilsdesigner` og `rollespilsdesigner-marketplace`). Selve pluginet er uændret og hedder stadig `rollespilsdesigner`, så skillenavnene er de samme. Tilføj marketplace'en igen med `KennethEU/kennethsplugins`.

### v1.5.2 (oktober 2026)
- Alle beskrivelser har fået konkrete, rodede triggervendinger og en "Brug ikke til"-del (inspireret af Anthropics skill-creator). Lærerguiden udløses nu også af "hvad siger jeg når vi skifter fase"
- 12 nye triggertests (rodede formuleringer og nære negativer), i alt 27
- Nyt punkt 9 i `rollespil-konsistenstjek`: læsertest med en frisk læser, der kun får elevintroduktion og ét rollekort
- HÅRD REGEL-formuleringer er erstattet af regler med begrundelse
- Otte docx-fælder fra Anthropics docx-skill i `template-kode.md`

### v1.5.1 (oktober 2026)
- 15 triggertests i `evals/` (`claude plugin eval plugins/rollespilsdesigner`). De afslørede, at `rollespil-sprogkvalitet-da` blev udløst af en Blooket-forespørgsel. Beskrivelsen er indsnævret til rollespilsmaterialer
- Scriptstier bruger `${CLAUDE_SKILL_DIR}`
- Indholdsfortegnelse i de tre store reference-filer
- Docx-trin i `rollespil-rollekort-docx` og `rollespil-nyt` virker nu også uden Anthropics docx-skill (`/mnt/skills/public/docx`)
- Faste minuttal ("5-10 min.") i designprincipper fjernet, så de følger projektreglerne

### v1.5.0 (oktober 2026)
- Nyt script `rollespil-sprogkvalitet-da/scripts/sprogtjek.py`: finder tankestreger, ae/oe/aa, delte sammensatte ord, ritualsætninger, `maks.`, `à`, `60 %` og minuttal i .docx, .md og .html. `rollespil-konsistenstjek` (nyt punkt 0) og sprogskillen kører det først
- Rettet brudt henvisning til `references/docx-skill.md` i `rollespil-rollekort-docx`
- Skarpere `description` på rollekort-docx, laererguide-docx, laerermateriale og projektregler, så de ikke overlapper og udløses rigtigt

### v1.4.0 (oktober 2026)
- `rollespil-mini` og `rollespil-simplificering` slået sammen til én skill
- Ny teknisk reference `rollespil-digitale-tillaeg/references/teknik.md` (arkitektur, kryptering, proxy, prompt, session, responsivt design, billeder og video, test, sikkerhed)
- Alle produktionsskills peger på `rollespil-projektregler`
- `rollespil-nyt` har oversigtstabel, spørgsmål om digitale dele og digitale tillæg i pipelinen
- `rollespil-konsistenstjek` har nyt punkt 8: beregner og digitale dele

### v1.3.0 (oktober 2026)
- Skills omdøbt med fælles præfiks `rollespil-`, nye skills `rollespil-projektregler` og `rollespil-digitale-tillaeg`

### v1.2.0 (marts 2026)
- **Migreret commands til skills-format** — ingen `commands/`-mappe mere
- Tilføjet pipeline-oversigt i README og i `rollespil-nyt`/`rollespil-mini`-skills
- Tilføjet "Typiske arbejdsgange"-sektion

### v1.1.0 (marts 2026)
- **Pluginet er nu selvstændigt** — masterguiden er valgfri ekstra reference
- Tilføjet `references/cases.md` — 14 cases med roller, stemmer, knaphed, fagbegreber
- Tilføjet `references/masterguide-kompakt.md` — teori, skabeloner, designmønstre, evaluering
- Tilføjet `rollespil-laerermateriale` skill (cheatsheet-workflow)
- Tilføjet `rollespil-sprogkvalitet-da` skill (dansk QA-tjekliste)
- Tilføjet `rollespil-simplificering` skill (miniversion-workflow)
- Tilføjet `rollespil-mini` skill
- Tilføjet cheatsheet-generatorkode (qaBlock) i template-kode.md
- Opdateret alle skills til at referere internt i stedet for til ekstern masterguide

### v1.0.0 (marts 2026)
- Første version med designprincipper, rollespil-rollekort-docx, rollespil-laererguide-docx, konsistenstjek
- `rollespil-nyt` skill
