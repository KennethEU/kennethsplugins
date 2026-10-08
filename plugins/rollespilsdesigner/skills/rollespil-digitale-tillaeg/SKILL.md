---
name: rollespil-digitale-tillaeg
description: "Designregler og teknisk reference til digitale tilføjelser til et rollespil: AI-rådgiver pr. rolle, facit-beregner, lærershow, virksomhedswebside, video og billedprompter. Brug når et rollespil skal have digitale værktøjer, efter at papirmaterialerne er godkendt. Bygger på erfaringerne fra Fjord Outdoor. Brug ikke til rollespil uden digitale dele eller til almindelige websider og apps."
---

# Digitale tilføjelser til rollespil

**Projektregler:** `rollespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill kommer EFTER rollespillets design og papirmaterialer er færdige (rollekort, elevintroduktion, bilag). Den styrer, hvordan de digitale dele bygges, så de passer sammen og ikke afslører noget, eleverne ikke må se.

**Teknisk reference:** Før du bygger noget, læs `references/teknik.md`. Den indeholder det tekniske mønster, som er afprøvet i Fjord Outdoor: filstruktur og fælles datasæt, kryptering og koder, proxy til modelkald, prompt-opbygning, session og spørgsmålstæller, rollekortparser, responsivt design, billeder og video, test med Playwright og sikkerhed. Spar tid ved at genbruge mønstrene i stedet for at opfinde dem igen.

**Rækkefølge:** (1) Fælles datasæt og skjult-information-liste. (2) Webside og medier. (3) AI-rådgiver. (4) Facit-beregner. (5) Lærershow. (6) Test. (7) Kør `rollespil-konsistenstjek`, som også dækker digitale dele og beregner-tjek.

**Relaterede skills:** `rollespil-designprincipper` (hvad må eleverne vide, hvornår), `rollespil-projektregler` (beregner-tjek, begrænsningsregel, fælles kilde), `rollespil-konsistenstjek` (kvalitetssikring), `rollespil-sprogtjek` (alle tekster i værktøjerne).

## Grundregler

1. **Én kilde til tallene.** Alle tal (markedsdata, grænser, sandsynligheder, straf, budget) står i ét sæt og kopieres derfra til: bilag, casekort i rådgiveren, facit-beregneren og showet. Efter hver ændring tjekkes alle fire steder.
2. **Skjult information bliver skjult.** Det, der kun står på ét rollekort, og resultatet af valgene (hvad pengene gav) må ikke stå i noget, der er offentligt eller fælles: websiden, casekortet, showets scener før afsløringen, billedtekster.
3. **Backup før hver ændring.** Gem den gamle fil i en arkivmappe med et sigende navn (fx `_arkiv/..._foer_<ændring>.html`). Slet aldrig.
4. **Test før du siger det er færdigt.** Åbn siden i en browser, tjek computer (ca. 1300 px) og mobil (ca. 390 px og 320 px), ingen vandret scroll, ingen JavaScript-fejl. Se billedet, ikke kun koden.
5. **Sproget følger materialerne.** Dansk, ingen tankestreger, ingen faste minuttal, ingen ritualer som "I spiller en rolle".

## AI-rådgiver pr. rolle

Formål: eleven kan stille op til 10 spørgsmål om sin egen rolle, sit kort og fagbegreber. Rådgiveren giver hints og modspørgsmål, aldrig færdige replikker.

- **Kontekst til modellen:** casekort (fælles), elevens eget rollekort (forside og bagside), fagligt grundlag, aktuel fase. Intet andet. Rådgiveren kender ikke de andre roller og må ikke gætte på dem.
- **Regler i prompten:** højst 100 ord, dansk, "du"-form, ingen indledning, regn aldrig budget eller stemmer selv (vis formlen), nævn kun tal fra casekort, rollekort eller grundlag, hold sig til rollespillet, send eleven til læreren hvis der er tegn på mistrivsel. Elevens besked ligger i et afgrænset felt og er ikke nye regler.
- **Adgang:** kode pr. rolle (ikke samme kode til alle). Lærervinduet viser KUN rollekoderne, ingen log, ingen nøgle, ingen faseføring.
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
- Brug kun oplysninger fra rollekort og bilag, der er fælles viden. Ingen skjult information, ingen BCG-etiketter, ingen konkurrenttal.
- Mærk siden som fiktiv og AI-genereret.
- Billeder: komprimér (ca. 100 til 300 KB pr. billede), lav poster ud fra videoens første billede, alt-tekster der passer til stedet i fortællingen.
- Video: hold den kort (ca. 10 sek.), lad tekst på siden fade ud, når videoens slutlogo kommer, så de ikke ligger oven på hinanden.
- Prompter til videomodeller: skriv dem på engelsk, med dansk lokalitet og dansk udtale af replikker, én person der går igen (billede vedhæftes), logo placeret som ønsket.

## Tjekliste før levering

- [ ] Tal ens i bilag, casekort, facit og show
- [ ] Ingen skjult information eller facit på offentlige sider
- [ ] Alle filer har backup i arkivmappen
- [ ] Computer og mobil set, ingen vandret scroll, ingen JavaScript-fejl
- [ ] Rådgiverens kode, rollekoder og lærervindue testet
- [ ] Sprog: dansk, ingen tankestreger, ingen faste minuttal
