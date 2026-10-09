---
name: casespil-digitale-tillaeg
description: "Designregler og teknisk reference til digitale tilføjelser til et casespil (også kaldet rollespil): AI-rådgiver pr. rolle, facit-beregner, lærershow, virksomhedswebside, casespilsside (hub) med indlejret spilintro (animation med voiceover og undertekster), video og billedprompter. Brug når et casespil eller rollespil skal have digitale værktøjer, efter at papirmaterialerne er godkendt. Bygger på erfaringerne fra Fjord Outdoor. Brug ikke til casespil eller rollespil uden digitale dele eller til almindelige websider og apps."
---

# Digitale tilføjelser til casespil

**Projektregler:** `casespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill kommer EFTER casespillets design og papirmaterialer er færdige (rollekort, elevintroduktion, bilag). Den styrer, hvordan de digitale dele bygges, så de passer sammen og ikke afslører noget, eleverne ikke må se.

**Teknisk reference:** Før du bygger noget, læs `references/teknik.md`. Den indeholder det tekniske mønster, som er afprøvet i Fjord Outdoor: filstruktur og fælles datasæt, kryptering og koder, proxy til modelkald, prompt-opbygning, session og spørgsmålstæller, rollekortparser, responsivt design, billeder og video, spilintroens opbygning og synkronisering, voiceover, grafisk stil og kontrast, mobil og Safari, test med Playwright og sikkerhed. Spar tid ved at genbruge mønstrene i stedet for at opfinde dem igen.

**Rækkefølge:** (1) Fælles datasæt og skjult-information-liste. (2) Webside og medier. (3) Casespilsside (hub) og spilintro (efter websiden, fordi de bruger websidens billeder og stil). (4) AI-rådgiver. (5) Facit-beregner. (6) Lærershow. (7) Test, også på en rigtig telefon. (8) Kør `casespil-konsistenstjek`, som også dækker digitale dele og beregner-tjek.

**Relaterede skills:** `casespil-designprincipper` (hvad må eleverne vide, hvornår), `casespil-projektregler` (beregner-tjek, begrænsningsregel, fælles kilde), `casespil-konsistenstjek` (kvalitetssikring), `casespil-sprogtjek` (alle tekster i værktøjerne).

## Grundregler

1. **Én kilde til tallene.** Alle tal (markedsdata, grænser, sandsynligheder, straf, budget, antal stemmer og flertalskrav) og alle roller med titel, stemmetal og beføjelse står i ét sæt og kopieres derfra til: bilag, casekort i rådgiveren, facit-beregneren, showet, spilintroen og casespilssiden. Efter hver ændring tjekkes alle steder.
2. **Skjult information bliver skjult.** Det, der kun står på ét rollekort, og resultatet af valgene (hvad pengene gav) må ikke stå i noget, der er offentligt eller fælles: websiden, casespilssiden, casekortet, spilintroen, showets scener før afsløringen, billedtekster.
3. **Backup før hver ændring.** Gem den gamle fil i en arkivmappe med et sigende navn (fx `_arkiv/..._foer_<ændring>.html`). Slet aldrig. Det gælder også ved gennemgang og små rettelser, ikke kun ved nybyggeri. I Fjord Outdoor blev filer ændret uden backup.
4. **Test før du siger det er færdigt.** Åbn siden i en browser, tjek computer (ca. 1300 px) og mobil (ca. 390 px og 320 px), ingen vandret scroll, ingen JavaScript-fejl. Se billedet, ikke kun koden. Safari på iPhone opfører sig anderledes end Chrome: bed læreren åbne siden på en rigtig telefon, før den kaldes færdig (se afsnit 14 i `references/teknik.md`).
5. **Sproget følger materialerne.** Dansk, ingen tankestreger, ingen faste minuttal, ingen ritualer som "I spiller en rolle".
6. **Samme faser overalt.** Webside, rådgiver og lærerguidens faseoversigt bruger kun de spilfaser, hvor eleverne agerer og har brug for sparring (Fjord Outdoor: 1 Forberedelse, 2 Pitches, 3 Korridorforhandlinger, 4 Bestyrelsesmødet). Introduktion og debriefing er ikke rådgiverfaser. Papirmaterialerne (elevintroduktion, rollekortenes faseguide, lærerguidens debriefingafsnit) må have Intro og Debriefing som før- og eftertrin uden fasenummer, men spilfaserne har samme navne, numre og rækkefølge i alle materialer.

## AI-rådgiver pr. rolle

Formål: eleven kan stille op til 10 spørgsmål om sin egen rolle, sit kort og fagbegreber. Rådgiveren giver hints og modspørgsmål, aldrig færdige replikker.

- **Kontekst til modellen:** casekort (fælles), elevens eget rollekort (forside og bagside), fagligt grundlag, aktuel fase (kun spilfaserne, se grundregel 6). Intet andet. Rådgiveren kender ikke de andre roller og må ikke gætte på dem.
- **Regler i prompten:** højst 100 ord, dansk, "du"-form, ingen indledning, regn aldrig budget eller stemmer selv (vis formlen), nævn kun tal fra casekort, rollekort eller grundlag, hold sig til casespillet, send eleven til læreren hvis der er tegn på mistrivsel. Elevens besked ligger i et afgrænset felt og er ikke nye regler.
- **Adgang:** en 4-cifret kode pr. rolle (ikke samme kode til alle). I siden gemmes kun en hash af koderne (se `references/teknik.md`, afsnit 2). Koden trykkes på forsiden af rollekortet i topbjælkens undertitel, fx "Fjord Outdoors bestyrelse | Leder mødet | Rådgiverkode: 2481", og ikke under en overskrift, fordi rådgiveren læser kortets faste overskrifter. Rådgiverens fejlbesked og tekster på casespilssiden må ikke skrive "fra dit kort", hvis koden ikke står der. Lærervinduet viser KUN rollekoderne, ingen log, ingen nøgle, ingen faseføring.
- **Spørgsmålstæller:** gemmes pr. rolle i browseren, så et rolleskift ikke giver 10 nye. Tælleren nulstilles først 2 timer efter start (fast starttidspunkt, ikke glidende). Det kan omgås med privat vindue eller ryddede data. Vil man have en hård grænse, skal den ligge på serveren.
- **Visning:** vis hele rollekortet i rådgiveren (hvis det ikke printes), som ét kort uden ramme i ramme, med teori og faseguide som almindelige sektioner nederst. Casekortet i egen fane ved siden af. Mobil: foldbare bokse. Ingen notefelt.
- **Pitch-fane (projektteams):** billeder og forslag er inspiration. Skriv, at teamet må bruge ét, flere eller alle forslag, kombinere dem eller finde på egne, og at bestyrelsen bedømmer sammenhæng med strategien og prisen.
- **Rollekortenes format er en grænseflade.** Rådgiveren læser rollekortet ud fra faste overskrifter (MÅL, BAGGRUND, HOLDNING, VÆRDIER, ARGUMENTER, DILEMMAER, SKJULT INFORMATION, SÆRLIG BEFØJELSE, TIP, evt. projekt og løfte). Ændres overskrifterne, skal rådgiveren ændres.
- **Sikkerhed (vigtigt):** alt i en statisk side kan læses af eleverne. Hemmeligheder (API-nøgle, proxy-kode, rollekoder, lærerkode) skal ligge hos en proxy med begrænsninger (herkomst, antal kald, dagsloft), og nøgler, der har stået i en side, skal skiftes før offentliggørelse. Krypterede rollekort stopper nysgerrighed, ikke en målrettet elev.

## Facit-beregner (til læreren)

- Indtast bestyrelsens beløb, afslør resultatet i debriefingen. Brug fast sandsynlighedsmodel med tydelige parametre øverst (CFG), så den kan justeres.
- Tjek at pengene afhænger af det, spillet siger (grænser, straf, sandsynligheder), og at pointer som "markedsandel" ikke udløser forvirring (se begrænsning af begreber nedenfor).
- Tilfældighed: vis forventet værdi og et udfald, og forklar forskellen i debriefingen.

## Lærershow (artefakt)

- Scener i den rækkefølge spillet har: plan, hvert projekt, portefølje, likviditet, flere år, hvad hvis, debriefing.
- Fjern scener, der trækker fokus væk fra målet. I Fjord Outdoor blev BCG-scenen fjernet, fordi BCG-forskydningen kom fra markedets grundtendens og ikke fra bestyrelsens ekstra penge, og det forvirrede mere end det forklarede. Test altid, om en mekanik "straffer" noget, eleverne ikke selv kan påvirke.
- Fjern også tilbageværende henvisninger i tekster og debriefingsspørgsmål, når en del skæres væk.
- Design: samme farver og skrift som resten af spillet (Fjord og Forretning: fjordblå 12344D, skovgrøn 2F5D50, rav D9822B, kalk F3EEE3, sand FBF1DE, baggrund E9E5DD, Source Sans 3 og Source Serif 4).

## Virksomhedsweb og medier

- Vis virksomheden **som den er før investeringen**. Billeder, tekst og video må ikke vise det, eleverne skal pitche (nye produkter, nye markeder, kurser).
- Brug kun oplysninger fra rollekort og bilag, der er fælles viden. Ingen skjult information, ingen BCG-etiketter, ingen Ansoff-strategi ved projekterne, ingen konkurrenttal.
- **Forsiden og casespillet:** forsiden har kun ét menupunkt, fx "Casespillet", i menuens almindelige farve (ikke i accentfarven), og en knap i heroen til casespilssiden. Forsiden har ingen popup eller modal og intet link til AI-rådgiveren, hverken i menu, hero eller footer. Rådgiveren nås fra casespilssiden.
- Mærk siden som fiktiv og AI-genereret.
- Billeder: komprimér (ca. 100 til 300 KB pr. billede), lav poster ud fra videoens første billede, alt-tekster der passer til stedet i fortællingen.
- Video: hold den kort (ca. 10 sek.), lad tekst på siden fade ud, når videoens slutlogo kommer, så de ikke ligger oven på hinanden.
- Prompter til videomodeller: skriv dem på engelsk, med dansk lokalitet og dansk udtale af replikker, én person der går igen (billede vedhæftes), logo placeret som ønsket.

## Casespilssiden (hub)

Formål: ét sted, eleverne kan åbne for at forstå spillet, uden at noget afsløres. Siden hedder fx `casespil.html` og ligger ved siden af forsiden. Opbygning og kode står i `references/teknik.md` (afsnit 15).

- **Indhold:** kort introtekst, den indlejrede spilintro, en knap til AI-rådgiveren, de spilfaser hvor eleverne handler (grundregel 6), og roller og regler.
- **Menu:** kun logo og ét link tilbage til virksomhedens forside. Ingen sektionsmenu.
- **Ingen popup eller modal på forsiden.** Gamle `#intro`-links (og `?intro=1`) på forsiden sendes videre til casespilssiden.
- **Hubben er offentlig og afslører aldrig det, eleverne selv skal finde ud af:** ingen modelplaceringer (fx BCG-felter som "malkeko", "stjerne" og "spørgsmålstegn"), ingen strategimodel ved projekterne (fx Ansoff) og ingen beskrivelser af rollernes holdninger. Roller vises kun med titel, antal stemmer og særlig beføjelse.
- **Hent, opfind ikke.** Roller, titler, stemmetal og beløb hentes fra rollekort og bilag. I Fjord Outdoor var seks bestyrelsesroller opfundet på siden og passede ikke til rollekortene.
- **Gengiv de regler, der gør spillet forståeligt:** hvordan der stemmes og hvor mange stemmer der kræves, om nogen har veto, hvad der sker, hvis der ikke findes flertal (standardplan), særlige beslutninger (Fjord Outdoor: fritidstøjet) og hvad der sker med det ubrugte (reserve). Brug bilagenes formuleringer.

## Spilintro og animation (multimedie)

Formål: sætte eleverne i stemning på 60 til 90 sekunder (Fjord Outdoor: 84). Introen etablerer den brændende platform (fx 10 mio. kr. på spil), de to lejre (fx bestyrelse mod projektteams), spillets faser og afgørelsens time. Længere introer mister opmærksomheden. Teknik, kode og voiceover står i `references/teknik.md` (afsnit 11 og 12).

- **Dramaturgi i 4 til 5 scener:** situationen, magtkampen, dilemmaet, faserne, finalen. Én idé pr. scene, så tekst, billede og stemme følges ad.
- **Format:** introen vises indlejret på casespilssiden. Der laves ingen popup på forsiden. Som ekstra kan en ren afspillerside (`intro.html`) bestå: afspilleren i fuld bredde, til læreren på storskærm og som direkte link i Aula eller Lectio.
- **Én afspiller i én fil.** Afspilleren og underteksterne bor i én fil, og casespilssiden indlejrer den, så der ikke findes to kopier, der kan drive fra hinanden (Fjord Outdoor havde afspilleren to steder). Når et format udgår, fjernes dets HTML, CSS og script helt (popup'en lå som død kode i forsiden). Sammenlign skærmbilleder af forsiden før og efter oprydning.
- **Indhold følger projektreglerne:** ingen ritualord eller pædagogiske metakommentarer (fx "flipped classroom" eller "lektie"), ingen faste minuttal, og faserne har samme navne og rækkefølge som i lærerguiden og elevintroduktionen (Fjord Outdoor: Forberedelse, Pitches, Korridorforhandlinger, Bestyrelsesmødet). Tal og regler (antal stemmer, flertalskrav) hentes fra den fælles kilde. Introen er offentlig: den må forklare spillets regler, men aldrig skjult information eller resultater.
- **Tjek scenetekster og voiceover mod bilagene, før stemmen indtales.** Voiceover kan ikke rettes uden ny indtaling, og formuleringer, der forstærker eller modsiger reglerne, skal væk (eksempler i `references/teknik.md`, afsnit 12).
- **Afspilleren er enkel:** afspil og pause, en tidslinje man kan trykke på, to knapper på -10 og +10 sekunder, undertekster der kan slås til og fra (CC), fuld skærm, mellemrum og piletaster. Ingen fremskridtsprikker oven på billedet og ingen knapper til næste eller forrige scene, fordi de forvirrer mere, end de hjælper.
- **Startskærm med knap:** lyd kan ikke starte af sig selv i en browser, så introen åbner med en titel og en tydelig "Start introduktion".
- **Altid brugbar uden lyd:** mangler lydfilen, kører scener og undertekster videre på et ur, så siden aldrig står tom.

## Grafisk stil: anti-AI og kontrast

Digitale dele skal ligne virksomhedens egen verden og ikke et generisk AI-dashboard. Detaljer og kode står i `references/teknik.md` (afsnit 13).

- **Undgå:** neonfarver, gradient-bokse, uigennemskuelige KPI-felter og kort med tyk farvet kant i venstre side som fast kendetegn.
- **Brug:** redaktionel, rolig typografi (Source Serif 4 til introens scenetitler og indledende tekst, Source Sans 3 til overskrifter, data og knapper). Hvide kort med 1 px kant (`#DDD5C4`) og afdæmpet skygge, oven på dæmpede fotobaggrunde.
- **Billeder skal passe til branchen og kunne ses.** Et bestyrelseslokale for en outdoorvirksomhed har træ, råt lys, overtøj og kaffekopper, ikke glasskærme og kold tech-stemning. Er billedet gemt bag et næsten dækkende farvelag, er valget spildt arbejde.
- **Kontrast er en regel, ikke en smagssag.** Rolle- og statusmærker (badges) har fast, mættet baggrund og eksplicit tekstfarve. Brug aldrig en CSS-variabel uden at tjekke, at den findes, og regn kontrasten efter i stedet for at antage den. Mål: mindst 4,5 til 1 (AA), og 7 til 1 (AAA) på små mærker, hvor det kan lade sig gøre.

## Tjekliste før levering

- [ ] Tal ens i bilag, casekort, facit, show, spilintro og casespilsside
- [ ] Roller, stemmer, beløb og regler på casespilssiden er sammenholdt med rollekort og bilag
- [ ] Ingen skjult information eller facit på offentlige sider (spilintro og casespilsside inkluderet), ingen BCG- eller Ansoff-svar
- [ ] Spilfaserne har samme navne og numre overalt, og rådgiver og webside viser kun spilfaserne
- [ ] Alle filer har backup i arkivmappen, også ved små rettelser
- [ ] Computer og mobil set, ingen vandret scroll, ingen JavaScript-fejl
- [ ] Rådgiverens kode, rollekoder og lærervindue testet, og koderne på rollekortene matcher hasherne i rådgiveren
- [ ] Spilintro: afspilleren findes i én fil, den indlejrede version og en evt. `intro.html` viser det samme, lyden virker, og undertekster følger stemmen
- [ ] Video og stemme er tjekket mod bilagene, før stemmen blev indtalt
- [ ] Forsiden har ét menupunkt og en hero-knap til casespilssiden, intet link til rådgiveren og ingen popup, og gamle `#intro`-links sendes videre
- [ ] Ingen død kode efter oprydning, og forsiden ser ens ud før og efter
- [ ] Mobil: menulinks virker, evt. overlays lukker helt (ingen frossen side), Tilbage-knappen virker, set på en rigtig telefon
- [ ] Kontrast tjekket på alle mærker, og ingen CSS-variabel er brugt uden at være defineret
- [ ] Sprog: dansk, ingen tankestreger, ingen faste minuttal
