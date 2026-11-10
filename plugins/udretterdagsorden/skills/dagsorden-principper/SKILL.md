---
name: dagsorden-principper
description: "Vidensbase for udretterdagsordener: selvkørende trin-for-trin-protokoller til gruppearbejde i STX. Indeholder pædagogisk grundlag, de tre roller (pas-på-tur, pas-på-tid, pas-på-doc), fasebibliotek, kvalitetskriterier, JSON-format til dida.dk og Word samt validerings- og Word-scripts. Læses af dagsorden-lav og dagsorden-ide. Brug direkte, når læreren spørger, hvad en udretterdagsorden er, hvad rollerne betyder, eller hvorfor en dagsorden skal have individuel tænketid og pause. Brug ikke til at lave en konkret dagsorden (dagsorden-lav), til at vælge struktur (dagsorden-ide), til CL-øvelser (cl-principper) eller til klasseledelse generelt (klasseledelse-principper)."
user-invocable: false
allowed-tools:
  - Read
  - Glob
---

# Udretterdagsorden: vidensbase

Trin-for-trin arbejdsprotokoller til gruppearbejde i gymnasiet (STX, elever 16 til 20 år). En udretterdagsorden designer selve interaktionen i gruppen: hvem gør hvad, hvornår, i hvilken rækkefølge og hvor længe.

En udretterdagsorden er **ikke** en opgavebeskrivelse og **ikke** en projektvejledning. Den er selvkørende: eleverne skal kunne arbejde uden løbende lærervejledning.

Scripts og eksempler ligger i denne skill. Andre skills kalder dem via `${CLAUDE_SKILL_DIR}/../dagsorden-principper/`.

---

## Arbejdsgang: hurtigt, kort og samlet

Gælder alle skills i pluginet og går forud for deres gates. Samme afsnit står i de andre undervisningsplugins, så de opfører sig ens.

### Hurtig eller grundig

Læreren vælger selv. Start med ét spørgsmål, og **VENT** på svar:

"Vil du have det hurtigt, hvor jeg antager resten og afleverer med det samme, eller en grundigere planlægning, hvor vi afklarer og godkender undervejs?"

Mangler der noget under "Skal kendes" i den enkelte skill, så spørg om det i samme besked.

Spørg ikke, når valget allerede er truffet:

- Læreren skriver "hurtigt", "bare lav den", "ingen spørgsmål" eller lignende: hurtig.
- Læreren beder om sparring, fx "hvad synes du?" eller "hjælp mig med at vælge", eller om den grundige udgave: grundig.
- Læreren har valgt tidligere i samtalen: valget gælder, indtil læreren siger andet.
- Opgaven kommer fra en anden skill, jf. "Når en anden skill sender videre".
- Skillen siger selv, at den ikke har nogen gate.

**Hurtig-tilstand:**

1. Stil ingen flere spørgsmål, og spring gates om afklaring og godkendelse over. Gates, der tilbyder printmateriale eller en anden skill, bliver til én linje til sidst.
2. Skriv dine antagelser i én linje øverst, fx "Antaget: 2.g, 90 min. med pause, de fleste har læst."
3. Aflever den korte version med det samme.
4. Slut med én linje om, hvad læreren kan bede om nu.

**Grundig planlægning:** brug gates, som de står i skillen. Outputtet er stadig kort som standard.

I begge tilstande gælder reglerne om indhold: find ikke på indhold fra tekster, du ikke har læst, og sig, hvad der ikke er tjekket.

### Kort som standard

- Aflever det, læreren skal bruge i timen. Begrundelser, optællinger og tjeklister skrives kun, når de viser et problem, eller når læreren beder om dem.
- Lav kvalitetstjek stille. Skriv kun de punkter, der ikke holder.
- Gentag ikke lærerens oplysninger, og forklar ikke, hvad du vil gøre.
- Den enkelte skill siger, hvad den korte version indeholder, og hvad der kun kommer på opfordring. Nævn det sidste i én linje, ikke som en liste af tilbud.

### Forløbsmappen

Kan du se filer, så søg efter `forloeb.md` i den mappe, I arbejder i (`**/forloeb.md`). Den laves af `didaktik-planlaeg-forloeb`. Findes den, og hører opgaven til forløbet:

- Læs den, og brug fag, klasse, modullængde, modulets mål og det, klassen har haft. Spørg ikke om det, der står der.
- Gem resultatet i forløbets mappe med modulnummeret først i filnavnet, fx `modul-03-drejebog.md`, og sig, hvor det ligger. Overskriv ikke en fil uden at sige det først.
- Ret ikke i `forloeb.md`. Det gør `didaktik-planlaeg-forloeb`.

Findes den ikke, så nævn den ikke, og gem kun filer, når læreren beder om det.

### Når en anden skill sender videre

Kommer opgaven fra en anden skill, eller ligger der en plan i samtalen, som læreren lige har godkendt, så brug det, der allerede er afklaret, og spring din egen afklaring og godkendelse af det samme over. Gå direkte til resultatet.

---

## Pædagogisk grundlag

Disse principper (Johnson & Johnson, Kagan, Gillies) skal gennemsyre alle dagsordener:

### 1. Positiv indbyrdes afhængighed
Eleverne lykkes kun, hvis gruppen lykkes. Sikres via rollefordeling, fælles produkt og delt ansvar.

### 2. Individuel ansvarlighed
Hvert medlem har en unik funktion, som ikke kan overtages af andre. Uden dette opstår social loafing (passageradfærd).

### 3. Individuel tænketid inden deling
Tavs, individuel refleksion (læsning, egne noter) skal komme *før* fælles diskussion. Det giver mere differentierede bidrag og aktiverer de stille elever.

### 4. Progressiv kompleksitet
Start let (orientering, overblik), bevæg dig mod det sværere (analyse, vurdering, fortolkning). Slut gerne med en opsummerende meta-refleksion.

### 5. Synlig dokumentation
Et fælles løbende dokument (typisk Google Doc) gør bidrag synlige og modvirker social loafing. Det er materialet, eleverne tager med sig.

### 6. Roller roterer
Faste roller tildeles ved starten via objektive kriterier og bør rotere fra gang til gang.

---

## De tre standardroller

Disse roller indgår i **alle** dagsordener:

| Rolle | Funktion |
|---|---|
| **Pas-på-tur** | Ordstyrer. Sikrer alle præsenterer på tur. Giver ordet videre. |
| **Pas-på-tid** | Tidsstyrer. Holder øje med uret. Giver besked ved halvtid og udløb. |
| **Pas-på-doc** | Referent/skriver. Skriver løbende stikord i det fælles dokument. |

### Tildelingskriterier

Kriterierne skal være **sjove, hurtige og objektive**, aldrig frivillighed. Vælg tre forskellige fra denne liste:

- Den der senest/snarest har fødselsdag
- Den ældste/yngste
- Den der bor tættest på/længst fra skolen
- Den der senest stod op i dag / tidligst stod op
- Den med kortest/længst fornavn
- Den der sidst var i udlandet
- Den der sidst så en film i biografen

Brug **altid** tre *forskellige* kriterier, aldrig det samme for to roller.

### Regler for rollebrug i dagsordenen

1. **Roller defineres kun ét sted**, i rolletabellen i toppen af dagsordenen. Senere trin må ikke gentage rolledefinitioner i en ny tabel, for så tror eleverne, at rollerne har skiftet.
2. **Roller bruges til instruktioner, ikke til fordeling af fagligt indhold.** Når eleverne i et trin skal fordele emner, faner eller cases mellem sig, så brug en simpel punktliste ("Fordel disse tre faner mellem jer, én per person:") og ikke en tabel, der mapper roller til emner. Rollenavne i faglig fordeling skaber forvirring om, hvorvidt rollerne har skiftet.
3. **Samme gruppe i begge runder**, når den samlede tid er under 45 minutter. Omgruppering kræver tid til nye roller, nyt doc og ny tillidsopbygning (mindst 5 til 8 min ekstra). Ved matrix- og jigsaw-strukturer (60+ min) kan omgruppering give mening.

---

## Fasetyper

En veldesignet dagsorden veksler systematisk mellem disse:

| Fasetype | Beskrivelse | Typisk varighed |
|---|---|---|
| **Rollevalg** | Fordeling af roller via objektive kriterier | 2 til 4 min |
| **Individuel forberedelse** | Tavs, individuel læsning eller notering | 3 til 8 min |
| **Individuel præsentation på tur** | Alle præsenterer deres pointer/fund én ad gangen | 5 til 12 min |
| **Fælles analyse / diskussion** | Fælles bearbejdning af materialet | 5 til 15 min |
| **Pause** | Hyggesnak, toilet, vand | 5 min |
| **Produktion** | Fælles produkt: noter, model, oversigt, opsummering | 5 til 15 min |
| **Afslutning / meta-refleksion** | Hvad lærte vi? Hvad er uklart? | 3 til 5 min |

Hvert trin bør kun have **ét klart formål**. Bland ikke overblik og analyse i samme trin.

---

## Regler for instruktionstekst

1. **Skriv til eleverne, ikke om dem.** Brug "I", "du", "jeres".
2. **Vær konkret og handlingsorienteret.** "Skim i tavshed", ikke "læs teksten".
3. **Angiv rækkefølge med numre** 1), 2), 3), når der er flere delopgaver.
4. **Angiv pas-på-docs opgave** eksplicit i alle trin, hvor der skal skrives.
5. **Undgå fagord, der skal forklares.** Dagsordenen skal være selvkørende.
6. **Brug OBS:** til vigtige præciseringer og særlige instruktioner.
7. **Materialereferencer skal være elevvendte.** Skriv "Jeres lektie (afsnit 4.5: Levevilkår)", ikke "Columbus 4.5" eller andre interne bogkoder. Eleverne kender ikke forlagsbetegnelser.
8. **Brug lærerens navn** i stedet for "læreren", hvis du kender det fra samtalen eller en CLAUDE.md. Skriv "deler med gruppen og Kenneth", ikke "deler med gruppen og læreren". Det er mere personligt og klart. Kender du ikke navnet, så spørg én gang, eller skriv "jeres lærer".

---

## Kvalitetskriterier

En god udretterdagsorden:

- Er **selvkørende**: eleverne behøver ikke spørge læreren
- Har **klare roller** tildelt via objektive kriterier
- Veksler mellem **individuel tænketid** og **fælles aktivitet**
- Har **progressiv kompleksitet**: starter lettere, slutter sværest
- Har **tidsangivelse på hvert trin** og en totaltid, der stemmer
- Angiver **eksplicit, hvad pas-på-doc skal skrive** i hvert trin
- Bruger **konkret, handlingsorienteret sprog**
- Har en **pause** midt i forløb over 25 minutter
- Ender med et **fælles produkt** eller en **opsummering**

En dårlig udretterdagsorden:

- Skriver "diskuter emnet" uden at specificere hvad
- Blander overblik og dyb analyse i samme trin
- Glemmer, hvad pas-på-doc skal gøre
- Bruger over 4 min på rollevalg
- Har tidsrammer, der ikke summer til totaltiden
- Bruger fagord, der kræver forklaring
- Har alle trin som gruppearbejde uden individuel fase
- Gentager rolledefinitioner i en ny tabel senere i dagsordenen
- Bruger rollenavne til at fordele fagligt indhold (brug neutral fordeling i stedet)
- Refererer til materiale med interne bogkoder, eleverne ikke kender

---

## Varianter

### Dagsorden uden pause (under 25 min)
Udelad pausetrinnet. Struktur: rollevalg, individuel fase, præsentation på tur, fælles bearbejdning, produkt/opsummering.

### Matrix/jigsaw-struktur
Eleverne fordeler emner/dele, arbejder individuelt, mødes med tilsvarende fra nabogruppe (matrix), vender tilbage og præsenterer. Kræver mindst 60 min. Se referenceeksemplet `eksempel-polkom-matrix.json`.

### Peer-feedback
Tilføj et trin, hvor eleverne læser hinandens produkt i tavshed, inden de giver feedback på tur. Pas-på-doc skriver feedback-pointer ned.

### Repetition / quiz-på-tur
Pas-på-tur stiller spørgsmål, de andre svarer tur for tur. Pas-på-doc skriver det, gruppen er usikre på. Slutter med at gennemgå det usikre.

### Model/begrebsforståelse
Individuel fase: tegn/skriv en model. Præsentation på tur: forklar din model. Fælles fase: byg én fælles model fra alle bidrag.

### Case med dilemma
Individuel fase: identificér problemet/dilemmaet. Præsentation: præsentér din identifikation og dit argument. Fælles fase: rangér argumenterne. Produkt: begrundet stillingtagen.

### Plenumforberedelse
Mange dagsordener afsluttes med forberedelse til klassediskussion. Tilføj et afsluttende trin: "Formulér ét spørgsmål eller én pointe, I vil bringe op i plenum."

---

## Output: kanonisk JSON-format

Alle dagsordener produceres som JSON i ét format. Samme JSON bruges til **tre outputs**:

| Output | Hvordan |
|---|---|
| **dida.dk** | Kopiér JSON, sæt den ind i importfeltet på `dida.dk/d/` og klik Importér. Eleverne følger dagsordenen på deres telefoner. |
| **Word** | `node "${CLAUDE_SKILL_DIR}/scripts/generate-dagsorden.js" --input fil.json --output fil.docx` |
| **Markdown** | AI'en renderer JSON som læsbar markdown direkte i chatten |

Dagsordenen er til gruppearbejdet på elevernes egne skærme. En lektionsplan til storskærmen laves med `dida-plan` i pluginet `dida`.

### Komplet JSON-skema

```json
{
  "title": "Velfærdsstaten i krise",
  "topic": "Velfærdsstaten og ideologier",
  "subject": "Samfundsfag",
  "klasse": "3x",
  "totalTime": 45,
  "groupCount": 4,
  "groupLabels": ["Liberalismen", "Konservatismen", "Socialdemokratismen", "Socialliberalismen"],
  "groupPaced": false,
  "freeGroupNumber": false,
  "roles": [
    {
      "navn": "Pas-på-tur",
      "beskrivelse": "Den der senest var i udlandet: ordstyrer, sikrer alle præsenterer på tur"
    },
    {
      "navn": "Pas-på-tid",
      "beskrivelse": "Den der tidligst stod op i dag: tidsstyrer, giver besked ved halvtid og udløb"
    },
    {
      "navn": "Pas-på-doc",
      "beskrivelse": "Den med kortest fornavn: referent, skriver stikord i det fælles dokument"
    }
  ],
  "steps": [
    {
      "heading": "Rollevalg",
      "type": "normal",
      "duration": 3,
      "instruction": "1) Fordel roller efter kriterierne ovenfor.\n2) Pas-på-doc opretter et Google Doc og deler med gruppen og Kenneth.",
      "note": null,
      "docInstruction": null,
      "requiresAnswer": false,
      "groupInstructions": null
    },
    {
      "heading": "Individuel forberedelse",
      "type": "individuel",
      "duration": 7,
      "instruction": "Læs teksten i tavshed og notér:\n\n1) To begreber du kender i forvejen\n2) Ét begreb du er i tvivl om",
      "note": "Stil ikke spørgsmål til hinanden endnu.",
      "docInstruction": null,
      "requiresAnswer": false,
      "groupInstructions": null
    },
    {
      "heading": "Gruppeanalyse",
      "type": "normal",
      "duration": 12,
      "instruction": "Diskutér: Hvad mener **jeres ideologi** om velfærdsstaten?\n\nBrug tekstens begreber: omfordelingsprincip, universalisme, behovsprøvning.",
      "note": "Husk: alle argumenter skal komme fra teksten.",
      "docInstruction": "Pas-på-doc skriver gruppens vigtigste pointer i stikord.",
      "requiresAnswer": true,
      "groupInstructions": {
        "1": "Fokusér på liberalismens syn: individuel frihed, minimal stat, behovsprøvning.",
        "2": "Fokusér på konservatismens syn: tradition, fællesskab, gradvis reform.",
        "3": "Fokusér på socialdemokratismens syn: lighed, universalisme, omfordeling.",
        "4": "Fokusér på socialliberalismens syn: frihed med socialt sikkerhedsnet."
      }
    }
  ]
}
```

### Feltregler

| Felt | Type | Påkrævet | Bruges i | Beskrivelse |
|---|---|---|---|---|
| `title` | string | ja | dida.dk, Word | Kort titel til sessionen |
| `topic` | string | ja | dida.dk, Word | Uddybende emnebeskrivelse |
| `subject` | string | ja | dida.dk, Word | Fagnavn |
| `klasse` | string | nej | Word | Klassenavn (ignoreres af dida.dk) |
| `totalTime` | number | ja | Word, validering | Samlet tid i minutter. **Skal** matche summen af alle steps. |
| `groupCount` | number | nej | dida.dk | Antal grupper. Standard: 0 (ingen gruppevalg) |
| `groupLabels` | string[] | nej | dida.dk | Navne på grupperne, fx ideologier, cases, lande |
| `groupPaced` | boolean | nej | dida.dk | Grupper styrer eget tempo. Standard: false |
| `freeGroupNumber` | boolean | nej | dida.dk | Elever skriver selv gruppenummer. Standard: false |
| `roles` | array[3] | ja | alle | Præcis 3 roller med `navn` og `beskrivelse` |
| `steps` | array | ja | alle | Alle trin i rækkefølge |

### Step-felter

| Felt | Type | Påkrævet | Bruges i | Beskrivelse |
|---|---|---|---|---|
| `heading` | string | ja | alle | Kort overskrift for trinnet |
| `type` | string | ja | alle | `"normal"`, `"individuel"` eller `"pause"` |
| `duration` | number | ja | alle | Tid i hele minutter |
| `instruction` | string | ja | alle | Fuld instruktion til eleverne. `\n` = ny linje, `\n\n` = ny blok. Understøtter `**fed**` markdown. |
| `note` | string | nej | alle | Vigtig præcisering (uden "OBS:"-præfiks, det tilføjes automatisk) |
| `docInstruction` | string | nej | Word, markdown | Separat pas-på-doc-instruktion. I dida.dk flettes den ind i `instruction`. |
| `requiresAnswer` | boolean | nej | dida.dk | Gruppen skal indsende et skriftligt svar. Standard: false |
| `groupInstructions` | object | nej | dida.dk | Gruppespecifik instruktion: `{"1": "...", "2": "..."}` |

### Type-værdier

| Type | Betydning | Hvornår |
|---|---|---|
| `"normal"` | Standard gruppetrin | De fleste trin |
| `"individuel"` | Tavs, individuel fase | Forberedelse, refleksion, læsning |
| `"pause"` | Pause | Hyggesnak, toilet, vand |

### Tekstformatering i `instruction`

- `\n` = ny linje (samme blok)
- `\n\n` = ny blok med ekstra afstand (visuelt adskilt)
- `**fed tekst**` = fremhævet tekst (virker i dida.dk og markdown)
- Brug `\n\n` til at adskille logiske dele, fx introduktion, rollefordelte opgaver og fælles instruktion

### Grupper og differentiering

Når `groupCount > 0`, kan hvert trin have `groupInstructions`, et objekt der mapper gruppenummer til en specifik instruktion:

```json
"groupInstructions": {
  "1": "Analysér Liberalismens syn på skattelettelser...",
  "2": "Analysér Konservatismens syn på tradition..."
}
```

- Eleven ser kun sin gruppes instruktion i dida.dk
- Grupper uden specifik instruktion ser standard-`instruction` som fallback
- `groupLabels` navngiver grupperne (vises i dida.dk ved gruppevalg)

### Validering

Kør altid valideringsscriptet, før du leverer JSON. Det fanger tidsfejl og strukturbrud, som er lette at overse i hånden:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/validate-dagsorden.py" dagsorden.json
```

Exit 0 = OK, exit 2 = fejl (med besked om, hvad der skal rettes). Kriterierne:
1. `totalTime` == sum af alle `steps[].duration`
2. Trin 1 er altid rollevalg (2 til 4 min)
3. Pause er med, hvis totalTime > 25
4. Alle trin med gruppeproduktion har `docInstruction` eller nævner pas-på-doc i `instruction`
5. Der er mindst én individuel fase (tavs læsning/notering) før første gruppefase
6. `note`-felter indeholder ikke "OBS:"-præfiks (det tilføjes automatisk)
7. `groupCount` matcher længden af `groupLabels` (hvis begge er angivet)
8. `groupInstructions`-nøgler er strenge ("1", "2") og matcher `groupCount`

---

## Word-generering

Når JSON er klar:

```bash
node "${CLAUDE_SKILL_DIR}/scripts/generate-dagsorden.js" \
  --input dagsorden.json \
  --output dagsorden.docx
```

Scriptet kræver npm-pakken `docx`. Fejler det med "Cannot find module 'docx'", så kør `npm install` i mappen `${CLAUDE_SKILL_DIR}/scripts` (der ligger en `package.json`), og prøv igen. Node leder efter pakker ved siden af scriptet, ikke i arbejdsmappen.

Scriptet accepterer det kanoniske JSON-format og mapper automatisk:
- `heading` til `hvad`-kolonnen
- `instruction` til `hvordan`-kolonnen (med `docInstruction` tilføjet)
- `totalTime` til total-rækken

Designet kan justeres i `DESIGN`-objektet øverst i scriptet.

---

## Referenceeksempler

Læs eksempler i `${CLAUDE_SKILL_DIR}/resources/` for format, detaljeniveau og sprog:

- `eksempel-polkom-matrix.json`: matrix/jigsaw med case-analyse (80 min, 3 elever, samfundsfag). Viser fordeling af arbejdsspørgsmål, matrix-fase med nabogruppe, stamgruppe-sammenskrivning og kvalitetstjek.

Brug eksemplerne som reference for:
- Detaljeniveau i `instruction`-feltet
- Hvornår `\n\n` bruges til visuelt brud
- Hvordan `note` og `docInstruction` supplerer `instruction`
- Passende tidsallokering pr. fasetype
