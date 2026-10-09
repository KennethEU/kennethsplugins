---
name: casespil-konsistenstjek
description: "Kvalitetssikrer færdige casespilsmaterialer (også rollespilsmaterialer) før de bruges i undervisningen: krydsreferencer, stemmematematik, person-perspektiv, sprog, balance, facilitering, beregner og digitale dele. Brug efter produktion og altid før levering, og når læreren spørger \"passer det hele sammen\", \"er det klar til print\", \"tjek lige alt\", kvalitetssikring eller konsistenstjek af et casespil eller rollespil. Brug ikke til eksamenscases eller andre materialer uden for casespil og rollespil."
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Konsistenstjek for Casespilsmaterialer

**Projektregler:** `casespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Kør dette tjek EFTER at alle materialer er genereret, MEN FØR levering til brugeren. Rapporten præsenteres som en samlet liste med ✅ (bestået) eller ❌ (fejl) for hvert punkt.

## 0. Kør scriptet først

Kør det deterministiske sprogtjek på alle leverede filer (.docx, .md, .html), før du læser noget selv. Det finder tankestreger, ASCII-erstatninger for æøå, delte sammensatte ord, ritualsætninger, `maks.`, `à`, `60 %` og minuttal:

```
python3 "${CLAUDE_SKILL_DIR}/../casespil-sprogtjek/scripts/sprogtjek.py" <materialemappe>
```

Fejl (FEJL) skal rettes. Advarsler vurderes. Punkt 4 nedenfor dækker kun det, scriptet ikke kan afgøre.

## 1. Krydsreference-tjek

For hvert rollekort, verificér:
- [ ] Nævner kort A noget om kort B → stemmer det med kort B's faktiske indhold?
- [ ] Refererer dilemmaer til positioner der faktisk findes på de nævnte kort?
- [ ] Er krydsreferencer symmetriske? (Hvis A har dilemma om B, har B perspektiv på A?)
- [ ] Har spilfaserne samme navne, numre og rækkefølge i elevintroduktion, rollekortenes faseguide, lærerguide og, hvis de findes, webside og rådgiver? Intro og Debriefing må stå som før- og eftertrin uden fasenummer, men er ikke rådgiverfaser.

**Typisk fejl:** Rollekort A siger "Professor Andersen foreslår 60 % af median" — men professor Andersens kort siger 50 %.

## 2. Stemmematematik-tjek

- [ ] Kan forslag X faktisk opnå nok stemmer til vedtagelse?
- [ ] Er der mindst 2-3 mulige vindende koalitioner?
- [ ] Kan ingen enkelt koalition af to roller opnå flertal alene?
- [ ] Kan en blokerende minoritet forhindre ALT? (bør undgås)
- [ ] Stemmer det samlede stemmetal med det der står i elevintroduktionen?

**Beregn:** List alle roller + stemmer. Beregn flertalskrav. List alle koalitioner med ≥ flertalskrav.

## 3. Person-perspektiv-tjek

For hvert rollekort, verificér:
- [ ] Baggrund er konsekvent i 2. person ("Du er...")
- [ ] Argumenter er konsekvent i 1. person ("Mine data viser...")
- [ ] Dilemmaer er konsekvent i 2. person ("Skal du...?")
- [ ] Tip er konsekvent i 2. person imperativ ("Brug din...")
- [ ] Skjult information er i 2. person ("Du ved at...")
- [ ] Der blandes ALDRIG perspektiver inden for samme felt

## 4. Sprogligt tjek (dansk)

- [ ] Alle æ, ø, å er korrekte (aldrig "ae", "oe", "aa")
- [ ] Sammensatte ord uden mellemrum ("fattigdomsgrænse", ikke "fattigdoms grænse")
- [ ] "maks." (ikke "max.")
- [ ] "à" i "grupper à 4-5 elever" (ikke "a")
- [ ] Bestemt artikel ved institutionsnavne ("Finansministeriet", ikke "finansministeriet")
- [ ] Ingen ufuldstændige sætninger
- [ ] Konsekvent brug af fagtermer (samme term hele vejen)

## 5. Balancetjek

- [ ] Har ALLE roller mindst ét stærkt argument?
- [ ] Har ALLE roller mindst ét ægte dilemma?
- [ ] Er der mindst én rolle med kompromis/brobygger-position?
- [ ] Er der mindst én rolle med uformel magt (wildcard/moralsk autoritet)?
- [ ] Er ingen rolle "oplagt vinder" — alle har trade-offs?

## 6. Differentierings-tjek

**Normalversionen er altid nok.** Mange casespil laves bevidst med kun én simpel rollekort-version, og nogle gange med en AI-rådgiver som støtte til de svage elever. Mangler støtte- og stærkversion, er det IKKE en fejl. Skriv i rapporten "✅ Kun normalversion (bevidst valg)". Tjek støtte- og stærkversion kun, hvis de findes.

### Normal-version (tjek altid):
- [ ] Passer på 1 A4-side?
- [ ] Har faseguide-tabel (eller faseguide på bagsiden)?
- [ ] Har alle sektioner (header, mål, baggrund, holdning, værdier, argumenter, dilemmaer, tip)?

### Støtte-version (kun hvis den findes):
- [ ] Er mindst dobbelt så lang som normal (2 sider)?
- [ ] Har "sig f.eks." til HVERT argument?
- [ ] Har alliancetabel med konkrete sætninger?
- [ ] Har ordliste med mindst 3 fagbegreber?
- [ ] Har nødhjælpsboks (gul)?
- [ ] Har forhandlingssætninger (grøn)?
- [ ] Har faseguide?

### Stærk-version (kun hvis den findes):
- [ ] Passer på 1 A4-side (kompakt)?
- [ ] Har stikord i stedet for fuldtekst-argumenter?
- [ ] Har teori-tags (fx [NEO], [REAL])?
- [ ] Har INGEN faseguide?
- [ ] Har tom noteboks?

### AI-rådgiver som støtte (kun hvis den findes):
- [ ] Kender kun fælles casekort og elevens eget rollekort, ikke de andre rollers kort?
- [ ] Afslører ikke andre rollers skjulte information?
- [ ] Bygger på de samme tal som bilag og rollekort?

## 7. Faciliterings-tjek (lærerguide)

- [ ] Har konkrete overgangssætninger til HVER faseovergang?
- [ ] Har tegn-på-godt/dårligt-flow for forhandlingsfasen?
- [ ] Har kort afsnit om ramme og tryghed, uden ritualsætninger som "I spiller en rolle"?
- [ ] Har RAS-debriefing med formålsbeskrivelse for hvert trin?
- [ ] Har eksplicit overgangssætning mellem A og S?
- [ ] Har inject drama-kort (mindst 2)?
- [ ] Har differentierings-sektion (ved flere versioner: råd til diskret uddeling; ved kun normalversion: kort note om det bevidste valg)?
- [ ] Har forberedelsestjekliste?
- [ ] Angiver at elevintro uddeles FØR rollekort?
- [ ] Har INGEN faste minuttal (kun rækkefølge og relativ vægtning)?

## 8. Beregner- og digitaltjek (kun hvis der er penge, grænser, tilfældighed eller digitale dele)

Kilder: `casespil-projektregler` (beregner-tjek) og `casespil-digitale-tillaeg` (tjekliste og teknisk reference).

- [ ] Pilot- og fuldgrænser står ens i elevintro, bilag, casekort, facit og show?
- [ ] Reserveformlen er den samme overalt?
- [ ] Straffen for ikke at forsvare et kerneprodukt er med i beregneren?
- [ ] Beregnerens og showets parametre er identiske?
- [ ] Resultatet kan ikke læses ud af elevmaterialer, webside, casespilsside eller casekort?
- [ ] Skjult information står ikke på offentlige sider eller i fælles billedtekster?
- [ ] Ingen BCG- eller Ansoff-svar og ingen beskrivelser af rollernes holdninger på offentlige sider (casespilssiden viser roller kun med titel, stemmetal og særlig beføjelse)?
- [ ] Roller, titler, stemmetal, beløb og regler på casespilssiden er sammenholdt med rollekort og bilag (intet opfundet), og reglerne om stemmer, veto, standardplan, særlige beslutninger og reserve er med?
- [ ] Spilfaserne har samme navne og numre overalt, og rådgiver og webside viser kun spilfaserne?
- [ ] Rollekoderne på kortene matcher hasherne i rådgiveren, og koderne på kort og i lærervinduet er ens?
- [ ] Rådgiverens fejlbesked og casespilssidens tekst skriver kun "fra dit kort", hvis koden står på kortet?
- [ ] Spilintroens scenetekster og voiceover er tjekket mod bilagene (ingen overdrivelser eller modsigelser; voiceover kan ikke rettes uden ny indtaling)?
- [ ] Forsiden har ét menupunkt og en hero-knap til casespilssiden, intet link til rådgiveren og ingen popup, og gamle `#intro`-links sendes videre?
- [ ] Ingen død kode efter oprydning, og forsiden ser ens ud før og efter?
- [ ] Rådgiverens rollekortoverskrifter svarer til de faste overskrifter?
- [ ] Websiden viser virksomheden før investeringen og er mærket som fiktiv?
- [ ] Digitale dele er testet på computer og mobil (ingen vandret scroll, ingen konsolfejl)?
- [ ] Backup findes i arkivmappen, også for små rettelser?

## 9. Læsertest med frisk læser

Formål: finde det, forfatteren ikke selv kan se. Du kender hele casespillet; eleven kender kun to dokumenter.

1. Vælg elevintroduktionen og ét rollekort (helst den mest komplekse rolle).
2. Start en frisk læser uden forhistorie: en underagent, hvis du kan, ellers beder du læreren åbne en ny samtale. Giv læseren kun de to dokumenter og denne opgave: "Du er elev i 2.g og har fået disse to papirer. Svar kun ud fra dem."
3. Stil læseren disse spørgsmål:
   - Hvad er dit mål, og hvad er du uenig med de andre om?
   - Hvad må du holde tilbage, og hvad må du ikke sige?
   - Hvem taler du med først, og hvad siger du?
   - Hvad gør du, hvis du er i tvivl midt i spillet?
   - Hvilke ord eller tal forstår du ikke?
   - Hvad tror du, de andre roller vil?
4. Vurdér svarene:
   - [ ] Læseren kan svare på de første fem spørgsmål korrekt. Hvis ikke, er det uklart i materialet.
   - [ ] Læseren kan ikke redegøre sikkert for de andre rollers skjulte information. Kan den, er der en lækage.
   - [ ] Intet af det, læseren ikke forstår, er et fagbegreb, eleverne ikke har mødt.

Brug punktet, når rollekort og elevintroduktion er færdige. Det er ikke relevant ved miniversioner uden elevintroduktion.

## Rapportformat

Præsentér resultatet som:

```
KONSISTENSTJEK: [Casespilnavn]

1. KRYDSREFERENCER: ✅ / ❌ [detaljer]
2. STEMMEMATEMATIK: ✅ / ❌ [detaljer]
3. PERSON-PERSPEKTIV: ✅ / ❌ [detaljer]
4. SPROG: ✅ / ❌ [detaljer]
5. BALANCE: ✅ / ❌ [detaljer]
6. DIFFERENTIERING: ✅ / ❌ [detaljer]
7. FACILITERING: ✅ / ❌ [detaljer]
8. BEREGNER OG DIGITALE DELE: ✅ / ❌ / ikke relevant [detaljer]
9. LÆSERTEST: ✅ / ❌ / ikke relevant [detaljer]

SAMLET: X af 7 til 9 bestået (punkt 8 og 9 kun hvis relevante)
KRITISKE FEJL: [liste over fejl der SKAL rettes]
ANBEFALINGER: [liste over forbedringer der KAN rettes]
```

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Alle relevante tjek bestået, materialer er klar til print
- **DONE_WITH_CONCERNS** — Tjek gennemført, men med fund der bør adresseres (fx: mindre sprogfejl, svag balancering)
- **BLOCKED** — Kritiske fejl fundet der SKAL rettes før brug (fx: stemmematematik fejler, krydsreferencer er forkerte). Angiv præcist hvilke fejl der skal rettes, og foreslå at køre `casespil-rollekort` eller `casespil-laererguide` igen med rettelserne.
- **NEEDS_CONTEXT** — Materialer er ufuldstændige (fx: lærerguide mangler, kun nogle rollekort er genereret). Angiv hvad der mangler før tjekket kan gennemføres.
