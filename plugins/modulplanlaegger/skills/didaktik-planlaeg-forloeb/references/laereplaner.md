# Hent gældende læreplan og vejledning

Læreplaner og vejledninger ligger som PDF'er hos Børne- og Undervisningsministeriet. Links og filnavne skifter, når der kommer nye versioner. Hent derfor altid oversigtssiden først, og gem aldrig PDF-links i skillen.

## Oversigtssider

| Uddannelse | Side |
|------------|------|
| stx | https://uvm.dk/uddannelse-til-unge/gymnasiale-uddannelser/fag-og-laereplaner/stx-laereplaner/ |
| hhx (bl.a. erhvervsøkonomi) | https://uvm.dk/uddannelse-til-unge/gymnasiale-uddannelser/fag-og-laereplaner/hhx-laereplaner/ |
| hf | https://uvm.dk/uddannelse-til-unge/gymnasiale-uddannelser/fag-og-laereplaner/hf-laereplaner/ |
| htx | https://uvm.dk/uddannelse-til-unge/gymnasiale-uddannelser/fag-og-laereplaner/htx-laereplaner/ |
| Valgfag | https://uvm.dk/uddannelse-til-unge/gymnasiale-uddannelser/fag-og-laereplaner/valgfag-laereplaner/ |

Er erhvervsøkonomi ikke et stx-fag, så slå op på hhx-siden og sig det. Kan en side ikke findes, så søg på uvm.dk efter "læreplaner til stx", og fortæl læreren, at adressen er ændret.

Hver fagblok på siden har et afsnit pr. niveau med links, hvis tekst består af "Læreplan til" eller "Vejledning til", fag, niveau, uddannelse og årstal, fx Samfundsfag B, stx 2017 og ofte et link til emu.dk med temaer og vejledningsmaterialer.

## Fremgangsmåde

1. **Hent oversigtssiden** med WebFetch, og bed om de præcise link-tekster og fulde adresser for fag og niveau. Linkene er relative, så sæt `https://uvm.dk` foran.
2. **Vælg den nyeste version.** Årstallet står i link-teksten og ofte som datokode først i filnavnet, fx `240827` for 27. august 2024. Står der flere versioner, så tag den nyeste, og spørg, hvis det er uklart, hvilken der gælder for klassen, fx ved en ny læreplan fra et bestemt skoleår. En læreplan kan være ældre end vejledningen. Det er normalt.
3. **Tjek cachen.** Ligger samme fil allerede i `_laereplaner/` i forløbsmappens rod, så brug den. Ellers hent den.
4. **Hent PDF'en** med `curl -sL -o "<forløbsrod>/_laereplaner/<fag>-<niveau>-<laereplan|vejledning>-<år>.pdf" "<adresse>"`. Spørg først, hvis mappen ikke findes.
5. **Udtræk teksten** med den første metode, der virker. Gem teksten ved siden af PDF'en som `.txt`:
   1. Read-værktøjet direkte på PDF'en med `pages`.
   2. `pdftotext -layout fil.pdf fil.txt`.
   3. `pdf2txt.py fil.pdf > fil.txt` (pdfminer, fx i `/opt/homebrew/bin`).
   4. `python3 -c` med `pypdf`, hvis modulet findes.
   5. Virker intet, så bed læreren indsætte de relevante afsnit. WebFetch kan ikke læse disse PDF'er pålideligt.
6. **Notér kilden** i `_laereplaner/kilder.md`: titel, version, adresse og hentedato. Skriv kilde og dato i `forloeb.md` under "Læreplan".

## Hvad der skal bruges

Læs ikke hele dokumentet ind i samtalen. Søg i teksten efter overskrifterne, og læs kun de afsnit, forløbet har brug for.

**Fra læreplanen:**

- Identitet og formål
- **Faglige mål:** citér dem ordret, med nummer, når forløbet skal dække dem
- **Kernestof** og **supplerende stof**
- Didaktiske principper, arbejdsformer, it, samspil med andre fag
- Evaluering og prøveformer, hvis forløbet skal forberede til en prøve

**Fra vejledningen:**

- Uddybning af de faglige mål og kernestoffet
- Eksempler på forløb, progression og arbejdsformer
- Krav til skriftligt arbejde og eventuelle spørgeord
- Bedømmelseskriterier og karakterbeskrivelser

Henvis til afsnitsnummeret, fx "læreplan 2.1" eller "vejledning 3.2", så læreren kan slå det op.

## Emu.dk

Linket "Find temaer og vejledningsmaterialer" fører til emu.dk med eksempler og materialer til faget. Det er inspiration, ikke regler. Tilbyd det kun, hvis læreren vil have idéer til indhold.

## Regler

- Brug kun læreplan og vejledning, du har hentet i denne samtale, eller som læreren har givet, som grundlag for gældende krav. Referencefilerne i `didaktik-principper` er fra 2010 til 2012 og må ikke bruges som regler.
- Kan noget ikke hentes, så sig det, og marker kravene i planen som "ikke tjekket mod gældende læreplan".
