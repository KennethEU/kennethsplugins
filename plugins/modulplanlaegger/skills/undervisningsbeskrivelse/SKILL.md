---
name: undervisningsbeskrivelse
description: "Undervisningsbeskrivelser i gymnasiet efter UVM's krav, forløb for forløb som i Lectio: skriver og opdaterer teksten til hvert forløb (forløbsbeskrivelse, faglige mål og kernestof, særlige fokuspunkter, arbejdsformer, skriftligt arbejde), så den kan kopieres ind i Lectio og læses af eleverne, holder holdets oversigt over forløb og manglende kernestof ajour og gør beskrivelsen klar til skoleårets slut eller eksamen. Bruger kun læreplanens ordrette tekst og skelner mellem afholdt og planlagt. Brug når læreren siger \"undervisningsbeskrivelse\", \"UV-beskrivelse\", \"opdatér undervisningsbeskrivelsen\", \"skriv forløbet til Lectio\", \"forløbsbeskrivelse\", \"hvad har vi dækket\", \"mangler vi noget af kernestoffet\", \"hvad mangler holdet før eksamen\" eller \"klar til censor\". Brug ikke til at planlægge et forløb eller et modul (didaktik-planlaeg-forloeb), til lektier og modulindhold i Lectio eller til eksamensspørgsmål."
argument-hint: "[hold eller forløb, og hvad der skal laves: forløbstekst, mangler eller klar til eksamen]"
allowed-tools:
  - Read
  - Glob
  - Write
  - Edit
  - Bash(python3:*)
---

# Undervisningsbeskrivelse

Undervisningsbeskrivelsen består af én tekst pr. forløb, sådan som den ligger i Lectio. Den dokumenterer den gennemførte undervisning over for censor, og eleverne bruger den til at se, hvad de skal kunne til eksamen. Skillen holder teksten ajour, mens forløbet kører, så den ikke skal skrives fra bunden i juni.

Læs `references/krav.md` første gang i en samtale. Formaterne står i `references/formater.md`.

## Faste regler

1. **Forløbet er enheden.** Én tekst pr. forløb med Lectios felter: forløbsbeskrivelse, faglige mål, særlige fokuspunkter, arbejdsformer og skriftligt arbejde. Holdsiden har kun oversigten over forløbene og det, der mangler.
2. **Skrevet til eleverne.** Forløbsbeskrivelsen og de særlige fokuspunkter skal kunne læses af en elev. Fokuspunkterne er "det skal du kunne", skrevet ud fra modulernes mål. Ingen interne noter i Lectio-teksten. De står i boksen "Til læreren".
3. **Afholdt og planlagt.** Lectio-teksten beskriver hele forløbet, også det planlagte. Boksen "Til læreren" siger præcist, hvilke moduler og hvilke mål der kun er planlagt. Før den endelige beskrivelse tages det ud, der ikke blev til noget (C). Et mål eller et kernestofpunkt tæller som dækket, når mindst ét afholdt modul har arbejdet med det.
4. **Læreplanens ordrette tekst.** Faglige mål og kernestof under "Faglige mål" citeres ordret fra læreplanen (2.1 og 2.2 eller tilsvarende afsnit i fagets læreplan), adskilt i "Kernestof" og "Mål". Find læreplanen først i Outline, se `${CLAUDE_SKILL_DIR}/../didaktik-planlaeg-forloeb/references/laereplaner.md`. Tjek hvert citat mod læreplanens tekst. Står der en anden ordlyd i det gamle forløb i Lectio, så skriv læreplanens.
5. **Kun ministeriets kilder om krav og form:** uvm.dk og retsinformation.dk. Kravene står i `references/krav.md`.
6. **Ingen e-bøger.** Åbn aldrig forlagenes sider eller iBog-links (fx Systime, Columbus, Plenum, Gyldendal, Praxis) for at finde sidetal eller indhold. Heller ikke én side. Skriv i boksen, at sider mangler, og lad læreren udfylde dem. Spørg først, med præcis adresse, hvis læreren selv beder dig åbne en side.
7. **Gæt ikke.** Står det ikke i forløbet, så skriv "ikke angivet" eller et "Tjek:"-punkt i boksen. Forløb, der kun ligger i Lectio eller i hovedet, kortlægges ikke. Skriv, at de mangler.
8. **Ét hold ad gangen.** Deler to klasser en side, så hold dem adskilt. De har hver sin undervisningsbeskrivelse.
9. **Ingen elevnavne.**
10. **Ret kun afsnittet.** I Outline: brug `update_document` med `editMode: "patch"`, så resten af siden ikke røres. Har forløbssiden en modultabel, så læg afsnittet under den. Ellers sidst på siden.

## Vælg opgave

Vælg ud fra lærerens besked. Spørg kun, hvis det er uklart.

| Opgave | Når læreren | Gå til |
|--------|-------------|--------|
| **A. Forløbsteksten** | vil have teksten til et forløb lavet eller opdateret, fx efter et modul | A |
| **B. Oversigt og mangler** | spørger, hvad holdet har haft, eller hvad der mangler af læreplanen | B |
| **C. Klar til eksamen** | skal gøre beskrivelsen færdig ved skoleårets slut, før eksamen eller til censor | C |

### Find forløbet

- **Outline:** `didaktik-planlaeg-forloeb` gemmer forløbssiden med en modulrække og en underside pr. modul ("Modul 01: <tema>"), som standard i lærerens private samling, evt. under en side for holdet. Se `${CLAUDE_SKILL_DIR}/../didaktik-planlaeg-forloeb/references/forloebsmappe.md`. Holdsiden er siden over forløbene, hvis der er en.
- **Mappe på computeren:** `forloeb.md` i forløbsmappen. Henviser den til Outline, så brug Outline.
- Læs forløbssiden. Læs modulsiderne, når du skal bruge emner, materiale, mål eller status, der ikke står på forløbssiden. Er der mange moduler (over ca. 15), så sig hvor mange sider du læser, før du går i gang.

## A. Forløbsteksten

1. Find forløbet og læreplanen.
2. Lav eller opdatér afsnittet "Til undervisningsbeskrivelsen" efter `references/formater.md`, afsnit 1. Ved en opdatering: ret kun det, der er ændret, fx nye emner, nyt materiale, nyt skriftligt arbejde og boksens liste over afholdte og planlagte moduler.
3. **Forløbsbeskrivelse:** problemstillingen og 2 til 3 sætninger til eleven, emner og begreber som en liste og materialet. Et bogafsnit er kernestof, når det dækker et punkt i læreplanens kernestof. Ellers er det supplerende stof. Artikler, tal, cases og videoer er supplerende stof.
4. **Faglige mål:** kun de kernestofpunkter og mål, forløbet faktisk arbejder med, ordret.
5. **Særlige fokuspunkter:** 4 til 8 punkter, der begynder med et verbum, fx "forklare", "beregne", "diskutere". Byg dem på modulernes mål.
6. **Arbejdsformer og skriftligt arbejde:** de væsentligste arbejdsformer. Afleveringer med titel og frist.
7. Opdatér oversigten på holdsiden, hvis forløbet er nyt, eller status har ændret sig (B).
8. Sig kort, hvad der er ændret, og hvad læreren skal udfylde.

## B. Oversigt og mangler

1. Find alle forløb for holdet. Mangler et forløb sin tekst, så lav den først (A).
2. Skriv oversigten over forløbene på holdsiden efter `references/formater.md`, afsnit 2, med link og status pr. forløb.
3. Find det kernestof og de mål fra læreplanen, som intet afholdt modul dækker. Gå hvert punkt i 2.1 og 2.2 igennem.
4. Tjek de krav fra læreplanen, der går på tværs, fx omfang i sider (2.4), materiale på engelsk (2.3), projekter og skriftligt arbejde (3.2), it (3.3) og samspil med andre fag (3.4). Tag kun dem med, der står i dette fags læreplan.
5. Skriv "Mangler i læreplanen" kort og i prioriteret rækkefølge. Skriv, hvilke forløb der ikke er kortlagt.

## C. Klar til eksamen

1. Spørg kun om det, der mangler: skoleår og termin, og om det gælder hele beskrivelsen eller ét forløb.
2. Gå hvert forløb igennem. Tag emner, materiale, mål og fokuspunkter ud, som hører til moduler, der ikke blev holdt. Mangler der stadig moduler, så sig, at teksten skal ses igen, når de er holdt.
3. Opdatér oversigten og manglerne (B).
4. Kør tjeklisten i `references/krav.md`, og vis læreren de punkter, der ikke er opfyldt. Gælder det kun ét forløb, så spring punkterne om hele året over. Sidetal, fordybelsestid og materiale, der må tilgås via internettet, er lærerens afgørelse.
5. Læreren kopierer selv teksten ind i Lectio. Skriv aldrig selv i Lectio. Skal den i UVM's skabelon i stedet, så brug `references/formater.md`, afsnit 3.
