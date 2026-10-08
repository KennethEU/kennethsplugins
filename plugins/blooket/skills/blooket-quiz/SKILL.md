---
name: blooket-quiz
description: Generér Blooket-quizzer som importklar CSV-fil fra undervisningsmateriale. Brug denne skill når brugeren nævner "Blooket", "quiz", "quizspørgsmål", "multiple choice til Blooket", eller beder om at lave spørgsmål der skal importeres i Blooket. Brug den også når brugeren uploader materiale (billeder, tekst, slides, PDF) og vil have lavet quizspørgsmål ud fra det. Trigges af alt der involverer Blooket — også redigering af eksisterende quizzer, tilføjelse af spørgsmål, eller ændring af format.
user-invocable: false
allowed-tools:
  - Read
  - Glob
  - Bash
  - Write
  - mcp__undervisning__hent_fag
  - mcp__undervisning__hent_forloeb
  - mcp__undervisning__hent_moduler
  - mcp__undervisning__hent_modul_detaljer
  - mcp__undervisning__hent_modul_aktiviteter
---

# Blooket Quiz Generator

Generér quizspørgsmål fra undervisningsmateriale og levér dem som CSV-fil klar til import i Blooket.

## Fase 0: Saml kontekst (automatisk — FØR alt andet)

1. Læs CLAUDE.md for at forstå lærerens fag og hold
2. Hvis et emne er nævnt, tjek om der findes relevante materialer i projektmappen (Glob for PDF, tekst, slides)
3. Hvis brugeren nævner et modul eller forløb, hent det via MCP for at forstå konteksten

**HÅRD REGEL:** Spørg IKKE læreren om fag eller niveau hvis det kan slås op.

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

Stil ALDRIG flere spørgsmål i samme besked.

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

Kopiér `${CLAUDE_SKILL_DIR}/references/generate_csv.py` til arbejdsmappen og kør det med din spørgsmålsliste. Scriptet tager en Python-liste af dicts og producerer en komplet Blooket-importfil.

**Format for spørgsmål:**

```python
questions = [
    {
        "text": "Hvad er BNP?",
        "answers": ["Bruttonationalprodukt", "Bruttonettopriser", "Bankernes nationalplan", "Budgettets nettopris"],
        "correct": "1",
        "time": 20
    },
    {
        "text": "Hvad er 2+2?",
        "answers": ["3", "4", "5"],  # 2-4 svar er OK
        "correct": "2",
        "time": 20
    },
    {
        "text": "Hvilke er nordiske lande?",
        "answers": ["Danmark", "Tyskland", "Norge", "Frankrig"],
        "correct": "1,3",  # flere korrekte svar
        "time": 20
    }
]
```

Kør scriptet sådan:

```bash
cp "${CLAUDE_SKILL_DIR}/references/generate_csv.py" .
# Tilpas questions-listen i scriptet eller indsæt den i bunden
python generate_csv.py
```

Scriptet producerer en fil der matcher Blookets officielle template 1:1, inkl. headers, padding-kolonner, tomme rækker, BOM og Windows-linjeskift.

### 4. Levér filen

Gem i `/mnt/user-data/outputs/` eller den mappe vi arbejder i med beskrivende navn: `Blooket_[Emne].csv`

Brug `present_files`. Giv en kort opsummering (emner, antal spørgsmål).

## Fejl der IKKE må ske

- Tabulator som separator → Skal være semikolon
- Manglende padding-kolonner → Alle rækker skal have 26 kolonner (8 brugte + 18 padding)
- Korrekt svar altid på position 1 → Randomisér
- Manglende BOM → Start med `\ufeff`
- Unix-linjeskift → Brug `\r\n`

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Quiz genereret, CSV-fil leveret og importklar
- **DONE_WITH_CONCERNS** — Quiz leveret, men med forbehold (fx: kun viden-spørgsmål pga. materiale, eller færre end 10 spørgsmål)
- **BLOCKED** — Kan ikke generere quiz (fx: intet materiale at arbejde ud fra)
- **NEEDS_CONTEXT** — Mangler information (fx: "Hvilket emne/materiale skal quizzen bygge på?")
