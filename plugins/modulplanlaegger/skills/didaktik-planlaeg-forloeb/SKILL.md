---
name: didaktik-planlaeg-forloeb
description: "Modulplanlægger: planlægger forløb i gymnasiet ud fra didaktisk viden, med tre indgange: hele modulrækken på én gang, kom i gang med et nyt forløb (kort ramme og skitse, kun første modul i detaljer) eller næste modul i et forløb, læreren er i gang med. Afklarer fag, niveau, mål og gældende læreplan, foreslår ramme, progression og evaluering, sender modulerne videre til de andre skills (drejebog, spørgsmål, CL, casespil, slides, quiz, dida-plan) og gemmer forløbet som filer i en forløbsmappe på computeren. Brug når læreren siger \"planlæg et forløb\", \"modulrække\", \"modulplan\", \"nyt forløb om\", \"jeg starter et forløb om\", \"første modul i et nyt forløb\", \"næste modul i forløbet\", \"modul 3 i mit forløb\" eller vil have didaktisk sparring på et forløb. Brug ikke til et enkeltstående modul uden et forløb (klasseledelse-planlaeg-lektion), til en time bygget på spørgsmål til en fagtekst (bloom-planlaeg-time), til et forløb af CL-øvelser alene (cl-forloeb) eller til casespil."
argument-hint: "[fag, niveau, emne og antal moduler]"
allowed-tools:
  - Read
  - Glob
  - Skill
  - Write
  - Edit
  - WebFetch
  - Bash(curl:*)
  - Bash(mkdir:*)
  - Bash(pdftotext:*)
  - Bash(pdf2txt.py:*)
  - Bash(python3:*)
---

# Planlæg et forløb

Lav et forløb, der kan begrundes didaktisk, har en tydelig progression og kan sendes videre til de skills, der laver de enkelte moduler. Denne skill ejer forløbsniveauet. Den skriver ikke selv drejebøger, spørgsmål eller slides.

## Trin

1. **Læs** `${CLAUDE_SKILL_DIR}/../didaktik-principper/SKILL.md`. Læs referencefilerne derfra, når et trin har brug for dem. Læs ikke alle på én gang. Stier som `references/planlaegning.md` nedenfor ligger i `didaktik-principper`. Denne skills egne filer skrives `${CLAUDE_SKILL_DIR}/references/...`.
2. **Vælg indgang.** Der er tre. Vælg ud fra lærerens besked, og spørg kun, hvis det er uklart: "Vil du planlægge hele forløbet nu, eller bare komme i gang med første modul?"

| Indgang | Når læreren | Vej gennem trinene |
|---------|-------------|--------------------|
| **A. Helt forløb** | vil have hele modulrækken nu | Gate 1, 2, 3, 4 og 5 |
| **B. Kom i gang** | starter et nyt forløb, men kun kan nå første modul, fx "jeg starter på EU i morgen" | Gate 1 kort, Gate 2 kort med skitse, Gate 4 for modul 1, Gate 5 |
| **C. Næste modul** | er i gang med et forløb og vil planlægge næste modul, fx "modul 3 i mit ulighedsforløb" | "Fortsæt et forløb" nedenfor |

Ved B og C ligger detaljerne for de senere moduler ikke fast. Sig det, og fasthold rammen, så modulerne stadig hænger sammen.

### Gate 1: Afklar rammer (VENT på svar)

Ved indgang B: spørg kun om fag, niveau, klasse, emne, omtrentligt antal moduler og hvad første modul skal nå. Hent læreplanens faglige mål og kernestof, hvis det kan gøres hurtigt. Vejledning, materialer og evaluering kan vente til næste modul. Skriv det, du antager.

Re-ground: "Vi planlægger et forløb. Jeg mangler nogle oplysninger, før jeg kan foreslå en ramme."

Spørg kun om det, læreren ikke allerede har sagt:

1. **Fag, niveau og klasse:** fx samfundsfag A, 2.g. Studieretning, hvis den betyder noget.
2. **Emne og omfang:** antal moduler, modullængde og omtrentlig placering i skoleåret.
3. **Mål og læreplan:** hvilke faglige mål og kernestofområder skal forløbet dække? Tilbyd at hente den nyeste læreplan og vejledning for fag og niveau fra uvm.dk efter `${CLAUDE_SKILL_DIR}/references/laereplaner.md`. Ligger de allerede i `_laereplaner/` i forløbsmappen, så tjek blot, om der er kommet en nyere version. Brug aldrig regler fra referencefilerne i `didaktik-principper` som gældende.
4. **Forudsætninger:** hvad har klassen haft før, og hvordan er klassen? Brug spørgsmålene i `references/elevforudsaetninger.md`, men stil højst tre.
5. **Afslutning og evaluering:** skal forløbet ende i et produkt, en prøve, en aflevering eller en mundtlig præsentation?
6. **Samspil og materialer:** er der et andet fag med, og er der en lærebog eller materialer, der skal bruges?

**Forløbsmappen:** planlægningen ligger som filer i en mappe på computeren. Læs `${CLAUDE_SKILL_DIR}/references/forloebsmappe.md`. Spørg, hvor forløbene skal ligge, hvis det ikke er klart. Søg efter tidligere forløb for samme klasse (`**/forloeb.md`), og brug dem til at se, hvad klassen har haft, og hvilke mål der allerede er dækket. Bed læreren bekræfte det, du finder.

Resten antager du og skriver tydeligt i Gate 2, så læreren kan rette det.

**VENT** på svar.

### Gate 2: Didaktisk ramme (VENT på OK)

Re-ground: "Vi er ved **Gate 2**. Her er den didaktiske ramme, før jeg laver modulrækken."

Læs `references/planlaegning.md`, `references/progression.md`, `references/dannelse-og-faglighed.md` og fagfilen i `references/fag/`, hvis der er en. Findes `references/fag/samfundsfag-polis.md`, så læs den også ved samfundsfag. Er faget erhvervsøkonomi eller et fag uden fagfil, så sig, at fagdidaktikken mangler, og brug de almene principper.

Vis rammen kort:

- **Formål i én sætning:** hvorfor er forløbet værd at lave, ud over at det står i læreplanen?
- **Slutkompetence:** hvad kan eleverne bagefter, som de ikke kunne før? Skriv det som en synlig handling.
- **Faglige mål:** de mål fra læreplanen, forløbet dækker, citeret ordret med afsnitsnummer fra den hentede læreplan, eller med lærerens ordlyd. Brug vejledningens uddybning og eksempler, når de passer til forløbet, og skriv versionen af læreplan og vejledning.
- **Tilgang:** induktiv eller deduktiv start, og om indholdet vælges ud fra faget, en aktuel udfordring eller begge. Anbefal én og begrund kort.
- **Progressionslinje:** hvordan selvstændighed, niveau og arbejdsformer udvikler sig fra første til sidste modul. Start med høj styring ved nyt og svært stof, og aftrap den, når klassen kan stoffet, jf. "Styring og forhåndsviden" i `didaktik-principper`. Læg de centrale begreber hver for sig først og saml dem senere, jf. "Dele før helhed" i `references/progression.md`.
- **Evaluering:** én formativ evaluering midt i forløbet, der kan ændre resten, og den afsluttende evaluering. Mål, aktiviteter og evaluering skal pege samme vej.
- **Antagelser:** det, du har antaget om klassen og rammerne.

**Ved indgang B** gør du rammen kort (formål, slutkompetence, tilgang og en foreløbig idé til evaluering, i alt få linjer) og tilføjer en **skitse**: én linje pr. modul med tema og hvad eleverne skal kunne. Planlæg derefter kun modul 1 i detaljer efter reglerne i Gate 3, og gå direkte til Gate 4 med modul 1. Første modul i et nyt forløb bør som regel afdække forforståelse og vise eleverne, hvor forløbet skal hen.

Spørg: "Passer rammen, eller skal formål, tilgang eller evaluering ændres?"

**VENT** på OK.

### Gate 3: Modulrække (VENT på OK)

Re-ground: "Vi er ved **Gate 3**. Her er modulrækken."

Læs `references/arbejdsformer-og-vejledning.md` og `references/evaluering.md`. Lav én række pr. modul:

| # | Tema | Mål for modulet | Arbejdsform og læringsrum | Stillads og støtte | Evaluering eller tjek | Lektie og hvorfor den er nødvendig |
|---|------|-----------------|---------------------------|--------------------|-----------------------|-----------------------------------|

Regler:

- Hvert modul har ét fagligt hovedmål. Skriv det, så det kan ses, om eleverne har nået det.
- Nye opgavetyper vises først (modellering), og støtten fjernes gradvist over forløbet.
- Ét nyt element pr. modul, når stoffet er nyt for klassen.
- Variér arbejdsformer og læringsrum over forløbet, men ikke i hvert modul.
- Lektier skal bruges i næste modul. Skriv hvordan.
- Læg den formative evaluering ind der, hvor resten af forløbet stadig kan ændres.
- Er det relevant, så læg små øvelser ind, der træner projektkompetencer før et større projekt.

Under tabellen:

- **Progression:** hvad bliver sværere eller mere selvstændigt fra modul til modul?
- **Tjekliste:** gå den samlede tjekliste i `didaktik-principper/SKILL.md` igennem, og skriv kun de punkter, der ikke er opfyldt, med et forslag til rettelse.
- **Praksisgreb:** tjek rækken mod faldgruberne i `references/praksisgreb.md`, og nævn kun dem, der rammer.
- **Evidens:** sæt et mærke, når læreren spørger hvorfor, eller når et valg koster noget.

Spørg: "Passer modulrækken, eller skal noget flyttes, slås sammen eller ændres?"

**VENT** på OK.

### Gate 4: Videre til de enkelte moduler (VENT på valg)

Re-ground: "Vi er ved **Gate 4**. Rækken er godkendt. Her er, hvad jeg kan lave til de enkelte moduler."

Foreslå konkret, pr. modul, hvilken skill der passer. Foreslå kun dem, modulet faktisk har brug for:

| Behov i modulet | Skill |
|-----------------|-------|
| Drejebog for et modul, hvor alle er med | `klasseledelse-planlaeg-lektion` |
| Tre-faset time om en fagtekst | `bloom-planlaeg-time` |
| Arbejdsspørgsmål eller lektiespørgsmål til en tekst | `bloom-spoergsmaal-til-tekst`, `bloom-lektiespoergsmaal` |
| En CL-øvelse eller et modul med CL | `cl-find-oevelse`, `cl-forloeb` |
| Gruppearbejde, der skal køre selv | `dagsorden-lav` |
| Casespil eller rollespil | `casespil-nyt` eller `casespil-miniversion` |
| Slides | `powerpoint-stil` |
| Quiz til repetition | `blooket-lav-quiz` |
| Køreplan på storskærm | `dida-plan` |

Spørg: "Hvilket modul og hvilken skill vil du starte med?"

**VENT** på valg. Kald derefter skillen med Skill-værktøjet, og giv den modulets tema, mål, arbejdsform, tid, klasse og forudsætninger fra modulrækken, så læreren ikke skal svare på det igen. Tag ét modul ad gangen, og vend tilbage til rækken bagefter. Er en skill ikke tilgængelig, så sig, at den hører til et plugin, der ikke ser ud til at være installeret, og fortsæt uden.

### Gate 5: Gem forløbet (VENT på ja)

Tilbyd at gemme forløbet i forløbsmappen, og nævn mappens sti. Skriv ikke filer uden et ja.

- Opret forløbets undermappe og `forloeb.md` efter skabelonen i `references/forloebsmappe.md`, med rammen og modulrækken.
- Opret en fil for hvert modul, der er planlagt i detaljer, fx `modul-01-<tema>.md`.
- Laver en anden skill materialer til et modul, så bed den gemme dem i samme forløbsmappe med modulnummeret først i filnavnet.
- **Ved indgang B:** sæt status til "foreløbig ramme", skriv de senere moduler som skitse i rækken, og opret kun filen for modul 1. Sig til læreren, at næste modul kan planlægges med "planlæg næste modul i [forløbets titel]".
- Sig bagefter, hvilke filer der er oprettet, og hvor de ligger.

## Fortsæt et forløb (indgang C)

Re-ground: "Vi fortsætter et forløb, du er i gang med."

1. **Find forløbet.** Søg efter `forloeb.md` i forløbsmappen, og læs den. Er der flere forløb, der kan passe, så spørg, hvilket. Findes der ingen fil, så bed læreren om en kort beskrivelse af rammen og de moduler, der er afholdt, og tilbyd at oprette `forloeb.md` ud fra den. Find ikke på tidligere moduler.
2. **Spørg kort (VENT på svar):** Hvordan gik sidste modul? Nåede klassen det planlagte? Var der noget, eleverne ikke forstod? Brug svaret som formativ evaluering, jf. `references/evaluering.md`.
3. **Justér skitsen.** Ret de kommende moduler, hvis klassen er foran eller bagud, og sig, hvad du har ændret, og hvorfor. Er forløbet planlagt med indgang B, så gør rammen færdig nu, fx med læreplan, vejledning og evaluering, hvis det mangler. Står der "ikke tjekket" ved læreplanen i `forloeb.md`, så tilbyd at hente den.
4. **Planlæg næste modul i detaljer** efter reglerne i Gate 3, og vis det som én række i samme tabel. Tjek, at det bygger på sidste modul og peger mod slutkompetencen.

**VENT** på OK. Fortsæt derefter med Gate 4 for modulet og Gate 5. Ved gem følges "Når forløbet fortsættes" i `references/forloebsmappe.md`: log, status, rettelser i rækken og en ny modulfil.

## Når læreren beder om ændringer

Ret kun det, læreren beder om. Tjek bagefter, at progressionen og sammenhængen mellem mål, aktiviteter og evaluering stadig holder, og sig det, hvis ændringen bryder den.

## Kvalitetstjek inden aflevering

- Summer modulerne til det antal, læreren har?
- Har hvert modul ét mål, der kan ses?
- Kan man se progressionen fra første til sidste modul?
- Er der en formativ evaluering, der kan ændre resten?
- Peger evalueringen på forløbets mål?
- Er alle henvisninger til læreplan og regler enten fra læreren, fra den gældende læreplan eller markeret som noget, der skal tjekkes?
- Er der intet, der bygger på læringsstile?

---

## Completion Status

- **DONE**: Ramme og modulrække (eller skitse og ét modul ved indgang B og C) godkendt, og videresendelse og gem tilbudt
- **DONE_WITH_CONCERNS**: Leveret, men stofmængden er stor, eller læreplanen er ikke tjekket
- **NEEDS_CONTEXT**: Mangler fag, niveau, antal moduler eller mål
