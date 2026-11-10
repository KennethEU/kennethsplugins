---
name: bloom-vurder-spoergsmaal
description: "Vurderer og forbedrer eksisterende arbejdsspørgsmål mod Bloom-kriterier: niveau, forbudte formuleringer, besvarlighed og balance. Brug når læreren siger \"vurdér mine spørgsmål\", \"er disse spørgsmål gode nok\", \"tjek spørgsmålene\", \"forbedr spørgsmålene\", eller indsætter spørgsmål, der skal kvalitetssikres. Brug ikke til at lave nye spørgsmål fra bunden (bloom-spoergsmaal-til-tekst) eller til at rette elevbesvarelser."
argument-hint: "[spørgsmål der skal vurderes]"
allowed-tools:
  - Read
  - Glob
  - Write
---

# Vurdér spørgsmål

Tjek og forbedr eksisterende arbejdsspørgsmål mod Bloom-kriterierne.

**Skal kendes:** spørgsmålene. Har du ikke teksten, de bygger på, så vurdér dem alligevel, og sig, at du ikke har kunnet tjekke, om de kan besvares ud fra teksten. Følg "Arbejdsgang" i `bloom-spoergsmaalsregler`: i hurtig-tilstand springer du gaten over.

## Trin

1. **Læs** `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/SKILL.md` og tjeklisten `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/references/forbudte-formuleringer.md` med vurderingsskemaet.

### Gate: Bekræft fokus (kun uden for hurtig-tilstand, VENT på svar)

Bruges, når læreren beder om sparring, eller når det er uklart, om spørgsmålene er til lektie, klassearbejde eller eksamen.

Spørg: "Hvad vil du have fokus på: generel kvalitet, taksonomisk balance eller sværhedsgrad?"

**VENT** på svar.

### Vurdér

2. **Vurdér hvert spørgsmål** stille med skemaet: Bloom-niveau, problemer og forbedret version.
3. **Find mønstret:** Hvad fungerer, hvordan er fordelingen på niveauer, og hvilke fejl går igen?

## Sådan afleverer du

**Kort version (standard):**

1. **Samlet vurdering** i to til tre sætninger: det, der virker, den vigtigste fejl, der går igen, og fordelingen på niveauer i én linje.
2. **Forbedret sæt:** alle spørgsmål i den rækkefølge, læreren gav dem, med Bloom-niveau i parentes. Under hvert ændret spørgsmål én kort linje om, hvad der var galt. Spørgsmål, der holder, står uændret og mærkes "uændret".
3. **Huller:** højst to forslag til nye spørgsmål, hvis et niveau mangler.
4. Én linje til sidst: "Sig til, hvis du vil se skemaet spørgsmål for spørgsmål, eller hvis noget skal justeres."

**På opfordring:** skemaet spørgsmål for spørgsmål med niveau, problemer og begrundelse.

## Typiske problemer

- "Og"-konstruktioner, der blander flere spørgsmål
- Forbudte verber (analysér, diskutér, redegør)
- Spørgsmål, der ikke kan besvares ud fra teksten
- Vage verber ("fortæl om", "beskriv")
- Ja/nej uden krav om begrundelse
- Forkert Bloom-niveau

---

## Completion Status

- **DONE**: Spørgsmål vurderet, og forbedret sæt leveret
- **DONE_WITH_CONCERNS**: Forbedret, men de oprindelige spørgsmål havde grundlæggende taksonomiske problemer, eller teksten manglede
- **NEEDS_CONTEXT**: Mangler spørgsmålene
