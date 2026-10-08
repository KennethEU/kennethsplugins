# kennethsplugins

Plugins til dansk gymnasieundervisning (STX), samlet i én marketplace.

| Plugin | Hvad det gør | Skills |
|--------|--------------|--------|
| [`rollespilsdesigner`](plugins/rollespilsdesigner/README.md) | Design af rollespil og simuleringer: rollekort, lærerguider, miniversioner, digitale værktøjer og kvalitetssikring | 10 |
| [`bloom`](plugins/bloom) | Arbejdsspørgsmål til fagtekster efter Blooms taksonomi: fuldt sæt, lektiespørgsmål, skabe-spørgsmål, vurdering af spørgsmål og tre-faset time | 6 |
| [`blooket`](plugins/blooket) | Blooket-quizzer som importklar CSV-fil ud fra undervisningsmateriale | 2 |

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

### oktober 2026
- Repository og marketplace omdøbt til `kennethsplugins`.
- Rollespilsdesigneren er flyttet til `plugins/rollespilsdesigner`.
- Nye plugins `bloom` og `blooket` (flyttet fra `uv`) og gennemgået efter samme principper som rollespilsdesigneren: skarpere beskrivelser med "Brug ikke til", MCP-kald fjernet, stier via `${CLAUDE_SKILL_DIR}`, begrundelser i stedet for HÅRD REGEL, indholdsfortegnelse i store referencer, 17 triggertests og test af CSV-scriptet.
- `generate_csv.py` læser nu en JSON-fil, stopper ved regelbrud og advarer, hvis det korrekte svar ligger skævt fordelt.
