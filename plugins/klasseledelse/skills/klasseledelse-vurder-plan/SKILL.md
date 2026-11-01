---
name: klasseledelse-vurder-plan
description: "Vurderer en eksisterende lektions- eller modulplan i gymnasiet med deltagelseskort og foreslår konkrete omskrivninger, så alle elever kommer med. Brug når læreren siger \"vurdér min lektionsplan\", \"kig på min plan\", \"hvordan får jeg alle med i den her time\", \"mine elever er passive i det her modul\", \"er min time for lærerstyret\", eller indsætter en timeplan, der skal forbedres. Brug ikke til at lave en plan fra bunden (klasseledelse-planlaeg-lektion), til at vurdere arbejdsspørgsmål (bloom-vurder-spoergsmaal), til casespil (casespil-konsistenstjek) eller til observation af en bestemt lærer."
argument-hint: "[lektionsplan eller modulplan]"
allowed-tools:
  - Read
  - Glob
  - Skill
---

# Vurdér lektionsplan

Giv læreren et ærligt billede af, hvem der deltager hvornår, og få konkrete forbedringer, der kan bruges i næste time.

Du giver ikke point, og du krydser ikke principper af. En plan, der bruger alle greb, kan stadig være dårlig. En plan med få greb kan være god.

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../klasseledelse-principper/SKILL.md`. Læs `${CLAUDE_SKILL_DIR}/../klasseledelse-principper/references/evidens.md`, før du henviser til forskning.
2. **Læs planen.** Hvis den er en fil, så læs filen. Hvis du ikke har nogen plan, så bed om den og stop.

### Tjek først: Er det en plan? (FØR Gate 1)

En plan siger, hvad der sker hvornår. Der skal mindst være en rækkefølge af faser, og noget om tid eller arbejdsformer. Tekster, sider og spørgsmål alene er en materialeliste.

Er det en materialeliste, så stil ikke spørgsmålene i Gate 1, og lav ikke et deltagelseskort. Sig i stedet:

"Jeg kan se, hvad du vil arbejde med, men det her er ikke en plan, så jeg kan ikke vurdere den. Skal jeg lave en plan ud fra materialet med klasseledelse-planlaeg-lektion?"

**VENT** på svar. Følg reglerne i "Videresendelse til andre skills".

### Gate 1: Afklar kun det nødvendige (VENT på svar)

Vurderingen afhænger især af formål, klasse og tid, og af om modulet er det sidste i forløbet. Hvis det hele fremgår, så spring denne gate over. Er modulet på 90 minutter eller mere, og står der intet om pause, så spørg også om det.

Re-ground: "Du vil have din plan vurderet. Jeg mangler kun lige det her."

Spørg kun om det, der mangler:

1. **Formål:** Hvad skal eleverne kunne bagefter?
2. **Klasse og tid:** Hvilken årgang, hvor lang er timen, og er der pause?
3. **Forløbet:** Er modulet det sidste i forløbet? Så skal planen samle op på hele forløbet og ikke kun på dagens tekst.
4. **Bevidste valg:** Er der noget, du gør med vilje, fx åbent gruppearbejde, som jeg ikke skal ændre?

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
   - Kan eleverne se, hvor de er i modulet, og ved de, hvad de skal ved hver overgang, herunder om skærmen er oppe eller nede?
   - Er modulet det sidste i forløbet, samler planen så op på hele forløbet og ikke kun på dagens tekst?
6. **Skel mellem problem og valg.** Hvis noget strider mod bogen, men tjener formålet, så omtal det som et valg, og sig, hvad der skal til for at det virker. Tving ikke Direct Instruction ned over et bevidst åbent forløb. Spørg til formål og placering.
7. **Tjek spørgsmålene.** Er arbejdsspørgsmålene mest på Huske/Forstå, så tilbyd at sende dem til `bloom-vurder-spoergsmaal`. Nævn det ikke bare som en svaghed. Se "Videresendelse til andre skills".
8. **Tjek lektien.** Bygger planen på, at eleverne har læst, så følg afsnittet "Elever, der ikke har læst" i principperne.
9. **Tjek aktiviteterne.** Mangler planen en aktivitet, fx en anderledes lektieopsamling eller en diskussionsform, så tilbyd `cl-find-oevelse`. Skal hele modulet bygges op om CL, så tilbyd `cl-forloeb`. Se "Videresendelse til andre skills".

### Sådan afleverer du

Som standard afleverer du den korte version, så den også kan læses på mobil: punkt 1, 2 og 3 og en enkelt linje for punkt 4 og for eventuelle bevidste valg. Slut med at tilbyde hele gennemgangen, princip for princip.

**1. Samlet vurdering.** To til tre sætninger: det vigtigste, der virker, og det vigtigste problem.

**2. Deltagelseskort.** Skriv forklaringen af koderne lige over tabellen med standardlinjen fra principperne.

| Tid | Fase | Kode | Kommentar |
|-----|------|------|-----------|

Under tabellen: længste strækning med L og E, første A, hvordan timen slutter, og om aktiviteterne træner målet.

**3. De tre vigtigste ændringer.** Højst tre, sorteret efter betydning. For hver:

- **Nu:** hvad planen gør, med henvisning til tid eller fase.
- **Ændring:** præcis hvad der skal gøres, med færdig formulering af replikken, spørgsmålet eller opgaven.
- **Hvorfor:** én sætning. Sæt evidensmærke, hvis du henviser til forskning.
- **Pris:** hvad det koster i tid eller kræver af klassen, og hvad der kan fjernes i stedet.

**4. Fem-succeser-tjekket.** Hvor mange gange kan den mest generte elev deltage trygt?

**5. Bevidste valg.** Hvad du lod stå, og hvad der skal til, for at det virker. Spring afsnittet over, hvis der ikke er nogen.

**6. Princip for princip (kun på opfordring).** Kort tabel med status: Til stede, Delvist, Ikke synligt i planen eller Ikke relevant. Højst én linje pr. princip.

### Gate 2: Omskriv planen (VENT på svar)

Spørg: "Hvilke af de tre ændringer skal med i den forbedrede plan? Jeg skriver kun dem, du vælger, ind, og resten af din plan står uændret."

**VENT** på svar. Skriv derefter planen om med de valgte ændringer og intet andet, i samme drejebogsformat som `klasseledelse-planlaeg-lektion`. Vil læreren have mere end de tre med, så skal det siges:

| Tid | Læreren gør og siger | Alle elever gør | Synligt tjek | Kode | Skærm |
|-----|----------------------|-----------------|--------------|------|-------|

Bevar lærerens eget indhold, formål og stemme. Tjek, at tiderne stadig summer, og vis det nye deltagelseskort sammen med det gamle. Sig til sidst, hvilke materialer der nu mangler, jf. principperne.

## Videresendelse til andre skills

- Tilbyd altid videresendelse, og **VENT** på svar. Gå aldrig videre af dig selv, for læreren skal vide, at opgaven skifter.
- Mangler planen en aktivitet, så er mulighederne `cl-find-oevelse` (én øvelse) og `cl-forloeb` (et helt modul med CL). Foreslå den, der passer, og sig kort hvorfor.
- Siger læreren ja, så start den anden skill, og giv den det, du allerede ved, så læreren ikke skal svare igen.
- Er skillen ikke tilgængelig, så sig, at den hører til et plugin, der ikke ser ud til at være installeret, og fortsæt uden. Lad være med at gætte på, hvad den ville have svaret.

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
- **NEEDS_CONTEXT**: Mangler planen, formålet eller tiden, eller input er en materialeliste
