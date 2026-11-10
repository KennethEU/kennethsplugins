---
name: cl-find-oevelse
description: "Inspirationskatalog: finder og tilpasser CL-øvelser (Cooperative Learning) til en konkret undervisningssituation og leverer en komplet beskrivelse med SPIL-tjek, trin og fagligt eksempel. Brug når læreren siger \"CL-øvelse\", \"cooperative learning\", \"giv mig en idé til en øvelse\", \"øvelse til lektieopsamling\", \"variation af gruppearbejde\", \"tavleopsamling på en anden måde\", beder om at se kataloget, eller nævner en øvelse som Svar-bazar, Mix og match, Møde på midten, Kuvertleg, Fishbowl, Ekspertgrupper, Quiz og byt eller Struktureret kontrovers. Brug ikke til en hel lektion med drejebog (klasseledelse-planlaeg-lektion), en time bygget på spørgsmål til en fagtekst (bloom-planlaeg-time), en øvelse fra bunden (cl-ny-oevelse), flere øvelser i et forløb (cl-forloeb), en hel gruppearbejdsprotokol med roller og faser (dagsorden-lav) eller casespil."
argument-hint: "[emne, formål, klasse og tid]"
allowed-tools:
  - Read
  - Glob
  - Skill
  - Write
---

# Find og tilpas en CL-øvelse

Find den rigtige øvelse til situationen, og gør den klar til brug.

## Trin

1. **Læs** `${CLAUDE_SKILL_DIR}/../cl-principper/SKILL.md` og `${CLAUDE_SKILL_DIR}/../cl-principper/references/oevelsesbank.md`.

**Skal kendes:** emne og formål, eller navnet på en øvelse og emnet. Følg "Arbejdsgang" i principperne: i hurtig-tilstand springer du Gate 1 og 2 over, vælger selv den øvelse, der passer bedst, og nævner ét alternativ i den afsluttende linje. Kender du ikke elevtallet, så skriv en grupperegel, der virker for 18 til 28 elever, fx "teams á 4, og går det ikke op, så ét eller to teams á 3". Tid og lokale antager du ud fra banken, og du skriver antagelsen øverst.

2. **Vælg spor:**
   - **Læreren vil bare se muligheder**, fx "hvad har du?" eller "giv mig lidt inspiration": vis de 8 til 10 øvelser fra banken, der passer bedst til det, læreren nævner, grupperet efter formål med én linje pr. øvelse, og tilbyd resten. Banken er stor, så vis ikke det hele på én gang. Stil ingen spørgsmål først. Slut med at spørge, hvad næste time handler om.
   - **Læreren nævner en bestemt øvelse:** gå til Gate 1 og derefter direkte til beskrivelsen. Er øvelsen svag på SPIL, så sig det og skriv skærpelsen ind.
   - **Læreren har en situation:** følg hele forløbet nedenfor.

### Gate 1: Afklar situationen (VENT på svar)

Spørg samlet i én besked om det, der mangler:

1. **Antal elever**
2. **Fagligt emne** (tekst, begreb, teori, case)
3. **Formål** (lektieopsamling, tekstanalyse, begrebsarbejde, repetition, beregning, holdning og argumentation, produktion, feedback)
4. **Tid til rådighed**
5. **Lokale** (bordgrupper, plads til bevægelse, tavle eller skærm)
6. **Elevforudsætninger** (er lektien læst, kendskab til emnet, klassens dynamik, herunder hvilke teorier klassen har mødt)

Spørg kort og kollegialt. Står noget allerede i beskeden, så spørg ikke igen.

**VENT** på svar.

### Gate 2: Anbefal 1 til 3 øvelser (VENT på valg)

For hver øvelse:

- navn og kort beskrivelse
- hvorfor den passer her
- hvilke SPIL-principper den især understøtter, og om den kræver en skærpelse

Vælg ud fra formål, tid og lokale. Er klassen fagligt svagere eller urolig, så foreslå en bevægelsesøvelse først, hvis lokalet tillader det. Passer ingen øvelse, så sig det og tilbyd `cl-ny-oevelse`.

Sæt din anbefaling øverst, og spørg: "Hvilken lyder bedst?"

**VENT** på valg.

### Skriv beskrivelsen

3. **Brug den korte version** fra principperne. Brug den fulde skabelon, når læreren beder om den.
4. **Regn på klassen:** fordel netop dette elevtal i grupper, og sig, hvad I gør med de elever, der ikke går op. Summér tiderne, så de passer, også med instruktion og overgange.
5. **Læg indholdet i:** skriv spørgsmål, kort eller opgaver færdige til emnet. Du må kun bruge indhold, du kender eller har fået. Mangler du teksten, så bed om den eller marker tydeligt, at spørgsmålene skal tjekkes.
6. **Skriv skærpelsen ind** i trinene, ikke kun som tip.
7. **Sørg for noter:** beskriv præcist, hvordan eleverne får noter.

### Sådan afleverer du

Giv beskrivelsen samlet i ét svar, i den korte version. Slut med én linje: "Sig til, hvis den skal justeres, eller hvis du vil have den fulde beskrivelse med SPIL-tjek og variationer, [alternativet] i stedet eller materialet til print." Nævn kun print, når øvelsen kræver kort, ark eller kuverter. Lav ikke printmateriale, før læreren har sagt ja, og følg så afsnittet "Printklart materiale" i principperne.

### Kvalitetstjek inden aflevering

Lav tjekket stille, og ret det, der ikke holder.

- Er alle fire SPIL-principper dækket i selve trinene, eller står svagheden i en linje?
- Passer elevtal, grupper og tid?
- Er alle spørgsmål skrevet færdige, og trækker de på målet?
- Har du prøvet spørgsmål og kort af? Skriv svaret selv, og svar så som en middelmådig elev på den tid, øvelsen giver. Kan du ikke skrive ét sikkert svar, eller er et tomt svar nok, så ret spørgsmålet.
- Står der, hvordan eleverne får noter?
- Har du skrevet, hvad der er ændret i forhold til bankens øvelse?

---

## Completion Status

- **DONE**: Øvelse beskrevet og tjekket
- **DONE_WITH_CONCERNS**: Leveret, men tid eller SPIL er stram, og det er sagt
- **NEEDS_CONTEXT**: Mangler oplysninger fra Gate 1
