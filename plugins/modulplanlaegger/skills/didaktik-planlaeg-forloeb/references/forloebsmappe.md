# Forløbsmappen

Planlægningen ligger i almindelige filer i en mappe på lærerens computer. Der bruges ingen database eller MCP-server.

## Placering

- Spørg første gang: "Hvor vil du have dine forløb liggende?" Foreslå den mappe, I arbejder i.
- Hvert forløb får sin egen undermappe: `<fag>-<klasse>-<emne>`, fx `samf-2b-ulighed`. Små bogstaver, bindestreger og ingen æ, ø og å i mappenavnet.
- Find eksisterende forløb ved at søge efter `forloeb.md` i mappen med Glob, fx `**/forloeb.md`.
- Hentede læreplaner og vejledninger ligger fælles for alle forløb i `_laereplaner/` i rodmappen, med en `kilder.md` over versioner og hentedatoer. Se `laereplaner.md`.

## Filer i en forløbsmappe

| Fil | Indhold |
|-----|---------|
| `forloeb.md` | Ramme, modulrække eller skitse, status pr. modul og log. Den eneste fil, der skal læses for at fortsætte forløbet |
| `modul-01-<tema>.md`, `modul-02-<tema>.md` ... | Detaljer for det enkelte modul, når det er planlagt |
| Filer fra andre skills | Drejebog, elevark, slides, quiz, dida-plan og lignende. Læg dem i samme mappe, og skriv modulnummeret først i filnavnet, fx `modul-03-drejebog.md` eller `modul-03-ulighed.dida-plan.json`. De andre plugins gør det selv, når de finder `forloeb.md` |

Opret aldrig filer uden for den forløbsmappe, læreren har godkendt. Overskriv ikke en eksisterende fil uden at læse den først og sige, hvad der ændres.

## Skabelon til forloeb.md

```markdown
# [Titel]

Fag og niveau: [fx samfundsfag B]
Klasse: [fx 2.b]
Moduler: [antal] á [minutter] min
Status: [foreløbig ramme | ramme godkendt]
Læreplan: [kilde og dato, eller "ikke tjekket"]

## Ramme

- Formål: ...
- Slutkompetence: ...
- Faglige mål: ...
- Tilgang: ...
- Progressionslinje: ...
- Evaluering: formativ i modul [x], afsluttende: ...
- Antagelser: ...

## Modulrække

| # | Tema | Mål | Arbejdsform og læringsrum | Stillads | Evaluering eller tjek | Lektie | Status |
|---|------|-----|---------------------------|----------|-----------------------|--------|--------|
| 1 | ... | ... | ... | ... | ... | ... | planlagt |
| 2 | ... | (skitse) | | | | | skitse |

Status er en af: skitse, planlagt, afholdt.

## Log

- [dato] Modul 1 afholdt. Det gik: ... Ændret i rækken: ...
```

## Når forløbet fortsættes

1. Læs `forloeb.md`.
2. Skriv lærerens svar om sidste modul i loggen, og sæt modulets status til afholdt.
3. Ret rækken, og skriv kort i loggen, hvad der er ændret, og hvorfor.
4. Opret filen for næste modul, og sæt dets status til planlagt.
