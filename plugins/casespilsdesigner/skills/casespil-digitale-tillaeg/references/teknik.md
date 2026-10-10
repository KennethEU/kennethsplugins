# Tekniske principper og mønstre til digitale casespilsværktøjer

Samlet fra to afprøvede spil: Fjord Outdoor (erhvervsøkonomi: AI-rådgiver, webside, facit, show, spilintro) og Kommunalbudget (samfundsfag: AI-rådgiver, budgetværktøj, resultatkoder, sammenligning, krypteret lærerpakke). Brug det som udgangspunkt, så hvert nyt værktøj ikke skal opfindes forfra. Alt er skrevet til almindelige HTML-sider uden byggetrin, som en lærer kan lægge på en almindelig webhost. Afsnit 16 til 23 gælder især spil, hvor eleverne selv fører en plan i et værktøj, og afsnit 24 beskriver lærerens cockpit.

## 1. Grundarkitektur

- **Én side pr. værktøj** (rådgiver, budget, opsamling, lærer, casespilsside, afspiller, facit, show). Ingen byggetrin, ingen pakkehåndtering. Fjord Outdoor lægger stil og script i hver fil. Kommunalbudget har fire eller flere værktøjer med samme data og stil og deler derfor filer: `stil.css`, `spildata.js` (det offentlige datasæt), `fælles.js` (hjælpefunktioner og kryptering) og `budgetlogik.js`, mens hver side kun har sin egen tynde HTML og sit eget script. Vælg delte filer, når tre eller flere værktøjer bruger det samme. Billeder og lyd ligger i en mappe ved siden af.
- **Ét datasæt som kilde.** Saml roller, tal, parametre og tekster i ét sæt (fx en JSON-fil eller et objekt øverst). Casespilssidens roller, stemmetal, beløb og regler hører også med. Lav helst et lille script, der indsætter dataene i rådgiver, facit, show og casespilsside, i stedet for at kopiere tal i hånden. Det fjerner den hyppigste fejltype: tal, der er rettet det ene sted men ikke de andre.
- **Én afspiller, én fil.** Samme afspiller og samme undertekster ligger aldrig i flere filer (afsnit 11).
- **Parametre øverst.** Alt, der kan justeres (grænser, priser, sandsynligheder, antal spørgsmål, tidsgrænse), står som navngivne konstanter i toppen af scriptet (fx `CFG`, `TOTAL_QUESTIONS`, `SESSION_TTL_MS`). Ingen magiske tal midt i koden.
- **Få afhængigheder til internettet:** selve modelkaldet og skrifttyperne (begge spil henter Source Sans 3 og Source Serif 4 fra Google Fonts). Siden skal se ordentlig ud med systemskrifttyper, hvis fonten ikke kan hentes, og ikoner lægges i filen eller i mappen.
- **Faste sidenavne på tværs af spil** gør det nemt at finde rundt og at skrive tests: `index.html` (præsentation), `casespil.html` (casespilssiden), `raadgiver.html`, `budget.html`, `laerer-assistent.html`, `sammenligning.html`, `intro.html`. Der er ingen særskilt dokumentside til læreren; materialerne hentes i `laerer-assistent.html`. En evt. `laerer.html` er kun en viderestilling.

## 2. Roller, koder og kryptering

- Hver rolle har en **egen 4-cifret adgangskode**. Gem kun en hash af koden (SHA-256) i siden, ikke koden selv.
- **Koden står på rollekortet**, på forsiden i topbjælkens undertitel, fx `Fjord Outdoors bestyrelse | Leder mødet | Rådgiverkode: 2481`. Den står ikke under en overskrift eller i en ny sektion, fordi rådgiverens parser læser kortets faste overskrifter (afsnit 5).
- **Ærlig begrænsning:** en 4-cifret kode har kun 10 000 muligheder. Hashen skjuler koden for den, der læser siden, men en målrettet elev kan afprøve dem alle. Vil man have en hård grænse, tælles forkerte forsøg på serveren (afsnit 3).
- **Kodetjek:** koden på hvert kort, hashen i rådgiveren og koden i lærervinduet skal høre sammen. Lav et lille script, der hasher koderne fra kortene og sammenligner med hasherne i siden, hver gang kort eller rådgiver er ændret.
- **Tekster om koden:** rådgiverens fejlbesked og casespilssidens tekst må kun skrive "fra dit kort", hvis koden faktisk står på kortet.
- Rollekortets indhold kan gemmes krypteret pr. rolle og dekrypteres i browseren, når koden er indtastet. Det stopper nysgerrige blikke i kildekoden og i udviklerværktøjer, men **ikke en målrettet elev**. Sig det til læreren, og lad aldrig hemmeligheder ligge her, som ikke må kendes.
- **Vælg kryptering efter, hvordan siden distribueres.** `crypto.subtle` (Web Crypto) virker kun på sikre adresser (https og localhost), ikke når siden åbnes som lokal fil.
  - **Hostet på https (Kommunalbudget på casespil.dk):** brug Web Crypto. Koden hashes med SHA-256 (hex) og bruges som nøgle i opslagstabellen `ROLE_LOCKS`. Indholdet låses med AES-GCM 256, hvor nøglen udledes af koden med PBKDF2-SHA256 (100 000 runder, 16 byte salt, 12 byte iv). Hver lås er `{salt, iv, data}` i base64. Siden skal fortælle eleven, hvis den åbnes uden sikker adresse ("Åbn siden via HTTPS eller localhost"). Byggekoden står i afsnit 20.
  - **Skal siden kunne åbnes som lokal fil (Fjord Outdoor):** brug en lille indbygget SHA-256 og en simpel strømkryptering (hash af nøgle plus tæller). Det er svagere og beskytter kun mod nysgerrighed.
- **Hvor stærk er en 4-cifret kode, egentlig?** Målt på Kommunalbudget: SHA-256 af alle 10 000 mulige koder tager under et sekund, og alle fem rollekoder kunne slås op med det samme, fordi hashen er opslagsnøglen. Derefter tager hver oplåsning ca. 50 ms (PBKDF2). En elev, der kan skrive en løkke i konsollen, kan altså læse alle rollekort, også dem med skjult information, på under et sekund. Kryptering med 4 cifre stopper nysgerrige klik, ikke en målrettet elev. Vælg ud fra, hvor følsom den skjulte information er:
  - Holder spillet til, at nogle elever kan snyde (de fleste klasser): behold 4 cifre, og sig det til læreren.
  - Skal den skjulte information tåle en målrettet elev: brug længere koder (fx 6 tegn fra et alfabet uden forvekslelige tegn, ca. en milliard muligheder), lad siden prøve koden mod hver lås i stedet for at gemme en hash som opslagsnøgle, og/eller lad proxyen levere rollekortet efter et kodetjek på serveren.
- Lærervinduet viser **kun rollekoderne**. Ingen log, ingen nøgle, ingen faseføring.

## 3. Modelkald (AI-rådgiver)

- **Kald via en proxy**, aldrig direkte fra siden med en nøgle i. En lille Cloudflare Worker er nok: siden sender sit kald og en delt kode i en header, workeren lægger den rigtige API-nøgle på og videresender. Nøglen ligger kun som hemmelighed i workeren.
- **Begræns proxyen:** tilladt herkomst (kun skolens eller sidens adresse), højst x kald pr. minut pr. adresse, et dagsloft i kald eller kroner, og afvis kald med for stor krop. Den delte kode i siden kan alle læse, så den er kun en forhindring, ikke en lås. Skift API-nøgle, hvis den nogensinde har stået i en side.
- **Prompten i to dele:** (1) faste regler, der er ens for alle roller; (2) rollens egen kontekst (casekort, rollekort, fagligt grundlag, aktuel fase). Elevens spørgsmål sendes i afgrænsede tags (fx `<spørgsmål>`), så det ikke kan læses som nye regler.
- **Indstillinger der virkede:** lav temperatur (ca. 0,4), ca. 2500 tokens som loft (svar skal alligevel være korte), laveste tilladte tænkeniveau, kun de seneste ca. 10 spørgsmål og svar som historik.
- **Robusthed:** tidsgrænse på kaldet (ca. 45 sekunder), to genforsøg ved netværksfejl, læsning af streaming-svar linje for linje, og danske fejlbeskeder til eleven ("Prøv igen om lidt") i stedet for rå fejltekst. Tæl kun et spørgsmål som brugt, når der kom et svar.
- **Svarlængde og tone** styres i prompten (højst ca. 100 ord, "du"-form, ingen indledning), ikke af tokenloftet. Kommunalbudget beder om ca. 50 til 85 ord.
- **Sokratisk prompt (Kommunalbudget):** (1) svar direkte og dialogisk; (2) træk på rollens værdier, holdninger og dilemmaer og hjælp eleven med at tænke taktisk over stemmetal; (3) brug den faglige model (fx Eastons model) når det giver mening; (4) afslut ALTID med et kort, åbent modspørgsmål; (5) skriv ALDRIG en færdig tale eller budgetløsning; (6) du kender kun dit eget rollekort og det fælles casekort; (7) ingen tankestreger, overskrifter eller emojis. Elevens spørgsmål ligger i `<elevspørgsmål>`-tags.
- **Åbningsbesked i stedet for forslagsknapper:** rådgiveren åbner hver samtale med en fast besked pr. rolle, der hilser, nævner rollens stemmer og mål og hvad der mangler for flertal, og slutter med et åbent spørgsmål (fx "Hvad overvejer I at lægge ud med?"). Ingen klikbare forslag til spørgsmål: de passiviserer eleverne. Læg åbningsbeskederne i rollens data, ikke hårdkodet i scriptet.
- **Én proxy kan tjene flere spil:** hvert spil har sit eget `appId`-token i en header, så proxyen kan skelne og begrænse dem hver for sig. Tokenet kan alle læse og er kun en forhindring.
- **Log:** kun hvis læreren har brug for den. Elevernes spørgsmål er personoplysninger, så ingen navne, kort opbevaring, og mulighed for at slå logning helt fra. Pris pr. kald kan regnes ud fra tokens, men vis det kun for læreren.

## 4. Session og spørgsmålstæller

- Gem sessionen i `localStorage` med et **fast starttidspunkt** (første handling), ikke et tidspunkt, der opdateres ved hver handling. Så nulstilles alt først en fast tid efter start (fx 2 timer).
- Gem kun, når der er en rolle eller en tråd. Ellers oprettes tomme sessioner.
- **Rolleskift må ikke nulstille tælleren.** Gem sessionen under en nøgle med spillets og rollens id (Kommunalbudget: `kommunalbudget-ai-<rolleid>`), så en elev, der skifter rolle eller afprøver en anden, ikke får 10 nye spørgsmål, og tælleren tæller pr. rolle. Tjek ved indlæsning, at den gemte session har den forventede form, ellers oprettes en ny.
- Tælleren i browseren kan omgås (privat vindue, ryddede data). En hård grænse kræver en tæller på serveren, fx i proxyen pr. rollekode.

## 5. Rollekort og casekort i siden

- Rollekortets **overskrifter er en grænseflade**: rådgiveren og kortvisningen læser dem. Fast sæt: MÅL, BAGGRUND, HOLDNING, VÆRDIER, ARGUMENTER, DILEMMAER, SKJULT INFORMATION, SÆRLIG BEFØJELSE, TIP, evt. projekt og løfte. Ændres de, skal parseren ændres.
- **Rådgiverens faser:** faselisten indeholder kun de spilfaser, hvor eleverne agerer og har brug for sparring (Fjord Outdoor: Forberedelse, Pitches, Korridorforhandlinger, Bestyrelsesmødet). Introduktion og debriefing er ikke rådgiverfaser. Navne og numre er de samme som på rollekort og i lærerguide.
- **Én komponent til kortet**, brugt både som fane i informationspanelet på computer (over ca. 900 px) og som fane i den faste fanelinje på mobil (afsnit 16). Foldbare bokse og popup-modaler bruges ikke på mobil: de giver lange scroll og skjuler det, eleven leder efter. Casekortet i egen fane ved siden af rollekortet.
- Design: ét kort uden ramme i ramme, ingen overflødige etiketter (fx "Bagsiden"), farver og skrift som resten af spillet.
- Tabeller på mobil: korte overskrifter, enheder i en note under tabellen, bløde orddelinger (`&shy;`) i lange ord.

## 6. Responsivt og tilgængeligt

- Knapper og miniaturer i et gitter med `repeat(auto-fit, minmax(104px, 1fr))` og tekst, der må ombrydes. Faste bredder giver afklippede knapper (set på pitch-fanen).
- Test altid ved ca. 1300, 390 og 320 px bredde. Vandret scroll findes ved at sammenligne `document.documentElement.scrollWidth` med `window.innerWidth`.
- Alt-tekster beskriver det konkrete motiv og er forskellige fra billede til billede. Tæller og statuslinjer skal kunne læses på en lille skærm uden at løbe ud over kanten.
- Kontrast og skriftstørrelse: mindst 16 px brødtekst, knapper der kan ramme med en tommelfinger. Regler for kontrast på mærker står i afsnit 13. Tekst inde i spilintroens scener er skærmgrafik og må være mindre end sidens brødtekst, men aldrig under 12 px (undertekster mindst 13 px). I rådgiverens chat og kort (et værktøj, ikke en artikel) er brødtekst mindst 14 px og sekundær tekst mindst 12 px. Kommunalbudget bruger mindst 12 px til mærker og hjælpetekster på mobil (første udgave brugte 10 til 11,5 px, og det var for småt).

## 7. Billeder og video

- Billeder: bredde højst ca. 1600 px, JPEG, ca. 100 til 300 KB pr. billede. Komprimér i en kopi og gem originalerne i arkivmappen først.
- Poster til video: tag videoens første billede (`ffmpeg -i video.mp4 -frames:v 1 hero-poster.jpg`), så siden ikke blinker ved indlæsning.
- Video: ca. 10 sekunder, uden lyd som standard, gentagelse fra start uden hak. Lad tekst på siden fade ud, når videoens slutlogo kommer.
- Webside og billeder viser virksomheden, **som den er før investeringen**.
- Billed- og videoprompter: engelsk, med dansk sted, én person der går igen (billedet vedhæftes), logo placeret som ønsket, intet læsbart tekststof, som modellen kan stave forkert.
- **Autentiske, fotorealistiske motiver:** beskriv det konkrete faglige miljø i naturligt lys med virkelighedsnære detaljer, fx et byrådsbord med kaffekopper, papirer og bærbare computere i dagslys, en lokal gade med cyklister og en rigtig bybus, en varm samtale mellem to mennesker i et fælleshus. Undgå sci-fi, 3D-render og stockfoto-klichéer.
- **`loading="lazy"` kun til lange lister.** På en forside med få vigtige sektionsbilleder (3 til 4) kan det give tomme eller grå kasser i headless browsere, ved skærmbilleder og ved hurtig scroll. Brug direkte indlæsning med eksplicit `width` og `height` (undgår layoutspring). Lazy er fint til et katalog med mange kort. Fjord Outdoors forside bruger stadig lazy på sine sektionsbilleder.

## 8. Facit-beregner og show

- Parametre i `CFG` øverst; vis forventet værdi og ét udfald, så tilfældighed kan forklares i debriefingen.
- Den samme sandsynlighedsmodel i beregner og show. Test med to eller tre kendte tilfælde og sammenhold med regnearket.
- Scener i show følger spillets rækkefølge. Skjult information vises først i afsløringsscenen.
- Brug samme farver og skrift som papirmaterialerne.

## 9. Arbejdsgang og test

1. **Backup først:** kopiér filen til `_arkiv/<fil>_foer_<ændring>.html` før hver ændring. Slet aldrig. Det gælder også ved gennemgang og små rettelser.
2. **Ændr i små trin**, ét emne ad gangen (pitch-fane, tæller, mobil), og test mellem trinene.
3. **Syntakscheck:** åbn siden eller kør `node --check` på det udtrukne script. En manglende anførselstegn i en skabelonstreng stoppede hele siden én gang.
4. **Automatisk test med Playwright** (eller tilsvarende): åbn siden i 1300, 390 og 320 px, tjek konsolfejl, vandret scroll, indtast en rollekode, skift rolle og kontrollér at tælleren er uændret, tag skærmbilleder og **se dem**. Et fuldt, afprøvet testmønster står i afsnit 21.
5. **Test den nyeste fil.** Åbn med en ny fanebladsadresse eller hård genindlæsning, så en gammel version i cachen ikke narrer.
6. **Test på en rigtig telefon, helst en iPhone.** Playwright med Chromium og en lille skærm efterligner ikke Safari. De fejl, der gjorde Fjord Outdoor frossen på mobilen (afsnit 14), blev opdaget på telefonen. Tjek: tryk på alle menulinks, åbn og luk eventuelle overlays tre gange, tryk Tilbage med et overlay åbent, og afspil introen med lyden på.
7. **Gennemlæs som elev:** er der noget på en offentlig side (også casespilssiden), som røber skjult information, modelsvar eller resultatet af valgene?
8. **Efter ændringer:** tjek tal og roller på tværs (bilag, casekort, facit, show, casespilsside) og ryd op i rester (overskrifter, debriefingsspørgsmål, død kode og styling), når en del er fjernet. Tag skærmbilleder af siden før og efter oprydning og sammenlign dem.

## 10. Sikkerhed og ansvar

- Alt i en statisk side kan læses. Antag det.
- Skift API-nøgle før offentliggørelse, hvis den har stået i en side. Sæt dagsloft på proxy og nøgle.
- Mærk siden som fiktiv og AI-genereret. Skriv ikke rigtige personnavne eller virksomheder, hvor det kan forveksles med virkeligheden.
- Giv eleverne en kort besked om, at spørgsmål til rådgiveren gemmes (hvis de gemmes), og hvor længe.

## 11. Spilintro: opbygning og synkronisering

Introen er en afspiller, ikke en video. Scener, undertekster og lyd styres af ét tal: tiden. Det gør den let at rette (ret en tekst, ikke en filmfil) og lader læreren hoppe rundt.

**Filer:** `casespil.html` (hubben, afsnit 15) med afspilleren indlejret, afspillerfilen `intro.html` (kan også bruges alene til storskærm og som direkte link), `voiceover.mp3` og billeder i `billeder/`. Afspilleren og underteksterne bor i den ene fil. Hubben indlejrer den, fx `<iframe src="intro.html?embed=1" title="Spilintro" allow="fullscreen" allowfullscreen>`, og `?embed=1` skjuler sidehoved og tilbagelink, så kun afspilleren vises. Så findes der ét sæt scener og undertekster, som ikke kan drive fra hinanden (afprøvet i Chromium: parameteren læses i den indlejrede side, og et klik inde i den virker).

I Fjord Outdoor lå afspilleren to steder, i en popup på forsiden og i `intro.html`, med klasser med præfikset `m-` og id'er som `mSc1`, så de ikke stødte ind i sidens egne. Det gav en kopi, der kunne drive, og popup'en er fjernet. Skal afspilleren af en grund bygges ind i flere sider, så læg `SCENES` og `SUBTITLES` i en fælles `intro-data.js` (et almindeligt `<script src>` virker også fra en lokal mappe). Tal og tekster i introen er en del af den fælles kilde (SKILL.md, grundregel 1).

**Lyden er mester.** Når lyden spiller, hentes tiden fra `audio.currentTime`; ellers fra et ur (`requestAnimationFrame`). Så glider tekst og stemme aldrig fra hinanden.

```javascript
// 1. Scener: sekunder, målt på den færdige lydfil. Ingen "dot"-felt, der er ingen fremskridtsprikker.
const SCENES = [
  { id: 'sc1', start: 0,    end: 18.2 },
  { id: 'sc2', start: 18.2, end: 35.0 },
  { id: 'sc3', start: 35.0, end: 53.0 },
  { id: 'sc4', start: 53.0, end: 69.3 },
  { id: 'sc5', start: 69.3, end: 84.0 }
];
// 2. Undertekster: begynd og slut sammen med sætningerne i lydfilen
const SUBTITLES = [
  { start: 0.0, end: 2.5, text: 'Ti millioner kroner.' },
  { start: 2.5, end: 6.5, text: 'Det er puljen, der skal afgøre fremtiden for Fjord Outdoor.' }
  // ...
];
// 3. Én funktion opdaterer hele skærmen ud fra tiden
function updateState(t) {
  currentTime = Math.max(0, Math.min(t, duration()));
  scrubberFill.style.width = (currentTime / duration() * 100) + '%';
  timeCurrent.textContent = formatTime(currentTime);          // m:ss
  SCENES.forEach(function (sc, i) {
    var last = i === SCENES.length - 1;                       // sidste scene bliver stående, når lyden slutter
    var active = currentTime >= sc.start && (currentTime < sc.end || last);
    document.getElementById(sc.id).classList.toggle('active', active);
  });
  var sub = SUBTITLES.find(function (s) { return currentTime >= s.start && currentTime < s.end; });
  subText.textContent = sub ? sub.text : '';
  if (currentTime >= duration()) pause();
}
```

- **Kun aktive scener er synlige** (`.scene.active`). Scener overlapper ikke, og overgangen er en blød fade (ca. 0,6 sek.) på selve scenen, ikke på de enkelte kort inde i den (se afsnit 14 D).
- **Tider findes sådan:** generér lyden først, find sætningernes tider, og sæt derefter scenegrænserne ved en naturlig pause. ElevenLabs kan give tidsstempler sammen med lyden (tjek den aktuelle dokumentation); ellers aflyttes filen, og tiderne justeres i hånden. Rettes teksten og lyden laves om, skal tiderne laves om.
- **Afspilleren:** `seek(t)` kalder `updateState(t)` og sætter `audio.currentTime`. Knapperne -10 og +10 kalder `seek(currentTime - 10)` og `seek(currentTime + 10)`. Tidslinjen er et klik (og gerne træk) på et spor, der omregnes til sekunder. Parameteren `?t=42` hopper til et tidspunkt, hvilket er nyttigt til test og skærmbilleder.
- **Tastatur, når afspilleren har fokus:** mellemrum eller K afspiller og pauser, venstre og højre pil giver -10 og +10, F er fuld skærm.
- **Fuld skærm i en indlejret afspiller:** iframe'en skal have `allow="fullscreen"`. Fuld skærm virker ikke overalt, især ikke for andet end video på iPhone, så vis kun knappen, hvis `document.fullscreenEnabled` er sandt. Fuld skærm i en iframe er ikke afprøvet på telefon.
- **Lyd og iPhone (anbefalet mønster, ikke afprøvet på iPhone i Fjord Outdoor):** Safari på iOS ignorerer `preload`, og `canplaythrough` udløses typisk først efter afspilning er startet. Fjord Outdoor satte `hasVoiceAudio = true` først på det event, og hvis det aldrig kommer, springer koden `audio.play()` over, så introen kører uden stemme. Gør i stedet sådan, og test på en iPhone:

```javascript
var hasAudio = true;                                          // antag lyd, giv kun op hvis filen fejler
function duration() {
  return (hasAudio && isFinite(audio.duration) && audio.duration) ? audio.duration : TOTAL_DURATION;
}
audio.addEventListener('loadedmetadata', function () { timeTotal.textContent = formatTime(duration()); });
audio.addEventListener('error', function () { hasAudio = false; });
function play() {
  isPlaying = true;
  splash.classList.add('hidden');
  if (hasAudio) {
    audio.currentTime = currentTime;
    var p = audio.play();                                     // kaldes direkte fra brugerens klik
    if (p && p.catch) p.catch(function () { hasAudio = false; lastTimestamp = 0; });
  }
  lastTimestamp = 0;
  animTimer = requestAnimationFrame(loop);
}
```

- **Tilgængelighed (anbefalet, ikke med i Fjord Outdoor):** gør tidslinjen til `role="slider"` med `aria-valuemin`, `aria-valuemax` og `aria-valuenow`, så den kan bruges med tastatur og skærmlæser. Bruger siden et overlay, flyttes fokus ind i det ved åbning og tilbage til knappen, der åbnede det, ved lukning.
- **Baggrundsvideo og overlays:** hvis en side med baggrundsvideo åbner et fuldskærmsoverlay med lyd eller video, sættes baggrundsvideoen på pause, så to videoer og lyde ikke kører samtidig, og den startes igen, uanset hvordan overlayet lukkes (kryds, Escape, klik på baggrunden eller Tilbage-knappen). Ligger introen på egen side, er der ingen baggrundsvideo at passe på. Den første udgave i Fjord Outdoor, hvor introen lå i en popup på forsiden, glemte genstarten, og videoen stod frosset, til siden blev genindlæst. Læg derfor genstarten i den ene funktion, som alle lukkeveje kalder, og spring den over ved `prefers-reduced-motion`:

```javascript
// i den fælles lukkefunktion
if (!reduce && v) {
  try {
    var p = v.play();
    if (p && p.catch) p.catch(function () {});   // afvist afspilning må ikke give fejl
  } catch (err) {}
}
```
- **Referér til elementer via variabler.** Dele af Fjord Outdoors deep link-kode brugte `mSplash` uden at have erklæret den. Det virkede kun, fordi browsere gør elementers id til globale navne. Det er skrøbeligt.

## 12. Voiceover med ElevenLabs

- **Tjek manuskriptet mod bilagene, før stemmen indtales.** Voiceover kan ikke rettes uden en ny indtaling, og underteksterne bliver stående som facit. Scenetekster og voiceover må ikke modsige bilagenes regler eller dramatisere ud over dem. Gennemgå hver sætning mod bilag og rollekort. I Fjord Outdoor var disse formuleringer for kraftige eller forkerte: "fuld satsning for overhovedet at virke", "halve løsninger er spildte penge", "overtager markedet", "med det samme", "nuværende succeser" (kun nogle af produkterne var kerneprodukter, i Fjord Outdoor P1 til P3) og "hvert eneste fravalg koster dyrt". Bilagenes regel var mere nuanceret: en pilotgrænse giver en chance, en fuldgrænse en større chance, og et kerneprodukt uden pilotbeløb mister yderligere markedsandel. Skriv, hvad reglerne siger, i stedet for at forstærke dem.
- **Skriv til øret.** Korte sætninger, ét budskab ad gangen, tal som ord ("Ti millioner kroner", ikke "10 mio. kr."), ingen tankestreger, parenteser eller forkortelser. Den samme tekst bliver til undertekster, så skriv den, som den skal stå på skærmen.
- **Længde:** 60 til 90 sekunder. Fjord Outdoor: 211 ord på 84 sekunder, altså ca. 150 ord i minuttet med pauser. Planlæg ca. 200 til 220 ord, og skær ned frem for at skrue op for tempoet.
- **Opdel i 4 til 5 scener** efter fortællingens bue: situationen, magtkampen, dilemmaet, faserne, finalen. Hver scene får sin egen stemning.
- **Stemningsmærker i firkantede klammer** foran den sætning, de gælder, fx `[thoughtful]`, `[intense]`, `[whispering]` og `[resolute]`. Mærkerne er hints til modellen og ikke kommandoer: lyt hver scene igennem, brug højst ét eller to pr. scene, og skift mærke, hvis det lyder påtaget.
- **Dramatiske pauser.** Komma og punktum giver for korte pauser. Brug `...`, `[pause]` eller et linjeskift foran de vigtige pointer:

```text
[intense] Ti millioner kroner... [pause]
Det er puljen, der skal afgøre fremtiden.
```

- **Mærkerne og pauserne er ikke undertekster.** Fjern dem fra den tekst, der vises på skærmen, og hold underteksterne i en separat liste (`SUBTITLES`).
- **Gem hver version** af lydfilen og den tekst, der gav den, i arkivmappen. Samme tekst kan give lidt forskellig lyd fra gang til gang, så en lyd, man kan lide, skal gemmes.
- **Tjek udtalen** af virksomhedsnavn, fagord og tal ved at lytte. Ret ved at skrive ordet, som det lyder, i lydteksten og beholde den rigtige stavning i underteksten.

## 13. Grafisk stil: anti-AI og kontrast

**Det generiske AI-look at undgå:** neonfarver, gradient-bokse, KPI-felter, ingen kan aflæse, ikoner uden mening og kort med tyk farvet kant i venstre side som fast kendetegn. Tyk venstrekant i en advarselsfarve er det værste, men mønstret virker lige så maskinelt i en accentfarve. Fjord Outdoors egen forside bruger en rav venstrekant på mange kort og bør ikke kopieres.

**Det, der skal ligne virksomheden:**

- Typografi: Source Serif 4 til introens scenetitler og indledende tekst, Source Sans 3 til overskrifter, data og knapper. Kraftig sans er fint til sidens overskrifter; pointen er rolig, redaktionel typografi og ikke et bestemt skrifttrick.
- Kort: rent hvide kort med 1 px kant (`#DDD5C4`) og en diskret skygge, oven på dæmpede fotobaggrunde.
- Billeder: autentiske og tilpasset branchen. Et bestyrelseslokale for en outdoorvirksomhed har træ, råt lys, overtøj og kaffekopper, ikke glasskærme og kold tech-stemning. Billedet skal kunne ses: i Fjord Outdoors intro ligger et mørkt farvelag (ca. 76 til 90 % dækkende) oven på et billede med 32 % dækning, så fotografiet næsten forsvinder. Vælg enten billedet og gør det synligt (lavere farvelag), eller drop det.

**Vælg designsystem efter spillets verden.** Sæt dig ind i, hvordan emnet ser ud i virkeligheden, og vælg få navngivne tokens derefter. Fjord Outdoor er outdoor-corporate; Kommunalbudget er civic editorial. Den samme metode gav to helt forskellige sider:

| | Fjord Outdoor | Kommunalbudget |
|---|---|---|
| Verden | Outdoor, fjord, råt træ, overtøj | Rådhus, forvaltning, avis, byrum |
| Mørk grundfarve | Fjordblå `#12344D` | Mørk petrol `--deep` `#102F2B`, `--green` `#173E38` |
| Baggrund | Kalk og sand | Varmt papir `--paper` `#F5F2EB`, hvid `--white` `#FFFEFB` |
| Støttefarver | Skovgrøn, rav | Salvie `--sage` `#E6ECDF`, kobber `--copper` `#A2492A`, guld `--gold` `#E7BB7A` |
| Tekst | Sort-blå | `--ink` `#203631`, `--muted` `#5B6860` |
| Typografi | Sans til de fleste overskrifter, serif til scener | Serif (Source Serif 4) til store overskrifter, sans (Source Sans 3) til brug |
| Billeder | Skov, kyst, butik | Byråd, byrum, omsorg, dagslys |

Kommunalbudgets kontrast er regnet efter: brødtekst på papir 11,5 til 1, `--muted` på papir 5,2 til 1, kobber på papir 5,3 til 1, guld på mørk petrol 8,1 til 1, hvid på grøn (rollekortets header) 11,7 til 1, aktiv fane 11,7 til 1 og inaktiv fane på salvie 4,85 til 1. Alt er over 4,5 til 1.

**Faldgruben med CSS-variabler.** En variabel, der ikke er defineret, giver ingen fejl: browseren bruger bare den nedarvede værdi. Så kan en badge få hvid tekst på lys sand, uden at nogen ser det i koden. I Fjord Outdoors `index.html` bruges `var(--mute)` til tidsvisningen, men siden definerer kun `--sten`. Regler:

1. Rolle- og statusmærker får **fast baggrund og eksplicit tekstfarve** som rå værdier (ikke variabler).
2. Tjek, at hver variabel, du bruger, står i `:root` (søg efter `var(--` og sammenhold med definitionerne).
3. **Regn kontrasten efter.** Husk også, at 12 px fed tekst ikke tæller som "stor tekst".

| Mærke | Baggrund | Tekst | Kontrast | Niveau |
|---|---|---|---|---|
| Bestyrelsen, magt | `#12344D` | `#FFFFFF`, vægt 800 | 12,9 til 1 | AAA |
| Projektteams, udfordrere | `#2F5D50` | `#FFFFFF`, vægt 800 | 7,5 til 1 | AAA |
| Korridorforhandlinger, dilemmaer | `#D9822B` | `#12344D`, vægt 800 | 4,4 til 1 | kun stor tekst (AA) |

Rav med marineblå tekst består ikke 4,5 til 1 til små mærker. Brug mærket på stor, fed tekst (mindst 18,7 px fed), eller gør teksten mørkere (`#0C2437` giver 5,4 til 1, sort giver 7,2 til 1). Til små tekster oven på marineblå flader (fx den lille overskrift over en scenetitel) er `#D9822B` også kun 4,4 til 1; brug en lysere rav som `#F0A04B` (6,1 til 1). Advarselsfarverne `#8A4E0E` og `#A8322B` på hvid ligger på ca. 6,6 til 1: godkendt til tekst, men ikke AAA.

```javascript
// Kontrast mellem to farver, fx contrast('#12344D', '#FFFFFF')
function contrast(a, b) {
  function lum(h) {
    var c = [1, 3, 5].map(function (i) { return parseInt(h.slice(i, i + 2), 16) / 255; })
      .map(function (v) { return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }
  var l1 = lum(a), l2 = lum(b);
  return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
}
```

## 14. Mobil-optimering og WebKit-fejlretning

Disse fejl fik Fjord Outdoors forside til at virke frossen på telefonen. Ingen af dem viser sig tydeligt på en computer. Mønstrene gælder enhver mobilmenu og ethvert fuldskærmslag. Fjord Outdoors intro lå oprindeligt i en popup på forsiden og ligger nu på en egen side (afsnit 15), men menuen og eventuelle andre overlays bruger stadig A til C.

### A. Den usynlige modal-fælde

**Problem:** et fuldskærmslag med `position: fixed; inset: 0; z-index: 1000; backdrop-filter: blur(8px)`, der kun skjules med `opacity: 0; visibility: hidden`, ligger stadig i lagene. Især Safari på iOS holder så et usynligt lag over hele skærmen, der kan opfange tryk og belaste grafikken, og siden føles frossen.

**Løsning:** fjern laget helt fra layoutet, når det er lukket, og tilføj først blurfilteret, når det er åbent.

```css
.intro-modal-backdrop {
  position: fixed; inset: 0; z-index: 1000;
  display: none;                 /* helt væk fra layoutet, når lukket */
  pointer-events: none;
}
.intro-modal-backdrop.open {
  display: flex;
  pointer-events: auto;
  backdrop-filter: blur(8px);    /* kun når laget er åbent */
  -webkit-backdrop-filter: blur(8px);
}
```

Prisen er, at en fade-ud ikke virker (en overgang kører ikke hen over `display`). Det er et rimeligt bytte. Brug `!important` kun, hvis en anden regel overstyrer `display`.

### B. Synkron menulukning afbryder link-klik

**Problem:** i en hamburgermenu på mobilen sætter `links.classList.remove('open')` i linkets klik-handler menuen til `display: none` i samme øjeblik. Safari kan nå at fjerne linket fra layoutet, før navigationen er startet, og klikket går tabt.

**Løsning:** vent 100 til 150 ms, før menuen lukkes. Links, der selv åbner popup'en og kalder `preventDefault()`, kan lukke straks, fordi der ikke er nogen navigation at afbryde.

```javascript
links.addEventListener('click', function (e) {
  var a = e.target.closest('a');
  if (!a) return;
  if (a.id === 'openIntroNav') {              // åbner popup, ingen navigation
    links.classList.remove('open');
    menu.setAttribute('aria-expanded', 'false');
    return;
  }
  setTimeout(function () {                    // lad browseren starte navigationen først
    links.classList.remove('open');
    menu.setAttribute('aria-expanded', 'false');
  }, 120);
});
```

### C. Tilbage-knappen og `#intro`

**Problem:** popup'en åbnes med `preventDefault()` på linket, så adressen får aldrig noget `#intro`, og der oprettes ingen historikpost. Telefonens Tilbage-knap kan derfor ikke lukke popup'en: den forlader hele siden. (Testet i Chromium med mobilvindue: åbn popup, tryk Tilbage, og siden blev erstattet af den forrige adresse.) En `popstate`-lytter alene hjælper ikke, for den udløses kun, når der er en historikpost at gå tilbage til.

**Løsning:** opret selv en historikpost, når popup'en åbnes, og fjern den igen ved lukning. Husk, om du oprettede den, så et direkte link til `index.html#intro` ikke sender eleven væk, når popup'en lukkes.

```javascript
var introPushed = false;

function openModal(e) {
  if (e && e.preventDefault) e.preventDefault();
  introModal.classList.add('open');
  document.body.style.overflow = 'hidden';
  if (location.hash !== '#intro') {
    try { history.pushState({ intro: 1 }, '', '#intro'); introPushed = true; } catch (err) {}
  }
  // ... pause baggrundsvideo, updateState(currentTime)
}

function closeModal(fromPopstate) {
  introModal.classList.remove('open');
  document.body.style.overflow = '';          // altid frigiv scroll
  pause();
  if (fromPopstate === true) { introPushed = false; return; }
  if (introPushed) {                          // kryds, Escape eller klik på baggrunden
    introPushed = false;
    try { history.back(); } catch (err) {}
  } else if (location.hash === '#intro') {    // åbnet via direkte link: ryd adressen uden at forlade siden
    try { history.replaceState(null, '', location.pathname + location.search); } catch (err) {}
  }
}

window.addEventListener('popstate', function () {   // telefonens Tilbage-knap
  if (introModal.classList.contains('open')) closeModal(true);
});
// Alle andre lukkeveje kalder closeModal() uden argument. Knappen skal pakkes ind:
closeBtn.addEventListener('click', function () { closeModal(); });
```

Afprøvet i Chromium (mobilvindue): Tilbage lukker popup'en uden at forlade siden, kryds og Escape fjerner `#intro` igen, tre åbn og luk i træk efterlader ren adresse og frigivet scroll, og et direkte link med `#intro` kan lukkes uden at forlade siden. Siden åbner kun popup'en ved indlæsning, hvis adressen indeholder `#intro` (eller `?intro=1`), så en genindlæsning efter lukning åbner den ikke igen.

### D0. Gitter og menuer ved 320 px

Ud over introen er der to klassiske årsager til, at en side bliver bredere end skærmen:

- **Gitter med fast minimum.** `grid-template-columns: repeat(auto-fit, minmax(310px, 1fr))` giver en kolonne på mindst 310 px, og med 16 px sidemargen på hver side bliver siden 326 px bred på en 320 px skærm. Brug `minmax(min(100%, 310px), 1fr)` eller ren `1fr` på mobil. Afprøvet: 326 px mod 320 px.
- **Vandrette menuer.** En række links (`.nav-links`) med `display: flex` og mange punkter blev 501 px bred. Giv rækken `overflow-x: auto; white-space: nowrap;` (afprøvet: 320 px), eller fold den i en menu.

### D. Layoutregler til introen på mobil (højst 768 px)

- **Lodret stabling i kortoverskrifter:** overskrift og mærke må aldrig tvinges ud på samme linje. Sæt `flex-direction: column; align-items: flex-start; gap: 4px;` på rækken (fx `.m-role-top`), så et mærke aldrig klippes af mod skærmkanten.
- **Faser i 2 gange 2:** `grid-template-columns: repeat(2, 1fr); gap: 7px;` giver balance uden at scenen skal rulle.
- **Scenen må rulle indvendigt** (`overflow-y: auto; -webkit-overflow-scrolling: touch;`) med nok luft nederst (`padding-bottom` ca. 64 px) til undertekstbjælken.
- **Ingen forsinkelser på enkeltkort.** Undgå `transition-delay` og `opacity: 0; transform: translateY(12px)` på kort inde i en scene, der allerede fader ind. Det giver flimmer og hak på langsommere telefoner. Lad hele scenen fade, ikke hvert kort.
- **Hold animationerne lette.** Fuldskærmsbilleder med langsom zoom (`transform: scale` over 12 sek.) og filtre (`brightness`, `blur`) er dyre på mobil. Brug højst ét filter pr. lag, og undgå `backdrop-filter` på lag, der ligger oven på video.
- **Højde på iPhone:** `max-height: 100vh` regner Safaris adresselinje med og kan skubbe afspillerens knapper ud af skærmen. Skriv `max-height: 100vh; max-height: 100dvh;` (den sidste vinder, hvor den findes).
- **Tekststørrelse:** se afsnit 6. Minimum 12 px i scenerne og 13 px til undertekster.

## 15. Casespilssiden (hub)

Hubben er den ene side, eleverne åbner for at forstå spillet. Den er offentlig og følger derfor de samme regler som websiden (SKILL.md, grundregel 2).

- **Fil:** `casespil.html` ved siden af `index.html`. Én fil med stil og script indeni, billeder i `billeder/`.
- **Opbygning oppefra og ned:** (1) sidehoved med logo og ét link tilbage til virksomhedens forside, ingen sektionsmenu, så der heller ikke er brug for en hamburgermenu; (2) kort introtekst; (3) den indlejrede spilintro (afsnit 11); (4) knap til AI-rådgiveren; (5) spilfaserne, hvor eleverne handler; (6) roller og regler.
- **Forsiden:** ét menupunkt, fx "Casespillet", i menuens almindelige farve og ikke i accentfarven, og en knap i heroen til hubben. Intet link til rådgiveren og ingen popup. Fjern menupunkter og footerlinks, der peger på rådgiveren.
- **Gamle links:** kode i forsiden sender `#intro` og `?intro=1` videre til hubben. Brug `location.replace`, så Tilbage-knappen ikke havner i en løkke.

```html
<script>
  // øverst på forsiden, før indholdet: gamle intro-links sendes videre til casespilssiden
  if (location.hash === '#intro' || new URLSearchParams(location.search).get('intro') === '1') {
    location.replace('casespil.html');
  }
</script>
```

  Afprøvet i Chromium: `index.html#intro` og `index.html?intro=1` ender på `casespil.html`, forsiden uden hash vises uændret, og Tilbage efter omdirigeringen går til den side, eleven kom fra.
- **Data fra kilden:** roller (titel, stemmetal, særlig beføjelse), beløb og regler hentes fra datasættet, rollekortene og bilagene. Opfind ikke roller, titler eller tal. Sammenhold siden med rollekortene hver gang noget er ændret.
- **Aldrig på hubben:** modelplaceringer (fx BCG-felter som "malkeko", "stjerne", "spørgsmålstegn"), strategimodel ved projekterne (fx Ansoff), beskrivelser af rollernes holdninger og alt andet, eleverne selv skal finde ud af. Roller vises kun med titel, stemmetal og særlig beføjelse.
- **Regler, der skal med:** stemmeregel og antal stemmer der kræves, veto, standardplan hvis der ikke findes flertal, særlige beslutninger (Fjord Outdoor: fritidstøjet) og at det ubrugte er reserve. Brug bilagenes formuleringer.
- **Faser:** kun spilfaserne, med samme navne og numre som på rollekort og i lærerguide.
- **Oprydning, når et format udgår:** fjern HTML, CSS og script helt (søg efter rest-id'er og klasser, fx `intro-modal` og `openIntro`), og sammenlign skærmbilleder af forsiden ved ca. 1300, 390 og 320 px før og efter. Forsiden skal se ens ud, bortset fra det, der med vilje er ændret.

## 16. Rådgiverens grænseflade på computer og mobil

Rådgiveren er et arbejdsbord, ikke en chatboks med et kort ved siden af. Alt eleven skal bruge under forhandlingen ligger i samme side.

**Computer (tre kolonner, fx `200px 1fr 320px`):**

- **Venstre kolonne (skinne):** spilfaserne som knapper (kun elevfaserne), en spørgsmålsmåler ("7 af 10 tilbage" med små prikker), og et lille kort om spillet (pulje, stemmer, hvad der sker uden aftale).
- **Midten:** chatten. Øverst rolletitel, stemmebadge og fasevælger med fasens opgave som hjælpetekst. Så tråden med bobler (rådgiveren venstre, eleven højre, en "tænker"-indikator), og nederst skrivefeltet (Enter sender, Shift+Enter giver ny linje, højst ca. 1200 tegn), en statuslinje og en diskret note ("Gemmes lokalt i 2 timer").
- **Højre kolonne:** tre faner, Rollekort, Startkrav og Fælles casekort.

**Mobil (højst 900 px): faner i stedet for kolonner.**

- Skinnen skjules. Øverst kommer en fast fanelinje (`position: sticky; top: 0`) med fire faner: Rådgiver, Rollekort, Startkrav, Casekort. Fire lige store kolonner, hver mindst 44 px høj, tekst 13 px fed, aktiv fane med hvid baggrund, 3 px understregning i accentfarven og kraftigere skrift. Faneknapperne følger sidens farver og skrift. Hold 44 px også på de smalleste skærme (under 360 px kan teksten krympe til 12 px, men ikke knappen).
- Containeren har et attribut (`data-active-view="chat"` eller `"kort"`, `"krav"`, `"case"`), og CSS viser enten chatten eller informationspanelet. Panelets egne faner skjules på mobil, fordi topfanerne styrer. Så skifter eleven på et tryk mellem sparring og faktatjek uden at scrolle eller åbne en modal.
- **Kompakt header:** rolletitel i serif (ca. 17 px), badge og fasevælger (lille, ca. 28 px høj, uden label) på én til to linjer, og hjælpeteksten under. Chathistorikken får resten af højden. Hold hjælpetekst og badge på mindst 12 px.
- **Sekundære handlinger bliver diskrete.** "Skift rolle" bruges sjældent under en lektion og må ikke fylde i toppen. På computer ligger den i skinnen, og på mobil som et lille understreget tekstlink i bunden ved skrivefeltet (Kommunalbudget: klassen `.subtle-link`).

**Lås arbejdsbordet til skærmens højde på computer (over 900 px).** Det er en klassisk CSS-fælde at give et tre-kolonnet arbejdsbord kun `min-height: calc(100vh - ...)`. Uden en fast højde bliver gitterets række lige så høj som den højeste kolonne, så et langt rollekort i højre kolonne strækker hele arbejdsbordet. Så skubbes alt, der står nederst, ned: spørgsmålstælleren i venstre kolonne (den har `margin-top: auto`) og skrivefeltet i midten havner langt under skærmkanten. Målt med et rollekort på 60 afsnit ved 1300 gange 800 px: arbejdsbordet blev 4589 px højt, skrivefeltet lå 4595 px nede, og siden fik 4046 px sidescroll. Med låsen nedenfor var arbejdsbordet 665 px, skrivefeltet lå i 735 px, der var ingen sidescroll, og højre panel rullede selv.

```css
:root { --chrome: 135px; }   /* højden af sidehoved og navigation over arbejdsbordet: mål den, gæt den ikke */
.dshell { display: grid; grid-template-columns: 230px minmax(0, 1fr) 360px; grid-template-areas: "rail conv panel"; }
@media (min-width: 901px) {
  .dshell {
    height: calc(100vh - var(--chrome));      /* fast højde, ikke kun min-height */
    max-height: calc(100vh - var(--chrome));
    min-height: 0;
    overflow: hidden;                          /* intet strækker containeren */
  }
  .rail, .conv, .panel2 { height: 100%; min-height: 0; }   /* min-height: 0 lader flex- og gitterbørn skrumpe */
  .rail  { overflow-y: auto; }                 /* skinnen ruller selv, hvis den bliver for høj */
  .conv  { overflow: hidden; }                 /* tråden i midten ruller selv: .thread { flex: 1; overflow-y: auto; } */
  .panel2 { overflow: hidden; }                /* panelets krop ruller selv: .pbody { overflow-y: auto; } */
}
```

- **Tre regler, der hører sammen:** (1) arbejdsbordet har fast `height` og `max-height` mod viewporten og `overflow: hidden`; (2) hver kolonne har `height: 100%` og `min-height: 0`; (3) det, der kan vokse (tråden, panelets krop, skinnen), har sit eget `overflow-y: auto`. Mangler én af dem, glider layoutet.
- **Mål sidehovedets højde i stedet for at gætte den.** I Kommunalbudget er tallet `88px + 47px` skrevet direkte ind i CSS. Brug en variabel, og kontrollér den i testen (afsnit 21), så et nyt sidehoved ikke stille ødelægger låsen.
- **Fælden med en mellemliggende blok.** `flex: 1; min-height: 0` på `.dshell` virker kun, hvis forælderen er en flex-container. I Fjord Outdoors lærer-cockpit lå `.dshell` i en `div#cockpitView` med `display: block` under en `body` i flex. Så havde `flex: 1` ingen effekt, arbejdsbordet voksede til 1795 px inde i en body på 800 px med `overflow: hidden`, og skrivefeltet lå 1824 px nede, uden mulighed for at nå det. Rettelsen (afprøvet: skrivefeltet i 764 af 800 px uden sidescroll):

```css
#cockpitView:not([hidden]) { display: flex; flex-direction: column; flex: 1; min-height: 0; }
.dshell { flex: 1; min-height: 0; grid-template-rows: minmax(0, 1fr); overflow: hidden; }   /* rækken må ikke vokse med indholdet */
.rail, .conv, .panel2 { height: 100%; min-height: 0; }
.rail, .pbody, .thread { overflow-y: auto; }
.conv, .panel2 { overflow: hidden; }
```

- **Arbejdsrum-klassen:** sæt en klasse på `body` (fx `in-workspace`), når arbejdsbordet vises. Den låser `body` til skærmens højde (`height: 100vh; overflow: hidden`, `display: flex; flex-direction: column`) og skjuler footeren, så ingen side ruller bagved. Fjern klassen igen, når man låser eller forlader arbejdsbordet.
- **På mobil gælder låsen ikke.** Under 900 px stables kolonnerne (se ovenfor), og siden må gerne rulle. Derfor står reglerne i en `min-width: 901px`-forespørgsel.

**Rollekortet i siden (højre panel eller fanen Rollekort):**

- Header med tag ("Interessegruppe"), titel og "N stemmer · Rådgiverkode: 2481".
- Mål som fremhævet kort; baggrund og holdning; værdier; argumenter; dilemmaer; **skjult information i en tydelig boks** ("kun jeres gruppe"); tip; og en foldbar faseguide.
- Rollens data er dekrypteret og betroet, men tekst, som eleven selv skriver (chatten, byrådets navn), indsættes altid med `textContent`.

**Fanen Startkrav:** kryds af højst tre af fire krav (gemmes i rollens session), med en tekst om, at markeringen kun er til gruppens egen forberedelse og kan ændres under forhandlingen. Markeringen læses aldrig af budgetværktøjet.

## 17. Budget- og beslutningsværktøj

Elevernes eget værktøj til at føre en fælles plan. Det er adskilt fra lærerens facit-beregner (afsnit 8), som bruges, når der er tilfældighed eller skjulte parametre.

**Filer:** `spildata.js` (det offentlige datasæt `window.CASE`), `budgetlogik.js` (ren logik), `budget.js` (siden) og `budget.html`.

**Datasættet `CASE`** er den ene kilde og bruges af casespilssiden, rådgiverens fælles casekort, budgetværktøjet, introen og opsamlingen. Det rummer: titel, sted og år, `budget` (puljen), `totalStemmer`, `flertal`, faser (`nr`, `navn`, `handling`), `regler` (tekstlinjer, som siderne viser), `initiativer` (`id`, `titel`, `pris`, `beskrivelse`, `omraade`, `mindreIndsats`), `intro` (scenetekster), `roller` (`id`, `titel`, `stemmer`) og en note om, at alt er fiktivt. Rollernes hemmeligheder ligger **ikke** her, men i de krypterede roller (afsnit 2).

**Logikken** ligger i en ren fil uden DOM, så den kan bruges i siden, i opsamlingen og i tests under Node (`module.exports`). Den læsbare udgave nedenfor giver de samme resultater som Kommunalbudgets i 4000 af 4000 tilfældige tilstande (`totals`, `errors`, `outcome` og `normalize`):

```javascript
// budgetlogik.js: ren logik uden DOM, så den kan bruges i browseren, i opsamlingen og i tests under Node
(function (g) {
  const D = g.CASE, VOTES = ['ja', 'nej', 'blankt'];
  function blank() {
    return { kind: 'kommunalbudget', version: 1, council: '', finalized: false, votes: {},
             amounts: Object.fromEntries(D.initiativer.map(i => [i.id, 0])) };
  }
  function totals(s) {
    const used = D.initiativer.reduce((sum, i) => sum + Number(s.amounts[i.id] || 0), 0);
    const yes = D.roller.reduce((sum, r) => sum + (s.votes[r.id] === 'ja' ? r.stemmer : 0), 0);
    return { used, reserve: D.budget - used, yes, complete: D.roller.every(r => VOTES.includes(s.votes[r.id])) };
  }
  function errors(s) {                                    // tekster til eleven, aldrig kast af fejl her
    const out = [];
    for (const i of D.initiativer) {
      const a = s.amounts[i.id];
      if (!Number.isInteger(a) || a < 0 || a > i.pris) out.push(i.titel + ': brug et helt beløb fra 0 til ' + i.pris + '.');
    }
    if (totals(s).used > D.budget) out.push('Planen overskrider puljen på ' + D.budget + ' mio. kr.');
    return out;
  }
  function normalize(v) {                                 // al indlæsning (fil, kode, gemt udkast) går gennem denne
    if (!v || v.kind !== 'kommunalbudget' || v.version !== 1) throw Error('Filen er ikke fra dette casespil.');
    if (typeof v.council !== 'string') throw Error('Byrådsnavnet mangler.');
    const s = blank(); s.council = v.council.slice(0, 60);
    for (const r of D.roller) if (v.votes && v.votes[r.id] !== undefined) {
      if (!VOTES.includes(v.votes[r.id])) throw Error('Ugyldige stemmer.');
      s.votes[r.id] = v.votes[r.id];
    }
    for (const i of D.initiativer) {
      const a = (v.amounts && v.amounts[i.id]) ?? 0;
      if (typeof a !== 'number' || !Number.isInteger(a) || a < 0 || a > i.pris) throw Error('Ugyldig bevilling.');
      s.amounts[i.id] = a;
    }
    s.finalized = v.finalized === true;
    if (s.finalized && (errors(s).length || !totals(s).complete)) throw Error('Beslutningen er ufuldstændig.');
    return s;
  }
  function outcome(s) {                                   // uden flertal ved afslutningen: ingen bevillinger, hele puljen i reserve
    const t = totals(s), valid = !errors(s).length && t.complete;
    const adopted = s.finalized && valid && t.yes >= D.flertal;
    return { adopted, finalized: s.finalized && valid, used: adopted ? t.used : 0, reserve: adopted ? t.reserve : D.budget, yes: t.yes };
  }
  g.BudgetLogic = { blank, totals, errors, normalize, outcome };
  if (typeof module !== 'undefined') module.exports = g.BudgetLogic;
})(typeof window === 'undefined' ? globalThis : window);
```

**Sådan bruges den i siden:**

- **Live validering.** Efter hvert tastetryk vises summen, reserven (`puljen minus bevillinger`, rød ved overforbrug), en statusbar og fejlteksterne. "Afslut" er deaktiveret, så længe der er fejl, eller en rolle ikke har svaret.
- **Delvis bevilling.** Eleven må give hele beløbet, et mindre beløb eller 0, men aldrig mere end fuld pris. Ved delvis bevilling viser værktøjet "Delvis bevilling · 50 % af det fulde beløb" og initiativets `mindreIndsats` ("Ved en delvis bevilling: ... Forklar jeres valg mundtligt. Andelen af beløbet er ikke et mål for effekten."). En halv bevilling lover ikke halv effekt, og eleverne skal beskrive, hvem forsøget omfatter.
- **Fælles initiativer tælles kun én gang** (fx flere busser og billigere billetter er to forskellige, fælles initiativer). Skriv det i initiativets beskrivelse og i reglerne.
- **Afstemning pr. rolle** (ja, nej, blankt). Blankt tæller ikke som ja. Alle roller skal svare. Flertallet beregnes af rollernes vægte (`yes >= flertal`).
- **Ændring låser op igen.** Enhver ændring af et beløb sætter `finalized = false`, nulstiller afstemningen (også i felterne) og skjuler resultatkoden. Det forhindrer en kode, der ikke svarer til planen.
- **Uden flertal ved afslutningen:** ingen nye bevillinger, hele puljen er reserve. Skriv resultatet som en fuld sætning, og pas på dobbelt punktum, når et beløb formateres med "kr." og står sidst i en sætning (Kommunalbudgets første udgave viste "kr..").
- **Gem, hent og udskriv.** Tilstanden gemmes i browseren under en versioneret nøgle (`kommunalbudget-plan-v1`) og tjekkes med `normalize` ved indlæsning. Udkast kan hentes som fil og åbnes igen (højst 200 KB, samme `normalize`). "Ny plan" beder om bekræftelse. Et print-stylesheet skjuler menu og knapper.
- **Gem aldrig tekst, der kan lække.** Tilstanden indeholder bordets navn, beløb og stemmer, ikke startkrav.

**Kalibrér spillet, før det bygges:** Kommunalbudget har 100 mio. kr. mod 335 mio. kr. i unikke ønsker (ca. 3,4 gange), vægtene 3, 3, 2, 2, 2 (i alt 12) og flertal 7. Så kan ingen to roller vinde alene, og 15 af 31 mulige koalitioner vinder. Tjek tallene i en test (afsnit 21).

## 18. Resultatkoder

Sådan afleverer bordene deres aftale til lærerens skærm uden login eller server: en kort kode, der kan læses op, skrives af eller sendes i en besked.

**Format (Kommunalbudget, version 2):** præfiks og version, så rummer koden: version (3 bit), bordets nummer (8 bit), et beløb pr. initiativ (6 bit hver, 0 til 63) og én stemme pr. rolle (2 bit: 1 ja, 2 nej, 3 blankt). Til sidst en kontrolsum (CRC-16/CCITT, 2 byte). Det hele skrives som base32 med et alfabet uden I, L, O og U og deles i grupper á 5 tegn, fx `KB2-81T00-M0S00-00000-00000-0000N-M00HT-R`. Koden indeholder **hverken startkrav, tekster, navne eller andet hemmeligt**, så den kan vises på storskærm og sendes frit.

**Regler:**

- Bit-bredden skal rumme den højeste pris. 6 bit rummer 63; er en pris højere, udvides `AMOUNT_BITS`, og koden får nyt præfiks og ny version. En test skal fange det.
- Afkodningen er **tolerant over for indtastning** (små bogstaver, mellemrum og bindestreger, O som 0, I og L som 1) og **streng over for indhold** (forkert præfiks, forkert længde, ukendt tegn, forkert kontrolsum, manglende stemme, ugyldig bevilling). Til sidst går den afkodede tilstand gennem samme `normalize` som filer.
- Et nyt spil får nyt præfiks. Gamle versioner kan stadig afkodes, hvis det er nødvendigt (Kommunalbudget læser også version 1).
- Kontrolsummen er en tastefejlsbeskyttelse, ikke sikkerhed: koden kan genskabes af en, der kender formatet.

Den læsbare udgave nedenfor giver **præcis samme kode som Kommunalbudgets** i 3000 af 3000 tilfældige planer, afkoder deres koder, og afviser alle 961 koder, hvor ét tegn er ændret:

```javascript
// resultatkode.js: kompakt kode med kontrolsum. Indeholder kun tal og stemmer, aldrig tekst eller startkrav.
(function (g) {
  const PREFIX = 'KB2', VERSION = 2;                      // nyt præfiks og ny version pr. spil
  const ALPHABET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ';    // 32 tegn uden I, L, O og U
  const AMOUNT_BITS = 6;                                  // rummer 0 til 63: skal kunne rumme den højeste pris
  const VOTE = { ja: 1, nej: 2, blankt: 3 }, VOTE_NAME = { 1: 'ja', 2: 'nej', 3: 'blankt' };

  function crc16(bytes) {                                 // CRC-16/CCITT (polynomium 0x1021)
    let c = 0xFFFF;
    for (const b of bytes) {
      c ^= b << 8;
      for (let n = 0; n < 8; n++) c = (c & 0x8000) ? ((c << 1) ^ 0x1021) & 0xFFFF : (c << 1) & 0xFFFF;
    }
    return c;
  }
  function writer() {                                     // skriver tal som bit, mest betydende først
    const bytes = []; let cur = 0, n = 0;
    return {
      put(value, width) {
        for (let j = width - 1; j >= 0; j--) { cur = (cur << 1) | ((value >>> j) & 1); if (++n === 8) { bytes.push(cur); cur = 0; n = 0; } }
      },
      finish() { if (n) bytes.push(cur << (8 - n)); return bytes; }
    };
  }
  function reader(bytes) {
    let pos = 0;
    return { get(width) { let v = 0; for (let j = 0; j < width; j++, pos++) v = (v << 1) | ((bytes[pos >> 3] >>> (7 - (pos & 7))) & 1); return v; } };
  }
  function toBase32(bytes) {
    let bits = 0, v = 0, out = '';
    for (const b of bytes) { v = (v << 8) | b; bits += 8; while (bits >= 5) { bits -= 5; out += ALPHABET[(v >>> bits) & 31]; } }
    if (bits) out += ALPHABET[(v << (5 - bits)) & 31];
    return out;
  }
  function fromBase32(text) {
    let bits = 0, v = 0; const out = [];
    for (const ch of text) {
      const k = ALPHABET.indexOf(ch); if (k < 0) throw Error('Koden indeholder et ukendt tegn.');
      v = (v << 5) | k; bits += 5; while (bits >= 8) { bits -= 8; out.push((v >>> bits) & 255); }
    }
    if (bits && (v & ((1 << bits) - 1))) throw Error('Kodens slutning er ugyldig.');
    return out;
  }

  function encode(state) {                                // state kommer fra budgetlogikken og skal være afsluttet
    const L = g.BudgetLogic, C = g.CASE;
    if (!state.finalized || L.errors(state).length || !L.totals(state).complete) throw Error('Afslut beslutningen først.');
    const w = writer(), m = state.council.match(/\d+/), nr = m ? Number(m[0]) : 0;
    w.put(VERSION, 3);
    w.put(nr <= 255 ? nr : 0, 8);                         // kun bordets nummer, aldrig et navn
    for (const i of C.initiativer) w.put(state.amounts[i.id], AMOUNT_BITS);
    for (const r of C.roller) w.put(VOTE[state.votes[r.id]], 2);
    const bytes = w.finish(), c = crc16(bytes);
    bytes.push(c >>> 8, c & 255);
    return PREFIX + '-' + toBase32(bytes).match(/.{1,5}/g).join('-');
  }

  function decode(code) {                                 // tolerant over for indtastning, streng over for indhold
    let s = code.toUpperCase().trim().replace(/[\s-]/g, '');
    if (!s.startsWith(PREFIX)) throw Error('Resultatkoden skal begynde med ' + PREFIX + '.');
    s = s.slice(PREFIX.length).replace(/O/g, '0').replace(/[IL]/g, '1');
    const C = g.CASE, bitCount = 3 + 8 + C.initiativer.length * AMOUNT_BITS + C.roller.length * 2;
    const expected = Math.ceil((Math.ceil(bitCount / 8) + 2) * 8 / 5);
    if (s.length !== expected) throw Error('Resultatkoden har forkert længde.');
    const bytes = fromBase32(s), got = (bytes.at(-2) << 8) | bytes.at(-1), data = bytes.slice(0, -2);
    if (crc16(data) !== got) throw Error('Kontrolsummen passer ikke. Kopiér hele koden igen.');
    const rd = reader(data);
    if (rd.get(3) !== VERSION) throw Error('Ukendt kodeversion.');
    const state = g.BudgetLogic.blank(), nr = rd.get(8);
    state.council = nr ? 'Byråd ' + nr : 'Byråd fra kode';
    for (const i of C.initiativer) state.amounts[i.id] = rd.get(AMOUNT_BITS);
    for (const r of C.roller) { const v = rd.get(2); if (!v) throw Error('Der mangler et stemmesvar.'); state.votes[r.id] = VOTE_NAME[v]; }
    state.finalized = true;
    return g.BudgetLogic.normalize(state);                // samme regler som for filer: ingen ugyldige beløb slipper igennem
  }
  g.ResultCode = { encode, decode };
  if (typeof module !== 'undefined') module.exports = g.ResultCode;
})(typeof window === 'undefined' ? globalThis : window);
```

## 19. Opsamling og sammenligning på storskærm

Læreren sammenligner bordenes beslutninger side om side i debriefingen, og klassen undersøger, hvordan kravene blev til beslutninger.

- **Indlæsning:** læreren indsætter resultatkoder (én pr. linje) i et felt eller henter resultatfiler (JSON, højst 200 KB pr. fil). Højst 30 borde ad gangen. Fejl vises pr. kode eller fil ("Kontrolsummen passer ikke. Kopiér hele koden igen"), og de rigtige bliver tilføjet alligevel. Filer, der kun er udkast, afvises.
- **Genbrug logikken.** Opsamlingen bruger `normalize` og `outcome` fra budgetlogikken, så den regner udfaldet på samme måde som eleverne.
- **Overblik pr. bord:** et kort pr. byråd med vedtaget eller forkastet og antal ja-stemmer, bevilget og reserve, stemmer pr. gruppe som små mærker (med symbol og tekst, ikke kun farve, fx "✓ Ja" og "✗ Nej") og de prioriterede indsatser med beløb (delvise markeret).
- **Tabel på tværs:** initiativer grupperet efter område, en række for beslutning, ja-stemmer og reserve, og stemmefordelingen pr. rolle. Et filter skjuler initiativer uden bevilling (slået til som standard), og en note forklarer beløb og flertal.
- **Skal kunne læses på en projektor:** store mærker, få farver, ingen tekst under ca. 13 px i tabellen.
- Uden data viser siden en venlig tom tilstand med en kort vejledning.

## 20. Krypteret lærerpakke

Lærerens materialer (rollekort, bilag, lærerguide, cheatsheet som .docx og .pdf) ligger i en ZIP, der er krypteret ind i spillets script-fil og låses op i lærercockpittet (afsnit 24). Der er ingen separat dokumentside.

- **Format:** nyttelasten i `laererdata.js` er `{ ..., files: <ZIP som base64> }` og låses med samme format som rollerne, `{salt, iv, data}`. I Kommunalbudget er ZIP'en omkring 140 KB. Ligger pakken i en selvstændig `lærerpakke.js` (`window.TEACHER_LOCK`), gælder det samme format.
- **Download:** efter oplåsning kalder cockpittet `LaererMotor.downloadMaterials(filnavn)`, som gør base64 om til en `Blob`, henter den som ZIP og frigiver objekt-URL'en igen. Knappen vises kun, når `hasMaterials()` er sand. Fejl giver en venlig besked ("Materialepakken er ikke tilgængelig. Lås cockpittet op først.").
- **Ingen rå filer.** Hverken .docx, .pdf eller ZIP ligger som almindelige filer på sitet. Tjek det med en gennemgang af den mappe, der publiceres (`find . -name "*.docx" -o -name "*.pdf" -o -name "*.zip"`) og med en test, der forsøger at hente de kendte filnavne og forventer 404.
- **Gamle referencer.** En evt. `laerer.html` er en viderestilling, der bevarer parametre og hash: `<meta http-equiv="refresh" content="0; url=laerer-assistent.html">` og `location.replace("laerer-assistent.html" + location.search + location.hash)`. Test, at `laerer.html?kode=...` ender i cockpittet med parameteren intakt.
- **Hvad det beskytter mod:** elever, der klikker rundt på sitet. Filen kan hentes af alle, og koden kan gættes offline, så **koden, der låser bundtet, skal være lang og tilfældig** (mindst 12 tilfældige tegn), ikke 4 cifre. Med PBKDF2 på 100 000 runder koster hvert gæt ca. 50 ms, og det er ubrugeligt mod en lang kode. Hvordan lærerne får adgang, står i afsnit 25.
- **Byg pakken med et script**, ikke i hånden: (1) generér .docx- og .pdf-filerne, (2) pak dem i en ZIP, (3) base64, (4) lås med bundtets kode, (5) skriv `laererdata.js`. Kør scriptet efter hver ændring i materialerne, og kør siden og testene bagefter. Giv hver elev kun sin egen rolles kort; del ikke den samlede pakke.

Låsegeneratoren nedenfor (gem den som `laas.cjs`) laver låse, som Kommunalbudgets egen `decrypt` kan åbne (afprøvet), og den samme funktion kan bruges til rollerne:

```javascript
// Bygger en lås {salt, iv, data} som siderne låser op med decrypt(kode, lås). Kør i Node 18 eller nyere.
const { webcrypto: crypto } = require('node:crypto');
const b64 = bytes => Buffer.from(bytes).toString('base64');
async function lock(code, payload) {                      // payload: objekt, fx en rolle eller { files: <zip som base64> }
  const salt = crypto.getRandomValues(new Uint8Array(16)), iv = crypto.getRandomValues(new Uint8Array(12));
  const base = await crypto.subtle.importKey('raw', new TextEncoder().encode(code), 'PBKDF2', false, ['deriveKey']);
  const key = await crypto.subtle.deriveKey({ name: 'PBKDF2', salt, iterations: 100000, hash: 'SHA-256' }, base, { name: 'AES-GCM', length: 256 }, false, ['encrypt']);
  const data = await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key, new TextEncoder().encode(JSON.stringify(payload)));
  return { salt: b64(salt), iv: b64(iv), data: b64(new Uint8Array(data)) };
}
async function hashOf(code) {                             // nøglen i ROLE_LOCKS: SHA-256 af koden som hex
  return Buffer.from(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(code))).toString('hex');
}
module.exports = { lock, hashOf };
```

## 21. Automatiserede end-to-end tests

Et testsæt, der kan køres igen efter hver ændring, fanger de fejl, man ellers først finder foran klassen. Gem testene i en mappe ved siden af spillet (fx `kvalitet/`) sammen med en kort rapport over seneste kørsel.

**Hvad en test skal dække:**

1. **Layout og fejl:** ingen vandret scroll ved ca. 1300, 390 og 320 px på alle sider, og ingen JavaScript-fejl i konsollen.
2. **Adgangskoder:** en forkert kode afvises, og en rigtig kode åbner kun sin egen rolle. Prøv også rolleskift og kontrollér, at spørgsmålstælleren er uændret.
3. **Rådgiverens prompt:** prompten indeholder kun den valgte rolles kort og det fælles casekort, ikke andres skjulte information. Test det ved at opfange kaldet til proxyen (`page.route`) og læse systemprompten, ikke ved at gætte.
4. **Rådgiverens grænseflade:** ingen forslagsknapper, åbningsbesked med spørgsmål, faser kun med elevfaser, på mobil fire faner på mindst 44 px, sticky, og på computer et meget langt rollekort, der ikke skubber skrivefeltet eller tælleren ud af skærmen (afsnit 16).
5. **Budgetværktøjet:** overforbrug, reserve, delvis bevilling, afslut kun når alle har svaret, og at en ændring nulstiller afstemning og kode.
6. **Resultatkoden:** roundtrip (encode og decode giver samme plan), kontrolsummen afviser manipulation, og koden indeholder ikke startkrav eller tekst.
7. **Opsamlingen:** flere koder, en manipuleret kode afvises, og tabellen vises.
8. **Spillets matematik:** vægtene summer til totalen, ingen to roller kan vinde alene, der findes flere vindende koalitioner, og alle priser kan rummes i koden.
9. **Lærerens cockpit:** gruppeplanen og printtallene hænger sammen for alle elevtal (afsnit 24), prompten henter fasenavne og tal fra datasættet, en forkert lærerkode afvises af dekrypteringen, og et meget langt opslag skubber ikke skrivefeltet ud af skærmen (ved 800 px skærmhøjde ligger skrivefeltets bund på højst 800 px, uden at vinduet ruller; skabelon i afsnit 24).

Logikken kan testes uden browser (hurtig og stabil). Skabelonen nedenfor er afprøvet mod Kommunalbudget og mod den læsbare udgave i afsnit 17 og 18:

```javascript
// test_logik.cjs: logik og resultatkode uden browser. Kør: node test_logik.cjs <mappen med spildata.js, budgetlogik.js, resultatkode.js>
const vm = require('vm'), fs = require('fs'), assert = require('assert');
const dir = process.argv[2];
const ctx = { console, TextEncoder, TextDecoder }; ctx.window = ctx; ctx.globalThis = ctx; vm.createContext(ctx);
for (const f of ['spildata.js', 'budgetlogik.js', 'resultatkode.js']) vm.runInContext(fs.readFileSync(dir + '/' + f, 'utf8'), ctx, { filename: f });
const { CASE: C, BudgetLogic: B, ResultCode: R } = ctx;
let seed = 1; const rand = n => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) % n;

// 1. Spillets matematik: ingen to roller kan vinde alene, og der findes flere vindende koalitioner
const w = C.roller.map(r => r.stemmer);
assert.strictEqual(w.reduce((a, b) => a + b, 0), C.totalStemmer, 'stemmerne summer ikke til totalStemmer');
let wins = 0;
for (let m = 1; m < 1 << w.length; m++) {
  const yes = w.reduce((a, v, i) => a + (m >> i & 1 ? v : 0), 0), size = w.filter((_, i) => m >> i & 1).length;
  if (yes >= C.flertal) { wins++; assert(size >= 3, 'to roller kan vinde alene'); }
}
assert(wins >= 2, 'for få vindende koalitioner');

// 2. Roundtrip: encode, decode giver samme bevillinger og stemmer
function randomState() {
  const s = B.blank(); s.council = 'Byråd ' + (1 + rand(40)); let left = C.budget;
  for (const i of C.initiativer) { const a = Math.min(left, rand(i.pris + 1)); s.amounts[i.id] = rand(3) ? a : 0; left -= s.amounts[i.id]; }
  for (const r of C.roller) s.votes[r.id] = ['ja', 'nej', 'blankt'][rand(3)];
  s.finalized = true; return s;
}
for (let k = 0; k < 2000; k++) {
  const s = randomState(), back = R.decode(R.encode(s));
  C.initiativer.forEach(i => assert.strictEqual(back.amounts[i.id], s.amounts[i.id]));
  C.roller.forEach(r => assert.strictEqual(back.votes[r.id], s.votes[r.id]));
}

// 3. Manipulation: ethvert ændret tegn afvises af kontrolsummen
const ALPHABET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ', good = R.encode(randomState());
let tried = 0;
for (let p = good.indexOf('-') + 1; p < good.length; p++) {
  if (good[p] === '-') continue;
  for (const ch of ALPHABET) { if (ch === good[p]) continue; tried++; assert.throws(() => R.decode(good.slice(0, p) + ch + good.slice(p + 1)), 'ændret tegn blev accepteret'); }
}

// 4. Tolerant indtastning og strenge afvisninger
assert.doesNotThrow(() => R.decode(good.toLowerCase().replace(/-/g, ' ')));
assert.doesNotThrow(() => R.decode(good.replace(/0/g, 'O')));
for (const bad of ['', 'XX1-AAAAA', good.slice(0, -2), good + 'A']) assert.throws(() => R.decode(bad));

// 5. Logikken afviser ugyldige data og regner udfaldet rigtigt
const s = B.blank(); C.initiativer.forEach(i => s.amounts[i.id] = 0); s.amounts[C.initiativer[0].id] = C.initiativer[0].pris + 1;
assert(B.errors(s).length, 'for høj bevilling blev ikke fanget');
const t = B.blank(); C.roller.forEach(r => t.votes[r.id] = 'nej'); t.finalized = true;
assert.strictEqual(B.outcome(t).adopted, false); assert.strictEqual(B.outcome(t).reserve, C.budget);
assert.throws(() => B.normalize({ kind: 'andet', version: 1 }));

// 6. Kodens felter er brede nok: højeste pris skal kunne ligge i AMOUNT_BITS
assert(Math.max(...C.initiativer.map(i => i.pris)) <= 63, 'pris over 63: udvid AMOUNT_BITS');
console.log('test_logik: alt bestået (' + wins + ' vindende koalitioner, ' + tried + ' manipulerede koder afvist)');
```

Browsertesten kræver en lokal server (Web Crypto virker kun på `localhost` og https) og Playwright. Skabelonen er afprøvet mod Kommunalbudget (31 kontroller bestået). Layoutkontrollen er også afprøvet mod den gamle CSS, hvor den fejler som forventet. Tilpas `CONFIG` til jeres spil, og udvid med rådgivertesten (punkt 2 til 4), når I kender rollekoderne:

```javascript
// test_browser.cjs: helt flow i Chromium. Kør efter at siden er serveret (HTTPS eller localhost), fx:
//   python3 -m http.server 8766 --bind 127.0.0.1   (i spillets overmappe), og derefter  node test_browser.cjs
const { chromium } = require('playwright');
const CONFIG = {
  base: 'http://127.0.0.1:8766/kommunebudget/',
  pages: ['', 'casespil.html', 'raadgiver.html', 'budget.html', 'laerer-assistent.html', 'sammenligning.html', 'intro.html'],
  widths: [1300, 390, 320],
  roleIds: ['familier', 'aeldre', 'unge', 'erhverv', 'klima'],
  plan: { skole: 40, pleje: 50, sfo: 10 },           // skal summe til højst puljen
  mobileTabs: 4
};
let failed = 0;
const check = (ok, text) => { console.log((ok ? 'OK    ' : 'FEJL  ') + text); if (!ok) failed++; };

(async () => {
  const browser = await chromium.launch();
  // 1. Ingen vandret scroll og ingen JavaScript-fejl på nogen side ved nogen bredde
  for (const w of CONFIG.widths) {
    const ctx = await browser.newContext({ viewport: { width: w, height: 800 } });
    for (const p of CONFIG.pages) {
      const page = await ctx.newPage(), errors = [];
      page.on('pageerror', e => errors.push(e.message));
      page.on('console', m => { if (m.type() === 'error' && !/Failed to load resource/.test(m.text())) errors.push(m.text()); });
      await page.goto(CONFIG.base + p); await page.waitForTimeout(250);
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      check(overflow <= 0 && !errors.length, `${w}px /${p || 'index'}: overskud ${overflow}px, fejl ${errors.length}`);
      await page.close();
    }
    await ctx.close();
  }
  // 2. Budgetværktøjet: overforbrug, reserve, afslutning, resultatkode og nulstilling ved ændring
  const ctx = await browser.newContext({ viewport: { width: 1300, height: 900 } }), page = await ctx.newPage();
  await page.goto(CONFIG.base + 'budget.html'); await page.waitForSelector('#budgetRows input');
  await page.fill('#council', 'Byråd 3');
  for (const [id, v] of Object.entries(CONFIG.plan)) await page.fill('#amount-' + id, String(v));
  await page.fill('#amount-veje', '30');
  check(/overskrider/.test(await page.textContent('#validation')), 'overforbrug giver advarsel');
  await page.fill('#amount-veje', '0');
  check(/klar/.test(await page.textContent('#validation')), 'rettet plan er klar');
  check(await page.isDisabled('#finish'), 'afslut er deaktiveret, før alle roller har stemt');
  for (const id of CONFIG.roleIds) await page.selectOption('#vote-' + id, 'ja');
  await page.click('#finish'); await page.waitForTimeout(150);
  const code = await page.inputValue('#resultCode');
  check(/^[A-Z0-9]{3}(-[0-9A-Z]{1,5})+$/.test(code), 'resultatkode vises: ' + code);
  await page.fill('#amount-skole', '35'); await page.waitForTimeout(100);
  check(await page.isHidden('#codeOutput') && (await page.inputValue('#vote-' + CONFIG.roleIds[0])) === '', 'ændret plan skjuler koden og nulstiller afstemningen');
  // 3. Opsamlingen afviser en manipuleret kode og accepterer en rigtig (også med små bogstaver og mellemrum)
  const cmp = await ctx.newPage(); await cmp.goto(CONFIG.base + 'sammenligning.html');
  const tampered = code.slice(0, 10) + (code[10] === 'A' ? 'B' : 'A') + code.slice(11);
  await cmp.fill('#codes', [code, code.toLowerCase().replace(/-/g, ' '), tampered].join('\n')); await cmp.click('#addCodes'); await cmp.waitForTimeout(200);
  const status = await cmp.textContent('#importStatus');
  check(/2 resultatkoder/.test(status) && /Kontrolsummen/.test(status), 'to rigtige koder tilføjet, manipuleret afvist');
  // 4. Rådgiveren: forkert kode afvises, ingen forslagsknapper, faner på mindst 44 px og sticky på mobil
  const mobile = await browser.newContext({ viewport: { width: 390, height: 800 }, isMobile: true, hasTouch: true }), adv = await mobile.newPage();
  await adv.goto(CONFIG.base + 'raadgiver.html');
  await adv.fill('#code', '0000'); await adv.click('#unlock button'); await adv.waitForTimeout(800);
  check(await adv.isHidden('#workspace'), 'forkert rollekode åbner ikke arbejdsbordet');
  check(!/class="[^"]*(chip|suggest)|Forslag til sp/i.test(await adv.content()), 'ingen forslagsknapper i rådgiveren');
  await adv.evaluate(() => { document.getElementById('setupView').hidden = true; document.getElementById('workspace').hidden = false; });
  const heights = await adv.evaluate(() => [...document.querySelectorAll('.mobile-tab-btn')].map(b => Math.round(b.getBoundingClientRect().height)));
  check(heights.length === CONFIG.mobileTabs && heights.every(h => h >= 44), 'mobilfaner: ' + heights.join(', ') + ' px');
  check((await adv.evaluate(() => getComputedStyle(document.getElementById('mobileTabs')).position)) === 'sticky', 'fanelinjen er sticky');
  // 5. Computerlayout: et meget langt rollekort må ikke skubbe skrivefeltet eller tælleren ud af skærmen
  const desk = await browser.newContext({ viewport: { width: 1300, height: 800 } }), dp = await desk.newPage();
  await dp.goto(CONFIG.base + 'raadgiver.html');
  await dp.evaluate(() => {
    document.getElementById('setupView').hidden = true; document.getElementById('workspace').hidden = false;
    document.getElementById('roleCard').innerHTML = Array.from({ length: 60 }, (_, i) => '<p>Afsnit ' + i + ': et langt rollekort med mange argumenter og dilemmaer.</p>').join('');
  });
  await dp.waitForTimeout(150);
  const lay = await dp.evaluate(() => ({
    vh: innerHeight, ask: Math.round(document.getElementById('ask').getBoundingClientRect().bottom),
    meter: Math.round(document.getElementById('meterDots').getBoundingClientRect().bottom),
    pageScroll: document.documentElement.scrollHeight - innerHeight,
    panelScrolls: (b => b.scrollHeight > b.clientHeight)(document.querySelector('.pbody'))
  }));
  check(lay.ask <= lay.vh && lay.meter <= lay.vh && lay.pageScroll <= 0 && lay.panelScrolls,
    `langt rollekort: skrivefelt ${lay.ask}px og tæller ${lay.meter}px af ${lay.vh}px, sidescroll ${lay.pageScroll}px, panelet ruller selv: ${lay.panelScrolls}`);
  await browser.close();
  console.log(failed ? `\n${failed} fejl` : '\nAlt bestået');
  process.exit(failed ? 1 : 0);
})();
```

Kør `node --check` på alle scripts, og se skærmbillederne af de vigtigste sider, ikke kun tallene. Vent på konkrete elementer og tilstande (`waitForSelector`), ikke på faste pauser.

## 22. Kildemappe og distributionsmappe

Når siderne genereres fra skabeloner og data, er der to mapper: en kildemappe og den distribuerede mappe, som ligger på webstedet. (Afsnittet bygger på oplysninger fra spiludviklingen. Kildemapperne til Kommunalbudget var ikke tilgængelige, da afsnittet blev skrevet.)

- **Typisk kildemappe:** `data/` med spillets data (fx `spil.json`, `laerer.json`), `produktion/` med skabeloner og generatorer (`webskabeloner/`) og `kvalitet/` med tests og en rapport over seneste kørsel.
- **Redigér ét sted.** Ret skabelonerne i kildemappen, og generér ud. Rettes en side kun i den distribuerede mappe, overskriver den næste generering rettelsen. Rettes den distribuerede side direkte (fx for at teste), porteres rettelsen til skabelonen samme dag.
- **Efter hver ændring:** generér, kør testene, og læs rapporten. Kontrollér med en `diff`, at den distribuerede mappe svarer til det, generatoren producerer.
- **Backup før ændring** gælder også her (grundregel 3).

## 23. Katalog og mappestruktur på tværs af spil

Flere spil kan bo på samme domæne og findes via et fælles katalog.

- **Én mappe pr. spil** (`fjord/`, `kommunebudget/`), hver med de faste sidenavne fra afsnit 1. Billeder og lyd ligger i spillets egen mappe.
- **`cases.json` i roden** beskriver hvert spil: `mappe`, `titel`, `fag`, `fag_noegle`, `niveau`, `begreber`, `tekst`, `billede` og `status` (`klar` eller `kommer`). Katalogsiden bygger kortene ud fra filen, filtrerer efter fag (via `#fag` i adressen, så et filter kan deles som link) og linker til `mappe/`.
- Et nyt spil tilføjes ved at oprette mappen og en post i `cases.json`. Ingen kode skal ændres.
- Kataloget er et sted, hvor `loading="lazy"` er rimeligt, fordi billederne er mange og står under skærmbunden (afsnit 7).

## 24. Lærerens cockpit (lærer-assistent)

Lærerens eget arbejdsbord bag lærerkoden. Det er afprøvet i to spil (Kommunalbudget og Fjord Outdoor), og afsnittet beskriver både, hvad der virker, og de fælder, der blev fundet ved gennemgang af første udgave.

**Filer:** `laerer-assistent.html` (siden), `laerer-motor.js` (den fælles motor) og `laererdata.js` (det krypterede databundt, genereret af et script). Siden indlæser `window.TEACHER_CONFIG = { gameId, gameTitle, proxyUrl, proxyToken, bundle: { salt, iv, data } }`. Proxyens adresse og token kommer altså fra spillets datasæt og ikke fra motoren. Der er ingen `masterHash` og intet SHA-256-tjek i koden (det blev fundet og fjernet efter første udgave, se nedenfor).

**Databundtets indhold (efter dekryptering):** `gameId`, `titel`, `fag`, `grupperegler`, `faser` (`nr`, `navn`, `handling`, `rad`), `begreber` (`begreb`, `forklaring`), `roller` (`id`, `titel`, `stemmer`, `kode`, `maal`, `skjult`, `dilemmaer`, evt. `front` og `back`), `guide` (en liste af `{ titel, afsnit: [...] }`) og `cheatsheet` (en liste af `{ spoergsmaal, modelsvar, faglig_begrundelse, typisk_fejl }`). Bundtet bygges af samme script som lærerpakken (afsnit 20), så det altid svarer til rollekortene. Prompten bygges af `faser`, `begreber` og `roller` i bundtet, så fasenavne og begreber kun står ét sted.

**Sikkerhed:**

- Alt fortroligt (lærerguide, facit, rollekort med hemmelige kompromiser, rollekoder) ligger kun i det krypterede bundt og dekrypteres i hukommelsen. Intet af det står i klartekst i siden.
- **Kontrollér koden ved dekrypteringen, ikke med en hurtig hash.** Kravet er: ingen `masterHash`, intet SHA-256-tjek i JavaScript. Koden verificeres udelukkende under selve dekrypteringen med Web Crypto: PBKDF2 (100 000 runder, SHA-256) og AES-256-GCM. En forkert kode fejler af sig selv på AES-GCM's autentificeringstag. Første udgave gemte en `masterHash` (SHA-256 af lærerkoden) og sammenlignede, før den dekrypterede. Målt: ca. 16 000 SHA-256-forsøg i sekundet mod ca. 20 PBKDF2-forsøg i sekundet, altså ca. 800 gange hurtigere, og specialværktøj er mange størrelsesordener hurtigere end en browser. Hashen var derfor en genvej til at gætte lærerkoden uden om nøgleudledningen. Den er fjernet i den nyeste casespil.dk, og det er afprøvet, at en forkert kode afvises af dekrypteringen, og at motoren ikke længere indeholder `masterHash` eller `digest('SHA-256')`.
- Lærerkoden er lang og tilfældig: et spilpræfiks og mindst 12 tilfældige tegn, fx `AB-3f9c0e7d21b8` eller `CD-7e41a9b05c26` (12 hex-tegn er 48 bit, så 2 i 48. potens forsøg à ca. 50 ms er ikke gennemførligt). Aldrig et ord, et årstal eller 4 cifre. Gem den højst i `sessionStorage` (den forsvinder, når fanen lukkes), og slet den ved "Lås". På en fælles computer bør læreren låse, før vedkommende forlader computeren.
- Proxyens `appId` er ikke en lås (alle kan læse den), så cockpittet og elevernes rådgiver kan ikke skelnes af proxyen. Dagsloft og herkomstbegrænsning på proxyen (afsnit 3) er det, der beskytter.

Oplåsning og streaming (afprøvet med rigtig og forkert kode og med datablokke, der brydes midt i en linje, inklusive tænketokens, der aldrig må vises):

```javascript
// laerer-kerne.js: oplåsning og streaming til lærer-assistenten (Node 18+ og browser)
(function (g) {
  const b64 = s => Uint8Array.from(atob(s), c => c.charCodeAt(0));

  // Oplåsning: den eneste kontrol er, at AES-GCM kan dekryptere. Gem IKKE en hurtig hash af koden til et "tjek først".
  // En hash kan afprøves ca. 800 gange hurtigere end PBKDF2, så den ville omgå hele nøgleudledningen.
  async function unlock(code, pack) {
    if (!g.crypto || !g.crypto.subtle) throw Error('Åbn siden via HTTPS eller localhost.');
    const base = await g.crypto.subtle.importKey('raw', new TextEncoder().encode(code.trim()), 'PBKDF2', false, ['deriveKey']);
    const key = await g.crypto.subtle.deriveKey({ name: 'PBKDF2', salt: b64(pack.salt), iterations: 100000, hash: 'SHA-256' },
      base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
    try {
      const plain = await g.crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(pack.iv) }, key, b64(pack.data));
      return JSON.parse(new TextDecoder().decode(plain));      // data lever kun i hukommelsen
    } catch (e) {
      throw Error('Forkert lærerkode.');                        // forkert nøgle giver altid en fejl fra AES-GCM
    }
  }

  // Tekst fra ét svarstykke: tænketokens (p.thought) må aldrig vises
  function textOf(v) {
    return ((v.candidates && v.candidates[0] && v.candidates[0].content && v.candidates[0].content.parts) || [])
      .filter(p => !p.thought && p.text).map(p => p.text).join('');
  }

  // Læser et svar fra proxyen, både som SSE-strøm (text/event-stream) og som almindelig JSON
  async function readReply(res, onChunk) {
    if (!(res.headers.get('content-type') || '').includes('event-stream')) {
      const text = textOf(await res.json()); onChunk && onChunk(text); return text;
    }
    const reader = res.body.getReader(), decoder = new TextDecoder();
    let buffer = '', full = '';
    for (;;) {
      const { value, done } = await reader.read();
      buffer += decoder.decode(value || new Uint8Array(), { stream: !done });
      const lines = buffer.split('\n');
      buffer = lines.pop();                                     // en halv linje venter på næste stykke
      if (done && buffer) { lines.push(buffer); buffer = ''; }
      for (const line of lines) {
        if (!line.trim().startsWith('data:')) continue;
        const raw = line.trim().slice(5).trim();
        if (!raw || raw === '[DONE]') continue;
        try { const piece = textOf(JSON.parse(raw)); if (piece) { full += piece; onChunk && onChunk(full); } } catch (e) { /* ufuldstændig linje */ }
      }
      if (done) break;
    }
    return full;
  }
  g.LaererKerne = { unlock, readReply, textOf };
  if (typeof module !== 'undefined') module.exports = g.LaererKerne;
})(typeof window === 'undefined' ? globalThis : window);
```

**Motoren er fælles, data er spillets egne.** Kravet er, at motoren (`laerer-motor.js`) er fælles på tværs af spil og ikke indeholder hårdkodede fasenavne eller spilkonstanter: auth, dekryptering, beregnere, markdown til chatten og proxykaldet ligger i motoren, og alt, der handler om det enkelte spil, ligger i datasættet. Status i den nyeste casespil.dk, målt:

- **Rettet:** `buildSystemPrompt()` bygger nu sine faser, begreber og roller dynamisk af bundtet (`data.faser`, `data.begreber`, `data.roller`) og indeholder reglerne om ingen faste minuttal, ingen rituelle fraser og ingen lange tankestreger. Første udgave havde fasenavne i prompten ("Forberedelse i interessegrupper", "Forhandling i udvalget", "Afstemning"), som afveg fra datasættets, og det brød reglen om samme faser overalt. Proxyens adresse og token modtages som `config.proxyUrl` og `config.proxyToken`.
- **Stadig åbent:** motoren indeholder stadig spilspecifikke ting: projektnavnene `P1 (Regntøj ...)` til `P5`, `boardSize = 6`, `12 stemmer` og `7 ja-stemmer` i tekster, forgreninger på `gameId === 'kommunebudget'` og `'fjord'` i printlisten (med tekster som "Tilst-scenariet", "18 initiativer" og "Fjord_Outdoor_Facit.html"), og en reservekonstant for Fjords proxy og token (`fjord2026`), hvis `config` mangler dem. Det skal flyttes til `grupperegler` og til printlistens data, og motoren skal fejle tydeligt i stedet for at falde tilbage til et andet spils proxy.
- **Stadig åbent:** motoren ligger i tre byte-identiske kopier (roden, `fjord/` og `kommunebudget/`). Hav én kopi og henvis til den (`../laerer-motor.js`). Findes kopier alligevel, skal en test sammenligne dem.

**Gruppe- og holdberegner.** Den er en ren funktion, som returnerer en plan. Visningen og printlisten bygger begge på planen, og printtallene er en projektion af planen og ikke en separat formel. Kravet er en gyldig fordeling for alle elevtal fra 4 til 60 og summen af elever på roller lig med antal elever uden undtagelse. Første udgave beregnede printlisten med `ceil(n/5)` og `floor(n/5)` og satte én elev på hver af fem roller, også ved et bord med fire elever: pladserne summerede ikke ved 23 af 57 elevtal, og rollekortene stemte hverken med elevtallet eller planen ved 34 af 57. I den nyeste casespil.dk er summen af elever på roller lig med N for alle 57 elevtal, og printlisten summerer til N (målt). Fjords projektteams viser nu det faktiske spænd, "4 til 5 pr. team" ved 30 elever. Koden nedenfor er datadrevet, har invarianter, og er testet for 4 til 80 elever (647 borde):

```javascript
// gruppeplan.js: ren funktion uden DOM. Én plan bruges til visning, til printtal og til tests.
(function (g) {
  // Type 1: borde, hvor hvert bord har alle roller (Kommunalbudget).
  // rules: { targetSize, merge: [[rolle, ind i rolle], ...], double: [rolle, ...] }
  function planTables(n, roles, rules) {
    n = Math.floor(n);
    const k = roles.length, target = rules.targetSize || k;
    if (!(n >= k - rules.merge.length)) throw Error('Mindst ' + (k - rules.merge.length) + ' elever kræves.');
    const count = Math.max(1, Math.round(n / target)), tables = [];
    for (let t = 0; t < count; t++) {
      const size = Math.floor(n / count) + (t < n % count ? 1 : 0);
      const seats = roles.map(r => ({ id: r.id, titel: r.titel, stemmer: r.stemmer, students: 1, mergedInto: null }));
      let free = size - k;                                   // negativ: for få elever, positiv: for mange
      for (const [from, into] of rules.merge) {              // slå roller sammen, til der er elever nok
        if (free >= 0) break;
        const s = seats.find(x => x.id === from);
        s.students = 0; s.mergedInto = into; free++;
      }
      for (let i = 0; free > 0; i++, free--) seats.find(x => x.id === rules.double[i % rules.double.length]).students++;
      if (free !== 0) throw Error('Bordet kan ikke fordeles: ' + size + ' elever.');
      tables.push({ nr: t + 1, size, seats });
    }
    return tables;
  }
  // To forskellige tal, som begge skal kunne forklares:
  // 1. Elever på roller: summen skal altid være lig med antal elever (planens invariant).
  function studentsOnRoles(tables) {
    return tables.reduce((a, t) => a + t.seats.reduce((x, s) => x + s.students, 0), 0);
  }
  // 2. Rollekort at printe pr. rolle: ét kort pr. elev på rollen, og ét kort til hvert bord, hvor rollen er slået sammen med
  //    en anden og stadig stemmer. En rolle uden elev, der stadig stemmer, SKAL have et kort. Ellers er summen kun lig med N,
  //    fordi kortet er udeladt.
  function cardCounts(tables) {
    const out = {};
    for (const t of tables) for (const s of t.seats) out[s.id] = (out[s.id] || 0) + Math.max(1, s.students);
    return out;
  }

  // Type 2: én bestyrelse og flere projektteams (Fjord Outdoor).
  // rules: { boardSize, minStudents, teams: [{ id, navn }], restOrder: [id, ...] }
  function planBoardAndTeams(n, rules) {
    n = Math.floor(n);
    if (n < rules.minStudents) return { warning: 'For få elever (' + n + '). Kør en miniversion.', minStudents: rules.minStudents };
    const rest = n - rules.boardSize, base = Math.floor(rest / rules.teams.length);
    const teams = rules.teams.map(t => ({ id: t.id, navn: t.navn, students: base }));
    let extra = rest % rules.teams.length;
    for (const id of rules.restOrder) if (extra > 0) { teams.find(t => t.id === id).students++; extra--; }
    return { board: rules.boardSize, teams };
  }
  g.Gruppeplan = { planTables, studentsOnRoles, cardCounts, planBoardAndTeams };
  if (typeof module !== 'undefined') module.exports = g.Gruppeplan;
})(typeof window === 'undefined' ? globalThis : window);
```

- **Regler i data (eksempel):** `{ targetSize: 5, merge: [['klima', 'unge'], ['erhverv', 'aeldre']], double: ['familier', 'aeldre'] }` for borde, og `{ boardSize: 6, minStudents: 11, teams: [...], restOrder: ['p2', 'p3', 'p5', 'p1', 'p4'] }` for bestyrelse og teams. `restOrder` skal være den samme som lærerguidens differentieringsregel, ellers siger guide og cockpit to forskellige ting.
- **Et åbent designvalg: en rolle uden elev.** I den nyeste casespil.dk får roller ved et bord med færre end fem elever 0 elever, og printlisten tæller kun elever, så summen af rollekort er N. Men rollen stemmer stadig (budgetværktøjet kræver, at alle fem roller svarer), og den har ikke noget kort. Målt: 23 af 57 elevtal har mindst ét bord, hvor Klima ikke har en elev og dermed ikke et kort, og ved fire elever råder bordet kun over 10 af 12 stemmer med kort. Vælg og beskriv det i lærerguiden: enten slås rollen sammen med en anden, og så printes et kort til den (kort = elever plus roller uden egen elev, `cardCounts` nedenfor), eller rollen udgår af afstemningen, og flertallet regnes om. Planen skal vise begge tal: elever på roller (altid N) og kort at printe.
- **Printlisten** bygges af planen og af formen (papir, hybrid, digital). Skriv ikke faste intervaller i teksten, men udled dem af planen (første udgave skrev "2 til 4 pr. team" ved 30 elever, hvor det er 4 til 5; nu udledes spændet af planen).
- Under minimumsantallet vises en advarsel og et råd om en miniversion (`casespil-miniversion`), ikke en plan.

Testen (gem gruppeplanen som `gruppeplan.js` og testen som `gruppeplan_test.cjs`, og kør `node gruppeplan_test.cjs .`, hver gang reglerne eller rollerne ændres):

```javascript
const assert = require('assert'), G = require(process.argv[2] + '/gruppeplan.js');
const roles = [['familier', 3], ['aeldre', 3], ['unge', 2], ['erhverv', 2], ['klima', 2]].map(([id, stemmer]) => ({ id, titel: id, stemmer }));
const rules = { merge: [['klima', 'unge'], ['erhverv', 'aeldre']], double: ['familier', 'aeldre'] };
let tablesSeen = 0, merged = 0;
for (let n = 4; n <= 80; n++) {
  const tables = G.planTables(n, roles, rules);
  assert.strictEqual(tables.reduce((a, t) => a + t.size, 0), n, 'bordene summer ikke til ' + n);
  for (const t of tables) {
    tablesSeen++;
    assert.strictEqual(t.seats.reduce((a, s) => a + s.students, 0), t.size, 'pladser != elever, n=' + n);
    t.seats.forEach(s => { assert(s.students >= 0 && (s.students > 0 || s.mergedInto)); if (s.mergedInto) { merged++; assert(t.seats.find(x => x.id === s.mergedInto).students > 0); } });
    assert(Math.abs(t.size - tables[0].size) <= 1, 'ujævne borde');
  }
  assert.strictEqual(G.studentsOnRoles(tables), n, 'elever på roller != ' + n);                 // invariant: summen er altid N
  const cards = G.cardCounts(tables), total = Object.values(cards).reduce((a, b) => a + b, 0);
  const doubles = tables.reduce((a, t) => a + t.seats.reduce((x, s) => x + Math.max(0, s.students - 1), 0), 0);
  assert.strictEqual(total, tables.length * roles.length + doubles, 'kortantal følger ikke planen, n=' + n);
  const noStudent = tables.reduce((a, t) => a + t.seats.filter(s => s.students === 0).length, 0);
  assert.strictEqual(total, n + noStudent, 'kort = elever + roller uden egen elev, n=' + n);   // hver stemmende rolle har sit kort
}
assert.throws(() => G.planTables(2, roles, rules));
assert.strictEqual(G.planTables(3, roles, rules)[0].seats.filter(s => s.mergedInto).length, 2);
const fr = { boardSize: 6, minStudents: 11, teams: ['p1', 'p2', 'p3', 'p4', 'p5'].map(id => ({ id, navn: id })), restOrder: ['p2', 'p3', 'p5', 'p1', 'p4'] };
for (let n = 11; n <= 80; n++) { const p = G.planBoardAndTeams(n, fr); assert.strictEqual(p.board + p.teams.reduce((a, t) => a + t.students, 0), n); assert(p.teams.every(t => t.students >= 1)); }
assert(G.planBoardAndTeams(10, fr).warning);
console.log('gruppeplan: bord-plan holder for 4 til 80 elever (' + tablesSeen + ' borde, ' + merged + ' sammenlagte roller), og bestyrelse + teams holder for 11 til 80');
```

Oplåsning og streaming testes sådan (gem koden ovenfor som `laerer-kerne.js` og kræver låsegeneratoren `laas.cjs` fra afsnit 20; kør `node laerer_test.cjs .`):

```javascript
const assert = require('assert'), K = require(process.argv[2] + '/laerer-kerne.js'), { lock } = require(process.argv[2] + '/laas.cjs');
(async () => {
  const pack = await lock('lang-tilfaeldig-kode-71', { titel: 'Test', roller: [1, 2] });
  assert.deepStrictEqual((await K.unlock(' lang-tilfaeldig-kode-71 ', pack)).roller, [1, 2]);
  await assert.rejects(() => K.unlock('forkert', pack), /Forkert lærerkode/);
  // SSE med tænketokens, og med datablokke der brydes midt i en linje
  const ev = o => 'data: ' + JSON.stringify({ candidates: [{ content: { parts: o } }] }) + '\n\n';
  const sse = ev([{ thought: true, text: 'INTERN TANKE' }, { text: 'Hej ' }]) + ev([{ text: 'læreren' }]) + ev([{ thought: true, text: 'mere tanke' }]) + 'data: [DONE]\n\n';
  const bytes = new TextEncoder().encode(sse);
  for (const cut of [7, 31, 64, 99]) {
    const body = new ReadableStream({ start(c) { c.enqueue(bytes.slice(0, cut)); c.enqueue(bytes.slice(cut)); c.close(); } });
    const res = new Response(body, { headers: { 'content-type': 'text/event-stream' } });
    const seen = []; const full = await K.readReply(res, t => seen.push(t));
    assert.strictEqual(full, 'Hej læreren'); assert(!full.includes('TANKE') && !full.includes('tanke'));
  }
  const json = new Response(JSON.stringify({ candidates: [{ content: { parts: [{ thought: true, text: 'x' }, { text: 'JSON-svar' }] } }] }), { headers: { 'content-type': 'application/json' } });
  assert.strictEqual(await K.readReply(json), 'JSON-svar');
  console.log('laerer-kerne: oplåsning (rigtig/forkert kode) og streaming (4 brudte stykker + JSON, tænketokens filtreret) består');
})().catch(e => { console.error(e); process.exit(1); });
```

**Layoutlås og oplåsning i cockpittet.** Kravet er, at skrivefeltet (`.composer` og `#chatInput`) aldrig skubbes ud af skærmen af en lang lærerguide i sidepanelet. `body.in-workspace`, `#cockpitView` og `.dshell` har en ubrudt flex-kæde (`height: 100vh; overflow: hidden; display: flex; flex-direction: column;` med `min-height: 0`), og chatten og panelets indhold ruller hver for sig (`overflow-y: auto`, fx på `.chat-scroll` og `.panel-content`). Ved 800 px skærmhøjde skal skrivefeltets bund ligge på højst 800 px uden at hele vinduet ruller (afsnit 16). Målt i den nyeste casespil.dk med en meget lang lærerguide: Kommunalbudget 762 af 800 px og Fjord 764 af 800 px, uden lodret scroll (Fjord lå 1824 px nede i første udgave). Testen nedenfor bygger sit eget låste bundt, så den rigtige lærerkode aldrig bruges, og den består mod begge spil (18 kontroller):

```javascript
// test_cockpit.cjs: lærerens cockpit i en rigtig browser. Testen bygger sit eget låste bundt med sin egen kode,
// så den rigtige lærerkode aldrig bruges. Kør (siden serveres på localhost): node test_cockpit.cjs <mappen med laas.cjs>
const { chromium } = require('playwright'), { lock } = require(process.argv[2] + '/laas.cjs');
const CONFIG = {
  base: 'http://127.0.0.1:8774/', code: 'AB-3f9c0e7d21b8',
  games: { kommunebudget: { type: 'tables' }, fjord: { type: 'board_and_teams', boardRoles: [] } },
  roles: [['familier', 3], ['aeldre', 3], ['unge', 2], ['erhverv', 2], ['klima', 2]]
};
let failed = 0;
const check = (ok, text) => { console.log((ok ? 'OK    ' : 'FEJL  ') + text); if (!ok) failed++; };

(async () => {
  const roller = CONFIG.roles.map(([id, stemmer], i) => ({ id, titel: id, stemmer, kode: String(1000 + i), maal: 'Mål', skjult: 'Hemmeligt kompromis. '.repeat(30), dilemmaer: 'D' }));
  const browser = await chromium.launch();
  for (const [game, regler] of Object.entries(CONFIG.games)) {
    // Et ekstremt langt indhold i opslagene: det må ikke skubbe skrivefeltet ud af skærmen
    const data = { gameId: game, titel: 'Test', fag: 'F', grupperegler: regler, roller,
      faser: [{ nr: 1, navn: 'Fase A', handling: 'h', rad: 'r' }], begreber: [{ begreb: 'B', forklaring: 'f' }],
      guide: Array.from({ length: 40 }, (_, i) => ({ titel: 'Sektion ' + i, afsnit: ['Lang tekst. '.repeat(80)] })),
      cheatsheet: Array.from({ length: 12 }, (_, i) => ({ spoergsmaal: 'Spørgsmål ' + i, modelsvar: 'Modelsvar. '.repeat(60) })) };
    const config = 'window.TEACHER_CONFIG=' + JSON.stringify({ gameId: game, gameTitle: 'T', bundle: await lock(CONFIG.code, data) }) + ';';
    for (const [w, h] of [[1300, 800], [1100, 700], [390, 800], [320, 800]]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h }, isMobile: w < 500, hasTouch: w < 500 }), page = await ctx.newPage(), errors = [];
      page.on('pageerror', e => errors.push(e.message));
      await page.route('**/laererdata.js', r => r.fulfill({ body: config, contentType: 'application/javascript' }));
      await page.goto(`${CONFIG.base}${game}/laerer-assistent.html`);
      if (w === 1300) {                                             // forkert kode afvises af AES-GCM, rigtig kode åbner
        await page.fill('#teacherCodeInput', 'forkert-kode-123'); await page.click('#authForm button'); await page.waitForTimeout(1200);
        check(await page.evaluate(() => document.getElementById('cockpitView').hidden), `${game}: forkert kode åbner ikke cockpittet`);
      }
      await page.fill('#teacherCodeInput', CONFIG.code); await page.click('#authForm button'); await page.waitForTimeout(1500);
      const m = await page.evaluate(() => { const r = document.getElementById('btnSend').getBoundingClientRect(); return {
        open: !document.getElementById('cockpitView').hidden, bottom: Math.round(r.bottom), shown: r.height > 0, vh: innerHeight,
        vscroll: document.documentElement.scrollHeight - innerHeight, hscroll: document.documentElement.scrollWidth - innerWidth }; });
      check(m.open && !errors.length, `${game} ${w}px: rigtig kode åbner, ${errors.length} JavaScript-fejl`);
      if (w >= 900) check(m.shown && m.bottom <= m.vh && m.vscroll <= 0, `${game} ${w}x${h}: skrivefeltets bund ${m.bottom}px af ${m.vh}px, lodret scroll ${m.vscroll}px`);
      else check(m.hscroll <= 0, `${game} ${w}px: vandret scroll ${m.hscroll}px`);
      await ctx.close();
    }
  }
  await browser.close();
  console.log(failed ? `\n${failed} fejl` : '\nAlt bestået'); process.exit(failed ? 1 : 0);
})();
```

**AI-sparring.** Systemprompten kommer fra datasættet og indeholder: rollen som kollegial sparringspartner, spillets ramme (pulje, vægte, flertal, faser, den faglige model), alle roller med skjult information, og de faste regler: fejlfrit dansk i en direkte tone, ingen rituelle fraser, ingen faste minuttal (tempoet styres af tegn på flow og milepæle), ingen lange tankestreger, og konkrete formuleringer læreren kan sige ved bordene. Svarkrav: fokuserede svar, punktopstilling hvor det hjælper, og hvad læreren kan gøre her og nu. Indstillinger: temperatur ca. 0,5 og `maxOutputTokens: 2500`, historik på de seneste ca. 8 beskeder. Giv kaldet tidsgrænse og genforsøg som i elevernes rådgiver (afsnit 3), og vis en dansk fejlbesked i stedet for proxyens rå fejltekst. Prompten bruger `systemInstruction: { parts: [{ text: systemPrompt }] }` og `maxOutputTokens: 2500`. Ved SSE-streaming (`text/event-stream`) fra Gemini via proxyen filtrerer læseren interne tænketokens fra med `(candidates[0].content.parts || []).filter(p => !p.thought && p.text).map(p => p.text).join('')` (koden i `laerer-kerne.js` ovenfor). Sparringen kender alle spildata, hemmeligheder, dilemmaer, modelsvar og RAS-debriefing.

**Siden:**

- **Venstre kolonne (værktøjer):** antal elever, gruppeplanen, en vælger for papir, hybrid og digital, og printlisten som afkrydsningsliste. Knappen "Lås" nederst.
- **Midten:** sparringen med bobler, en "overvejer"-indikator, et skrivefelt (Enter sender), "Ryd samtale" og hurtigspørgsmål til læreren.
- **Højre kolonne (fanerne):** Lærerguide (foldbare sektioner, den første åben), Cheatsheet (spørgsmål med modelsvar, faglig begrundelse og typisk elevfejl), Roller og hemmeligheder, og Rollekoder (en tabel til at dele ud eller skrive på kortene).
- **Mobil:** de tre kolonner bliver faner. Layoutlåsen og fælderne i afsnit 16 gælder også her (og blev først fundet i cockpittet, da en lang lærerguide skubbede skrivefeltet ud).
- Indsæt tekst fra bundtet med `escapeHtml` eller `textContent`. Markdown i chatten laves først efter, at teksten er escapet.

## 25. Lærernes adgang: personlig e-mail, magic link og 7 dages udløb

Dette afsnit er standarden for, hvordan lærere får adgang til cockpittet og materialerne. Det er en designbeskrivelse med skitseret serverlogik. Endepunktsskitsen er kørt mod SQLite i hukommelsen (udsted, åbn, ugyldigt token, forfalsket udløb), men mail, rate limiting og godkendelse er ikke afprøvet her, så kør testene nederst på din egen løsning, før den tages i brug.

**Hvorfor ikke en fast kode.** En fast kode i en mail eller i kildekoden lever videre: den videresendes til en kollega, ender hos en elev eller stadig virker hos en klasse tre år senere. Den bundtnøgle, der låser `laererdata.js`, er derfor aldrig det, lærerne får. De får en personlig, kortlivet adgang, som serveren veksler til nøglen.

**Flow:**

1. Læreren skriver sin skolemail i formularen i cockpittet (eller på kodeskærmen) og sender den med et `fetch` (AJAX) til `api/laereradgang`. Ingen sidegenindlæsning.
2. Serveren validerer adressen, rate-limiter og slår op: er adressen forhåndsgodkendt, eller hører domænet til en godkendt skole?
3. **Kendt:** serveren laver en tilfældig engangskode, gemmer kun dens hash sammen med mailadresse, spil og `expires_at` (nu plus 7 dage), og sender mailen straks. Svaret til siden er "sendt", uanset om adressen var kendt eller ej (så svaret ikke afslører, hvem der er godkendt).
4. **Ukendt:** serveren gemmer en anmodning og underretter administratoren, som godkender med ét klik. Godkendelsen sender læreren det friske link.
5. Mailen indeholder et magic link `…/laerer-assistent.html?kode=<personlig kode>`. Cockpittet læser parameteren, fjerner den straks fra adresselinjen med `history.replaceState`, og kalder `api/laereradgang` med `action: "aabn"` og koden.
6. Serveren sammenligner hashen, tjekker `expires_at` og mailadressen og svarer med enten bundtets nøgle (med `Cache-Control: no-store`) eller en statuskode (`udloebet`, `ugyldig`). Nøglen bruges straks til `unlock()` (afsnit 24) og gemmes højst i `sessionStorage`.
7. Er linket udløbet, viser cockpittet den venlige besked og formularen med mailadressen udfyldt (serveren kan sende adressen med tilbage, hvis den kendes), så et nyt link kan bestilles med ét klik.

**Datamodel (SQLite eller tilsvarende):**

- `approved_emails (email unique, name)` og `approved_domains (domain unique, school_name)` til forhåndsgodkendelse. Domæner sammenlignes med små bogstaver.
- `access_tokens (id, email, game_id, token_hash, expires_at, created_at, used_at)`. `token_hash` er SHA-256 af en tilfældig værdi på mindst 128 bit (`random_bytes(16)` eller mere i PHP, `crypto.randomBytes` i Node). Her er hash i orden, fordi værdien er helt tilfældig og lang og kan kun slås op, ikke gættes. Det er en anden situation end en lærerkode, som en person har fundet på.
- `requests (email, name, school, game_id, status)` for ukendte adresser og `send_log (email, ip_address, sent_at)` til rate limiting (fx højst 5 pr. IP på 10 minutter, og et loft pr. adresse).
- Slet udløbne rækker løbende.

**Mailtekst.** Mailen er i spillets visuelle stil, nævner spillets navn og indeholder altid udløbsdatoen som en rigtig dato, regnet ud på serveren:

> Dette adgangslink er gyldigt i 7 dage (indtil DD-MM-YYYY). Herefter skal du blot bestille et nyt link på siden.

Mailen indeholder ingen anden kode end den personlige. Den indeholder ikke bundtets nøgle. Linket bør ikke sendes videre; skriv det.

**Skitse af endepunktet (PHP, forkortet):**

```php
// api/laereradgang.php (skitse). Forbered statements, svar altid som JSON, og brug aldrig mailadressen i et svar til en ukendt.
function udsted_link(PDO $db, string $email, string $spil): array {
    $raa = bin2hex(random_bytes(16));                          // 128 bit, vises kun i mailen
    $udloeb = (new DateTimeImmutable('+7 days'));
    $db->prepare('INSERT INTO access_tokens (email, game_id, token_hash, expires_at) VALUES (?,?,?,?)')
       ->execute([$email, $spil, hash('sha256', $raa), $udloeb->format('Y-m-d H:i:s')]);
    return [$raa, $udloeb->format('d-m-Y')];                   // datoen skal stå i mailen
}
function aabn(PDO $db, string $raa, string $spil, string $bundtNoegle): array {
    $st = $db->prepare('SELECT email, expires_at FROM access_tokens WHERE token_hash = ? AND game_id = ?');
    $st->execute([hash('sha256', $raa), $spil]);
    $r = $st->fetch();
    if (!$r) return ['status' => 'ugyldig'];
    if (strtotime($r['expires_at']) < time()) return ['status' => 'udloebet', 'email' => $r['email']];
    return ['status' => 'ok', 'noegle' => $bundtNoegle];       // bundtNoegle ligger i en miljøvariabel eller en fil uden for webroden
}
```

**Status i casespil.dk (commit 457fa0e) og fælderne deri.** Tokentabel, 7 dages udløb, serverside `verify`, udløbsbesked med mailadressen udfyldt og mail med udløbstidspunkt er nu på plads, og det virker som beskrevet. Ved gennemgang og en kørsel af koden lokalt (PHP og SQLite) viste fem ting sig, som standarden derfor kræver:

1. **Den korte kode er den svageste adgang.** Ud over det lange token udsteder koden en kort kode (`L-` og 6 hex-tegn, 24 bit), som verify-endepunktet accepterer alene og slår op på tværs af alle lærere. Endepunktet har ingen rate limiting (kørt: 300 gæt i træk fik 300 svar uden 429), så en angriber kan prøve sig frem, og hvert ramt gæt giver bundtets nøgle. Brug kun det lange token som adgang. Skal der være en kort kode, så kun sammen med mailadressen, med mindst 64 bit, og med et loft pr. IP og pr. adresse på selve `verify`.
2. **Nøglen er den samme for alle og står i kildekoden.** Serveren returnerer en fælles `master_key`, som står i `get_games_catalog()` og dermed i versionshistorikken (Fjords er et ord med årstal). Udløbet styrer kun, hvem der kan hente nøglen, ikke hvor længe nøglen virker. Hold nøglen uden for repoet (miljø eller fil uden for webroden), brug en tilfældig nøgle, og udskift den og byg bundtet på ny, når et semester slutter eller ved mistanke om lækage.
3. **Klienten må ikke have en lokal omvej.** Cockpittet prøver serveren, men falder tilbage til at låse op lokalt med det indtastede, "hvis masternøgle eller offline", også når serveren har svaret `udloebet` på en tidligere, eller netværket fejler. Så omgår den, der kender en nøgle, hele udløbet. Svarer serveren ugyldig, udløbet eller en fejl, vises beskeden, og der låses ikke op lokalt. Offline-brug skal være et bevidst valg, ikke et fald tilbage.
4. **Tokens gemmes som hash.** Tabellen gemmer token og kort kode i klartekst, så en læst database giver gyldig adgang. Gem SHA-256 af tokenet (afsnittets skitse) og slet udløbne rækker løbende.
5. **Linket bliver stående i adresselinjen.** Cockpittet fjerner ikke `?token=` efter indlæsning. Kald `history.replaceState` straks, så linket ikke ligger i historik, skærmbilleder og `Referer`.

Mindre afvigelser: mailen skriver "indtil 17.10.2026 kl. 16:46" og ikke den faste tekst med DD-MM-YYYY; svaret skelner mellem "sendt" og "afventer godkendelse", så et gæt kan afsløre, om en adresse er godkendt (det kan være et bevidst valg, men så skal det være et valg); udløbssvaret sender mailadressen tilbage til den, der har en udløbet kode (send den kun, når brugeren selv har tastet den); og der er ingen grænse pr. mailadresse, så en lærers indbakke kan oversvømmes. Administratorens standardadgangskode genereres stadig af kildekoden.

**Krav til driften:**

- Bundtnøglen, administratorens adgangskode og SMTP-oplysninger ligger uden for det, der serveres, og ikke i versionshistorikken. Ingen standardadgangskode i kildekoden: ved første kørsel genereres en tilfældig, som vises én gang, eller den læses fra miljøet.
- Datamappen er lukket for web (`Require all denied`), og databasefilen ligger ikke i webroden, hvis hosten tillader det.
- Mails sendes med afsenderdomænets SPF og DKIM, og administratoren har en testmail og et afsendelseslog, så man kan se, om en lærer fik sin mail.
- Spillets egen mail (andre sprog, andet navn) bruger spillets navn fra datasættet, ikke en fast tekst.

**Tests, der skal bestå:**

1. Et kendt domæne får en mail med det samme, og mailen indeholder en udløbsdato 7 dage frem i formatet DD-MM-YYYY.
2. En ukendt adresse får samme svar som en kendt, og administratoren får besked.
3. Et friskt link åbner cockpittet; samme link efter forfalsket tid (sæt `expires_at` til i går) giver `udloebet`, den venlige besked og en formular med adressen udfyldt.
4. Et gættet eller ændret token giver `ugyldig`, og 6 hurtige anmodninger fra samme IP giver svar 429.
5. Linket står ikke længere i adresselinjen efter indlæsning, og nøglen ligger ikke i klartekst i HTML, JavaScript eller versionshistorik (`grep` i den publicerede mappe og `git log -S` på nøglen).
6. `laerer.html?kode=…` ender i cockpittet, og ingen .docx, .pdf eller .zip kan hentes på en gæt-sti.
