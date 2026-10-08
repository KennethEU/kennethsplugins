---
name: bloom-skabe
description: Generér 8-12 kreative niveau 6-spørgsmål (design, planlæg, producér). Brug når læreren siger "skabe-spørgsmål", "kreative opgaver", "niveau 6", "projektopgaver", "eleverne skal producere noget", eller vil have spørgsmål der kræver at eleverne designer, planlægger eller skaber noget nyt.
argument-hint: "[fagtekst eller emne]"
allowed-tools:
  - Read
  - Glob
---

# Skabe-spørgsmål (Bloom niveau 6)

Generér dedikerede kreative spørgsmål der kræver at eleverne designer, planlægger og producerer noget nyt. Velegnet til projektarbejde, større opgaver og eksamensforberedelse.

## Kategorier

- **Design/Konstruktion** — byg en model, kampagne, regelsæt
- **Planlægning** — lav en strategi eller handlingsplan
- **Generering** — udvikl hypoteser eller alternativer
- **Produktion** — skriv et scenarie, debatindlæg, interview
- **Integration** — kombinér elementer fra flere dele af teksten

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../bloom-arbejdsspoergsmaal/SKILL.md`.
2. **Læs Skabe-verberne** i `${CLAUDE_SKILL_DIR}/../bloom-arbejdsspoergsmaal/references/bloom-verber.md` (Niveau 6-sektionen).
3. **Identificér kreativt potentiale** i teksten: hvad kan redesignes, planlægges, genereres?

### Gate: Bekræft fokus — VENT på OK

Re-ground: "Jeg har analyseret teksten for kreativt potentiale. Her er hvad eleverne kan arbejde med på Skabe-niveau."

Præsentér for læreren:

- **Kreativt potentiale:** [3-4 muligheder fra teksten]
- **Anbefalede kategorier:** [Hvilke af de 5 kategorier der passer bedst]
- **Foreslået antal:** [8-12 spørgsmål, med fordeling på kategorier]

Spørg: "Hvilke kategorier vil du have flest spørgsmål i? Skal de bruges til gruppearbejde, individuelt projekt, eller eksamensforberedelse?"

**VENT** på svar.

Giv en anbefaling: "Jeg anbefaler at vi fokuserer på [kategori] fordi [begrundelse — fx teksten har stærkest potentiale til design/planlægning]."

### Generér og præsentér

4. **Formulér spørgsmål** i de valgte kategorier med dansk kontekst og videnstype angivet.
5. **Kvalitetstjek:** Kræver hvert spørgsmål at eleven SKABER noget nyt?

Afslut med: "Vil du justere ambitionsniveauet, tilføje flere i en bestemt kategori, eller ændre konteksten?"

---

## Completion Status

- **DONE** — Skabe-spørgsmål leveret i valgte kategorier
- **DONE_WITH_CONCERNS** — Leveret, men nogle spørgsmål er tæt på Evaluere-niveau
- **NEEDS_CONTEXT** — Mangler information om kontekst (gruppe/individ/eksamen)
