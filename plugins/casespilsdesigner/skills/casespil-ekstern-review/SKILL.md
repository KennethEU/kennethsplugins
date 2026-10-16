---
name: casespil-ekstern-review
description: "Styrer et eksternt review af et casespil (også kaldet rollespil) eller dets digitale dele: laver en prompt til en ekstern AI (fx ChatGPT med mappeadgang), modtager svaret, verificerer hvert fund i koden og materialerne før noget ændres, foreslår rettelser, retter efter brugerens valg, tester og laver prompten til næste runde. Brug når læreren siger ekstern gennemgang, review, uvildig gennemgang, runde 2, ChatGPT-prompt til reviewet, eller indsætter et eksternt review til behandling. Brug ikke til den løbende kvalitetssikring før levering (casespil-konsistenstjek) eller til sprogtjek (casespil-sprogtjek)."
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Write
  - Edit
---

# Ekstern review af casespil

**Projektregler:** `casespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

En ekstern AI kan finde fejl, ingen af os har set. Men en tredjedel af de eksterne fund viste sig at være forkerte, forældede eller bevidste beslutninger. Derfor verificeres hvert fund, før noget ændres, og listen over kendte beslutninger følger med fra runde til runde.

## Tilstande

- **Ingen review endnu:** lav prompten (forløb 1 og 2) og gem den som `ChatGPT_prompt_runde_N.md`.
- **Review indsat:** verificér hvert fund (forløb 4) før noget ændres.
- **Verificeret:** anbefal, få svar på de valg, der er brugerens, ret, genbyg og test (forløb 5 til 7).
- **Rettet:** opdatér kendte beslutninger og nylige rettelser, og lav prompten til næste runde (forløb 8).

## Forløb

1. **Opsamling (automatisk).** Læs `CLAUDE.md`, spilmappen, kilderne og tidligere rundeprompter. Find spillets korte beskrivelse, et mappekort, de kendte beslutninger og de seneste rettelser.
2. **Prompt (output 1).** Generér prompten efter skabelonen i `references/prompt-skabelon.md`, og gem den som `ChatGPT_prompt_runde_N.md` i projektet. Fortæl kort, hvordan den bruges (indsæt den i den eksterne AI, giv den adgang til en kopi af mappen, og indsæt svaret her).
3. **Vent på svaret.** Brugeren indsætter den eksterne AI's svar.
4. **Verificér (output 2).** Hvert fund får en dom i en tabel: **Bekræftet**, **Delvist**, **Afvist** eller **Ikke verificeret**, med bevis (fil og linje, testoutput, beregning eller kilde). Ret intet endnu. Afviste fund begrundes kort.
5. **Anbefaling.** Skriv, hvad der bør rettes, hvad der er en bevidst beslutning, og hvad der kræver brugerens valg. Stil kun spørgsmål, hvor et valg er brugerens.
6. **Ret.** Efter anbefalingen: først data og generatorer, derefter genbygning, så tests (modeltest, logiktest, browsertest, sprogtjek, sidetal og `casespil-konsistenstjek`).
7. **Rapportér.** Skriv ærligt, hvad der er rettet, hvad der ikke er, og hvilke rettelser ingen test dækker.
8. **Næste runde.** Opdatér listerne "kendte beslutninger" og "nylige rettelser", og generér prompten til næste runde.

## Regler

1. **Ingen ændring før verificering.** Dommene er Bekræftet, Delvist, Afvist og Ikke verificeret, alle med bevis.
2. **Bevidste beslutninger fra tidligere runder fastholdes**, medmindre fundet kan vise, at de er forkerte.
3. **Ret ved kilden** (data og generatorer), genbyg, test. Ret aldrig kun de genererede filer.
4. **Hemmeligheder åbnes eller vises aldrig,** hverken af denne skill eller af den eksterne AI: nøglefiler, `.env`, adgangskoder, `data/keys.php`, rollekoder og lærerkoder står ikke i prompten. Rapportér kun placering.
5. **Den eksterne AI skriver ikke i projektmappen.** Midlertidige filer lægges uden for projektet.
6. **En rettelse, der skaber en ny fejl,** medtages som nyt fund i næste runde.
7. **Ærlig rapport.** Skriv, hvad testene ikke dækker.

## Svar til brugeren

En kort tabel: fund, dom, bevis, handling. Derefter hvad der er rettet, og hvad der ikke er. Ingen lang tilbageblik.

## Completion Status

Afslut ALTID med én af: **DONE**, **DONE_WITH_CONCERNS**, **BLOCKED** eller **NEEDS_CONTEXT**.
