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

- `bloom-arbejdsspoergsmaal` og `blooket-quiz` kan bruge en MCP-forbindelse til en undervisningsdatabase (`mcp__undervisning__...`), hvis den er tilsluttet. Uden den virker skillene stadig, men de henter ikke fag, hold og forløb.
- Skillene i `bloom` og `blooket` er flyttet hertil fra pluginet `uv`. Har du begge installeret, ligger skillene to steder og kan udløses af hinanden. Fjern dem fra `uv`, når du har afprøvet de nye.

## Changelog

### oktober 2026
- Repository og marketplace omdøbt til `kennethsplugins`.
- Rollespilsdesigneren er flyttet til `plugins/rollespilsdesigner`.
- Nye plugins `bloom` og `blooket` (flyttet fra `uv`, nu med stier via `${CLAUDE_SKILL_DIR}` og triggertests).
