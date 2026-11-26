---
name: vidensbase-feedback
description: "Skriver en note til opfølgning på siden \"Feedback på mgai\" i mgai dok (dok.mgai.dk), når læreren støder på en fejl, bliver frustreret eller har ris, ros eller en idé til noget på mgai: mgai dok, skills, websider, AI-bots, rum eller serveren. Brug når noget på mgai ikke virker som ventet, når en skill giver et dårligt resultat, eller når læreren siger \"skriv det ind\", \"giv feedback\", \"det skal Kenneth se\", \"ris\" eller \"ros\". Spørg altid først. Brug ikke til fejl i lærerens egne filer eller programmer uden for mgai, eller til feedback til elever."
---

# Feedback på mgai

Fejl, ris, ros og idéer til mgai samles på siden "Feedback på mgai" i collectionen Fælles i Outline (https://dok.mgai.dk/doc/feedback-pa-mgai-2Krt0pcMfx). Kenneth og andre følger op derfra.

## Kræver

Outline-connectoren (MCP på `https://dok.mgai.dk/mcp`). Mangler den, så skriv noten i chatten efter skabelonen nedenfor, og bed læreren sende den til Kenneth.

## Trin

1. **Spørg først.** Når noget på mgai går galt, eller læreren har ris eller ros, så spørg: "Skal jeg skrive det ind til opfølgning?" Skriv kun ved ja. Spørg højst én gang pr. sag.
2. **Find siden.** Søg med `list_documents` på "Feedback på mgai", eller hent siden direkte med `fetch`. Læs titlerne på undersiderne.
3. **Findes sagen allerede,** så skriv en kommentar på den note med det nye i stedet for at lave en ny.
4. **Lav en ny note** som underside til "Feedback på mgai" (`create_document` med `parentDocumentId`). Følg skabelonen nedenfor.
5. **Giv læreren linket** til noten i én linje.

## Skabelon

Titel: `ÅÅÅÅ-MM-DD Område: kort beskrivelse`, fx `2026-11-26 AI-bots: svaret blev skåret af`.

```
**Område:** mgai dok / skills / websider / AI-bots / rum / serveren / andet
**Type:** fejl / ris / ros / idé
**Status:** ny
**Lærer:** initialer
**Dato:** ÅÅÅÅ-MM-DD

## Hvad skete der
Kort og konkret. Hvad prøvede læreren, og hvad gik galt eller godt?

## Hvor
Side, skill, bot eller adresse.

## Fejlbesked
Ordret, hvis der var en. Ellers "ingen".

## Hvad Claude allerede har fundet ud af
Dit bud på årsagen, og hvad der er prøvet. Skriv også, hvad der IKKE virkede.

## Forslag til løsning
Dit og lærerens forslag. Gerne konkret: hvilken fil, hvilken tekst i skillen, hvilken indstilling.

## Opfølgning
(tom, udfyldes af den, der følger op)
```

## Regler

- Udfyld "Hvad Claude allerede har fundet ud af" og "Forslag til løsning" grundigt. Den, der følger op, skal ikke starte forfra.
- Ingen elevnavne eller andre oplysninger om elever. Ingen API-nøgler, koder eller andre hemmeligheder. Fjern dem også fra fejlbeskeder.
- Én sag pr. note. Kort og på dansk.
- Ret ikke i andres noter, og ændr ikke status. Kun den, der følger op, gør det.
- Er der en skill involveret, så skriv skillens navn og hvilket trin, der gik galt.
