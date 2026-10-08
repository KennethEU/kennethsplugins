---
name: bloom-bloom
description: Fuld Bloom-kørsel med to versioner og taxonomy table. Brug når læreren siger "lav arbejdsspørgsmål", "Bloom-spørgsmål", "spørgsmål til denne tekst", "analyser teksten med Bloom", eller uploader en fagtekst og vil have et komplet sæt spørgsmål på alle taksonomiske niveauer.
argument-hint: "[fagtekst eller emne]"
allowed-tools:
  - Read
  - Glob
---

# Fuld Bloom-kørsel

Generér et komplet sæt arbejdsspørgsmål baseret på Bloom's Reviderede Taksonomi med to versioner og taxonomy table.

## Leverancer

1. **Version 1 — Taksonomisk progression:** Spørgsmål organiseret efter de 6 Bloom-niveauer (Huske → Skabe) plus 2-3 brede hovedspørgsmål.
2. **Version 2 — Tekstnær struktur:** Spørgsmål organiseret efter tekstens afsnit med overordnede, uddybende og detaljespørgsmål.
3. **Taxonomy Table:** Oversigt over spørgsmålsfordelingen med balance-kommentar og anbefalinger til klasserum.

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../bloom-arbejdsspoergsmaal/SKILL.md` og forstå reglerne.
2. **Analysér teksten** stille: hovedemne, fagbegreber, afsnitsstruktur, teksttype.

### Gate 1: Bekræft analyse — VENT på OK

Re-ground: "Vi er ved **Gate 1** — jeg har analyseret teksten. Her er hvad jeg fandt."

Præsentér en kort analyse for læreren:

- **Hovedemne:** [Emnet]
- **Teksttype:** [Argumenterende / informerende / analyserende]
- **Centrale begreber:** [4-6 nøglebegreber fra teksten]
- **Tekstlængde:** [Kort / normal / lang] → forventet **[X-Y] spørgsmål**
- **Forventet Bloom-fordeling:** [Fx "tung i Forstå/Anvende pga. informerende tekst"]

Giv en anbefaling: "Jeg anbefaler at vi fokuserer på [X begreber] og laver ca. [Y] spørgsmål med vægt på [niveau] fordi [begrundelse]."

Spørg: "Passer det med dit fokus? Er der begreber du vil prioritere — eller niveauer du vil have flere/færre af?"

**VENT** på svar. Justér fokus hvis læreren ønsker det.

### Gate 2: Generér og præsentér

3. **Generér Version 1** med spørgsmål på alle 6 niveauer. Læs `${CLAUDE_SKILL_DIR}/../bloom-arbejdsspoergsmaal/references/bloom-verber.md` for korrekte verber.
4. **Generér Version 2** der følger tekstens kronologi med Bloom-niveau i parentes.
5. **Kvalitetstjek** mod reglerne: ét spørgsmål ad gangen, ingen forbudte verber, besvarligt fra teksten. Læs `${CLAUDE_SKILL_DIR}/../bloom-arbejdsspoergsmaal/references/forbudte-formuleringer.md` ved tvivl.
6. **Taxonomy Table** — læs `${CLAUDE_SKILL_DIR}/../bloom-arbejdsspoergsmaal/references/taxonomy-table-template.md` og udfyld med antal + kommentar.

Præsentér begge versioner + taxonomy table. Afslut med:

> "Vil du justere noget? Fx flytte spørgsmål mellem niveauer, ændre sværhedsgrad, eller tilføje/fjerne spørgsmål?"

---

## Completion Status

- **DONE** — Begge versioner + taxonomy table leveret
- **DONE_WITH_CONCERNS** — Leveret, men taksonomisk balance er skæv eller begreber mangler
- **BLOCKED** — Teksten er for kort/uklar til at generere meningsfulde spørgsmål
- **NEEDS_CONTEXT** — Mangler information om fag, niveau eller fokusområde
