# Tekniske principper og mønstre til digitale rollespilsværktøjer

Samlet fra Fjord Outdoor (AI-rådgiver, webside, facit, show). Brug det som udgangspunkt, så hvert nyt værktøj ikke skal opfindes forfra. Alt er skrevet til enkeltstående HTML-sider, som en lærer kan lægge på en almindelig webhost eller åbne direkte fra en mappe.

## 1. Grundarkitektur

- **Én HTML-fil pr. værktøj** (rådgiver, facit, show, webside). Ingen byggetrin, ingen pakkehåndtering. Stil og script ligger i filen. Billeder og video ligger i en mappe ved siden af.
- **Ét datasæt som kilde.** Saml roller, tal, parametre og tekster i ét sæt (fx en JSON-fil eller et objekt øverst). Lav helst et lille script, der indsætter dataene i rådgiver, facit og show, i stedet for at kopiere tal i hånden. Det fjerner den hyppigste fejltype: tal, der er rettet det ene sted men ikke de andre.
- **Parametre øverst.** Alt, der kan justeres (grænser, priser, sandsynligheder, antal spørgsmål, tidsgrænse), står som navngivne konstanter i toppen af scriptet (fx `CFG`, `TOTAL_QUESTIONS`, `SESSION_TTL_MS`). Ingen magiske tal midt i koden.
- **Ingen faste afhængigheder til internettet** ud over selve modelkaldet. Skrifttyper og ikoner lægges i filen eller i mappen.

## 2. Roller, koder og kryptering

- Hver rolle har en **egen adgangskode**. Gem kun en hash af koden (SHA-256) i siden, ikke koden selv.
- Rollekortets indhold kan gemmes krypteret pr. rolle og dekrypteres i browseren, når koden er indtastet. Det stopper nysgerrige blikke i kildekoden og i udviklerværktøjer, men **ikke en målrettet elev**. Sig det til læreren, og lad aldrig hemmeligheder ligge her, som ikke må kendes.
- `crypto.subtle` virker kun på sikre adresser (https og localhost), ikke når siden åbnes som lokal fil. Brug derfor en lille indbygget SHA-256 og en simpel strømkryptering (hash af nøgle plus tæller), så det virker begge steder.
- Lærervinduet viser **kun rollekoderne**. Ingen log, ingen nøgle, ingen faseføring.

## 3. Modelkald (AI-rådgiver)

- **Kald via en proxy**, aldrig direkte fra siden med en nøgle i. En lille Cloudflare Worker er nok: siden sender sit kald og en delt kode i en header, workeren lægger den rigtige API-nøgle på og videresender. Nøglen ligger kun som hemmelighed i workeren.
- **Begræns proxyen:** tilladt herkomst (kun skolens eller sidens adresse), højst x kald pr. minut pr. adresse, et dagsloft i kald eller kroner, og afvis kald med for stor krop. Den delte kode i siden kan alle læse, så den er kun en forhindring, ikke en lås. Skift API-nøgle, hvis den nogensinde har stået i en side.
- **Prompten i to dele:** (1) faste regler, der er ens for alle roller; (2) rollens egen kontekst (casekort, rollekort, fagligt grundlag, aktuel fase). Elevens spørgsmål sendes i afgrænsede tags (fx `<spørgsmål>`), så det ikke kan læses som nye regler.
- **Indstillinger der virkede:** lav temperatur (ca. 0,4), ca. 2500 tokens som loft (svar skal alligevel være korte), laveste tilladte tænkeniveau, kun de seneste ca. 10 spørgsmål og svar som historik.
- **Robusthed:** tidsgrænse på kaldet (ca. 45 sekunder), to genforsøg ved netværksfejl, læsning af streaming-svar linje for linje, og danske fejlbeskeder til eleven ("Prøv igen om lidt") i stedet for rå fejltekst. Tæl kun et spørgsmål som brugt, når der kom et svar.
- **Svarlængde og tone** styres i prompten (højst ca. 100 ord, "du"-form, ingen indledning), ikke af tokenloftet.
- **Log:** kun hvis læreren har brug for den. Elevernes spørgsmål er personoplysninger, så ingen navne, kort opbevaring, og mulighed for at slå logning helt fra. Pris pr. kald kan regnes ud fra tokens, men vis det kun for læreren.

## 4. Session og spørgsmålstæller

- Gem sessionen i `localStorage` med et **fast starttidspunkt** (første handling), ikke et tidspunkt, der opdateres ved hver handling. Så nulstilles alt først en fast tid efter start (fx 2 timer).
- Gem kun, når der er en rolle eller en tråd. Ellers oprettes tomme sessioner.
- **Rolleskift må ikke nulstille tælleren.** Tråden gemmes med rolle-id på hver besked, og tælleren tæller pr. rolle.
- Tælleren i browseren kan omgås (privat vindue, ryddede data). En hård grænse kræver en tæller på serveren, fx i proxyen pr. rollekode.

## 5. Rollekort og casekort i siden

- Rollekortets **overskrifter er en grænseflade**: rådgiveren og kortvisningen læser dem. Fast sæt: MÅL, BAGGRUND, HOLDNING, VÆRDIER, ARGUMENTER, DILEMMAER, SKJULT INFORMATION, SÆRLIG BEFØJELSE, TIP, evt. projekt og løfte. Ændres de, skal parseren ændres.
- **Én komponent til kortet**, brugt både som fane på computer (fra ca. 900 px) og som foldbare bokse på mobil. Casekortet i egen fane ved siden af rollekortet.
- Design: ét kort uden ramme i ramme, ingen overflødige etiketter (fx "Bagsiden"), farver og skrift som resten af spillet.
- Tabeller på mobil: korte overskrifter, enheder i en note under tabellen, bløde orddelinger (`&shy;`) i lange ord.

## 6. Responsivt og tilgængeligt

- Knapper og miniaturer i et gitter med `repeat(auto-fit, minmax(104px, 1fr))` og tekst, der må ombrydes. Faste bredder giver afklippede knapper (set på pitch-fanen).
- Test altid ved ca. 1300, 390 og 320 px bredde. Vandret scroll findes ved at sammenligne `document.documentElement.scrollWidth` med `window.innerWidth`.
- Alt-tekster beskriver det konkrete motiv og er forskellige fra billede til billede. Tæller og statuslinjer skal kunne læses på en lille skærm uden at løbe ud over kanten.
- Kontrast og skriftstørrelse: mindst 16 px brødtekst, knapper der kan ramme med en tommelfinger.

## 7. Billeder og video

- Billeder: bredde højst ca. 1600 px, JPEG, ca. 100 til 300 KB pr. billede. Komprimér i en kopi og gem originalerne i arkivmappen først.
- Poster til video: tag videoens første billede (`ffmpeg -i video.mp4 -frames:v 1 hero-poster.jpg`), så siden ikke blinker ved indlæsning.
- Video: ca. 10 sekunder, uden lyd som standard, gentagelse fra start uden hak. Lad tekst på siden fade ud, når videoens slutlogo kommer.
- Webside og billeder viser virksomheden, **som den er før investeringen**.
- Billed- og videoprompter: engelsk, med dansk sted, én person der går igen (billedet vedhæftes), logo placeret som ønsket, intet læsbart tekststof, som modellen kan stave forkert.

## 8. Facit-beregner og show

- Parametre i `CFG` øverst; vis forventet værdi og ét udfald, så tilfældighed kan forklares i debriefingen.
- Den samme sandsynlighedsmodel i beregner og show. Test med to eller tre kendte tilfælde og sammenhold med regnearket.
- Scener i show følger spillets rækkefølge. Skjult information vises først i afsløringsscenen.
- Brug samme farver og skrift som papirmaterialerne.

## 9. Arbejdsgang og test

1. **Backup først:** kopiér filen til `_arkiv/<fil>_foer_<ændring>.html` før hver ændring. Slet aldrig.
2. **Ændr i små trin**, ét emne ad gangen (pitch-fane, tæller, mobil), og test mellem trinene.
3. **Syntakscheck:** åbn siden eller kør `node --check` på det udtrukne script. En manglende anførselstegn i en skabelonstreng stoppede hele siden én gang.
4. **Automatisk test med Playwright** (eller tilsvarende): åbn siden i 1300, 390 og 320 px, tjek konsolfejl, vandret scroll, indtast en rollekode, skift rolle og kontrollér at tælleren er uændret, tag skærmbilleder og **se dem**.
5. **Test den nyeste fil.** Åbn med en ny fanebladsadresse eller hård genindlæsning, så en gammel version i cachen ikke narrer.
6. **Gennemlæs som elev:** er der noget på en offentlig side, som røber skjult information eller resultatet af valgene?
7. **Efter ændringer:** tjek tal på tværs (bilag, casekort, facit, show) og ryd op i rester (overskrifter, debriefingsspørgsmål), når en del er fjernet.

## 10. Sikkerhed og ansvar

- Alt i en statisk side kan læses. Antag det.
- Skift API-nøgle før offentliggørelse, hvis den har stået i en side. Sæt dagsloft på proxy og nøgle.
- Mærk siden som fiktiv og AI-genereret. Skriv ikke rigtige personnavne eller virksomheder, hvor det kan forveksles med virkeligheden.
- Giv eleverne en kort besked om, at spørgsmål til rådgiveren gemmes (hvis de gemmes), og hvor længe.
