---
name: casespil-digitale-tillaeg
description: "Designregler og teknisk reference til digitale tilføjelser til et casespil (også kaldet rollespil): AI-rådgiver pr. rolle, budget- og beslutningsværktøj med resultatkoder, sammenligning på storskærm og krypteret lærerpakke, facit-beregner, lærershow, forside og casespilsside (hub) med indlejret spilintro (animation med voiceover og undertekster), video og billedprompter. Brug når et casespil eller rollespil skal have digitale værktøjer, efter at papirmaterialerne er godkendt. Bygger på Fjord Outdoor (erhvervsøkonomi) og Kommunalbudget (samfundsfag). Brug ikke til casespil eller rollespil uden digitale dele eller til almindelige websider og apps."
---

# Digitale tilføjelser til casespil

**Projektregler:** `casespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill kommer EFTER casespillets design og papirmaterialer er færdige (rollekort, elevintroduktion, bilag). Den styrer, hvordan de digitale dele bygges, så de passer sammen og ikke afslører noget, eleverne ikke må se.

**Teknisk reference:** Før du bygger noget, læs `references/teknik.md`. Den indeholder de mønstre, der er afprøvet i to forskellige spil: filstruktur og fælles datasæt, kryptering og koder, proxy til modelkald, prompt-opbygning, session og spørgsmålstæller, rådgiverens grænseflade på computer og mobil, budgetværktøj, resultatkoder, sammenligning, krypteret lærerpakke, billeder og video, spilintroens opbygning og synkronisering, voiceover, grafisk stil og kontrast, mobil og Safari, automatiserede tests og sikkerhed. Spar tid ved at genbruge mønstrene i stedet for at opfinde dem igen.

## Vælg spiltype først

Fjord Outdoor (erhvervsøkonomi) og Kommunalbudget (samfundsfag) er to forskellige slags casespil. Tag det, der passer, og drop resten.

| | Virksomhedscase (Fjord Outdoor) | Samfundsfaglig forhandlingscase (Kommunalbudget) |
|---|---|---|
| Forside | Virksomhedens webside som den er før investeringen | Spillets egen forside med roller og stemmetal, spillets faser og den faglige ramme for læreren |
| Elevværktøjer | AI-rådgiver, pitch-fane | AI-rådgiver, budgetværktøj, resultatkode |
| Beslutning | Bestyrelsen vælger, læreren indtaster beløb i facit-beregneren | Bordene fører selv planen i budgetværktøjet og afleverer en resultatkode |
| Lærerværktøjer | Facit-beregner (tilfældighed), lærershow | Sammenligning af bordene på storskærm, krypteret lærerpakke |
| Stil | Virksomhedens verden (outdoor, fjord, rå materialer) | Fagets verden (offentlig forvaltning, redaktionel stil) |

**Rækkefølge:** (1) Fælles datasæt og skjult-information-liste. (2) Forside og medier. (3) Casespilsside (hub) og spilintro (efter forsiden, fordi de bruger dens billeder og stil). (4) AI-rådgiver. (5) Budgetværktøj, resultatkode og sammenligning, eller facit-beregner og lærershow, alt efter spiltype. (6) Lærerpakke. (7) Automatiserede tests og test på en rigtig telefon. (8) Kør `casespil-konsistenstjek`, som også dækker digitale dele og beregner-tjek.

**Relaterede skills:** `casespil-designprincipper` (hvad må eleverne vide, hvornår), `casespil-projektregler` (beregner-tjek, begrænsningsregel, fælles kilde), `casespil-konsistenstjek` (kvalitetssikring), `casespil-sprogtjek` (alle tekster i værktøjerne).

## Grundregler

1. **Én kilde til tallene.** Alle tal (markedsdata, grænser, sandsynligheder, straf, budget, antal stemmer og flertalskrav) og alle roller med titel, stemmetal og beføjelse står i ét sæt og kopieres derfra til: bilag, casekort i rådgiveren, budgetværktøj, facit-beregneren, showet, spilintroen og casespilssiden. Efter hver ændring tjekkes alle steder. Offentlige data (regler, initiativer, faser, roller uden hemmeligheder) ligger ukrypteret i ét datasæt, og hemmeligheder (rollekort, lærerpakke) ligger krypteret hver for sig.
2. **Skjult information bliver skjult.** Det, der kun står på ét rollekort, og resultatet af valgene (hvad pengene gav) må ikke stå i noget, der er offentligt eller fælles: websiden, casespilssiden, casekortet, spilintroen, showets scener før afsløringen, billedtekster.
3. **Backup før hver ændring.** Gem den gamle fil i en arkivmappe med et sigende navn (fx `_arkiv/..._foer_<ændring>.html`). Slet aldrig. Det gælder også ved gennemgang og små rettelser, ikke kun ved nybyggeri. I Fjord Outdoor blev filer ændret uden backup.
4. **Test før du siger det er færdigt.** Åbn siden i en browser, tjek computer (ca. 1300 px) og mobil (ca. 390 px og 320 px), ingen vandret scroll, ingen JavaScript-fejl. Se billedet, ikke kun koden. Lav en automatisk test, der kan køres igen efter hver ændring (afsnit 21 i `references/teknik.md`). Safari på iPhone opfører sig anderledes end Chrome: bed læreren åbne siden på en rigtig telefon, før den kaldes færdig (afsnit 14).
5. **Sproget følger materialerne.** Dansk, ingen tankestreger, ingen faste minuttal, ingen ritualer som "I spiller en rolle".
6. **Samme faser overalt.** Webside, rådgiver og lærerguidens faseoversigt bruger kun de spilfaser, hvor eleverne agerer og har brug for sparring (Fjord Outdoor: 1 Forberedelse, 2 Pitches, 3 Korridorforhandlinger, 4 Bestyrelsesmødet. Kommunalbudget: 1 Interessegrupper, 2 Byrådsforhandling, 3 Beslutning og afstemning). Introduktion og debriefing er ikke rådgiverfaser. Papirmaterialerne (elevintroduktion, rollekortenes faseguide, lærerguidens debriefingafsnit) må have Intro og Debriefing som før- og eftertrin uden fasenummer, men spilfaserne har samme navne, numre og rækkefølge i alle materialer.

## Pædagogiske principper for de digitale værktøjer

Et digitalt værktøj skal gøre eleverne bedre til at tænke og forhandle, ikke overflødiggøre det.

- **Eleven formulerer selv.** Rådgiveren åbner med et åbent spørgsmål ("Hvad vil du forberede til forhandlingen?") og har ingen forudindstillede spørgsmålsknapper. Forslag til klik gør eleverne passive: de vælger blandt forslagene i stedet for at formulere deres egne dilemmaer og strategiske tanker. Fjord Outdoors rådgiver har stadig sådanne knapper og bør have dem fjernet; Kommunalbudgets rådgiver har ingen.
- **Startkrav er forberedelse, ikke en lås.** Når eleverne vælger startkrav (fx tre af fire mærkesager), er det et personligt redskab, der skærper prioriteringen i første fase. Startkravene afleveres ikke, og de må aldrig låse forhandlingen eller budgetværktøjet. Alle initiativer er tilgængelige for alle grupper under forhandlingen, ellers blokeres kompromiser.
- **Rådgiveren guider mod strategi, ikke facit.** Faseliste og svar handler om alliancer, prioritering, argumenter og kompromiser over for de andre grupper. Rådgiveren regner ikke stemmer og budget for eleven og skriver aldrig færdige indlæg.
- **Kompromisvejledning er privat.** Rollekortet rummer en hemmelig kompromisvejledning med rollens smertegrænse. Rådgiveren kender kun elevens eget kort og hjælper eleven med at finde sit eget kompromis ved at stille modspørgsmål, uden at røbe det over for andre og uden at opfordre til at sige noget usandt. Reglen til eleverne er: man må holde noget tilbage, men ikke sige noget usandt.
- **Begrund både valg og fravalg mundtligt.** Værktøjet registrerer tal; forklaringen sker i rummet. Derfor har delvise bevillinger en konkret beskrivelse af, hvad et mindre forsøg kunne være, og værktøjet skriver, at andelen af beløbet ikke er et mål for effekten.
- **Knaphed og fælles interesser skal kunne mærkes.** Kalibrér puljen mod den samlede efterspørgsel (Kommunalbudget: 100 mio. kr. mod 335 mio. kr. i unikke ønsker), og lad fælles initiativer kun tælle én gang, så alliancer belønnes.
- **Vægte, der tvinger til koalitioner.** Kontrollér, at ingen to roller kan vinde alene, at der findes flere vindende koalitioner, og at fiaskoen har et tydeligt udfald (Kommunalbudget: uden flertal ved afslutningen gives ingen nye bevillinger, og puljen forbliver reserve).
- **Skalér til klassen.** Hvert bord har alle roller. Flere elever kan dele en rolle, deler dens stemmer og afgiver ét svar. Bordene afleverer en resultatkode, så læreren kan sammenligne dem.

## AI-rådgiver pr. rolle

Formål: eleven kan stille op til 10 spørgsmål om sin egen rolle, sit kort og fagbegreber. Rådgiveren giver hints og modspørgsmål, aldrig færdige replikker.

- **Kontekst til modellen:** casekort (fælles), elevens eget rollekort (forside og bagside), fagligt grundlag, aktuel fase (kun spilfaserne, se grundregel 6). Intet andet. Rådgiveren kender ikke de andre roller og må ikke gætte på dem.
- **Regler i prompten:** højst 100 ord (Kommunalbudget: ca. 50 til 85), dansk, "du"-form, ingen indledning, afslut med et kort, åbent modspørgsmål, regn aldrig budget eller stemmer selv (vis formlen), skriv aldrig en færdig tale eller løsning, nævn kun tal fra casekort, rollekort eller grundlag, hold sig til casespillet, send eleven til læreren hvis der er tegn på mistrivsel. Elevens besked ligger i et afgrænset felt og er ikke nye regler. Faglige modeller (fx Eastons model) nævnes i prompten, så rådgiveren bruger dem, når det giver mening.
- **Åbning uden forslagsknapper:** rådgiveren åbner med en fast, rollespecifik besked, der nævner gruppens stemmer og mål og slutter med et åbent spørgsmål. Ingen "forslag til spørgsmål".
- **Faseliste:** rådgiverens fasevælger indeholder kun de aktive elevfaser (grundregel 6).
- **Adgang:** en 4-cifret kode pr. rolle (ikke samme kode til alle). I siden gemmes kun en hash af koderne (se `references/teknik.md`, afsnit 2). Koden trykkes på forsiden af rollekortet i topbjælkens undertitel, fx "Fjord Outdoors bestyrelse | Leder mødet | Rådgiverkode: 2481", og ikke under en overskrift, fordi rådgiveren læser kortets faste overskrifter. Rådgiverens fejlbesked og tekster på casespilssiden må ikke skrive "fra dit kort", hvis koden ikke står der. Lærervinduet viser KUN rollekoderne, ingen log, ingen nøgle, ingen faseføring.
- **Spørgsmålstæller:** gemmes pr. rolle i browseren (nøglen indeholder rollens id), så et rolleskift eller en prøve af en anden rolle ikke nulstiller de 10 spørgsmål. Tælleren nulstilles først 2 timer efter start (fast starttidspunkt, ikke glidende). Et spørgsmål tælles kun, når der kom et svar. Det kan omgås med privat vindue eller ryddede data. Vil man have en hård grænse, skal den ligge på serveren.
- **Visning:** vis hele rollekortet i rådgiveren (hvis det ikke printes), som ét kort uden ramme i ramme, med faseguide som almindelig sektion nederst. På computer står chatten i midten og informationspanelet (rollekort, startkrav, casekort) ved siden af, og arbejdsbordet er låst til skærmens højde: fast `height` og `max-height` mod viewporten med `overflow: hidden`, hver kolonne med `height: 100%` og `min-height: 0`, og tråden, skinnen og panelets krop ruller hver for sig. Uden den lås strækker et langt rollekort hele arbejdsbordet og skubber skrivefeltet og spørgsmålstælleren ud af skærmen (`references/teknik.md`, afsnit 16). På mobil bruges faner i stedet for foldbare bokse og popup-modaler: en fast topbjælke med fire faner (Rådgiver, Rollekort, Startkrav, Casekort), mindst 44 px høje. Ingen notefelt.
- **Kompakt mobilheader:** rolletitel, stemmebadge og fasevælger på én til to linjer, så chatten får maksimal højde. "Skift rolle" bruges sjældent og lægges som et diskret tekstlink nederst, ikke i toppen.
- **Pitch-fane (virksomhedscase med projektteams):** billeder og forslag er inspiration. Skriv, at teamet må bruge ét, flere eller alle forslag, kombinere dem eller finde på egne, og at bestyrelsen bedømmer sammenhæng med strategien og prisen.
- **Rollekortenes format er en grænseflade.** Rådgiveren læser rollekortet ud fra faste overskrifter (MÅL, BAGGRUND, HOLDNING, VÆRDIER, ARGUMENTER, DILEMMAER, SKJULT INFORMATION, SÆRLIG BEFØJELSE, TIP, evt. projekt og løfte). Ændres overskrifterne, skal rådgiveren ændres.
- **Sikkerhed (vigtigt):** alt i en statisk side kan læses af eleverne. Hemmeligheder (API-nøgle, proxy-kode, rollekoder, lærerkode) skal ligge hos en proxy med begrænsninger (herkomst, antal kald, dagsloft), og nøgler, der har stået i en side, skal skiftes før offentliggørelse. Krypterede rollekort med en 4-cifret kode stopper nysgerrighed, ikke en målrettet elev: i Kommunalbudget kunne alle fem rollekoder slås op på under et sekund, fordi hashen af koden er opslagsnøglen (målt, afsnit 2). Skal skjult information tåle en målrettet elev, kræver det længere koder eller et kodetjek på serveren. Lærerkoden skal altid være lang og tilfældig.

## Budget- og beslutningsværktøj (til eleverne)

Bruges, når spillet ender i en fælles plan med penge og en afstemning (Kommunalbudget). Kode og mønstre står i `references/teknik.md` (afsnit 17 til 19).

- **Elevernes værktøj, ikke lærerens.** Bordet fører selv planen: beløb pr. initiativ, afstemning pr. rolle og afslutning. Læreren ser kun resultatet.
- **Live validering:** summen mod puljen, reserve, overforbrug, hele beløb mellem 0 og fuld pris. Delvise bevillinger vises som andel af fuld pris med en note om, at andelen ikke er et mål for effekten.
- **Flertal beregnes ud fra rollernes vægte** (Kommunalbudget: mindst 7 af 12), blanke stemmer tæller ikke som ja, og alle roller skal svare, før planen kan afsluttes.
- **Ændring låser op igen:** rettes planen efter afstemningen, nulstilles afstemningen og resultatkoden automatisk.
- **Gem og flyt:** udkast gemmes i browseren og kan hentes som fil; planen kan udskrives.
- **Resultatkode:** en kort kode med kontrolsum, som bordet læser op eller sender til læreren. Den indeholder kun tal og stemmer, aldrig startkrav eller tekster.
- **Sammenligning (til læreren):** koder eller resultatfiler fra 3 til 6 borde (op til 30) vises side om side på storskærm i debriefingen.

## Facit-beregner (til læreren)

Bruges, når resultatet afhænger af tilfældighed eller skjulte parametre (Fjord Outdoor).

- Indtast bestyrelsens beløb, afslør resultatet i debriefingen. Brug fast sandsynlighedsmodel med tydelige parametre øverst (CFG), så den kan justeres.
- Tjek at pengene afhænger af det, spillet siger (grænser, straf, sandsynligheder), og at pointer som "markedsandel" ikke udløser forvirring (se begrænsning af begreber i projektreglerne).
- Tilfældighed: vis forventet værdi og et udfald, og forklar forskellen i debriefingen.

## Lærershow (artefakt)

- Scener i den rækkefølge spillet har: plan, hvert projekt, portefølje, likviditet, flere år, hvad hvis, debriefing.
- Fjern scener, der trækker fokus væk fra målet. I Fjord Outdoor blev BCG-scenen fjernet, fordi BCG-forskydningen kom fra markedets grundtendens og ikke fra bestyrelsens ekstra penge, og det forvirrede mere end det forklarede. Test altid, om en mekanik "straffer" noget, eleverne ikke selv kan påvirke.
- Fjern også tilbageværende henvisninger i tekster og debriefingsspørgsmål, når en del skæres væk.
- Design: samme farver og skrift som resten af spillet.

## Krypteret lærerpakke

- Lærerens materialer (rollekort, bilag, lærerguide, cheatsheet som .docx i en ZIP) ligger krypteret i en script-fil og låses op med en lærerkode på en side til læreren. Efter oplåsning kan læreren hente hele pakken som ZIP.
- Det beskytter mod elever, der bare klikker rundt på sitet, ikke mod en elev, der målrettet henter filen og gætter koden offline. Brug en lang, tilfældig lærerkode (ikke 4 cifre), og del den kun med kolleger.
- Pakken bygges af et script, ikke i hånden (`references/teknik.md`, afsnit 20). Efter hver ændring i materialerne bygges pakken og siden på ny.

## Forside og medier

Forsiden bærer meget mere end en titel og en knap. Den skal give læreren og eleverne det samlede overblik, før de åbner spillet.

- **Informationsarkitektur:** (1) en hero med fagligt løfte og én tydelig knap; (2) nøgletal (pulje, antal roller, stemmer); (3) de modstridende roller med stemmetal eller vægt; (4) spillets faser i klassen; (5) den faglige ramme for læreren (fag og niveau, kernestof, forløbets omfang, klassestørrelse og hvordan flere elever deler en rolle, materialepakken); (6) en afsluttende knap. Rollerne vises med titel, stemmetal og en kort mærkesag, aldrig med skjult information.
- **Virksomhedscase:** vis virksomheden **som den er før investeringen**. Billeder, tekst og video må ikke vise det, eleverne skal pitche (nye produkter, nye markeder, kurser). Brug kun oplysninger fra rollekort og bilag, der er fælles viden. Ingen skjult information, ingen BCG-etiketter, ingen Ansoff-strategi ved projekterne, ingen konkurrenttal. Forsiden har kun ét menupunkt, fx "Casespillet", i menuens almindelige farve (ikke accentfarven), og en knap i heroen til casespilssiden. Forsiden har ingen popup eller modal og intet link til AI-rådgiveren, hverken i menu, hero eller footer. Rådgiveren nås fra casespilssiden.
- **Samfundsfaglig case uden fiktiv virksomhed:** spillet har selv en forside (præsentationen) og en casespilsside (værktøjerne). Forsiden linker til casespilssiden og til lærerens materialer, ikke direkte til rådgiveren.
- Mærk siden som fiktiv og AI-genereret.
- **Billeder:** komprimér (ca. 100 til 300 KB pr. billede), lav poster ud fra videoens første billede, alt-tekster der passer til stedet i fortællingen. Giv altid `width` og `height`. Brug `loading="lazy"` kun til lange lister af billeder under skærmbunden; på en forside med få vigtige sektionsbilleder (3 til 4) giver det tomme eller grå kasser i headless browsere, ved skærmbilleder og ved hurtig scroll, så brug direkte indlæsning.
- **Billedprompter til fotorealistiske billeder:** vis det konkrete faglige miljø i naturligt lys med virkelighedsnære detaljer, fx et byrådsbord med kaffekopper, papirer og bærbare computere i dagslys, en lokal gade med cyklister og en rigtig bybus, en varm samtale mellem to mennesker. Undgå sci-fi, 3D-render og stockfoto-klichéer. Intet læsbart tekststof, som modellen kan stave forkert.
- Video: hold den kort (ca. 10 sek.), lad tekst på siden fade ud, når videoens slutlogo kommer, så de ikke ligger oven på hinanden.
- Prompter til videomodeller: skriv dem på engelsk, med dansk lokalitet og dansk udtale af replikker, én person der går igen (billede vedhæftes), logo placeret som ønsket.

## Casespilssiden (hub)

Formål: ét sted, eleverne kan åbne for at forstå spillet, uden at noget afsløres. Siden hedder fx `casespil.html` og ligger ved siden af forsiden. Opbygning og kode står i `references/teknik.md` (afsnit 15).

- **Indhold:** kort introtekst, den indlejrede spilintro, værktøjerne som kort med nummer og tydelig opgave (fx 01 Forbered din rolle med rådgiveren, 02 Forhandl i byrådet med budgetværktøjet), de spilfaser hvor eleverne handler (grundregel 6), og roller og regler. Lærerens links (materialer, sammenligning) ligger adskilt.
- **Menu:** i en virksomhedscase kun logo og ét link tilbage til virksomhedens forside, ingen sektionsmenu. I en case uden virksomhedsside en simpel sidenavigation mellem værktøjerne (Overblik, Din rolle, Budget, Lærer, Opsamling), så eleverne kan skifte uden at gå tilbage.
- **Ingen popup eller modal på forsiden.** Gamle `#intro`-links (og `?intro=1`) på forsiden sendes videre til casespilssiden.
- **Hubben er offentlig og afslører aldrig det, eleverne selv skal finde ud af:** ingen modelplaceringer (fx BCG-felter som "malkeko", "stjerne" og "spørgsmålstegn"), ingen strategimodel ved projekterne (fx Ansoff) og ingen beskrivelser af rollernes holdninger. Roller vises kun med titel, antal stemmer og særlig beføjelse.
- **Hent, opfind ikke.** Roller, titler, stemmetal og beløb hentes fra rollekort og bilag. I Fjord Outdoor var seks bestyrelsesroller opfundet på siden og passede ikke til rollekortene.
- **Gengiv de regler, der gør spillet forståeligt:** hvordan der stemmes og hvor mange stemmer der kræves, om nogen har veto, hvad der sker, hvis der ikke findes flertal (standardplan), særlige beslutninger (Fjord Outdoor: fritidstøjet) og hvad der sker med det ubrugte (reserve). Brug bilagenes formuleringer.

## Spilintro og animation (multimedie)

Formål: sætte eleverne i stemning på 60 til 90 sekunder (Fjord Outdoor: 84). Introen etablerer den brændende platform (fx 10 mio. kr. på spil), de to lejre (fx bestyrelse mod projektteams), spillets faser og afgørelsens time. Længere introer mister opmærksomheden. Teknik, kode og voiceover står i `references/teknik.md` (afsnit 11 og 12).

- **Dramaturgi i 4 til 5 scener:** situationen, magtkampen, dilemmaet, faserne, finalen. Én idé pr. scene, så tekst, billede og stemme følges ad.
- **Format:** introen vises indlejret på casespilssiden. Der laves ingen popup på forsiden. Som ekstra kan en ren afspillerside (`intro.html`) bestå: afspilleren i fuld bredde, til læreren på storskærm og som direkte link i Aula eller Lectio.
- **Én afspiller i én fil.** Afspilleren og underteksterne bor i én fil, og casespilssiden indlejrer den, så der ikke findes to kopier, der kan drive fra hinanden (Fjord Outdoor havde afspilleren to steder). Når et format udgår, fjernes dets HTML, CSS og script helt (popup'en lå som død kode i forsiden). Sammenlign skærmbilleder af forsiden før og efter oprydning.
- **Indhold følger projektreglerne:** ingen ritualord eller pædagogiske metakommentarer (fx "flipped classroom" eller "lektie"), ingen faste minuttal, og faserne har samme navne og rækkefølge som i lærerguiden og elevintroduktionen. Tal og regler (antal stemmer, flertalskrav) hentes fra den fælles kilde. Introen er offentlig: den må forklare spillets regler, men aldrig skjult information eller resultater.
- **Tjek scenetekster og voiceover mod bilagene, før stemmen indtales.** Voiceover kan ikke rettes uden ny indtaling, og formuleringer, der forstærker eller modsiger reglerne, skal væk (eksempler i `references/teknik.md`, afsnit 12).
- **Afspilleren er enkel:** afspil og pause, en tidslinje man kan trykke på, to knapper på -10 og +10 sekunder, undertekster der kan slås til og fra (CC), fuld skærm, mellemrum og piletaster. Ingen fremskridtsprikker oven på billedet og ingen knapper til næste eller forrige scene, fordi de forvirrer mere, end de hjælper.
- **Startskærm med knap:** lyd kan ikke starte af sig selv i en browser, så introen åbner med en titel og en tydelig "Start introduktion".
- **Altid brugbar uden lyd:** mangler lydfilen, kører scener og undertekster videre på et ur, så siden aldrig står tom.

## Grafisk stil: anti-AI og kontrast

Digitale dele skal ligne spillets egen verden og ikke et generisk AI-dashboard. Detaljer og kode står i `references/teknik.md` (afsnit 13).

- **Undgå:** neonfarver, gradient-bokse, uigennemskuelige KPI-felter og kort med tyk farvet kant i venstre side som fast kendetegn.
- **Vælg stil efter faget og emnet.** Spørg: hvilken verden hører spillet til, og hvordan ser den ud i virkeligheden? Fjord Outdoor er outdoor-corporate (fjordblå, rå materialer, rav). Kommunalbudget er civic editorial (mørk petrol, varm papirbaggrund, afdæmpet salviegrøn, kobber og guld, serif til overskrifter). Definér farverne som få navngivne tokens, og brug dem overalt. Et nyt spil får sit eget designsystem, ikke en kopi af det forrige.
- **Brug:** redaktionel, rolig typografi (Source Serif 4 til scenetitler, store overskrifter og indledende tekst, Source Sans 3 til brødtekst, data og knapper). Hvide kort med 1 px kant og afdæmpet skygge, oven på dæmpede fotobaggrunde.
- **Billeder skal passe til branchen og kunne ses.** Et bestyrelseslokale for en outdoorvirksomhed har træ, råt lys, overtøj og kaffekopper, ikke glasskærme og kold tech-stemning. Er billedet gemt bag et næsten dækkende farvelag, er valget spildt arbejde.
- **Kontrast er en regel, ikke en smagssag.** Rolle- og statusmærker (badges) har fast, mættet baggrund og eksplicit tekstfarve. Brug aldrig en CSS-variabel uden at tjekke, at den findes, og regn kontrasten efter i stedet for at antage den. Mål: mindst 4,5 til 1 (AA), og 7 til 1 (AAA) på små mærker, hvor det kan lade sig gøre.

## Tjekliste før levering

- [ ] Tal ens i bilag, casekort, budgetværktøj, facit, show, spilintro og casespilsside
- [ ] Roller, stemmer, beløb og regler på casespilssiden er sammenholdt med rollekort og bilag
- [ ] Ingen skjult information eller facit på offentlige sider (spilintro og casespilsside inkluderet), ingen BCG- eller Ansoff-svar
- [ ] Spilfaserne har samme navne og numre overalt, og rådgiver og webside viser kun spilfaserne
- [ ] Alle filer har backup i arkivmappen, også ved små rettelser
- [ ] Computer og mobil set, ingen vandret scroll, ingen JavaScript-fejl, og den automatiske test består
- [ ] Rådgiverens kode, rollekoder og lærervindue testet, og koderne på rollekortene matcher hasherne i rådgiveren
- [ ] Rådgiveren åbner med et åbent spørgsmål, har ingen forslagsknapper, og tælleren overlever rolleskift
- [ ] Startkrav låser hverken forhandling eller budgetværktøj
- [ ] Mobil rådgiver: fire faner på mindst 44 px, kompakt header, "Skift rolle" som diskret link nederst
- [ ] Computer: arbejdsbordet er låst til skærmens højde, og et meget langt rollekort skubber hverken skrivefeltet eller tælleren ud af skærmen
- [ ] Budgetværktøj: overforbrug og reserve vises, ændring nulstiller afstemning og kode, og resultatkoden består roundtrip og afviser manipulation
- [ ] Resultatkoden indeholder hverken startkrav eller tekster, og sammenligningen viser flere borde side om side
- [ ] Lærerpakken er bygget på ny efter sidste ændring i materialerne, og lærerkoden er lang og tilfældig
- [ ] Spilintro: afspilleren findes i én fil, den indlejrede version og en evt. `intro.html` viser det samme, lyden virker, og undertekster følger stemmen
- [ ] Video og stemme er tjekket mod bilagene, før stemmen blev indtalt
- [ ] Forsiden har de rigtige menupunkter og en hero-knap til casespilssiden, intet link til rådgiveren og ingen popup, og gamle `#intro`-links sendes videre
- [ ] Billeder har `width` og `height`, og `loading="lazy"` bruges kun til lange lister
- [ ] Ingen død kode efter oprydning, og forsiden ser ens ud før og efter
- [ ] Mobil: menulinks virker, evt. overlays lukker helt (ingen frossen side), Tilbage-knappen virker, set på en rigtig telefon
- [ ] Kontrast tjekket på alle mærker, og ingen CSS-variabel er brugt uden at være defineret
- [ ] Sprog: dansk, ingen tankestreger, ingen faste minuttal
