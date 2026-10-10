# Casespilsdesigner

Et Cowork-plugin til design af casespil (også kaldet rollespil) og simuleringer i dansk gymnasieundervisning (STX). Bygger på evidensbaseret pædagogik med 10 designprincipper, 8 casespilsformater og struktureret debriefing.

## Hvad pluginet gør

- **Designer casespil** baseret på fagligt emne, elevgruppe og praktisk ramme
- **Genererer Word-dokumenter** med rollekort (normalversion som standard, støtte/stærk efter ønske), lærerguider, elevintroduktioner og cheatsheats
- **Laver miniversioner** (10-20 min) af eksisterende casespil eller fra bunden
- **Bygger digitale værktøjer** (AI-rådgiver, facit-beregner, lærershow, webside, spilintro med voiceover, video) ud fra en teknisk reference med afprøvede mønstre
- **Kører kvalitetssikring** — konsistenstjek + dansk sprogcheck — før levering
- **Understøtter 8 formater:** Forhandling, krisehåndtering, lev-et-liv, konsekvens-kredsløb, retssag, bestyrelse, parlamentarisk lovproces, interaktiv virksomhedssimulation

## Struktur

```
casespilsdesigner/
├── .claude-plugin/plugin.json
├── README.md
└── skills/
    ├── casespil-nyt/              ← Start nyt casespilsdesign
    ├── casespil-miniversion/      ← Miniversion (forløb og metode samlet)
    ├── casespil-designprincipper/ ← Faglig rygrad: 10 principper + 8 formater
    ├── casespil-rollekort/        ← Docx-produktion: farver, margener, layout
    │   └── references/template-kode.md
    ├── casespil-laererguide/      ← Lærerguide: 12 obligatoriske sektioner + RAS
    ├── casespil-cheatsheet/       ← Cheatsheets: spørgsmål + modelbesvarelser
    ├── casespil-sprogtjek/        ← Dansk retskrivning + QA-tjekliste
    │   └── scripts/sprogtjek.py
    ├── casespil-projektregler/    ← Ingen ritualer, normalversion nok, beregner-tjek
    ├── casespil-digitale-tillaeg/ ← Digitale værktøjer: designregler
    │   └── references/teknik.md
    └── casespil-konsistenstjek/   ← Kvalitetssikring af materialer
```

I `evals/` ligger automatiske triggertests (`claude plugin eval plugins/casespilsdesigner`) og en plan for de tests, der skal køres i Cowork. Se `evals/README.md`.

## Pipeline

Skillsene kører i en fast rækkefølge — du behøver kun starte med en command, resten sker automatisk.

**Fuldt casespil** (`/casespilsdesigner:casespil-nyt`):
```
casespil-nyt → design → rollekort → lærerguide → materiale → (digitale tillæg) → sprogtjek → konsistenstjek → levér
```

`casespil-projektregler` gælder hele vejen og overstyrer de øvrige skills.

**Hvem kender hvem:** `casespil-nyt` har en oversigtstabel over alle skills. Alle produktionsskills peger på projektreglerne, og `casespil-digitale-tillaeg` peger på designprincipper, projektregler og konsistenstjek, som også har et tjek af beregner og digitale dele.

**Miniversion** (`/casespilsdesigner:casespil-miniversion`):
```
miniversion → rollekort → sprogtjek → konsistenstjek → levér
```

## Skills

Kommandoerne skrives med plugin-navnet foran, fx `/casespilsdesigner:casespil-rollekort`.

| Skill | Type | Trigger |
|-------|------|---------|
| `casespil-nyt` | Indgang | "nyt casespil", "design et casespil" |
| `casespil-miniversion` | Indgang | "miniversion", "kort version", "simplificér", "kan vi lave det kortere" |
| `casespil-designprincipper` | Auto | Design-beslutninger, format-valg, brainstorming |
| `casespil-rollekort` | Auto | Docx-generering af rollekort og materialer |
| `casespil-laererguide` | Auto | Produktion af lærerguider |
| `casespil-cheatsheet` | Auto | Cheatsheats, modelbesvarelser, facitlister |
| `casespil-sprogtjek` | Auto | Sprogcheck, korrektur, dansk tekst |
| `casespil-projektregler` | Auto | Regler der overstyrer de øvrige skills (ritualer, versioner) |
| `casespil-digitale-tillaeg` | Auto | AI-rådgiver, facit-beregner, lærershow, webside, spilintro, video |
| `casespil-konsistenstjek` | Auto | Kvalitetssikring, "er det færdigt", "klar til print" |

## Anbefalet mappestruktur (Cowork)

```
min-casespilsmappe/
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
Du er casespilsdesigner til dansk gymnasieundervisning.
Skriv altid på dansk med korrekt retskrivning (æøå).
Brug aldrig faste minuttal i materialer — læreren styrer tempoet.
Brug "du" til læreren.
```

## Installation

I Claude: tilføj en marketplace med adressen `KennethEU/kennethsplugins` (se hovedsiden i repositoryet), og installér pluginet `casespilsdesigner` (installationsnavn `casespilsdesigner@kennethsplugins`). Alternativt kan zip-filen med pluginets indhold uploades direkte.

## Kompatibilitet

- **Claude Cowork** (primært) — fuld funktionalitet med filsystem-adgang
- **Claude Code** — fungerer som plugin
- **Claude.ai** — skills kan uploades individuelt via Settings > Skills

## Changelog

### v2.4.1 (oktober 2026)
- Nye regler efter gennemgang af, hvad `fjord2026` bruges til i casespil.dk: nøglen ligger aldrig sammen med det, den låser, et offentligt id (proxyens `appId`) er ikke en kode og kaldes `APP_ID`, hjemmelavet kryptering og SHA-256-tjek er ingen lås, og gamle lærerkataloger og lærer-pinkoder fjernes fra elevsiderne, når cockpittet overtager
- Opdateret i `casespil-projektregler` (tillæg 12 til 14), `casespil-digitale-tillaeg` (sikkerhedsafsnit og tjekliste) og `references/teknik.md`

### v2.4.0 (oktober 2026)
- Skills opdateret efter arkitektur- og sikkerhedsrevisionen på casespil.dk (dd294e8): læreradgang kun via lærer-assistenten med et personligt 1-klik link (`?token=` med 128 bit, 7 dage, standardtekst med DD-MM-YYYY), ingen korte koder, ingen `laerer.html` downloadside eller statiske masternøgler, ingen lokal dekrypteringsfallback, `history.replaceState`, nøgler i `data/keys.php` eller miljøet uden for git, ensartede svar og rate limiting (10 verify, 5 anmodninger, 3 mails i timen)
- Fælles motor: én `laerer-motor.js` i roden, aldrig kopier i spilmapper, 100 % agnostisk og datadrevet via `window.TEACHER_CONFIG`
- Små borde: Σ elever = N og kort = `max(elever, 1)` for stemmende roller. Roller uden elev deles af en naborolle og får alligevel et fysisk rollekort. Det tidligere åbne designvalg er afgjort
- Opdateret i `casespil-projektregler`, `casespil-digitale-tillaeg` (SKILL.md og `references/teknik.md`, afsnit 20, 24 og 25), `casespil-rollekort` (nyt afsnit om gruppeplanlægning og printliste) og `casespil-laererguide` (adgangsflow og små borde)

### v2.3.1 (oktober 2026)
- Afsnit 25 i `references/teknik.md` er opdateret efter casespil.dk (457fa0e), hvor tokentabel, 7 dages udløb og serverside verifikation nu er implementeret og fungerer. Ved en lokal kørsel af koden fandt gennemgangen fem fælder, som standarden nu kræver rettet: en kort kode på 24 bit uden rate limiting giver nøglen, nøglen er den samme for alle og står i kildekoden, klienten har en lokal omvej, der omgår udløbet, tokens gemmes i klartekst, og linket bliver stående i adresselinjen
- Tilsvarende punkter i `casespil-digitale-tillaeg` (adgangsafsnit og tjekliste) og `casespil-projektregler`

### v2.3.0 (oktober 2026)
- Ny adgangsstandard for lærere: ingen særskilt dokumentside med kodefelt (`laerer.html` er udfaset og sender straks videre til `laerer-assistent.html`), og al lærerindhold inklusive download af Word- og PDF-materialer ligger i ét lærercockpit
- Materialer som base64-ZIP i `bundle.files` i den krypterede `laererdata.js` (PBKDF2 og AES-256-GCM), dekrypteret i hukommelsen og hentet med ét klik. Ingen rå .docx eller .pdf på gættelige stier
- Personlige magic links og koder pr. skolemail, gyldige i 7 dage, med udløbsdatoen i mailen, en venlig udløbsbesked med formular til nyt link og øjeblikkelig mail til forhåndsgodkendte adresser og gymnasiedomæner via API. Ingen permanente fælles koder
- `references/teknik.md` har nyt afsnit 25 (flow, datamodel, mailtekst, endepunktsskitse, driftskrav og seks tests) og omskrevet afsnit 20. Afsnit 25 er et design, og endepunktsskitsen er kun kørt mod SQLite i hukommelsen
- Ærligt om casespil.dk (b987dfe): downloaden er samlet, men mailen indeholder stadig en fast kode pr. spil i kildekoden uden udløb, så de 7 dage endnu ikke kan håndhæves
- Eksempelkoderne i skillen er ændret til opdigtede værdier
- Ny triggertest `trigger-adgang-1`

### v2.2.1 (oktober 2026)
- Lærer-cockpittet er opdateret efter den hærdede udgave på casespil.dk og kontrolleret mod den: `masterHash` og SHA-256-tjek er væk (koden verificeres kun ved AES-GCM-dekrypteringen), gruppeplanens elever summerer til N for alle elevtal fra 4 til 60, Fjords projektteams viser det faktiske spænd, prompten bygges dynamisk af `faser`, `begreber` og `roller`, og skrivefeltet ligger inden for skærmen ved 800 px i begge spil
- Kravet til lærerkoden er skærpet: et spilpræfiks og mindst 12 tilfældige tegn (fx `AB-3f9c0e7d21b8`)
- Ny cockpit-test i `references/teknik.md` (bygger sit eget låste bundt, 18 kontroller bestået mod begge spil) og en gruppeplan, der viser både elever på roller (altid N) og kort at printe
- Ærligt om det, der stadig er åbent: motoren indeholder stadig spilspecifikke konstanter og ligger i tre kopier, og 23 af 57 elevtal har et bord med en stemmende rolle uden kort (Klima)

### v2.2.0 (oktober 2026)
- `casespil-digitale-tillaeg` har fået et nyt afsnit om lærerens cockpit (lærer-assistent): krypteret databundt, kontrol af lærerkoden ved selve dekrypteringen, én fælles motor med spillets fakta i datasættet, gruppe- og holdberegner for to spiltyper, printliste for papir, hybrid og digital, AI-sparring med streaming, der filtrerer tænketokens, og hurtigopslag. `references/teknik.md` har nyt afsnit 24 med afprøvet kode og tests
- Layoutregler: arbejdsbordet låses også, når der ligger en blok uden flex imellem (klassen `in-workspace`, `grid-template-rows: minmax(0, 1fr)`), gitter bruger `minmax(min(100%, 310px), 1fr)`, og vandrette menuer får `overflow-x: auto` (alt afprøvet ved 320 px)
- `casespil-projektregler`: AI-assistenter følger sprogreglerne og henter data fra datasættet, fælles kode har ingen spilspecifikke fakta, beregnere har én plan og invarianter, fortroligt lærermateriale ligger krypteret, og layout testes med langt indhold
- `casespil-laererguide`: regler for skæve elevtal, printtal for tre former og guiden som datakilde
- Fund ved gennemgang af første udgave af cockpittet (rettes i spillene): gruppeplan og printtal passede ikke sammen ved mange elevtal, `masterHash` gav en hurtig genvej til at gætte lærerkoden, fasenavnene i prompten afveg fra datasættet, og Fjords cockpit havde ingen layoutlås
- Ny triggertest `trigger-cockpit-1`

### v2.1.0 (oktober 2026)
- `casespil-digitale-tillaeg` er udvidet med erfaringerne fra Kommunalbudget (samfundsfag), så skillen dækker både erhvervsøkonomiske og samfundsfaglige casespil: valg af spiltype, pædagogiske principper for de digitale værktøjer, rådgiver uden forslagsknapper, startkrav som forberedelse og ikke som lås, fase- og kompromisregler, rådgiverens fanelayout på mobil, budget- og beslutningsværktøj, resultatkoder med kontrolsum, sammenligning på storskærm, krypteret lærerpakke, designsystem efter emne, billeder og forside, automatiserede tests og katalog på tværs af spil
- `references/teknik.md` har fået afsnit 16 til 23 og opdaterede afsnit 1 til 7, 9 og 13. Kode til budgetlogik, resultatkode, låsegenerator, logiktest og browsertest er afprøvet mod Kommunalbudgets egen kode
- Ærlig note om kodernes styrke: i Kommunalbudget kan alle fem 4-cifrede rollekoder slås op på under et sekund. Skillen beskriver, hvornår det er nok, og hvad der skal til, hvis skjult information skal tåle en målrettet elev
- Lektie om layout: et tre-kolonnet arbejdsbord skal låses til skærmens højde (fast `height`, `overflow: hidden`, `min-height: 0` og intern scroll), ellers skubber et langt rollekort skrivefeltet og tælleren ud af skærmen. Fejlen er gengivet og testet, og testskabelonen har en kontrol for den
- Ny triggertest `trigger-budget-1`

### v2.0.0 (oktober 2026)
- Pluginet og alle skills hedder nu `casespil` i stedet for `rollespil`. Pluginet `rollespilsdesigner` er blevet til `casespilsdesigner` (installationsnavn `casespilsdesigner@kennethsplugins`), og skillene har skiftet gruppenavn fra `rollespil-` til `casespil-`: `casespil-nyt`, `casespil-miniversion`, `casespil-rollekort`, `casespil-laererguide`, `casespil-cheatsheet`, `casespil-sprogtjek`, `casespil-konsistenstjek`, `casespil-digitale-tillaeg`, `casespil-designprincipper` og `casespil-projektregler`. Skriv `/casespil` i Cowork for at se hele gruppen
- Sproget i alle skills, README og materialer er nu casespil (fx casespilsside, `casespil.html` og menupunktet "Casespillet"). Ordet rollespil står kun som accepteret synonym i skillenes beskrivelser, så det stadig udløser dem, og i en ny ordvalgsregel i `casespil-projektregler`. Indholdet er ellers uændret
- Gamle navne står uændret i de ældre changelog-poster nedenfor
- Installationen skal gøres om: fjern `rollespilsdesigner` og tilføj `casespilsdesigner`

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
