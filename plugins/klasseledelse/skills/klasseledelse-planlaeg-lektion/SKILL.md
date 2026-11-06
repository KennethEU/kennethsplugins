---
name: klasseledelse-planlaeg-lektion
description: "Planlægger en lektion eller et modul i gymnasiet, så alle elever løbende deltager: hook, aktivering, gennemgang, repetition og afslutning, med drejebog, lærerens replikker, køreplan til eleverne og printklare elevark efter ønske. Brug når læreren siger \"få alle med\", \"aktivere eleverne\", \"planlæg gennemgang af\", \"eleverne er passive\", \"klasseledelse\", \"planlæg et modul om\" eller \"planlæg en time om\" et emne uden en bestemt fagtekst. Brug ikke til en time bygget på spørgsmål til en fagtekst med Bloom-progression (bloom-planlaeg-time), til at vurdere en færdig plan (klasseledelse-vurder-plan), til at finde en enkelt CL-øvelse (cl-find-oevelse) eller til casespil."
argument-hint: "[emne, klasse og tid]"
allowed-tools:
  - Read
  - Glob
  - Skill
  - Write
---

# Planlæg lektion, hvor alle er med

Lav en lektion, hvor alle løbende gør noget fagligt, læreren kan se, og som læreren kan gennemføre uden at forberede meget mere.

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../klasseledelse-principper/SKILL.md`. Læs `${CLAUDE_SKILL_DIR}/../klasseledelse-principper/references/evidens.md`, før du henviser til forskning.

### Gate 1: Afklar rammer (VENT på svar)

Re-ground: "Vi planlægger en lektion, hvor alle er med. Jeg mangler et par oplysninger."

Spørg kun om det nødvendige, hvis læreren ikke allerede har svaret:

1. **Fag, emne og klasse:** Hvilket fag og hvilken årgang?
2. **Tid:** Hvor lang er lektionen, og er der pause, hvis den er på 90 minutter eller mere?
3. **Mål:** Hvad skal alle kunne, når de går, fx et begreb, en metode eller en genre?
4. **Tekster (hvis eleverne skal læse eller slå op):** Har eleverne teksten på papir eller kun på skærm, fx som iBog?
5. **Forløbet:** Er modulet det sidste i forløbet? Så skal planen samle op på hele forløbet og ikke kun på dagens tekst.

Får du tekster som link, så følg "Vær ærlig om tekster" i principperne. Bygger timen på lektie, så følg "Elever, der ikke har læst".

Resten antager du og skriver tydeligt i Gate 2, så læreren kan rette det: forkundskab og hvad klassen kommer fra sidst, om eleverne skal bruge computer, om klassen har særlige forhold eller faste rutiner, og hvor elevernes slutprodukt ender (som standard deres egne noter).

**VENT** på svar. Hvis alt ovenfor fremgår, så gå direkte videre til Gate 2.

### Gate 2: Foreslå skelet (VENT på OK)

Re-ground: "Vi er ved **Gate 2**. Her er skelettet, før jeg skriver drejebogen."

Træf først disse to valg og begrund dem kort:

- **Rækkefølge:** instruktion først eller problem først, ud fra forkundskab, stoffets sværhedsgrad og klassen. Anbefal ét, og begrund det med skærpelse 4, 9 og 10 i principperne og ét evidensmærke. Vælger du problem først, så skriv, hvordan forsøget stilladseres, og hvor opsamlingen ligger. Er gennemgangen lang, så skriv, hvor aktiviteten ligger undervejs.
- **Model:** skal eleverne se et eksemplarisk produkt? Vis det ved nyt, og aftrap det, når klassen kender genren.

Vis derefter skelettet med koder fra deltagelseskortet, og skriv forklaringen af koderne lige over tabellen med standardlinjen fra principperne:

| Tid | Fase | Kode | Hvad alle elever gør |
|-----|------|------|----------------------|
| [x] | [fase] | A/G/E/L | [synlig handling] |

Under tabellen: dine antagelser, længste strækning med L og E, hvad du har valgt fra og hvorfor, og en optælling mod aktivitetsbudgettet i principperne: faser, nye strukturer, skift, elevark og minutter. Er budgettet overskredet, så sig det, og foreslå, hvad der kan fjernes.

Bruger skelettet grupper, og kender du ikke fremmødet, så spørg også: "Hvor mange elever plejer at møde op, som et spænd pr. klasse, fx 10-12 og 13-19?"

Spørg: "Passer skelettet, eller skal noget flyttes eller ændres?"

**VENT** på OK.

### Skriv drejebogen

Hold planen inden for aktivitetsbudgettet, og skriv opgaverne præcist, jf. "Enkelhed før aktivering" i principperne. Læg aktiveringen inde i faserne, ikke i flere skift. Trinene nedenfor er et tjek, ikke noget, der skal stå som egne punkter i planen. I drejebogen skal der kun stå de replikker, læreren faktisk skal bruge, fx opgaven og overgangene. Opgavens tekst kan genbruges på instruktionsslidet, så intet skrives to gange.

2. **Start:** skriv lærerens faste opmærksomhedssignal, målet og hvorfor det er vigtigt, en hook, der er koblet direkte til målet, og en aktiv start, hvor alle henter noget frem fra sidst. Den aktive start er også et tjek af forudsætningerne: en lille opgave til alle, ikke "kan I huske det?" og ikke én elev ved tavlen. Tjek, at hooken ikke kun er underholdning. Er relevansen ikke oplagt, så lad eleverne sige til sidemanden, hvor de kan bruge det.
3. **Gennemgang:** del stoffet op i små bidder. Læg en aktivering ind efter hver bid. Skriv hvert sidemandsspørgsmål færdigt, så det kan besvares af alle og får eleverne til at tænke over målet. Skal de analysere, skal de også øve sig i at analysere. Er det en ny færdighed, så skriv de tre trin: læreren viser og tænker højt, klassen løser én sammen med læreren, eleverne løser selv. Skriv, hvad læreren gør, hvis mange svarer forkert i parsnakken: én ekstra fælles opgave før det selvstændige arbejde. I det fælles trin fortæller læreren først, spørger så og minder til sidst kun om det.
4. **Cold calling:** sæt den efter sidemandssnak, til et spørgsmål, eleven kan svare på. Skriv, hvordan du markerer øverum.
5. **Fagtermer:** vælg få, håndfaste begreber, alle skal kunne sige og bruge. Skriv for hvert nyt begreb to til tre klare eksempler og ét ikke-eksempel, der ligner, men ikke er det, fx flexicurity over for gig-økonomi. Tjek forudsætninger og typiske misforståelser, før nyt stof bygges ovenpå.
6. **Slides:** beskriv hvert slide med billede eller diagram og højst få stikord.
7. **Selvstændigt arbejde:** giv det en rolle, et produkt og nedslag, så det bliver A. Hvis koden stadig er G, så skriv hvorfor. Skriv også en udfordring til de stærke elever. Tjek hver gruppefase efter "Grupper og fravær" i principperne, og sig det, hvis en øvelse ikke er afprøvet.
8. **Afslutning:** lad alle skrive eller hente stoffet frem fra hukommelsen, fx i en stilladseret note eller et lille tjek. Skriv, hvad der skal gentages næste gang, og hvordan produktet kommer i noterne, jf. "Noter" i principperne. Sig, hvad der skal ske næste gang. Giv kun selvstændig lektie i det nye, hvis eleverne kan det. Ellers giv tidligere stof for.
9. **Forventninger og begrundelser:** skriv de få sætninger, der siger, hvad eleverne skal, og hvorfor. Skriv i et sprog, der passer til 16-19-årige.
10. **Den sårbare elev:** tæl, hvor mange gange en genert elev kan deltage trygt. Der skal være mindst fem, og sidemandssnak og skrivning tæller med. Nævner læreren en bestemt elev, så følg afsnittet "Sårbare elever".
11. **Tid, og hvis noget skrider:** følg "Tid" og "Det vigtigste først" i principperne, og giv overgange egne rækker i drejebogen. Skriv én plan for det, der kan springes helt over, hvis tiden løber, og én replik til at holde tempoet, hvis nogen afsporer timen.
12. **Skærme:** følg "Tekster kun på skærm" i principperne, hvis teksten kun findes på skærm. Drejebogen skal selv sige, hvornår skærmene er oppe og nede.
13. **Grupper:** bruger planen grupper, så lav tabellen over fremmøde nedenfor.
14. **Sidste modul i forløbet:** lad genkaldelse og afslutning dække hele forløbet, så eleverne kobler dagens tekst til det, de har arbejdet med før.
15. **Genkaldelse i stedet for spørgsmål:** dækker en genkaldelse, fx et tomt skema, de samme arbejdsspørgsmål på Huske/Forstå, så foreslå at erstatte dem, og sig det tydeligt. Eleverne skal bagefter tjekke deres svar mod teksten.

### Sådan afleverer du

Skriv først målet i én sætning og derefter drejebogen:

| Tid | Læreren gør og siger | Alle elever gør | Synligt tjek | Kode | Skærm |
|-----|----------------------|-----------------|--------------|------|-------|

Efter tabellen:

- **Køreplan til eleverne:** lever den altid. Ét trin pr. fase med modulets mål eller problemformulering øverst, skrevet til eleverne, så den kan stå fremme hele modulet med det aktuelle trin fremhævet.
- **Instruktionsslide til hver fase:** kort tekst, der siger, hvad eleverne laver, med hvem, hvor længe, om skærmen er oppe eller nede, og hvornår de er klar. Brug de samme korte overgangssætninger hver gang, fx "Nu gør vi én sammen" og "Nu prøver I selv". Lærerens replikker hører til i notefeltet.
- **Fremmøde (hvis planen bruger grupper):** en enkel regel og en kort tabel med mindste, typiske og største elevtal: antal grupper og fordeling, fx 13 elever = 3 grupper á 3 + 1 gruppe á 4. Tjek, at hver fordeling summer til elevtallet, og prøv selv gruppereglen af på alle elevtal i spændet. Derunder en printliste med én kolonne pr. holdstørrelse, der regner med det højeste elevtal og det højeste antal grupper for holdet.
- **Deltagelseskort:** forklaring af koderne, rækkefølgen af koder, længste strækning med L og E og antal trygge deltagelser.
- **Planens vægt:** optælling mod aktivitetsbudgettet og anslået forberedelse. Skriv, at tiderne er regnet igennem og ikke afprøvet.
- **Materialer:** hvad der skal forberedes, fx slides og noteark. Mangler planen en aktivitet, fx en anderledes lektieopsamling eller en diskussionsform, så tilbyd `cl-find-oevelse` (én øvelse) eller `cl-forloeb` (et helt modul med CL). Har planen en gruppefase på 20 minutter eller mere, hvor eleverne skal arbejde selv, så tilbyd `dagsorden-lav` (en udretterdagsorden med roller og faser til den fase). Tilbyd og **VENT** på svar. Er skillen ikke tilgængelig, så sig, at den hører til et plugin, der ikke ser ud til at være installeret, og fortsæt uden.
- **Det kan du forvente:** én typisk reaktion fra eleverne, og hvordan du møder den, hvis formen er ny for klassen. Er planen mere aktiv, end klassen er vant til, så skriv en kort begrundelse til eleverne om, at det føles sværere, men giver mere læring (Moderat).

### Kvalitetstjek inden aflevering

- Passer tiderne, og summer de til lektionens længde?
- Er hvert spørgsmål skrevet færdigt?
- Peger alle aktiviteter på målet, og træner de det, eleverne skal kunne?
- Har de stærke elever noget at strække sig efter?
- Har overgange egne minutter, og er der slack, når pause, hej og oprydning er trukket fra?
- Står skærm oppe eller nede ved hver fase?
- Passer køreplanen, instruktionsslides og drejebogen sammen?
- Holder gruppereglen og fraværsreglen på alle elevtal i spændet?
- Er opgaverne skrevet færdigt, og er planen stadig så enkel, at læreren kan huske den?
- Står der kun varighed og ingen klokkeslæt i det, eleverne ser?
- Holder planen aktivitetsbudgettet, og starter den vigtigste aktivitet senest 25 minutter før slut?
- Kan klassen nå den vigtigste aktivitet, hvis alt tager 20 % længere tid?

Afslut med: "Vil du justere noget, fx tempoet, en aktivitet eller tonen?" Beder læreren om ændringer, så følg "Når læreren beder om ændringer" i principperne.

### Gate 3: Tilbyd materialer (VENT på svar)

Når læreren har godkendt planen, så tilbyd: "Skal jeg lave printklare elevark, en lærerpakke med drejebog og facit og slides til planen?" Nævn de ark, planen konkret bruger: skemaer, ekspertkort, kort til at klippe ud eller skriveark.

**VENT** på svar. Siger læreren ja, så læs `${CLAUDE_SKILL_DIR}/references/materialer.md`, og:

1. Lav kun det, læreren har sagt ja til, og kun de ark, planen bruger, så de kan printes uden redigering. Brug en dokumentskill som `docx`, hvis den er tilgængelig. Ellers skriv arkene i chatten, og sig det.
2. Lav lærerpakken som en særskilt fil med facit, så facit ikke ryger med ud til eleverne, og del elevarkene i printfiler efter modtager.
3. Mærk hvert punkt i facittet:
   - **Fra teksten:** bygger på en tekst, du har læst.
   - **Ikke tjekket:** du har ikke kunnet læse teksten. Læreren skal selv tjekke punktet.
4. Find ikke på indhold. Har du slet ikke læst en tekst, så bed om den, før du laver facit, der bygger på den. Du må gerne lave skemaets struktur uden facit.

Skal læreren bruge et helt sæt arbejdsspørgsmål til en tekst, så tilbyd `bloom-spoergsmaal-til-tekst` i stedet.

Tilbyd også at vise køreplan og opgaver på storskærm med `dida-plan`. Den supplerer slides, men erstatter dem ikke: faser med gennemgang, figurer eller billeder skal stadig have slides. Tilbyd og **VENT** på svar. Er skillen ikke tilgængelig, så sig, at den hører til et plugin, der ikke ser ud til at være installeret, og fortsæt uden.

---

## Completion Status

- **DONE**: Drejebog og køreplan leveret og tjekket, og materialer tilbudt
- **DONE_WITH_CONCERNS**: Leveret, men tid eller stofmængde er stram
- **NEEDS_CONTEXT**: Mangler fag, tid eller mål
