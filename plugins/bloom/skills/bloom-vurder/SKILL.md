---
name: bloom-vurder
description: Kvalitetstjek og forbedr eksisterende arbejdsspørgsmål mod Bloom-kriterier. Brug når læreren siger "vurdér mine spørgsmål", "er disse spørgsmål gode nok", "tjek spørgsmålene", "forbedr spørgsmålene", eller har eksisterende spørgsmål der skal kvalitetssikres mod Blooms taksonomi.
argument-hint: "[spørgsmål der skal vurderes]"
allowed-tools:
  - Read
  - Glob
---

# Vurdér spørgsmål

Kvalitetstjek og forbedr eksisterende arbejdsspørgsmål mod Bloom-kriterier.

## Brug

Giv mig eksisterende spørgsmål (dine egne eller kollegers) samt teksten de er baseret på. Jeg leverer:

1. **Samlet vurdering** — hvad fungerer, hvad er gennemgående problemer
2. **Spørgsmål-for-spørgsmål** — Bloom-niveau, problemer, forbedret version
3. **Forbedret sæt** — alle spørgsmål omformuleret
4. **Anbefalinger** — manglende Bloom-niveauer, forslag til supplering

## Trin

1. **Læs tjeklisten** `${CLAUDE_SKILL_DIR}/../bloom-arbejdsspoergsmaal/references/forbudte-formuleringer.md` for vurderingsskemaet.

### Gate: Bekræft fokus — VENT på svar

Re-ground: "Du har givet mig spørgsmål der skal kvalitetstjekkes. Før jeg går i gang, vil jeg lige sikre mig at jeg fokuserer rigtigt."

Spørg læreren: "Hvad vil du have fokus på — generel kvalitetsforbedring, taksonomisk balance, eller sværhedsgrad? Er der noget specifikt du er i tvivl om?"

**VENT** på svar.

2. **Samlet vurdering:** Hvad fungerer? Taksonomisk fordeling? Gennemgående fejl?
3. **Vurdér hvert spørgsmål** med skemaet: Bloom-niveau, problemer, forbedret version.
4. **Præsentér forbedret sæt** samlet.
5. **Anbefal** supplerende spørgsmål der lukker huller i taksonomien.

Afslut med: "Vil du justere noget i det forbedrede sæt?"

## Typiske problemer jeg kigger efter

- "Og"-konstruktioner der blander flere spørgsmål
- Forbudte verber (analysér, diskutér, redegør)
- Ubesvarlige fra teksten
- Vage verber ("fortæl om", "beskriv")
- Ja/nej uden begrundelseskrav
- Forkert Bloom-niveau

---

## Completion Status

- **DONE** — Spørgsmål vurderet, forbedret sæt præsenteret
- **DONE_WITH_CONCERNS** — Forbedret, men originale spørgsmål havde grundlæggende taksonomiske problemer
- **NEEDS_CONTEXT** — Mangler den tekst spørgsmålene er baseret på
