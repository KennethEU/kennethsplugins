---
name: vidensbase-find-skill
description: "Slår op i faggruppens fælles vidensbase i Outline (dok.mgai.dk) og finder den skill, der passer til opgaven, før den løses. Brug ALTID ved pædagogiske, administrative og planlægningsmæssige opgaver for en gymnasielærer, også når læreren ikke nævner Outline eller en skill: arbejdsspørgsmål og lektiespørgsmål til en tekst, quizzer, lektions- og modulplaner, forløb, CL-øvelser, gruppearbejde og udretterdagsordener, casespil og rollespil, feedback og rettevejledninger, klassemøder, mødedagsordener og forældremøder. Brug også, når læreren siger \"tjek vidensbasen\", \"findes der en skill til\", \"brug vores skill\" eller nævner Outline. Brug ikke til kode, serveropsætning, almindelige spørgsmål uden et undervisningsprodukt eller opgaver, hvor læreren selv har bedt om en bestemt lokal skill."
---

# Find skill i vidensbasen

Faggruppens skills ligger som sider i Outline på https://dok.mgai.dk. Find den rigtige skill, læs den, og følg den. Læreren skal ikke kende skill'ens navn.

## Kræver

Outline-connectoren (MCP på `https://dok.mgai.dk/mcp`). Værktøjerne hedder fx `list_documents`, `list_collection_documents` og `fetch`.

Mangler den, så løs opgaven uden og skriv én linje til sidst: "Outline er ikke forbundet, så jeg har ikke tjekket vidensbasen. Tilføj den som connector med adressen https://dok.mgai.dk/mcp."

## Trin

1. **Søg kort.** Kald `list_documents` med 2 til 4 ord fra opgaven (fx "lektiespørgsmål tekst" eller "casespil rollekort"). Skill-sider starter med en linje "**Skill:** ... **Beskrivelse:** ...", så beskrivelsen står i søgeresultatet. Giver det intet, så søg på titlen "Skills" og se undersiderne med `list_collection_documents`.
2. **Vælg i denne rækkefølge,** når flere passer:
   1. Lærerens egen private collection.
   2. Lærerens faggruppe (fx Samfundsfag, Erhvervsøkonomi).
   3. Fælles.
   4. Andre collections med skills, fx "Kenneths plugins".

   Vælg ud fra beskrivelsen. Den siger både, hvornår skill'en bruges, og hvornår den ikke gør. Passer ingen, så løs opgaven uden og sig det i én linje.
3. **Læs hele skill-siden** med `fetch`. Følg dens trin, regler, godkendelsespunkter og skabeloner præcist.
4. **Læs undersider, når skill'en beder om det.** Henvisninger er links til andre sider i Outline (`/doc/...`). Hent dem med `fetch`, når et trin har brug for dem, ikke alle på én gang. Står der en filsti i stedet, så søg på filnavnet uden endelse.
5. **Scripts.** Ligger et script som kodeblok på en underside, så kopier det til en fil i arbejdsmappen eller kode-sandkassen, og kør det derfra. Ret ikke i scriptet.
6. **Lokale filer.** Nævner skill'en filer på lærerens computer (fx `CLAUDE.md` eller `forloeb.md`), så brug dem, hvis du har adgang. Ellers spring det trin over uden at nævne det.
7. **Sig, hvilken skill du bruger,** i én kort linje øverst, med link til siden.

## Regler

- Outline-versionen af en skill er den gældende. Er en lokal skill med samme navn også installeret, så brug Outline-versionen, og brug kun den lokale, hvis Outline ikke kan nås.
- Ret, flyt og slet ikke skill-sider, medmindre læreren beder om det.
- Nye dokumenter lægges i lærerens private collection, medmindre læreren siger andet. Brug skabelonen "Skill", når der laves en ny skill.
- Skriv aldrig elevnavne eller andre personoplysninger om elever i Outline.
- Hold opslaget kort: højst 2 søgninger, før du vælger. Hent ikke hele collections.
