---
name: undervisningsbeskrivelse
description: "Undervisningsbeskrivelser i gymnasiet efter UVM's krav: holder afsnittet til undervisningsbeskrivelsen opdateret på forløbssiden efter hvert modul, laver et dækningstjek af læreplanens faglige mål og kernestof for et hold og samler den færdige undervisningsbeskrivelse til Lectio eller UVM's skabelon ved skoleårets slut eller før eksamen. Bruger kun gennemført undervisning og læreplanens ordrette tekst. Brug når læreren siger \"undervisningsbeskrivelse\", \"UV-beskrivelse\", \"opdatér undervisningsbeskrivelsen\", \"hvad har vi dækket\", \"dækning af læreplanen\", \"mangler vi noget af kernestoffet\", \"hvad mangler holdet før eksamen\", \"klar til censor\" eller \"skriv forløbet til Lectio\". Brug ikke til at planlægge et forløb eller et modul (didaktik-planlaeg-forloeb), til lektier og modulindhold i Lectio eller til eksamensspørgsmål."
argument-hint: "[hold eller forløb, og hvad der skal laves: opdatér, dækning eller saml]"
allowed-tools:
  - Read
  - Glob
  - Write
  - Edit
  - Bash(python3:*)
---

# Undervisningsbeskrivelse

Undervisningsbeskrivelsen dokumenterer den undervisning, der er **gennemført**, og om den lever op til læreplanen. Censor bruger den til at se prøvegrundlaget. Denne skill holder den ajour, mens forløbene kører, så den ikke skal skrives fra bunden i juni.

Læs `references/krav.md` første gang i en samtale. Formaterne står i `references/formater.md`.

## Faste regler

1. **Kun gennemført undervisning tæller.** Marker hvert mål, hvert kernestofpunkt og hvert materiale med modul og status: afholdt eller planlagt. Planlagt er ikke dækket. Et mål eller et kernestofpunkt tæller som dækket, når mindst ét afholdt modul har arbejdet med det. Er kun en lille del afholdt, så skriv "delvist" og hvad der mangler. Undervisningstid regnes kun for afholdte moduler.
2. **Læreplanens ordrette tekst.** Faglige mål og kernestof citeres ordret fra læreplanen (2.1 og 2.2). Find den først i Outline, se `${CLAUDE_SKILL_DIR}/../didaktik-planlaeg-forloeb/references/laereplaner.md`. Står der en sammenfattet eller ældre ordlyd i forløbet (fx fra Lectio), så ret den ikke. Skriv den ordrette tekst ved siden af.
3. **Kun ministeriets kilder om krav og form:** uvm.dk og retsinformation.dk. Kravene står i `references/krav.md`.
4. **Ingen e-bøger.** Åbn aldrig forlagenes sider eller iBog-links (fx Systime, Columbus, Plenum, Gyldendal, Praxis) for at finde sidetal eller indhold. Heller ikke én side. Skriv "?" i sidekolonnen, og lad læreren udfylde den. Spørg først, med præcis adresse, hvis læreren selv beder dig åbne en side.
5. **Gæt ikke.** Står det ikke i forløbet, så skriv "ikke angivet" eller "tjek:" og en kort grund. Forløb, der kun ligger i Lectio eller i hovedet, kortlægges ikke. Skriv, at de mangler.
6. **Ét hold ad gangen.** Deler to klasser en side eller et forløb, så hold dem adskilt. De har hver sin undervisningsbeskrivelse.
7. **Ingen elevnavne** i undervisningsbeskrivelsen eller i Outline.
8. **Ret små dele.** I Outline: brug `update_document` med `editMode: "patch"`, så resten af siden ikke røres. Læg nye afsnit under modultabellen, aldrig over den.

## Vælg opgave

Vælg ud fra lærerens besked. Spørg kun, hvis det er uklart.

| Opgave | Når læreren | Gå til |
|--------|-------------|--------|
| **A. Opdatér forløbet** | har holdt et modul, eller beder om at få afsnittet lavet eller opdateret | A |
| **B. Dækningstjek** | spørger, hvad holdet har dækket, eller hvad der mangler | B |
| **C. Saml beskrivelsen** | skal aflevere den ved skoleårets slut, før eksamen eller til censor | C |

### Find forløbet

- **Outline:** forløbssiden ligger typisk under lærerens private collection → hold → forløb, med en modultabel og en underside pr. modul. Holdsiden er siden over forløbene.
- **Mappe på computeren:** `forloeb.md` i forløbsmappen. Henviser den til Outline, så brug Outline.
- Læs forløbssiden. Læs kun modulsiderne, når du skal bruge materiale eller status, der ikke står på forløbssiden. Er der mange moduler (over ca. 15), så sig hvor mange sider du læser, før du går i gang.

## A. Opdatér forløbet

1. Find forløbet og læreplanen.
2. Findes afsnittet "Til undervisningsbeskrivelsen" ikke, så lav det efter skabelonen i `references/formater.md`. Ellers opdatér kun det, der er ændret: status for de afholdte moduler, nye materialer og nye mål eller nyt kernestof.
3. Materialetabellen har én række pr. modul. Et bogafsnit er kernestof, når det dækker et punkt i læreplanens kernestof. Ellers er det supplerende stof, fx et afsnit om break-even, når break-even ikke står i kernestoffet. Artikler, tal, cases og videoer er supplerende stof. Er du i tvivl, så skriv "tjek:". Sider skrives som "?", medmindre tallet står i forløbet.
4. Opdatér "Dækning af læreplanen" på holdsiden, hvis den findes.
5. Sig kort, hvad der er ændret, og hvad læreren skal udfylde (sider, "tjek:"-punkter).

## B. Dækningstjek

1. Find alle forløb for holdet og afsnittet "Til undervisningsbeskrivelsen" i hvert. Mangler det, så lav det først (A).
2. Lav dækningstabellen fra `references/formater.md`: alle faglige mål og alle kernestofpunkter fra læreplanen som rækker, ét forløb pr. kolonne.
3. Tjek de krav fra læreplanen, der går på tværs, fx omfang i sider (2.4), materiale på engelsk (2.3), projekter og skriftligt arbejde (3.2), it (3.3) og samspil med andre fag (3.4). Tag kun dem med, der står i dette fags læreplan.
4. Svar med det, der mangler, i prioriteret rækkefølge. Det vigtigste er kernestof og mål, der ikke er dækket af noget afholdt modul. Skriv, hvilke forløb der ikke er kortlagt.
5. Gem tabellen på holdsiden, hvis læreren vil have det.

## C. Saml beskrivelsen

1. Spørg kun om det, der mangler: termin og skoleår, institution, uddannelse, fag og niveau, lærer og hold, om den skal skrives i Lectio eller i UVM's skabelon, og om det er hele beskrivelsen eller kun ét forløb.
2. Saml forløbene i rækkefølge. Tag kun afholdte moduler med, og udelad planlagte moduler. Mangler der moduler i et forløb, så sig, at teksten skal laves igen, når de er afholdt. Forløb, der ikke ligger i Outline eller forløbsmappen, skrives i oversigten som "ikke kortlagt".
3. Lav forsiden, oversigten over forløbene og en tekst pr. forløb i formatet fra `references/formater.md`, klar til at kopiere ind i Lectio eller UVM's skabelon. Skriv aldrig selv i Lectio.
4. Kør dækningstjekket (B), eller genbrug tabellen på holdsiden, hvis den er opdateret. Kør så tjeklisten i `references/krav.md`, og vis læreren de punkter, der ikke er opfyldt. Gælder det kun ét forløb, så spring punkterne om hele året over. Sidetal, fordybelsestid og materiale, der må tilgås via internettet, er lærerens afgørelse.
5. Vil læreren have en fil, så lav den i Outline eller som markdown, og sig, hvor den ligger.
