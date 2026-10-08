# kennethsplugins

Plugins til dansk gymnasieundervisning (STX), samlet i én marketplace.

| Plugin | Hvad det gør | Skills |
|--------|--------------|--------|
| [`rollespilsdesigner`](plugins/rollespilsdesigner/README.md) | Design af rollespil og simuleringer: rollekort, lærerguider, miniversioner, digitale værktøjer og kvalitetssikring | 10 |
| [`bloom`](plugins/bloom) | Arbejdsspørgsmål til fagtekster efter Blooms taksonomi: fuldt sæt, lektiespørgsmål, skabe-spørgsmål, vurdering af spørgsmål og tre-faset time | 6 |
| [`blooket`](plugins/blooket) | Blooket-quizzer som importklar CSV-fil ud fra undervisningsmateriale | 2 |

## Kommandoer

Skrives med plugin-navnet foran, fx `/bloom:`. Skillene er navngivet efter det, de gør:

| Kommando | Hvad den gør |
|----------|--------------|
| `/rollespilsdesigner:nyt-rollespil` | Designer et nyt rollespil sammen med dig |
| `/rollespilsdesigner:miniversion` | Kort version (10 til 20 minutter) af et rollespil |
| `/rollespilsdesigner:rollekort` | Rollekort og elevintroduktion som Word-filer |
| `/rollespilsdesigner:laererguide` | Lærerguide med faseovergange og debriefing |
| `/rollespilsdesigner:cheatsheet` | Cheatsheet med modelsvar |
| `/rollespilsdesigner:konsistenstjek` | Kvalitetssikring før print |
| `/rollespilsdesigner:sprogtjek` | Sprogcheck af materialerne |
| `/rollespilsdesigner:digitale-tillaeg` | AI-rådgiver, facit-beregner og andre digitale dele |
| `/bloom:spoergsmaal-til-tekst` | Komplet sæt arbejdsspørgsmål til en tekst, to versioner og taxonomy table |
| `/bloom:lektiespoergsmaal` | 3 lektiespørgsmål på Huske/Forstå |
| `/bloom:skabe-opgaver` | 8 til 12 kreative skabe-spørgsmål |
| `/bloom:vurder-spoergsmaal` | Vurdering og forbedring af eksisterende spørgsmål |
| `/bloom:planlaeg-time` | Tre-faset time med spørgsmål og arbejdsformer |
| `/blooket:lav-quiz` | Blooket-quiz som CSV-fil |

`designprincipper` og `projektregler` (rollespil), `spoergsmaalsregler` (Bloom) og `quizformat` (Blooket) er baggrundsviden, som de andre skills læser. De kan også udløses direkte, men står ikke i kommandomenuen.

## Installation

**Claude Cowork og claude.ai:** tilføj en marketplace med adressen `KennethEU/kennethsplugins`, og vælg de plugins, du vil have.

**Claude Code:**
```
claude plugin marketplace add KennethEU/kennethsplugins
claude plugin install rollespilsdesigner@kennethsplugins
claude plugin install bloom@kennethsplugins
claude plugin install blooket@kennethsplugins
```

## Struktur

```
kennethsplugins/
├── .claude-plugin/marketplace.json     ← kataloget over plugins
└── plugins/
    ├── rollespilsdesigner/             ← hvert plugin har sin egen mappe
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

### rollespilsdesigner 1.6.0 (oktober 2026)
- Skillene er omdøbt til sigende kommandonavne uden `rollespil-` foran (se plugin-READMEen for gammelt og nyt navn).

### bloom og blooket 1.1.0 (oktober 2026)
- Skillene er omdøbt, så kommandoerne forklarer sig selv uden at gentage plugin-navnet: `bloom-bloom` er nu `spoergsmaal-til-tekst`, `bloom-lektie` er `lektiespoergsmaal`, `bloom-skabe` er `skabe-opgaver`, `bloom-vurder` er `vurder-spoergsmaal`, `bloom-klasseflow` er `planlaeg-time`, `bloom-arbejdsspoergsmaal` er `spoergsmaalsregler`, `blooket` er `lav-quiz` og `blooket-quiz` er `quizformat`.

### oktober 2026
- Repository og marketplace omdøbt til `kennethsplugins`.
- Rollespilsdesigneren er flyttet til `plugins/rollespilsdesigner`.
- Nye plugins `bloom` og `blooket` (flyttet fra `uv`) og gennemgået efter samme principper som rollespilsdesigneren: skarpere beskrivelser med "Brug ikke til", MCP-kald fjernet, stier via `${CLAUDE_SKILL_DIR}`, begrundelser i stedet for HÅRD REGEL, indholdsfortegnelse i store referencer, 17 triggertests og test af CSV-scriptet.
- `generate_csv.py` læser nu en JSON-fil, stopper ved regelbrud og advarer, hvis det korrekte svar ligger skævt fordelt.
