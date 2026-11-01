---
name: cl-forloeb
description: "Kombinerer flere CL-øvelser (Cooperative Learning) til et sammenhængende modul eller forløb, hvor den ene øvelse bygger på den anden. Brug når læreren siger \"kombinér CL-øvelser\", \"flere CL-øvelser i træk\", \"et CL-forløb\", \"et helt modul med CL\" eller \"hvilke øvelser passer sammen\". Brug ikke til én enkelt øvelse (cl-find-oevelse), en lektion, hvor CL ikke er omdrejningspunktet (klasseledelse-planlaeg-lektion), en tre-faset time om en fagtekst (bloom-planlaeg-time) eller casespil."
argument-hint: "[emne, antal moduler og mål]"
allowed-tools:
  - Read
  - Glob
  - Skill
---

# Kombinér CL-øvelser til et forløb

Sæt øvelser sammen, så produktet fra den ene bliver råstof til den næste.

## Trin

1. **Læs** `${CLAUDE_SKILL_DIR}/../cl-principper/SKILL.md` og `${CLAUDE_SKILL_DIR}/../cl-principper/references/oevelsesbank.md`.

### Gate 1: Afklar rammer (VENT på svar)

Spørg samlet om det, der mangler: antal elever, emne og mål, antal moduler og deres længde, lokale og elevforudsætninger.

**VENT** på svar.

### Gate 2: Foreslå rækkefølgen (VENT på OK)

| Tid | Øvelse | Hvad eleverne får ud af det | Hvad det giver videre |
|-----|--------|-----------------------------|-----------------------|

Vælg efter disse regler:

- **Rød tråd:** hver øvelse skal bruge noget fra den forrige. Ellers er det blot flere aktiviteter i træk.
- **Progression:** fra at hente stof frem, til at bruge det, til at vurdere eller producere.
- **Variation:** veksl mellem stille og bevægelse, og mellem par og teams.
- **Få strukturer:** en ny struktur tager tid at lære. Brug højst to nye pr. modul, og gentag hellere en, klassen kender.
- **Lærerens plads:** læg korte gennemgange ind, hvor eleverne har brug for dem. Forløbet er ikke bedre, fordi det kun består af CL.

Spørg: "Passer rækkefølgen, eller skal noget byttes?"

**VENT** på OK.

### Skriv forløbet

2. **Lav en samlet oversigt** med tider, overgange og grupper, så de samme grupper ikke skal laves om uden grund.
3. **Beskriv hver øvelse** efter skabelonen i principperne, men gentag ikke materialer og rammer, der allerede står. Skriv spørgsmål og opgaver færdige, hvor du kender indholdet.
4. **Skriv overgangene:** hvad siger læreren, og hvad tager eleverne med videre?
5. **Skriv noterne:** hvad står eleverne med, når forløbet er slut?
6. **Skriv, hvad der kan skæres væk,** hvis tiden løber.

### Sådan afleverer du

Giv det hele samlet i ét svar, og vis overblikket først. Tilbyd printklart materiale som Word efter afsnittet i principperne. **VENT** på svar.

### Kvalitetstjek inden aflevering

- Summer tiderne til modulets længde, også med overgange?
- Er alle øvelser med svag SPIL skærpet?
- Bygger øvelserne reelt på hinanden?
- Er der færre nye strukturer, end klassen kan nå at lære?

---

## Completion Status

- **DONE**: Forløb leveret og tjekket
- **DONE_WITH_CONCERNS**: Leveret, men tid eller stofmængde er stram
- **NEEDS_CONTEXT**: Mangler emne, tid eller rammer
