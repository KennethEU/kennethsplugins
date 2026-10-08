# Rollespilsdesigner

Et Cowork-plugin til design af rollespil og simuleringer i dansk gymnasieundervisning (STX). Bygger på evidensbaseret pædagogik med 10 designprincipper, 8 rollespilsformater og struktureret debriefing.

## Hvad pluginet gør

- **Designer rollespil** baseret på fagligt emne, elevgruppe og praktisk ramme
- **Genererer Word-dokumenter** med rollekort (normalversion som standard, støtte/stærk efter ønske), lærerguider, elevintroduktioner og cheatsheats
- **Laver miniversioner** (10-20 min) af eksisterende rollespil eller fra bunden
- **Bygger digitale værktøjer** (AI-rådgiver, facit-beregner, lærershow, webside, video) ud fra en teknisk reference med afprøvede mønstre
- **Kører kvalitetssikring** — konsistenstjek + dansk sprogcheck — før levering
- **Understøtter 8 formater:** Forhandling, krisehåndtering, lev-et-liv, konsekvens-kredsløb, retssag, bestyrelse, parlamentarisk lovproces, interaktiv virksomhedssimulation

## Struktur

```
rollespilsdesigner/
├── .claude-plugin/plugin.json
├── README.md
└── skills/
    ├── nyt-rollespil/       ← Start nyt rollespilsdesign
    ├── miniversion/         ← Miniversion (forløb og metode samlet)
    ├── designprincipper/    ← Faglig rygrad: 10 principper + 8 formater
    ├── rollekort/           ← Docx-produktion: farver, margener, layout
    │   └── references/template-kode.md
    ├── laererguide/         ← Lærerguide: 12 obligatoriske sektioner + RAS
    ├── cheatsheet/          ← Cheatsheets: spørgsmål + modelbesvarelser
    ├── sprogtjek/           ← Dansk retskrivning + QA-tjekliste
    │   └── scripts/sprogtjek.py
    ├── projektregler/       ← Ingen ritualer, normalversion nok, beregner-tjek
    ├── digitale-tillaeg/    ← Digitale værktøjer: designregler
    │   └── references/teknik.md
    └── konsistenstjek/      ← Kvalitetssikring af materialer
```

I `evals/` ligger automatiske triggertests (`claude plugin eval plugins/rollespilsdesigner`) og en plan for de tests, der skal køres i Cowork. Se `evals/README.md`.

## Pipeline

Skillsene kører i en fast rækkefølge — du behøver kun starte med en command, resten sker automatisk.

**Fuldt rollespil** (`/rollespilsdesigner:nyt-rollespil`):
```
nyt-rollespil → design → rollekort → lærerguide → materiale → (digitale tillæg) → sprogtjek → konsistenstjek → levér
```

`projektregler` gælder hele vejen og overstyrer de øvrige skills.

**Hvem kender hvem:** `nyt-rollespil` har en oversigtstabel over alle skills. Alle produktionsskills peger på projektreglerne, og `digitale-tillaeg` peger på designprincipper, projektregler og konsistenstjek, som også har et tjek af beregner og digitale dele.

**Miniversion** (`/rollespilsdesigner:miniversion`):
```
miniversion → rollekort → sprogtjek → konsistenstjek → levér
```

## Skills

Kommandoerne skrives med plugin-navnet foran, fx `/rollespilsdesigner:rollekort`.

| Skill | Type | Trigger |
|-------|------|---------|
| `nyt-rollespil` | Indgang | "nyt rollespil", "design et rollespil" |
| `miniversion` | Indgang | "miniversion", "kort version", "simplificér", "kan vi lave det kortere" |
| `designprincipper` | Auto | Design-beslutninger, format-valg, brainstorming |
| `rollekort` | Auto | Docx-generering af rollekort og materialer |
| `laererguide` | Auto | Produktion af lærerguider |
| `cheatsheet` | Auto | Cheatsheats, modelbesvarelser, facitlister |
| `sprogtjek` | Auto | Sprogcheck, korrektur, dansk tekst |
| `projektregler` | Auto | Regler der overstyrer de øvrige skills (ritualer, versioner) |
| `digitale-tillaeg` | Auto | AI-rådgiver, facit-beregner, lærershow, webside, video |
| `konsistenstjek` | Auto | Kvalitetssikring, "er det færdigt", "klar til print" |

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
