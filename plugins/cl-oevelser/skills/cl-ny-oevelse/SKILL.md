---
name: cl-ny-oevelse
description: "Udvikler en ny CL-øvelse (Cooperative Learning) ud fra SPIL-principperne, når kataloget ikke dækker behovet, eller omskriver lærerens egen aktivitet eller gruppearbejde, så det bliver til CL. Brug når læreren siger \"lav en ny CL-øvelse\", \"opfind en øvelse\", \"ingen af øvelserne passer\", \"kan du gøre mit gruppearbejde til CL\" eller \"lav den her aktivitet om, så alle deltager lige meget\". Brug ikke til at finde eller tilpasse en øvelse fra kataloget (cl-find-oevelse), til at vurdere en hel lektionsplan (klasseledelse-vurder-plan), til en hel gruppearbejdsprotokol med roller og faser på 20 minutter eller mere (dagsorden-lav) eller til casespil."
argument-hint: "[behov eller aktivitet]"
allowed-tools:
  - Read
  - Glob
  - Skill
  - Write
---

# Udvikl en ny CL-øvelse

Byg en øvelse, hvor reglerne sikrer SPIL, så læreren ikke skal håbe på det.

## Trin

1. **Læs** `${CLAUDE_SKILL_DIR}/../cl-principper/SKILL.md` og `${CLAUDE_SKILL_DIR}/../cl-principper/references/oevelsesbank.md`. Tjek først, om en øvelse i banken allerede kan løse det. Så sig det, og spørg, om læreren hellere vil bruge den.

**Skal kendes:** behovet eller den aktivitet, der skal omskrives, og emnet. Følg "Arbejdsgang" i principperne: i hurtig-tilstand springer du Gate 1 og 2 over, skriver antagelserne i én linje og afleverer øvelsen i den korte version. Tabellen over, hvilken regel der sikrer hvert princip, skal med, fordi øvelsen er ny.

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

2. **Brug den korte version** fra principperne, og regn elevtal og tid igennem. Brug den fulde skabelon, når læreren beder om den.
3. **Læg indholdet i** med færdigskrevne spørgsmål, kort eller opgaver. Find ikke på indhold fra tekster, du ikke har læst, og følg "Fakta, tal og aktuelle forhold" og "Kun det, klassen har mødt" i principperne.
4. **Prøv den i hovedet:** hvad gør den elev, der ikke har læst? Den stille elev? Den stærke elev, der er hurtigt færdig? Hvad sker der, hvis fire elever mangler, jf. "Elevtal og fravær" i principperne? Justér, hvis nogen kan gemme sig eller løbe fra opgaven.

### Sådan afleverer du

Skriv tydeligt øverst: "Ny øvelse, ikke fra kataloget og ikke afprøvet." Omtal den ikke som en etableret CL-struktur.

Slut med én linje om, hvad læreren kan bede om: ændringer, den fulde beskrivelse, materiale til print og en katalogpost i samme format som banken, hvis øvelsen virker i klassen. Lav ikke printmateriale, før læreren har sagt ja, og følg så afsnittet i principperne.

---

## Completion Status

- **DONE**: Ny øvelse beskrevet og SPIL-tjekket
- **DONE_WITH_CONCERNS**: Leveret, men et princip er svagt, og det er sagt
- **NEEDS_CONTEXT**: Mangler behov, emne eller rammer
