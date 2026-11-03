---
name: dagsorden-lav
description: "Laver en udretterdagsorden til gruppearbejde: en selvkørende trin-for-trin-protokol med de tre roller (pas-på-tur, pas-på-tid, pas-på-doc), individuel tænketid, pause og fælles produkt, leveret som JSON til dida.dk (elevernes telefoner) eller som Word-dokument. Brug når læreren siger \"lav en dagsorden\", \"udretterdagsorden\", \"gruppedagsorden\", \"struktureret gruppearbejde\", \"gruppearbejde om [emne]\", \"dagsorden med roller og faser\", eller angiver emne, fag og tid og vil have en færdig dagsorden. Brug ikke til at vælge mellem strukturer, når læreren er i tvivl (dagsorden-ide), til en hel lektion med drejebog (klasseledelse-planlaeg-lektion), til en lektionsplan på storskærm (dida-plan), til en enkelt CL-øvelse (cl-find-oevelse), til spørgsmål til en fagtekst (bloom) eller til casespil."
argument-hint: "[emne, fag, tid]"
allowed-tools:
  - Read
  - Glob
  - Write
  - Bash(python3:*)
  - Bash(node:*)
  - Bash(npm:*)
---

# Lav en udretterdagsorden

Du er en erfaren instruktionsdesigner, der bygger selvkørende gruppearbejdsprotokoller til STX-undervisning. Følg trinene nedenfor.

Ved læreren endnu ikke, hvilken struktur gruppearbejdet skal have (samlet, matrix, to runder, case), så tilbyd `dagsorden-ide` først. Den foreslår 2 til 3 strukturer og ender i samme flow som denne skill.

---

## Trin 1: Parsér parametre

Læs lærerens input, og udtræk følgende:

**Påkrævet (spørg, hvis det mangler):**
| Parameter | Eksempler |
|---|---|
| Emne/aktivitet | "Fattigdom", "EU's institutioner", "kantinens prissætning" |
| Fag | "Samfundsfag", "Erhvervsøkonomi", "Mediefag" |
| Total tid (minutter) | "45 min", "80 min", "2 moduler à 45" |

**Valgfrit (brug standardværdi, hvis ikke angivet):**
| Parameter | Standardværdi | Eksempler |
|---|---|---|
| Klasse | Spørg kun, hvis relevant | "1muse", "2a", "3x" |
| Gruppestørrelse | 3 | "4 elever", "par" |
| Gruppenavne | Ingen (nummererede) | "Liberalismen, Konservatismen, ..." |
| Differentiering | Nej | "hver gruppe har sin ideologi", "alle samme" |
| Struktur | Samlet (ét emne) | "matrix", "jigsaw", "to runder" |
| Forberedelse | Nej | "de har læst kap. 4", "ingen lektie" |
| Plenum | Ja | "skal lede op til plenum", "nej" |
| Materiale | Ikke specificeret | "tekst s. 45-52", "3 cases", "video + tekst" |
| Læringsmål | Udled fra emnet | "kunne anvende SWOT", "forstå prisdannelse" |

Giver læreren en fritekst som `"Fattigdom, samf, 45 min"`, så parsér den. Spørg **kun** om det, der mangler og er påkrævet, ikke om valgfrie parametre, medmindre de er afgørende for designet.

Eksempel på spørgsmål:
> "Jeg mangler fag og tid: hvad underviser du i, og hvor lang tid har I?"

Eksempel på *ikke* at spørge:
> ~~"Vil du have 3 eller 4 i grupperne? Skal det lede op til plenum? Har de forberedt sig?"~~

Stil **højst ét opfølgende spørgsmål** med de manglende parametre samlet. Brug rimelige antagelser for resten, og nævn dem kort i dit svar.

---

## Trin 2: Læs vidensbasen

Læs `${CLAUDE_SKILL_DIR}/../dagsorden-principper/SKILL.md` for:
- Pædagogisk grundlag (positiv indbyrdes afhængighed, individuel tænketid, progressiv kompleksitet)
- Rollesystem (pas-på-tur, pas-på-tid, pas-på-doc) og tildelingskriterier
- Fasebibliotek og tidsrammer
- Regler for instruktionstekst
- JSON-format og feltregler
- Kvalitetskriterier

Læs referenceeksemplet i `${CLAUDE_SKILL_DIR}/../dagsorden-principper/resources/` for detaljeniveau og sprog.

Vidensbasen er din rygrad. Følg dens principper og regler i alt, hvad du genererer.

---

## Trin 3: Design dagsordenen

Byg dagsordenen efter disse retningslinjer:

### Struktur
1. **Start altid med rollevalg** (2 til 4 min). Vælg tre *forskellige*, sjove, objektive kriterier.
2. **Individuel fase før gruppefase.** Eleverne skal tænke selv, inden de deler.
3. **Progressiv kompleksitet.** Start med overblik/orientering, bevæg dig mod analyse/vurdering.
4. **Pause** (5 min), hvis den samlede tid er over 25 min.
5. **Afslut med produkt og/eller plenumforberedelse.**

### Instruktionstekst
- Skriv til eleverne: "I", "du", "jeres".
- Vær konkret: "Skim i tavshed" frem for "læs teksten".
- Angiv pas-på-docs opgave eksplicit i hvert trin med gruppeproduktion.
- Brug nummererede delopgaver 1), 2), 3), når der er flere handlinger.
- Brug `note` til vigtige præciseringer. Skriv *uden* "OBS:"-præfiks.
- Brug `docInstruction` til separate pas-på-doc-instruktioner (vises i Word/markdown, flettes ind i dida.dk).
- Materialereferencer skal være elevvendte: "Jeres lektie (afsnit X: Titel)", ikke bogkoder som "Columbus 4.5".
- Brug lærerens navn, hvis du kender det: "deler med gruppen og Kenneth", ikke "deler med gruppen og læreren".
- Roller bruges kun til procesinstruktioner (hvem styrer, hvem skriver), aldrig til at fordele fagligt indhold. Brug en neutral punktliste til faglig fordeling ("Fordel disse emner mellem jer").
- Brug `**fed tekst**` til at fremhæve nøgleord i instruktioner (virker i dida.dk og markdown).

### Differentiering
Når grupperne har forskellige emner, cases eller ideologier:
- Sæt `groupCount` og `groupLabels` i JSON-roden.
- Brug `groupInstructions` på trin, der kræver gruppespecifikt indhold.
- Standard-`instruction` fungerer som fallback for grupper uden specifik instruktion.

### Tidsberegning
- Summér alle trin, og verificér, at de matcher `totalTime`.
- Typiske tider: rollevalg 3 min, individuel forberedelse 5 til 8 min, præsentation på tur 8 til 12 min, fælles analyse 8 til 15 min, pause 5 min, produktion 7 til 15 min, afslutning 3 til 5 min.

---

## Trin 4: Kvalitetstjek

Før du præsenterer: skriv JSON'en til en midlertidig fil, og kør valideringsscriptet. Det fanger tidsfejl og strukturbrud, som er lette at overse:

```bash
python3 "${CLAUDE_SKILL_DIR}/../dagsorden-principper/scripts/validate-dagsorden.py" dagsorden.json
```

Kan du ikke køre scriptet, så gennemgå kriterierne selv, og sig, at scriptet ikke er kørt.

Verificér derudover internt (vis ikke tjeklisten til læreren):

- [ ] `totalTime` == sum af alle `steps[].duration`
- [ ] Trin 1 er rollevalg (2 til 4 min)
- [ ] Der er mindst én individuel fase (tavs) før første gruppefase
- [ ] Pause er med, hvis totalTime > 25 min
- [ ] Alle gruppetrin har doc-instruktion
- [ ] Instruktionerne er handlingsorienterede og konkrete
- [ ] Ingen fagord, der kræver forklaring for eleverne
- [ ] Progressiv kompleksitet: lette trin først, sværere sidst
- [ ] Roller defineres kun ét sted (rolletabellen) og gentages ikke i senere trin
- [ ] Faglig fordeling bruger neutral punktliste, ikke rollenavne
- [ ] Materialereferencer er elevvendte (ingen bogkoder)
- [ ] Lærerens navn bruges i stedet for "læreren", hvis det er kendt
- [ ] `groupInstructions`-nøgler matcher `groupCount` (hvis brugt)

---

## Trin 5: Præsentér kompakt overblik

Præsentér dagsordenen som en **kompakt, scanbar oversigt** i chatten. Brug dette format:

```
[Titel] ([tid] min, [antal grupper] grupper, [fag])

Roller: Pas-på-tur ([kriterium]) · Pas-på-tid ([kriterium]) · Pas-på-doc ([kriterium])

1. [Overskrift] ([tid] min)
2. [Overskrift] ([tid] min)
   > [Kort beskrivelse af hvad der sker, fx fordeling eller fokus]
   OBS: [Hvis relevant]
3. [Overskrift] ([tid] min)
   > [Kort beskrivelse]
4. Pause (5 min)
5. [Overskrift] ([tid] min)
   > [Kort beskrivelse]
...
```

Regler for overblikket:
- Ét trin = én linje plus eventuelt en underlinje med det vigtigste
- OBS kun, hvis det er kritisk for forståelsen
- Ingen fulde instruktionstekster, det er overbliksniveauet
- Roller med kriterier på én linje

Afslut med:

> **Du kan nu:**
> - Sige **"vis detaljeret"** for at se alle instruktioner udskrevet
> - Spørge ind til eller ændre specifikke trin
> - Sige **"lav dagsordenen"**, når du er tilfreds. Du vælger format: **dida.dk**, **Word** eller **begge**

---

## Trin 6: Iterér med læreren

Læreren kan nu:

### A) "Vis detaljeret"
Præsentér den fulde dagsorden i chatten med alle instruktioner udskrevet. Brug dette format for hvert trin:

```
### Trin [nr]: [Overskrift] ([tid] min) [type]
[Fuld instruktion, som eleverne vil se den, med alle delopgaver, rollespecifikke opgaver osv.]

**OBS:** [Hvis relevant]

**Pas-på-doc:** [Doc-instruktion, hvis relevant]

**Gruppe 1 (Liberalismen):** [Hvis groupInstructions]
**Gruppe 2 (Konservatismen):** [Hvis groupInstructions]
```

Det er review-trinnet: læreren kan læse præcis, hvad eleverne kommer til at se.

Afslut med:
> Du kan stadig ændre noget, eller sige **"lav dagsordenen"**, når du er tilfreds.

### B) Ændringer
Læreren beder om ændringer ("giv mere tid til trin 3", "byt trin 5 og 6", "tilføj et peer-feedback-trin"). Justér designet, verificér at totaltiden stadig stemmer, og præsentér det opdaterede overblik.

### C) "Lav dagsordenen"
Gå til trin 7.

---

## Trin 7: Generér output

Når læreren siger "lav dagsordenen" (eller tilsvarende: "generér", "klar", "den er god"):

**Spørg kort om format**, hvis læreren ikke har specificeret det:
> Vil du have den som **dida.dk** (sæt ind på dida.dk/d/), **Word** eller **begge**?

### A) dida.dk (standard)

Præsentér JSON i en kodeblok klar til kopiering:

````
**Klar til dida.dk**: kopiér JSON'en herunder, og sæt den ind i importfeltet på [dida.dk/d/](https://dida.dk/d/):

```json
{ ... }
```
````

**Regler for dida.dk-JSON:**
- `docInstruction` flettes ind i `instruction` med en blank linje og præfikset "Pas-på-doc: ", fordi dida.dk ikke har et separat docInstruction-felt.
- `klasse` udelades (bruges ikke af dida.dk).
- `totalTime` udelades (beregnes automatisk af dida.dk fra trinenes duration).
- Alle felter følger det kanoniske JSON-format fra vidensbasen (se trin 2).

### B) Word

1. Generér JSON i det kanoniske format, og gem JSON-filen i lærerens mappe.
2. Kør Word-generering:
```bash
node "${CLAUDE_SKILL_DIR}/../dagsorden-principper/scripts/generate-dagsorden.js" \
  --input <json-fil> \
  --output <output-fil>.docx
```
   Fejler det med "Cannot find module 'docx'", så kør `npm install` i mappen `${CLAUDE_SKILL_DIR}/../dagsorden-principper/scripts`, og prøv igen.
3. Sig, hvor Word-dokumentet ligger.

### C) Begge

Kør både A og B.

---

## Completion Status

- **DONE**: Dagsorden genereret i valgt format og tjekket med scriptet
- **DONE_WITH_CONCERNS**: Genereret, men scriptet er ikke kørt, tidsberegningen er stram, eller strukturen er utestet
- **BLOCKED**: Mangler kritisk information (fag eller tid)
- **NEEDS_CONTEXT**: Mangler information om materiale eller forberedelsesniveau
