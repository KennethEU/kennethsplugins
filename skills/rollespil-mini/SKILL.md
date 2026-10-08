---
name: rollespil-mini
description: Lav en 10-20 minutters miniversion af et rollespil, enten ved at forenkle et eksisterende eller ved at designe en kort version fra bunden. Brug når læreren siger "miniversion", "kort version", "simplificér rollespillet", "forenklet version", "hurtig øvelse", "kan vi lave det kortere", "15 minutter" eller vil have en smagsprøve på et større rollespil.
allowed-tools:
  - Read
  - Glob
  - Bash
  - Write
---

# Miniversion af et rollespil

Komprimér et rollespil til en selvkørende øvelse på 10 til 20 minutter. Skillen indeholder både forløbet med godkendelsespunkter (gates) og metoden til at forenkle.

**Fælles regler:** `rollespil-projektregler` gælder og går forud (ingen ritualer, normalversion nok, ingen faste minuttal i elevmaterialer, dansk uden lange tankestreger). Faglig rygrad: `rollespil-designprincipper`. Produktion: `rollespil-rollekort-docx`.

## HÅRD REGEL: Trinvis proces med gates

Producér ALDRIG Word-dokumenter før Gate 3. Læreren skal godkende designet først.

## Fase 0: Saml kontekst (automatisk, før alt andet)

1. Læs CLAUDE.md for lærerens fag og hold, hvis den findes.
2. Scan projektmappen for eksisterende rollespilsmaterialer (rollekort, lærerguider).
3. Læs `rollespil-designprincipper`, så de 10 principper overholdes i miniversionen.

Spørg IKKE om det originale rollespil, hvis materialet allerede findes i mappen.

## Trin 1: Hvad er udgangspunktet?

- Findes der et rollespil i samtalen eller mappen, eller har brugeren uploadet materiale?
- Eller skal en miniversion designes fra bunden?

Hvis der ikke er noget udgangspunkt, spørg: "Vil du forenkle et eksisterende rollespil, eller skal vi designe en miniversion fra bunden?"

## Gate 1: Afklaring, VENT på svar

Re-ground: "Vi laver en miniversion af [rollespillet/emnet]. Jeg har et par spørgsmål."

Stil højst 3 til 4 spørgsmål (spring over det besvarede):
1. Hvor mange elever?
2. Hvor lang tid (10, 15 eller 20 minutter)?
3. Skal materialet være selvforklarende (minimal lærerintro)?
4. Er der et læringsmål, der SKAL bevares?

## Gate 2: Design, VENT på OK

Re-ground: "Vi er ved Gate 2 (design). Her er mit forslag til miniversion."

Følg metoden nedenfor og præsentér resultatet:

| Element | Forslag |
|---------|---------|
| Kernekonflikt | Den centrale spænding i ét spørgsmål |
| Roller | 3 til 5 roller med perspektiv |
| Knaphed | Hvad er knapt? |
| Protokol | Selvkørende flow: læs, forhandl, stem, kort debriefing |
| Begreber | Hvilke fagbegreber kommer i spil? |

Giv en anbefaling (triangel eller pentagon) med begrundelse. Spørg: "Passer designet? Skal roller tilføjes eller fjernes, eller skal konflikten justeres?"

## Metode til at forenkle

### Kernekonflikt
Ethvert rollespil har ÉN central spænding. Eksempler: Fattigdomskommission: "Er Lone fattig?" (målemetoder giver modsatrettede svar). EU-reformkonference: "Mere integration eller mere suverænitet?" Budgetforhandling: "Hvem får mest af de knappe ressourcer?" Makrokrise: "Ekspansiv eller kontraktiv politik, og hvem betaler?" Kan du ikke formulere den i ét spørgsmål, er rollespillet ikke klar til at blive forenklet.

### Roller
- **Triangel (3 roller), 10 til 15 min.:** A stærk for, B stærk imod, C kompromis eller wildcard.
- **Pentagon (5 roller), 15 til 20 min.:** A og B modpoler, C kompromis, D ekspert med data, E berørt part eller wildcard.
- Bevar den skarpeste konfliktakse, mindst én rolle med moralsk autoritet og mindst én med faglig tyngde. Drop roller, der kun tilføjer nuance.
- Er der mange begreber i det store spil, så følg begrænsningsreglen i `rollespil-projektregler` og skær modeller væk, som eleverne ikke kan påvirke i en kort øvelse.

### Mini-rollekort
Navn og titel, stemmer, MÅL (1 sætning), 2 argumenter, 1 dilemma. Ingen faseguide, værdier eller udvidet baggrund. Højst en halv A4-side, læsbart på 2 minutter. Kun normalversion, medmindre læreren beder om andet.

### Selvkørende protokol (tre faser, relativ vægt)
1. Læs og forbered (ca. en femtedel): læs kortet, formulér ét argument.
2. Forhandling (ca. tre femtedele): åbningsudtalelser, fri forhandling, afstemning med simpelt flertal (ingen kvalificeret flertal, det tager for lang tid at forklare).
3. Kort debriefing (ca. en femtedel): 2 til 3 spørgsmål i plenum.

### Materiale
Ét samlet dokument: fælles case med afstemningsspørgsmål (en halv side), alle rollekort (en halv side hver, sideskift imellem) og evt. en lærersektion bagerst med debriefingsspørgsmål. Alternativt case som separat ark og rollekort til at klippe ud.

### Kvalitetstjek for miniversionen
- [ ] Kan en elev læse sit kort på under 2 minutter?
- [ ] Er afstemningsspørgsmålet krystalklart (ja/nej eller A/B/C)?
- [ ] Er der ægte uenighed, så ikke alle lander på samme svar?
- [ ] Kan det køres uden 5 minutters forklaring fra læreren?
- [ ] Er der mindst ét overraskende element (skjult information, moralsk dilemma)?

Miniversionen er ikke bare "færre roller", men en skarpere struktur. Den bør kunne fungere som appetitvækker til det fulde rollespil.

## Gate 3: Produktion, først NU laves dokumenter

Re-ground: "Vi er ved Gate 3 (produktion). Designet er godkendt, nu laver jeg materialet."

```
rollekort → sprogtjek → konsistenstjek → levér
```

1. `rollespil-rollekort-docx`: ét samlet Word-dokument med case, rollekort og evt. lærer-debriefing.
2. `rollespil-sprogkvalitet-da` på det producerede materiale.
3. `rollespil-konsistenstjek` som endelig kvalitetssikring.
4. Levér filerne.

Skal miniversionen have digitale dele (fx en AI-rådgiver), så brug `rollespil-digitale-tillaeg`. Hold dem små.

## Gå tilbage

Indser læreren ved Gate 2, at udgangspunktet eller afklaringen skal ændres, så gå tilbage til den relevante gate. Behold det, der stadig holder.

## Afslutningsstatus

- **DONE:** Miniversion produceret, kvalitetstjekket og leveret
- **DONE_WITH_CONCERNS:** Leveret, men fx kernekonflikten er forsimplet eller en vigtig rolle er droppet
- **BLOCKED:** Kan ikke finde det originale rollespil eller har ingen klar kernekonflikt
- **NEEDS_CONTEXT:** Mangler klassestørrelse eller tidsramme

$ARGUMENTS
