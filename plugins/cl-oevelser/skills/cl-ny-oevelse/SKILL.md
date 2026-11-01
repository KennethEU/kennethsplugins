---
name: cl-ny-oevelse
description: "Udvikler en ny CL-øvelse (Cooperative Learning) ud fra SPIL-principperne, når kataloget ikke dækker behovet, eller omskriver lærerens egen aktivitet eller gruppearbejde, så det bliver til CL. Brug når læreren siger \"lav en ny CL-øvelse\", \"opfind en øvelse\", \"ingen af øvelserne passer\", \"kan du gøre mit gruppearbejde til CL\" eller \"lav den her aktivitet om, så alle deltager lige meget\". Brug ikke til at finde eller tilpasse en øvelse fra kataloget (cl-find-oevelse), til at vurdere en hel lektionsplan (klasseledelse-vurder-plan) eller til casespil."
argument-hint: "[behov eller aktivitet]"
allowed-tools:
  - Read
  - Glob
  - Skill
---

# Udvikl en ny CL-øvelse

Byg en øvelse, hvor reglerne sikrer SPIL, så læreren ikke skal håbe på det.

## Trin

1. **Læs** `${CLAUDE_SKILL_DIR}/../cl-principper/SKILL.md` og `${CLAUDE_SKILL_DIR}/../cl-principper/references/oevelsesbank.md`. Tjek først, om en øvelse i banken allerede kan løse det. Så sig det, og spørg, om læreren hellere vil bruge den.

### Gate 1: Afklar behovet (VENT på svar)

Spørg samlet om det, der mangler: antal elever, fagligt emne, formål, tid, lokale og elevforudsætninger. Har læreren en aktivitet, der skal omskrives, så bed om den.

**VENT** på svar.

### Gate 2: Foreslå en skitse (VENT på OK)

Giv øvelsen et arbejdsnavn og vis den i 4 til 6 korte trin. Under trinene:

| Princip | Hvilken regel sikrer det? |
|---------|---------------------------|

Skriv reglen, ikke hensigten. "Alle deltager" er ikke en regel. "Hver elev siger sit svar i en runde, før teamet diskuterer" er en regel. Omskriver du en aktivitet, så sig først, hvilke principper den manglede.

Spørg: "Rammer den, eller skal noget ændres?"

**VENT** på OK.

### Skriv øvelsen

2. **Brug skabelonen** fra principperne, og regn elevtal og tid igennem.
3. **Læg indholdet i** med færdigskrevne spørgsmål, kort eller opgaver. Find ikke på indhold fra tekster, du ikke har læst.
4. **Prøv den i hovedet:** hvad gør den elev, der ikke har læst? Den stille elev? Den stærke elev, der er hurtigt færdig? Justér, hvis nogen kan gemme sig eller løbe fra opgaven.

### Sådan afleverer du

Skriv tydeligt øverst: "Ny øvelse, ikke fra kataloget og ikke afprøvet." Omtal den ikke som en etableret CL-struktur.

Tilbyd printklart materiale som Word efter afsnittet i principperne, og tilbyd en katalogpost i samme format som banken, hvis øvelsen virker i klassen. **VENT** på svar.

---

## Completion Status

- **DONE**: Ny øvelse beskrevet og SPIL-tjekket
- **DONE_WITH_CONCERNS**: Leveret, men et princip er svagt, og det er sagt
- **NEEDS_CONTEXT**: Mangler behov, emne eller rammer
