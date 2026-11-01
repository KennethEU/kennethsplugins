---
name: klasseledelse-vurder-plan
description: "Vurderer en eksisterende lektions- eller modulplan i gymnasiet med deltagelseskort og foreslår konkrete omskrivninger, så alle elever kommer med. Brug når læreren siger \"vurdér min lektionsplan\", \"kig på min plan\", \"hvordan får jeg alle med i den her time\", \"mine elever er passive i det her modul\", \"er min time for lærerstyret\", eller indsætter en timeplan, der skal forbedres. Brug ikke til at lave en plan fra bunden (klasseledelse-planlaeg-lektion), til at vurdere arbejdsspørgsmål (bloom-vurder-spoergsmaal), til casespil (casespil-konsistenstjek) eller til observation af en bestemt lærer."
argument-hint: "[lektionsplan eller modulplan]"
allowed-tools:
  - Read
  - Glob
---

# Vurdér lektionsplan

Giv læreren et ærligt billede af, hvem der deltager hvornår, og få konkrete forbedringer, der kan bruges i næste time.

Du giver ikke point, og du krydser ikke principper af. En plan, der bruger alle greb, kan stadig være dårlig. En plan med få greb kan være god.

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../klasseledelse-principper/SKILL.md`. Læs `${CLAUDE_SKILL_DIR}/../klasseledelse-principper/references/evidens.md`, før du henviser til forskning.
2. **Læs planen.** Hvis den er en fil, så læs filen. Hvis du ikke har nogen plan, så bed om den og stop.

### Gate 1: Afklar kun det nødvendige (VENT på svar)

Vurderingen afhænger især af formål, klasse og tid. Hvis de tre fremgår, så spring denne gate over.

Re-ground: "Du vil have din plan vurderet. Jeg mangler kun lige det her."

Spørg kun om det, der mangler:

1. **Formål:** Hvad skal eleverne kunne bagefter?
2. **Klasse og tid:** Hvilken årgang, og hvor lang er timen?
3. **Bevidste valg:** Er der noget, du gør med vilje, fx åbent gruppearbejde, som jeg ikke skal ændre?

**VENT** på svar.

### Analyse

3. **Lav deltagelseskortet.** Giv hver fase en kode (A, G, E eller L). Mangler planen tider, så anslå dem og skriv tydeligt, at de er anslået.
4. **Find det vigtigste.** Spørg: Hvor falder eleverne fra, og hvad betyder det for målet? Se på den længste strækning med L og E, på længere selvstændigt arbejde, på afslutningen og på, om aktiviteterne faktisk træner målet. En plan med mange A'er og lav faglig tyngde har et større problem end en plan med få, gode aktiviteter.
5. **Tjek skærpelserne:**
   - Tænker eleverne over det, de skal lære, og træner aktiviteterne målet?
   - Har de stærke elever noget at strække sig efter?
   - Hentes noget frem fra sidst, og er der en plan for at gentage det næste gang?
   - Er hooken og historierne koblet til målet?
   - Skal eleverne læse tekst, mens læreren taler?
   - Passer model og styring til, hvor meget klassen kan i forvejen?
   - Er repetition reel genkaldelse?
   - Er skærmbrug tænkt ind i hver fase?
   - Kan en genert elev svare trygt, og er øverum markeret? Følg afsnittet "Sårbare elever", hvis læreren nævner en bestemt elev.
   - Er forventninger og begrundelser skrevet ind, og er der kontakt i planen ud over styring?
6. **Skel mellem problem og valg.** Hvis noget strider mod bogen, men tjener formålet, så omtal det som et valg, og sig, hvad der skal til for at det virker. Tving ikke Direct Instruction ned over et bevidst åbent forløb. Spørg til formål og placering.

### Sådan afleverer du

**1. Samlet vurdering.** To til tre sætninger: det vigtigste, der virker, og det vigtigste problem.

**2. Deltagelseskort.**

| Tid | Fase | Kode | Kommentar |
|-----|------|------|-----------|

Under tabellen: længste strækning med L og E, første A, hvordan timen slutter, og om aktiviteterne træner målet.

**3. De tre vigtigste ændringer.** Højst tre, sorteret efter betydning. For hver:

- **Nu:** hvad planen gør, med henvisning til tid eller fase.
- **Ændring:** præcis hvad der skal gøres, med færdig formulering af replikken, spørgsmålet eller opgaven.
- **Hvorfor:** én sætning. Sæt evidensmærke, hvis du henviser til forskning.
- **Pris:** hvad det koster i tid eller kræver af klassen, og hvad der kan fjernes i stedet.

**4. Princip for princip.** Kort tabel med status: Til stede, Delvist, Ikke synligt i planen eller Ikke relevant. Højst én linje pr. princip.

**5. Fem-succeser-tjekket.** Hvor mange gange kan den mest generte elev deltage trygt?

**6. Bevidste valg.** Hvad du lod stå, og hvad der skal til, for at det virker. Spring afsnittet over, hvis der ikke er nogen.

### Gate 2: Omskriv planen (VENT på svar)

Spørg: "Hvilke ændringer skal med i den forbedrede plan?"

**VENT** på svar. Skriv derefter planen om med de valgte ændringer, i samme drejebogsformat som `klasseledelse-planlaeg-lektion`:

| Tid | Læreren gør og siger | Alle elever gør | Synligt tjek | Kode |
|-----|----------------------|-----------------|--------------|------|

Bevar lærerens eget indhold, formål og stemme. Tjek, at tiderne stadig summer, og vis det nye deltagelseskort sammen med det gamle.

## Sådan undgår du typiske fejl

- Skriv ikke "mangler" om noget, du ikke kan se. Skriv "ikke synligt i planen".
- Læg ikke ti nye aktiviteter oven i en fuld plan. Hver tilføjelse skal have en pris.
- Giv ikke samme råd til 1.g og 3.g.
- Ros ikke for at være venlig. Sig, hvad der faktisk virker, og hvorfor.
- Vurdér planen, ikke læreren.

---

## Completion Status

- **DONE**: Plan vurderet og ændringer foreslået
- **DONE_WITH_CONCERNS**: Vurderet, men planen er for løs til at sige noget sikkert om deltagelsen
- **NEEDS_CONTEXT**: Mangler planen, formålet eller tiden
