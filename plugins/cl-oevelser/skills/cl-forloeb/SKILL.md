---
name: cl-forloeb
description: "Kombinerer flere CL-øvelser (Cooperative Learning) til et sammenhængende modul eller forløb, hvor den ene øvelse bygger på den anden. Brug når læreren siger \"kombinér CL-øvelser\", \"flere CL-øvelser i træk\", \"et CL-forløb\", \"et helt modul med CL\" eller \"hvilke øvelser passer sammen\". Brug ikke til én enkelt øvelse (cl-find-oevelse), en lektion, hvor CL ikke er omdrejningspunktet (klasseledelse-planlaeg-lektion), en tre-faset time om en fagtekst (bloom-planlaeg-time) eller casespil."
argument-hint: "[emne, antal moduler og mål]"
allowed-tools:
  - Read
  - Glob
  - Skill
  - Write
---

# Kombinér CL-øvelser til et forløb

Sæt øvelser sammen, så produktet fra den ene bliver råstof til den næste.

## Trin

1. **Læs** `${CLAUDE_SKILL_DIR}/../cl-principper/SKILL.md` og `${CLAUDE_SKILL_DIR}/../cl-principper/references/oevelsesbank.md`.

**Skal kendes:** emne og mål, og modulets længde. Følg "Arbejdsgang" i principperne: i hurtig-tilstand springer du Gate 1 og 2 over, skriver antagelserne i én linje og viser overblikstabellen fra Gate 2 øverst i det færdige forløb.

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

2. **Lav en samlet oversigt** med tider, overgange og grupper, så de samme grupper ikke skal laves om uden grund. Skriv gruppereglen, så den også virker, når der mangler elever, jf. "Elevtal og fravær" i principperne.
3. **Beskriv hver øvelse** efter den korte version i principperne, men gentag ikke materialer og rammer, der allerede står. Skriv spørgsmål og opgaver færdige, hvor du kender indholdet, og følg "Fakta, tal og aktuelle forhold" og "Kun det, klassen har mødt" i principperne.
4. **Skriv overgangene:** hvad siger læreren, og hvad tager eleverne med videre?
5. **Skriv noterne:** hvad står eleverne med, når forløbet er slut?
6. **Skriv, hvad der kan skæres væk,** hvis tiden løber.

### Sådan afleverer du

Giv det hele samlet i ét svar, og vis overblikket først. Slut med én linje om, hvad læreren kan bede om: ændringer, materiale til print, modulet som dida-plan til storskærmen og, hvis forløbet har en gruppefase på 20 minutter eller mere, hvor eleverne arbejder selv, `dagsorden-lav` til den fase. Lav ikke printmateriale, og start ikke en anden skill, før læreren har sagt ja. Giv så den anden skill forløbet, så den ikke spørger igen. Er en skill ikke tilgængelig, så fortsæt uden.

### Kvalitetstjek inden aflevering

Lav tjekket stille, og ret det, der ikke holder.

- Summer tiderne til modulets længde, også med overgange?
- Virker grupperne og hver øvelse, også når fire elever mangler?
- Bruger forløbet kun teorier og teoretikere, klassen har mødt, eller står de i antagelseslinjen?
- Er tal, aktuelle forhold og usikre svar samlet i linjen "Tjek"?
- Ved de par eller teams, der er færdige først, hvad de skal?
- Er alle øvelser med svag SPIL skærpet?
- Bygger øvelserne reelt på hinanden?
- Har du prøvet spørgsmål og opgaver af? Skriv svaret selv, og svar så som en middelmådig elev på den tid, øvelsen giver. Kan du ikke skrive ét sikkert svar, eller er et tomt svar nok, så ret spørgsmålet.
- Er der færre nye strukturer, end klassen kan nå at lære?

---

## Completion Status

- **DONE**: Forløb leveret og tjekket
- **DONE_WITH_CONCERNS**: Leveret, men tid eller stofmængde er stram
- **NEEDS_CONTEXT**: Mangler emne, tid eller rammer
