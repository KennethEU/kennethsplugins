# kennethsplugins

Plugins til dansk gymnasieundervisning (STX), samlet i én marketplace.

| Plugin | Hvad det gør | Skills |
|--------|--------------|--------|
| [`casespilsdesigner`](plugins/casespilsdesigner/README.md) | Design af casespil (også kaldet rollespil) og simuleringer: rollekort, lærerguider, miniversioner, digitale værktøjer og kvalitetssikring | 10 |
| [`bloom`](plugins/bloom) | Arbejdsspørgsmål til fagtekster efter Blooms taksonomi: fuldt sæt, lektiespørgsmål, skabe-spørgsmål, vurdering af spørgsmål og tre-faset time | 6 |
| [`blooket`](plugins/blooket) | Blooket-quizzer som importklar CSV-fil ud fra undervisningsmateriale | 2 |

## Kommandoer

Hver skill hedder gruppen først og så det, den gør (`casespil-`, `bloom-`, `blooket-`), så de står samlet i menuen. Skriv `/casespil`, `/bloom` eller `/blooket` i Cowork for at se hele gruppen. I Claude Code kommer plugin-navnet også foran (`/bloom:bloom-lektiespoergsmaal`).

| Kommando | Hvad den gør |
|----------|--------------|
| `/casespilsdesigner:casespil-nyt` | Designer et nyt casespil sammen med dig |
| `/casespilsdesigner:casespil-miniversion` | Kort version (10 til 20 minutter) af et casespil |
| `/casespilsdesigner:casespil-rollekort` | Rollekort og elevintroduktion som Word-filer |
| `/casespilsdesigner:casespil-laererguide` | Lærerguide med faseovergange og debriefing |
| `/casespilsdesigner:casespil-cheatsheet` | Cheatsheet med modelsvar |
| `/casespilsdesigner:casespil-konsistenstjek` | Kvalitetssikring før print |
| `/casespilsdesigner:casespil-sprogtjek` | Sprogcheck af materialerne |
| `/casespilsdesigner:casespil-digitale-tillaeg` | AI-rådgiver, facit-beregner og andre digitale dele |
| `/bloom:bloom-spoergsmaal-til-tekst` | Komplet sæt arbejdsspørgsmål til en tekst, to versioner og taxonomy table |
| `/bloom:bloom-lektiespoergsmaal` | 3 lektiespørgsmål på Huske/Forstå |
| `/bloom:bloom-skabe-opgaver` | 8 til 12 kreative skabe-spørgsmål |
| `/bloom:bloom-vurder-spoergsmaal` | Vurdering og forbedring af eksisterende spørgsmål |
| `/bloom:bloom-planlaeg-time` | Tre-faset time med spørgsmål og arbejdsformer |
| `/blooket:blooket-lav-quiz` | Blooket-quiz som CSV-fil |

`casespil-designprincipper` og `casespil-projektregler` (casespil), `bloom-spoergsmaalsregler` (Bloom) og `blooket-quizformat` (Blooket) er baggrundsviden, som de andre skills læser. De kan også udløses direkte, men står ikke i kommandomenuen.

## Installation

**Claude Cowork og claude.ai:** tilføj en marketplace med adressen `KennethEU/kennethsplugins`, og vælg de plugins, du vil have.

**Claude Code:**
```
claude plugin marketplace add KennethEU/kennethsplugins
claude plugin install casespilsdesigner@kennethsplugins
claude plugin install bloom@kennethsplugins
claude plugin install blooket@kennethsplugins
```

## Struktur

```
kennethsplugins/
├── .claude-plugin/marketplace.json     ← kataloget over plugins
└── plugins/
    ├── casespilsdesigner/              ← hvert plugin har sin egen mappe
    │   ├── .claude-plugin/plugin.json
    │   └── skills/...
    ├── bloom/
    └── blooket/
```

## Tests

Hvert plugin har en `evals/`-mappe med triggertests, der tjekker, at den rigtige skill vælges (`claude plugin eval plugins/<navn>`). Kør `claude plugin validate . --strict` efter hver ændring.

## Bemærkninger

- Skillene i `bloom` og `blooket` er flyttet hertil fra pluginet `uv`. Har du begge installeret, ligger skillene to steder og kan udløse hinanden. Fjern dem fra `uv`, når du har afprøvet de nye.
- Pluginsene bruger ingen MCP-forbindelser. De tidligere kald til en undervisningsdatabase er fjernet.
- `blooket` bruger scriptet `generate_csv.py`, som tjekker spørgsmålene og skriver Blooket-filen. Test det med `python3 plugins/blooket/tests/test_generate_csv.py`.

## Changelog

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
