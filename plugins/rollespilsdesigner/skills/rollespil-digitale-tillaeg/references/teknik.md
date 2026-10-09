# Tekniske principper og mønstre til digitale rollespilsværktøjer

Samlet fra Fjord Outdoor (AI-rådgiver, webside, facit, show, spilintro). Brug det som udgangspunkt, så hvert nyt værktøj ikke skal opfindes forfra. Alt er skrevet til enkeltstående HTML-sider, som en lærer kan lægge på en almindelig webhost eller åbne direkte fra en mappe.

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
- Kontrast og skriftstørrelse: mindst 16 px brødtekst, knapper der kan ramme med en tommelfinger. Regler for kontrast på mærker står i afsnit 13. Tekst inde i spilintroens scener er skærmgrafik og må være mindre end sidens brødtekst, men aldrig under 12 px (undertekster mindst 13 px).

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
6. **Test på en rigtig telefon, helst en iPhone.** Playwright med Chromium og en lille skærm efterligner ikke Safari. De fejl, der gjorde Fjord Outdoor frossen på mobilen (afsnit 14), blev opdaget på telefonen. Tjek: åbn og luk popup'en tre gange, tryk på alle menulinks, tryk Tilbage med popup'en åben, og afspil introen med lyden på.
7. **Gennemlæs som elev:** er der noget på en offentlig side, som røber skjult information eller resultatet af valgene?
8. **Efter ændringer:** tjek tal på tværs (bilag, casekort, facit, show) og ryd op i rester (overskrifter, debriefingsspørgsmål), når en del er fjernet.

## 10. Sikkerhed og ansvar

- Alt i en statisk side kan læses. Antag det.
- Skift API-nøgle før offentliggørelse, hvis den har stået i en side. Sæt dagsloft på proxy og nøgle.
- Mærk siden som fiktiv og AI-genereret. Skriv ikke rigtige personnavne eller virksomheder, hvor det kan forveksles med virkeligheden.
- Giv eleverne en kort besked om, at spørgsmål til rådgiveren gemmes (hvis de gemmes), og hvor længe.

## 11. Spilintro: opbygning og synkronisering

Introen er en afspiller, ikke en video. Scener, undertekster og lyd styres af ét tal: tiden. Det gør den let at rette (ret en tekst, ikke en filmfil) og lader læreren hoppe rundt.

**Filer:** `intro.html` (selvstændig side), en popup i `index.html` (afsnit 14 A til C), `voiceover.mp3` og billeder i `billeder/`. Popup og side er to udgaver af samme afspiller. I Fjord Outdoor ligger scener, CSS og script to steder; popup'ens klasser har præfikset `m-` og dens id'er hedder fx `mSc1`, så de ikke støder ind i sidens egne. En kopi driver fra originalen, og tal og tekster i introen er en del af den fælles kilde (SKILL.md, grundregel 1). Brug derfor en fælles `intro-data.js` med `SCENES` og `SUBTITLES` (et almindeligt `<script src>` virker også fra en lokal mappe), og ret altid begge sider, når en scenetekst ændres.

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
- **Tastatur, kun mens popup'en er åben:** mellemrum eller K afspiller og pauser, venstre og højre pil giver -10 og +10, F er fuld skærm, Escape lukker.
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

- **Tilgængelighed (anbefalet, ikke med i Fjord Outdoor):** gør tidslinjen til `role="slider"` med `aria-valuemin`, `aria-valuemax` og `aria-valuenow`, så den kan bruges med tastatur og skærmlæser. Flyt fokus ind i popup'en ved åbning og tilbage til knappen, der åbnede den, ved lukning.
- **Baggrundsvideo på forsiden:** sæt den på pause, når popup'en åbner, og start den igen ved lukning (undtagen ved `prefers-reduced-motion`). Fjord Outdoor satte den på pause og glemte at starte den igen.
- **Referér til elementer via variabler.** Dele af Fjord Outdoors deep link-kode brugte `mSplash` uden at have erklæret den. Det virkede kun, fordi browsere gør elementers id til globale navne. Det er skrøbeligt.

## 12. Voiceover med ElevenLabs

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

Disse fejl fik Fjord Outdoors forside til at virke frossen på telefonen. Ingen af dem viser sig tydeligt på en computer.

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

### D. Layoutregler til introen på mobil (højst 768 px)

- **Lodret stabling i kortoverskrifter:** overskrift og mærke må aldrig tvinges ud på samme linje. Sæt `flex-direction: column; align-items: flex-start; gap: 4px;` på rækken (fx `.m-role-top`), så et mærke aldrig klippes af mod skærmkanten.
- **Faser i 2 gange 2:** `grid-template-columns: repeat(2, 1fr); gap: 7px;` giver balance uden at scenen skal rulle.
- **Scenen må rulle indvendigt** (`overflow-y: auto; -webkit-overflow-scrolling: touch;`) med nok luft nederst (`padding-bottom` ca. 64 px) til undertekstbjælken.
- **Ingen forsinkelser på enkeltkort.** Undgå `transition-delay` og `opacity: 0; transform: translateY(12px)` på kort inde i en scene, der allerede fader ind. Det giver flimmer og hak på langsommere telefoner. Lad hele scenen fade, ikke hvert kort.
- **Hold animationerne lette.** Fuldskærmsbilleder med langsom zoom (`transform: scale` over 12 sek.) og filtre (`brightness`, `blur`) er dyre på mobil. Brug højst ét filter pr. lag, og undgå `backdrop-filter` på lag, der ligger oven på video.
- **Højde på iPhone:** `max-height: 100vh` regner Safaris adresselinje med og kan skubbe afspillerens knapper ud af skærmen. Skriv `max-height: 100vh; max-height: 100dvh;` (den sidste vinder, hvor den findes).
- **Tekststørrelse:** se afsnit 6. Minimum 12 px i scenerne og 13 px til undertekster.
