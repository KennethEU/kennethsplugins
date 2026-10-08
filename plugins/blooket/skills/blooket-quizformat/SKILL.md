---
name: blooket-quizformat
description: "Formatregler og CSV-generator til Blooket-quizzer: svarmuligheder, tidsgrænser, placering af korrekte svar og Blookets importformat. Læses af skillen blooket-lav-quiz. Brug direkte, når læreren vil rette en eksisterende Blooket-CSV, tilføje spørgsmål eller har problemer med import. Brug ikke til arbejdsspørgsmål efter Bloom eller til andre quizplatforme."
user-invocable: false
allowed-tools:
  - Read
  - Glob
  - Bash
  - Write
---

# Blooket Quiz Generator

Generér quizspørgsmål fra undervisningsmateriale og levér dem som CSV-fil klar til import i Blooket.

## Fase 0: Saml kontekst (før alt andet)

1. Læs CLAUDE.md for at forstå lærerens fag og hold
2. Hvis et emne er nævnt, tjek om der findes relevante materialer i projektmappen (Glob for PDF, tekst, slides)
3. Hvis brugeren nævner et modul eller forløb og har lagt beskrivelsen i projektmappen, så læs den

Spørg ikke læreren om fag eller niveau, hvis det kan læses af materialet. Læreren har allerede givet oplysningen, og gentagne spørgsmål koster tid.

---

## Dialog med læreren: ét spørgsmål ad gangen

Når du skal afklare noget, brug dette mønster:

1. **Re-ground:** Hvad arbejder vi på? (1 sætning)
2. **Forklar simpelt:** Hvad er valget?
3. **Anbefaling:** "Jeg foreslår X fordi [grund]"
4. **Muligheder:** A) ... B) ... C) ...

**Eksempel:**
> Jeg laver en Blooket-quiz til dit modul om marketing (EØ C).
>
> Jeg kan se du har en tekst om segmentering og en om branding.
> Skal quizzen dække begge, eller fokusere på én?
>
> ANBEFALING: Vælg A — begge emner. 15 spørgsmål giver plads
> til at blande, og det fungerer som repetition af hele modulet.
>
> A) Begge emner (15 spørgsmål, blandet)
> B) Kun segmentering (10 spørgsmål, fokuseret)
> C) Kun branding (10 spørgsmål, fokuseret)

Stil kun ét spørgsmål ad gangen, så læreren kan svare kort uden at miste tråden.

---

## Arbejdsgang

### 1. Forstå materialet

Læs alt tilgængeligt: uploadede billeder, tekst, slides, PDF, eller brugerens mundtlige beskrivelse. Identificér begreber, fakta, formler og sammenhænge der kan testes.

Hvis brugeren ikke angiver et antal, lav 10-15 spørgsmål.

### 2. Formulér spørgsmål

Hvert spørgsmål har 2-4 svarmuligheder (4 er standard). Følg disse regler:

**Spørgsmålskvalitet:**
- Bland taksonomiske niveauer: viden (hvad er X?), forståelse (hvad betyder X?), anvendelse (beregn/vurdér)
- Forkerte svar skal være plausible — ikke åbenlyst forkerte
- Hold teksten kort — Blooket viser det på små kort
- Undgå "alle ovenstående" og "ingen af ovenstående"
- Undgå negationer ("Hvad er IKKE...") medmindre det giver pædagogisk mening

**Korrekte svar:**
- Randomisér placeringen — det korrekte svar skal fordeles jævnt over position 1-4
- Hvis et spørgsmål har flere korrekte svar, angiv dem kommasepareret (fx "1,3")

**Tidsbegrænsning:**
- Standard: 20 sekunder
- Beregninger eller lange spørgsmål: 30-60 sekunder
- Brugeren kan angive andet. Max 300 sekunder.

### 3. Generér CSV-filen

Skriv spørgsmålene som en JSON-fil og kør scriptet på den. Scriptet tjekker reglerne (2 til 4 svar, korrekt svarnummer findes, tid højst 300 sekunder, ingen semikolon eller linjeskift i teksten), advarer, hvis det korrekte svar ligger skævt fordelt, og skriver den komplette Blooket-importfil.

**Format for spørgsmål** (filen `spoergsmaal.json`):

```json
[
  {"text": "Hvad er BNP?",
   "answers": ["Bruttonationalprodukt", "Bruttonettopriser", "Bankernes nationalplan", "Budgettets nettopris"],
   "correct": "1", "time": 20},
  {"text": "Hvilke af disse er nordiske lande?",
   "answers": ["Danmark", "Tyskland", "Norge", "Frankrig"],
   "correct": "1,3", "time": 20}
]
```

`answers` har 2 til 4 svar, `correct` er svarnumre (flere adskilles med komma), og `time` er sekunder (valgfri). Kør scriptet sådan:

```bash
python "${CLAUDE_SKILL_DIR}/references/generate_csv.py" spoergsmaal.json Blooket_Emne.csv
```

Ved FEJL retter du spørgsmålene og kører igen. Ved ADVARSEL om skæv placering blander du svarene.

Scriptet producerer en fil der matcher Blookets officielle template 1:1, inkl. headers, padding-kolonner, tomme rækker, BOM og Windows-linjeskift.

### 4. Levér filen

Gem i den mappe, vi arbejder i (eller `/mnt/user-data/outputs/`, hvis den findes), med beskrivende navn: `Blooket_[Emne].csv`. Hvis værktøjet `present_files` findes, så brug det til at levere filen. Giv en kort opsummering (emner, antal spørgsmål).

## Fejl, der ødelægger importen (scriptet sørger for dem)

- Tabulator som separator → Skal være semikolon
- Manglende padding-kolonner → Alle rækker skal have 26 kolonner (8 brugte + 18 padding)
- Korrekt svar altid på position 1 → Bland placeringen (scriptet advarer)
- Manglende BOM → Start med `\ufeff`
- Unix-linjeskift → Brug `\r\n`

---

## Completion Status

Afslut med én af:

- **DONE** — Quiz genereret, CSV-fil leveret og importklar
- **DONE_WITH_CONCERNS** — Quiz leveret, men med forbehold (fx: kun viden-spørgsmål pga. materiale, eller færre end 10 spørgsmål)
- **BLOCKED** — Kan ikke generere quiz (fx: intet materiale at arbejde ud fra)
- **NEEDS_CONTEXT** — Mangler information (fx: "Hvilket emne/materiale skal quizzen bygge på?")
