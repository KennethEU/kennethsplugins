# kennethsplugins

Plugins til dansk gymnasieundervisning (STX), samlet i én marketplace.

| Plugin | Hvad det gør | Skills |
|--------|--------------|--------|
| [`casespilsdesigner`](plugins/casespilsdesigner/README.md) | Design af casespil (også kaldet rollespil) og simuleringer: rollekort, lærerguider, miniversioner, digitale værktøjer og kvalitetssikring | 10 |
| [`bloom`](plugins/bloom) | Arbejdsspørgsmål til fagtekster efter Blooms taksonomi: fuldt sæt, lektiespørgsmål, skabe-spørgsmål, vurdering af spørgsmål og tre-faset time | 6 |
| [`blooket`](plugins/blooket) | Blooket-quizzer som importklar CSV-fil ud fra undervisningsmateriale | 2 |
| [`klasseledelse`](plugins/klasseledelse) | Planlægning og vurdering af lektioner, så alle elever deltager, holdt op mod forskningen | 3 |
| [`cl-oevelser`](plugins/cl-oevelser) | Inspirationskatalog med CL-øvelser: find og tilpas, udvikl nye og kombinér til forløb, holdt op mod SPIL-principperne | 4 |
| [`dida`](plugins/dida) | Lektionsplan som JSON-fil til storskærmsvisning på dida.dk/plan | 1 |
| [`udretterdagsorden`](plugins/udretterdagsorden) | Udretterdagsordener til gruppearbejde: selvkørende protokol med roller, individuel tænketid, pause og fælles produkt, til dida.dk eller Word, med idésparring om struktur | 3 |
| [`modulplanlaegger`](plugins/modulplanlaegger) | Forløb og modulrækker ud fra didaktisk viden: mål, progression, evaluering og fagdidaktik, med videresendelse til de andre plugins | 2 |

## Kommandoer

Hver skill hedder gruppen først og så det, den gør (`casespil-`, `bloom-`, `blooket-`, `klasseledelse-`, `cl-`, `dagsorden-`, `dida-`, `didaktik-`), så de står samlet i menuen. Skriv `/casespil`, `/bloom`, `/blooket`, `/klasseledelse`, `/cl`, `/dagsorden`, `/dida` eller `/didaktik` i Cowork for at se hele gruppen. I Claude Code kommer plugin-navnet også foran (`/bloom:bloom-lektiespoergsmaal`).

| Kommando | Hvad den gør |
|----------|--------------|
| `/casespilsdesigner:casespil-nyt` | Designer et nyt casespil sammen med dig |
| `/casespilsdesigner:casespil-miniversion` | Kort version (10 til 20 minutter) af et casespil |
| `/casespilsdesigner:casespil-rollekort` | Rollekort og elevintroduktion som Word-filer |
| `/casespilsdesigner:casespil-laererguide` | Lærerguide med faseovergange og debriefing |
| `/casespilsdesigner:casespil-cheatsheet` | Cheatsheet med modelsvar |
| `/casespilsdesigner:casespil-konsistenstjek` | Kvalitetssikring før print |
| `/casespilsdesigner:casespil-ekstern-review` | Ekstern AI-gennemgang i runder med verificering af fund |
| `/casespilsdesigner:casespil-sprogtjek` | Sprogcheck af materialerne |
| `/casespilsdesigner:casespil-digitale-tillaeg` | AI-rådgiver, facit-beregner og andre digitale dele |
| `/bloom:bloom-spoergsmaal-til-tekst` | Sæt arbejdsspørgsmål til en tekst i taksonomisk progression. Tekstnær version og taxonomy table på opfordring |
| `/bloom:bloom-lektiespoergsmaal` | 3 lektiespørgsmål på Huske/Forstå |
| `/bloom:bloom-skabe-opgaver` | 6 kreative skabe-spørgsmål, op til 12 på opfordring |
| `/bloom:bloom-vurder-spoergsmaal` | Vurdering og forbedring af eksisterende spørgsmål |
| `/bloom:bloom-planlaeg-time` | Tre-faset time med spørgsmål og arbejdsformer, til 45 eller 90 minutter |
| `/blooket:blooket-lav-quiz` | Blooket-quiz som CSV-fil |
| `/klasseledelse:klasseledelse-planlaeg-lektion` | Lektion eller modul med drejebog, hvor alle er med |
| `/klasseledelse:klasseledelse-vurder-plan` | Vurdering af en plan med deltagelseskort og konkrete omskrivninger |
| `/cl-oevelser:cl-find-oevelse` | Finder og tilpasser en CL-øvelse fra kataloget |
| `/cl-oevelser:cl-ny-oevelse` | Udvikler en ny CL-øvelse, eller gør en aktivitet til CL |
| `/cl-oevelser:cl-forloeb` | Kombinerer CL-øvelser til et modul eller forløb |
| `/dida:dida-plan` | Omsætter en plan til en fil til dida.dk/plan |
| `/udretterdagsorden:dagsorden-lav` | Udretterdagsorden til gruppearbejde ud fra emne, fag og tid, til dida.dk eller Word |
| `/udretterdagsorden:dagsorden-ide` | Foreslår 2 til 3 strukturer for gruppearbejdet og laver derefter dagsordenen |
| `/modulplanlaegger:didaktik-planlaeg-forloeb` | Planlægger et forløb eller en modulrække og sender modulerne videre til de andre skills |

`casespil-designprincipper` og `casespil-projektregler` (casespil), `bloom-spoergsmaalsregler` (Bloom), `blooket-quizformat` (Blooket), `klasseledelse-principper` (klasseledelse), `cl-principper` (CL), `dagsorden-principper` (udretterdagsorden) og `didaktik-principper` (modulplanlægger) er baggrundsviden, som de andre skills læser. De kan også udløses direkte, men står ikke i kommandomenuen.

## Hurtigt og kort

Skillene til daglig planlægning (`klasseledelse`, `bloom`, `cl-oevelser`, `dida`, `udretterdagsorden` og `modulplanlaegger`) følger samme arbejdsgang:

- **Hurtig eller grundig:** skillen spørger først, om du vil have det hurtigt eller en grundigere planlægning. Hurtigt betyder ingen flere spørgsmål, antagelserne i én linje øverst og aflevering med det samme. Grundigt betyder afklaring og godkendelsestrin undervejs. Skriver du "hurtigt" eller "bare lav den", eller beder du om sparring ("hvad synes du?"), springer den spørgsmålet over, og valget gælder resten af samtalen.
- **Kort som standard:** du får det, du skal bruge i timen. Deltagelseskort, taxonomy table, fuld øvelsesbeskrivelse og lignende kommer, når du beder om dem. Det står i den sidste linje af svaret, hvad du kan bede om.
- **Forløbsmappen:** findes der en `forloeb.md` fra `didaktik-planlaeg-forloeb`, læser de andre skills rammerne dér og gemmer deres materialer i forløbets mappe med modulnummeret først i filnavnet.
- **Ingen dobbelt godkendelse:** når én skill sender videre til en anden, fx en godkendt drejebog til `dida-plan`, laver modtageren resultatet direkte.

Reglerne står i afsnittet "Arbejdsgang" i hvert plugins principfil. `python3 tjek_arbejdsgang.py` tjekker, at afsnittet er ens i alle fem.

## Installation

**Claude Cowork og claude.ai:** tilføj en marketplace med adressen `KennethEU/kennethsplugins`, og vælg de plugins, du vil have.

**Claude Code:**
```
claude plugin marketplace add KennethEU/kennethsplugins
claude plugin install casespilsdesigner@kennethsplugins
claude plugin install bloom@kennethsplugins
claude plugin install blooket@kennethsplugins
claude plugin install klasseledelse@kennethsplugins
claude plugin install cl-oevelser@kennethsplugins
claude plugin install dida@kennethsplugins
claude plugin install udretterdagsorden@kennethsplugins
claude plugin install modulplanlaegger@kennethsplugins
```

**Antigravity (Gemini):** scriptet `update_plugins.sh` henter den nyeste version og kobler alle plugins til Antigravity. Det forventer en klon af repoet i `~/.gemini/repos/kennethsplugins` og mappen `~/.gemini/config/plugins`. Første gang:
```
git clone git@github.com:KennethEU/kennethsplugins.git ~/.gemini/repos/kennethsplugins
mkdir -p ~/.gemini/config/plugins
```
Kør derefter scriptet, når du vil opdatere, eller når der er kommet et nyt plugin:
```
bash ~/.gemini/repos/kennethsplugins/update_plugins.sh
```
Scriptet kører `git pull`, laver en genvej `plugin.json` i hver plugin-mappe (Antigravity leder efter den dér og ikke i `.claude-plugin/`) og en genvej fra `~/.gemini/config/plugins/<navn>` til hvert plugin. Fordi det er genveje, slår rettelser i et eksisterende plugin igennem uden at køre scriptet igen.

## Struktur

```
kennethsplugins/
├── .claude-plugin/marketplace.json     ← kataloget over plugins
├── update_plugins.sh                   ← opdaterer og kobler plugins til Antigravity
├── tjek_arbejdsgang.py                 ← tjekker, at "Arbejdsgang" er ens i principfilerne
└── plugins/
    ├── casespilsdesigner/              ← hvert plugin har sin egen mappe
    │   ├── .claude-plugin/plugin.json
    │   └── skills/...
    ├── bloom/
    ├── blooket/
    ├── klasseledelse/
    ├── cl-oevelser/
    ├── dida/
    ├── udretterdagsorden/
    └── modulplanlaegger/
```

## Tests

Hvert plugin har en `evals/`-mappe med triggertests, der tjekker, at den rigtige skill vælges (`claude plugin eval plugins/<navn>`). Kør `claude plugin validate . --strict` efter hver ændring.

## Bemærkninger

- Skillene i `bloom` og `blooket` er flyttet hertil fra pluginet `uv`. Har du begge installeret, ligger skillene to steder og kan udløse hinanden. Fjern dem fra `uv`, når du har afprøvet de nye.
- Pluginsene bruger ingen MCP-forbindelser. De tidligere kald til en undervisningsdatabase er fjernet.
- `blooket` bruger scriptet `generate_csv.py`, som tjekker spørgsmålene og skriver Blooket-filen. Test det med `python3 plugins/blooket/tests/test_generate_csv.py`.
- `udretterdagsorden` tjekker dagsordenen med `validate-dagsorden.py` og laver Word-udgaven med `generate-dagsorden.js`, som kræver npm-pakken `docx` (kør `npm install` i `plugins/udretterdagsorden/skills/dagsorden-principper/scripts`).

## Changelog

### bloom 1.4.0, blooket 1.3.0, cl-oevelser 1.5.1, klasseledelse 1.13.1 og udretterdagsorden 1.1.1 (november 2026)
- **Afprøvning før aflevering:** skillene prøver nu selv det af, eleverne skal svare på, i stedet for kun at tjekke formuleringen. Baggrunden er et sæt lektiespørgsmål, hvor tre af fire først faldt, da læreren selv bad om en elevtest.
- `bloom`: nyt afsnit "Afprøvning på teksten" i `bloom-spoergsmaalsregler` med facit-test (skriv svaret, og find stedet i teksten), elevtest (svar som en middelmådig elev: stopper eleven for tidligt, kan svaret skrives af, slipper et tomt svar igennem, kan stedet findes) og ikke-læst-test til lektie. Alle fem skills kører den stille, også når spørgsmål omformuleres eller vælges ud, og skriver kun det, der ikke kunne afgøres. Facit kan fås på opfordring. `bloom-vurder-spoergsmaal` afprøver nu også lærerens egne spørgsmål på teksten.
- `blooket`: nyt trin "Prøv quizzen af" (svar uden facit, kun ét svar kan forsvares, kan ikke gættes, kan nås på tiden). `generate_csv.py` advarer, når det rigtige svar oftest er det længste.
- `cl-find-oevelse`, `cl-forloeb`, `klasseledelse-planlaeg-lektion` og `dagsorden-lav` har fået afprøvningen som punkt i kvalitetstjekket.

### klasseledelse 1.13.0, bloom 1.3.0, cl-oevelser 1.5.0, dida 1.1.0, udretterdagsorden 1.1.0 og modulplanlaegger 0.2.0 (november 2026)
- **Hurtig-tilstand og kort output** i alle skills til daglig planlægning, beskrevet i et fælles afsnit "Arbejdsgang" i principfilerne. Skillene spørger først, om det skal være hurtigt eller grundigt. Hurtigt springer spørgsmål og godkendelse over og afleverer en kort version. Resten kommer på opfordring.
- `klasseledelse-planlaeg-lektion` afleverer mål, drejebog, køreplan og tre linjer til læreren. Instruktionsslides, deltagelseskort, fremmødetabel og planens vægt er flyttet til den grundige udgave.
- `bloom`: ét sæt i taksonomisk progression som standard, 3 lektiespørgsmål uden godkendelsestrin, 6 skabe-spørgsmål, kort vurdering med forbedret sæt og en ny skabelon til 90 minutter i `bloom-planlaeg-time` med lektietjek som genkaldelse og individuel skrivning til sidst. Tankestreger er fjernet.
- `cl-oevelser`: kort øvelsesbeskrivelse som standard, fuld skabelon på opfordring. `cl-principper` har nu det rigtige antal øvelser fra søgning (29).
- **Forløbsmappen** bruges af alle: skillene læser `forloeb.md`, når den findes, og gemmer materialer med modulnummer. `dida-plan` laver filen direkte, når planen lige er godkendt.
- `dagsorden-ide` gentager ikke længere designreglerne fra `dagsorden-lav`.
- Nyt script `tjek_arbejdsgang.py`, `.gitignore` i evals for `dida` og `modulplanlaegger`, og præfikserne `dida-` og `didaktik-` står nu i oversigten.

### cl-oevelser 1.4.0 (november 2026)
- Seks nye øvelser fra søgning på tysk, spansk, japansk og koreansk: Dækkeserviet, Læretempo-duet, Blyanter i midten, Tre minutters stop, Ekspertgrupper med før og efter og Havruta. Varianterne 1-2-4 og Holdpoint for fremgang (STAD). Ekspertgrupper har fået et forbehold, fordi lodtrukne forsøg ikke fandt ekstra læring. Kataloget har nu 44 øvelser, og `cl-find-oevelse` viser højst 8 til 10 ad gangen, når læreren vil se muligheder.

### cl-oevelser 1.3.0 (november 2026)
- Otte nye øvelser fra Kagans strukturer: Nummererede hoveder, Afsløring, Taleperler, Gentag før du taler, Team, par, alene, Fordel pointene, Find den falske og Giv én, få én. Træner og løser har fået varianten Par tjekker par, og Karrusel-feedback har fået Gallerivandring. Kataloget har nu 38 øvelser.

### cl-oevelser 1.2.1 (november 2026)
- Tavlegrupper har fået seks varianter, der kan bruges i alle fag: citat eller kilde på tavlen, vandring med spørgsmål, overblik til repetition, model eller tankeeksperiment, tjek af noterne og lektie som refleksionsspørgsmål.

### cl-oevelser 1.2.0 og klasseledelse 1.12.0 (november 2026)
- Ny øvelse i kataloget, Tavlegrupper, efter Det tænkende klasserum (Liljedahl): tilfældige grupper på tre, lodrette tavler, én tusch på skift og opsamling ud fra tavlerne. Kataloget har nu 30 øvelser. `evidens.md` har et afsnit om metoden med kritikken og danske erfaringer, og principperne nævner synligt gruppearbejde.

### klasseledelse 1.11.0 og modulplanlaegger 0.1.5 (november 2026)
- Rosenshine (2012), IES om læsning hos unge (2008), Dunlosky m.fl. (2013) og Deans for Impact er læst og står i `evidens.md`. Nyt: korte besøg ved bordene, en plan for elever på forskelligt niveau, eksplicit undervisning i fagord og læsestrategier, selvtest frem for genlæsning, cases med samme mekanisme og aldrig "Er der nogen spørgsmål?" som tjek. Forløbsplanlæggeren får ugentlig og månedlig repetition og studieteknik.

### klasseledelse 1.10.0 og modulplanlaegger 0.1.4 (november 2026)
- Archer og Hughes, *Explicit Instruction*, kapitel 1 og 2: modulets start med fast signal, mål, relevans og tjek af forudsætninger hos alle, vejledt øvelse i tre trin, succesrate på ca. 80 % som tommelfingerregel og skemaer, der organiserer viden. Forløbsplanlæggeren kobler delene til helheden i samme forløb.
- HLP 16 (Hughes, Riccomini og Morris): vejledningen trappes ned fra at fortælle over at spørge til at minde om, faste overgangssætninger, lektie kun når eleverne kan stoffet, og øvelse over tid med spredte gentagelser, blandede opgaver og genkaldelse med feedback. Forløbsplanlæggeren lægger spredt genkaldelse ind i modulrækken.

### klasseledelse 1.9.0 og modulplanlaegger 0.1.3 (november 2026)
- Metaanalysen af Direct Instruction (Stockard m.fl. 2018) er læst i fuld længde. `evidens.md` har nu de præcise tal, aldersfordelingen og DI's designprincipper. Nye begreber introduceres med eksempler og et ikke-eksempel i planlaeg-lektion og tjekkes i vurder-plan. Forløbsplanlæggeren lægger begreberne hver for sig først og samler dem senere.

### klasseledelse 1.8.0 og modulplanlaegger 0.1.2 (november 2026)
- Forskning om styring og aktivitet fra 15 år og op (PISA, metaanalyser om opdagelse og vejledning, universitetsstudier) står nu i `evidens.md`. Ny skærpelse 10: ren forelæsning og opdagelse uden hjælp er de svage yderpunkter. Planlaeg-lektion begrunder rækkefølgen med evidensmærke, vurder-plan nævner yderpunkterne, og forløbsplanlæggeren aftrapper styringen over forløbet.

### klasseledelse 1.7.0 og modulplanlaegger 0.1.1 (november 2026)
- Direct Instruction er gennemgået: metaanalysen fra 2018, debatten om Project Follow Through, vejledt instruktion og kritikken af Rosenshines principper står nu med evidensmærker i `evidens.md`. Principperne har en ny skærpelse: brug DI's principper, ikke programmerne. `didaktik-principper` har et kort afsnit om styring og forhåndsviden.

### klasseledelse 1.6.1, cl-oevelser 1.1.2 og udretterdagsorden 1.0.1 (november 2026)
- `klasseledelse-planlaeg-lektion`, `klasseledelse-vurder-plan` og `cl-forloeb` tilbyder nu `dagsorden-lav`, når en plan har en gruppefase på 20 minutter eller mere, hvor eleverne skal arbejde selv. `cl-find-oevelse` og `cl-ny-oevelse` sender hele gruppearbejdsprotokoller videre til `dagsorden-lav`, og `dagsorden-lav` tilbyder omvendt `dida-plan` og `cl-find-oevelse` efter levering.

### udretterdagsorden 1.0.0, dida 1.0.3 og bloom 1.2.4 (november 2026)
- Nyt plugin `udretterdagsorden` med skillene `dagsorden-lav` og `dagsorden-ide` og vidensbasen `dagsorden-principper`, flyttet hertil fra pluginet `uv` (`dag-dagsorden`, `dag-dagsorden-ide` og `udretterdagsorden`). Dagsordenen er en selvkørende protokol til gruppearbejde med rollerne pas-på-tur, pas-på-tid og pas-på-doc, individuel tænketid, pause og fælles produkt, og leveres som JSON til dida.dk/d/ eller som Word-dokument. Stierne går nu via `${CLAUDE_SKILL_DIR}`, henvisningerne til `uv` er væk, beskrivelserne har fået "Brug ikke til", og Word-scriptet har sin egen `package.json`. `dida-plan`, `bloom-planlaeg-time` og `bloom-spoergsmaalsregler` henviser nu til `dagsorden-lav`.

### cl-oevelser 1.1.0 (november 2026)
- Kataloget er udvidet fra 15 til 29 øvelser med strukturer til start, beregning, tekstarbejde, holdning og argumentation. De nye står adskilt fra Kenneths egne, med kilder og tydelig markering af, hvad der ikke er afprøvet eller bekræftet.

### cl-oevelser 1.0.1 (november 2026)
- Vises nu som "CL-øvelser". Det tekniske navn er stadig `cl-oevelser`.

### cl-oevelser 1.0.0, klasseledelse 1.1.1 og bloom 1.2.2 (november 2026)
- Nyt plugin `cl-oevelser` med fire skills og et katalog på 15 CL-øvelser. Hver øvelse har en SPIL-vurdering, skærpelser, hvor den er svag, og fagidéer til samfundsfag, mediefag og erhvervsøkonomi. `klasseledelse-planlaeg-lektion` og `bloom-planlaeg-time` henviser nu til pluginet ved enkelte CL-øvelser.

### klasseledelse 1.6.0 og dida 1.0.2 (november 2026)
- Nyt afsnit i principperne, "Enkelhed før aktivering": et aktivitetsbudget (højst 4 faser pr. 90 minutter, én ny struktur, højst 2 elevark), den vigtigste aktivitet senest 25 minutter før slut, "Hvad kan vi fjerne?" ved ændringer og materiale, der ikke ligner AI. `klasseledelse-planlaeg-lektion` og `klasseledelse-vurder-plan` tæller planen mod budgettet. `dida-plan` laver ét trin pr. fase.

### klasseledelse 1.5.0 (november 2026)
- Nye materialeregler i `klasseledelse-planlaeg-lektion`: elevark i klassisk stil uden etiketter, navnelinjer og andet, der ligner noget AI-lavet, printfiler delt efter modtager, en lærerpakke på højst 4 sider med drejebog og facit, og et tjek af, at opgaverne kan løses med teksterne.

### dida 1.0.1 og klasseledelse 1.4.1 (november 2026)
- `dida-plan` er nu beskrevet som et supplement til lærerens slides og ikke som en erstatning. Faser med gennemgang, figurer eller billeder skal stadig have slides.

### dida 1.0.0, klasseledelse 1.4.0, cl-oevelser 1.1.1 og bloom 1.2.3 (november 2026)
- Nyt plugin `dida` med skillen `dida-plan`, der omsætter en plan til en JSON-fil, som vises på storskærm på dida.dk/plan. Filen tjekkes med et lille script. `klasseledelse-planlaeg-lektion`, `klasseledelse-vurder-plan`, `cl-forloeb` og `bloom-planlaeg-time` tilbyder den.

### klasseledelse 1.3.0 (november 2026)
- Ny hovedregel: enkel plan, præcis opgave. Planer holdes på ca. 5 til 6 faser med én bærende aktivitet i et modul på 90 minutter, og opgaverne skrives færdigt.
- `klasseledelse-planlaeg-lektion` viser nu planens vægt og foreslår en forenkling, hvis den er tung. Overgange får egne minutter, slack er defineret, og gruppereglen prøves på hver række i fremmødetabellen. Instruktionsslides siger, hvornår eleverne er klar, og Gate 3 tilbyder også slides med regler i `references/materialer.md`.
- Principperne har nye afsnit om tid og planens vægt, grupper og fravær og noter. Blandede koder som L/A er væk fra deltagelseskortet. `klasseledelse-vurder-plan` tjekker tid, noter og gruppefaser. Alt nyt er mærket som praksisråd.

### klasseledelse 1.2.0 (november 2026)
- Planlægning leverer køreplan til eleverne og instruktionsslides, styrer skærme ved tekster kun på skærm, laver tabel over fremmøde og printliste og tilbyder printklare elevark og mærket lærerfacit. Begge skills spørger, om modulet er det sidste i forløbet, og vurderingen tjekker, om eleverne kan se, hvor de er.

### klasseledelse 1.1.2 (november 2026)
- Skillene kan tilbyde `cl-find-oevelse` og `cl-forloeb`, når en plan mangler en aktivitet.

### klasseledelse 1.1.0 (november 2026)
- Vurderingsskillen genkender en materialeliste og tilbyder at planlægge i stedet. Koderne A, G, E og L forklares hver gang, svage spørgsmål kan sendes til Bloom, og skillene er ærlige om materialer og tekster, de ikke kan læse. Kort version som standard, spørgsmål om pause og råd til elever, der ikke har læst.

### klasseledelse 1.0.1 (november 2026)
- Vurdering og planlægning tjekker nu faglig tyngde, udfordring til stærke elever og sammenhæng over tid. Minutgrænserne gælder ikke længere projekt- og gruppearbejde med produkt og nedslag, og nyt afsnit om sårbare elever. Planlægning kræver kun fag, tid og mål.

### klasseledelse 1.0.0 og bloom 1.2.1 (november 2026)
- Nyt plugin `klasseledelse` med tre skills til at planlægge og vurdere lektioner, så alle elever deltager. Principperne er holdt op mod forskningen i `references/evidens.md`. `bloom-planlaeg-time` henviser nu til det nye plugin ved timer uden fagtekst.

### casespilsdesigner 2.9.0 (oktober 2026)
- Bordregler fra spillets data, trafiklys-mandat, milliarddosering, aftalevisning og faseshow i casespil-skills. Se plugin-READMEen.

### casespilsdesigner 2.8.0 (oktober 2026)
- Opdateret efter 36 nye commits i casespil.dk: rådgiver i to kolonner, session og beskedidentitet, streng resultatkode, proxyens bytegrænse og fælles moduler. Se plugin-READMEen.

### casespilsdesigner 2.7.1 (oktober 2026)
- Fortsæt-knappen i rådgivere: højst én fortsættelse pr. svar, med test. Se plugin-READMEen.

### casespilsdesigner 2.7.0 (oktober 2026)
- Ny skill `casespil-ekstern-review`, tre mandatkategorier, sideparring ved dobbeltsidet print og regler for gemt tilstand og faner fra runderne på Kampen om velfærdsstaten. Se plugin-READMEen.

### casespilsdesigner 2.6.0 (oktober 2026)
- Opdateret efter 171 nye commits i casespil.dk: `materialer.json`, Lærersiden med single sign-on, rate limits og proxy, `Math.floor` til borde og nyt afsnit 26 om drift, privatliv og robusthed. Se plugin-READMEen.

### casespilsdesigner 2.5.1 (oktober 2026)
- Gendannet `references/teknik.md` efter en fejl i tidligere versioner, cockpit i to kolonner, jævn fordeling af ekstra elever (ny gruppeplan med test), retskrivning uden bindestreg og regler for proxyens dagsloft. Se plugin-READMEen.

### casespilsdesigner 2.5.0 (oktober 2026)
- To adskilte elevpakker (Uden AI og Med AI-rådgiver), dobbeltsidede rollekort (forside og bagside) og én samlet lærerpakke. Se plugin-READMEen.

### casespilsdesigner 2.4.1 (oktober 2026)
- Regler om nøgler og offentlige id'er: nøglen ligger aldrig sammen med det, den låser, `appId` er ikke en kode, ingen hjemmelavet kryptering, og gamle lærerkataloger ryddes. Se plugin-READMEen.

### casespilsdesigner 2.4.0 (oktober 2026)
- Skills opdateret efter sikkerhedsrevisionen på casespil.dk: personlige 1-klik links med 128-bit token og 7 dages udløb, ingen korte koder eller lokal fallback, nøgler uden for git, én agnostisk motor i roden og kort = `max(elever, 1)` ved små borde. Se plugin-READMEen.

### casespilsdesigner 2.3.1 (oktober 2026)
- Adgangsstandarden for lærere er skærpet efter gennemgang af den nye implementering på casespil.dk: kun det lange token er adgang, tokens hashes, `verify` har rate limiting, ingen lokal omvej og ingen nøgle i kildekoden. Se plugin-READMEen.

### casespilsdesigner 2.3.0 (oktober 2026)
- Ny adgangsstandard for lærere i `casespil-digitale-tillaeg`, `casespil-projektregler` og `casespil-laererguide`: al lærerindhold og download af Word- og PDF-materialer i ét cockpit (ingen separat `laerer.html`), materialer krypteret i `bundle.files`, og personlige magic links pr. skolemail, gyldige i 7 dage, med udløbsdato i mailen og venlig udløbsbesked. Se plugin-READMEen.

### casespilsdesigner 2.2.1 (oktober 2026)
- Lærer-cockpittet i `casespil-digitale-tillaeg` er opdateret efter den hærdede udgave på casespil.dk: ingen hurtig hash, gruppeplan der summerer til N, lærerkode med præfiks og 12 tilfældige tegn, dynamisk prompt og en cockpit-test. Se plugin-READMEen.

### casespilsdesigner 2.2.0 (oktober 2026)
- Lærerens cockpit (lærer-assistent) i `casespil-digitale-tillaeg`, nye regler i `casespil-projektregler`, og fordeling ved skæve elevtal i `casespil-laererguide`. Se plugin-READMEen.

### casespilsdesigner 2.1.0 (oktober 2026)
- `casespil-digitale-tillaeg` er udvidet med erfaringerne fra Kommunalbudget: budgetværktøj, resultatkoder, sammenligning, krypteret lærerpakke, rådgiver uden forslagsknapper og med fanelayout på mobil, samt automatiserede tests. Se plugin-READMEen.

### casespilsdesigner 2.0.0 (oktober 2026)
- Pluginet `rollespilsdesigner` er omdøbt til `casespilsdesigner`, og alle dets skills har skiftet gruppenavn fra `rollespil-` til `casespil-`. Sproget er nu casespil, og rollespil virker stadig som søgeord. Mappen er flyttet til `plugins/casespilsdesigner`. Installér igen med `claude plugin install casespilsdesigner@kennethsplugins`. Se plugin-READMEen for de nye skillenavne.

### navngivning 1.7.0 og 1.2.0 (oktober 2026)
- Alle skills har fået gruppenavnet foran (`rollespil-`, `bloom-`, `blooket-`), fordi Cowork kun viser skillens navn i kommandomenuen og ikke plugin-navnet. Skriver du `/bloom`, `/blooket` eller `/rollespil`, står hver gruppe nu samlet.

### rollespilsdesigner 1.6.0 (oktober 2026)
- Skillene er omdøbt til sigende kommandonavne uden `rollespil-` foran (se plugin-READMEen for gammelt og nyt navn).

### bloom og blooket 1.1.0 (oktober 2026)
- Skillene er omdøbt, så kommandoerne forklarer sig selv uden at gentage plugin-navnet: `bloom-bloom` er nu `spoergsmaal-til-tekst`, `bloom-lektie` er `lektiespoergsmaal`, `bloom-skabe` er `skabe-opgaver`, `bloom-vurder` er `vurder-spoergsmaal`, `bloom-klasseflow` er `planlaeg-time`, `bloom-arbejdsspoergsmaal` er `spoergsmaalsregler`, `blooket` er `lav-quiz` og `blooket-quiz` er `quizformat`.

### oktober 2026
- Repository og marketplace omdøbt til `kennethsplugins`.
- Rollespilsdesigneren er flyttet til `plugins/rollespilsdesigner`.
- Nye plugins `bloom` og `blooket` (flyttet fra `uv`) og gennemgået efter samme principper som rollespilsdesigneren: skarpere beskrivelser med "Brug ikke til", MCP-kald fjernet, stier via `${CLAUDE_SKILL_DIR}`, begrundelser i stedet for HÅRD REGEL, indholdsfortegnelse i store referencer, 17 triggertests og test af CSV-scriptet.
- `generate_csv.py` læser nu en JSON-fil, stopper ved regelbrud og advarer, hvis det korrekte svar ligger skævt fordelt.
