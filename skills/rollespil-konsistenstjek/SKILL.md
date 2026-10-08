---
name: rollespil-konsistenstjek
description: "Kører kvalitetssikring på rollespilsmaterialer før de bruges i undervisningen. Brug denne skill efter generering af rollekort, lærerguider og elevintroduktioner — og altid før endelig levering til brugeren. Trigger ved 'tjek', 'kvalitetssikring', 'konsistenstjek', 'klar til print', 'er det færdigt' eller lignende. Skillen tjekker krydsreferencer, stemmematematik, person-perspektiv, sprog, balance og differentiering."
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Konsistenstjek for Rollespilsmaterialer

**Projektregler:** `rollespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Kør dette tjek EFTER at alle materialer er genereret, MEN FØR levering til brugeren. Rapporten præsenteres som en samlet liste med ✅ (bestået) eller ❌ (fejl) for hvert punkt.

## 0. Kør scriptet først

Kør det deterministiske sprogtjek på alle leverede filer (.docx, .md, .html), før du læser noget selv. Det finder tankestreger, ASCII-erstatninger for æøå, delte sammensatte ord, ritualsætninger, `maks.`, `à`, `60 %` og minuttal:

```
python3 <plugin>/skills/rollespil-sprogkvalitet-da/scripts/sprogtjek.py <materialemappe>
```

Fejl (FEJL) skal rettes. Advarsler vurderes. Punkt 4 nedenfor dækker kun det, scriptet ikke kan afgøre.

## 1. Krydsreference-tjek

For hvert rollekort, verificér:
- [ ] Nævner kort A noget om kort B → stemmer det med kort B's faktiske indhold?
- [ ] Refererer dilemmaer til positioner der faktisk findes på de nævnte kort?
- [ ] Er krydsreferencer symmetriske? (Hvis A har dilemma om B, har B perspektiv på A?)

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

**Normalversionen er altid nok.** Mange rollespil laves bevidst med kun én simpel rollekort-version, og nogle gange med en AI-rådgiver som støtte til de svage elever. Mangler støtte- og stærkversion, er det IKKE en fejl. Skriv i rapporten "✅ Kun normalversion (bevidst valg)". Tjek støtte- og stærkversion kun, hvis de findes.

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

Kilder: `rollespil-projektregler` (beregner-tjek) og `rollespil-digitale-tillaeg` (tjekliste og teknisk reference).

- [ ] Pilot- og fuldgrænser står ens i elevintro, bilag, casekort, facit og show?
- [ ] Reserveformlen er den samme overalt?
- [ ] Straffen for ikke at forsvare et kerneprodukt er med i beregneren?
- [ ] Beregnerens og showets parametre er identiske?
- [ ] Resultatet kan ikke læses ud af elevmaterialer, webside eller casekort?
- [ ] Skjult information står ikke på offentlige sider eller i fælles billedtekster?
- [ ] Rådgiverens rollekortoverskrifter svarer til de faste overskrifter?
- [ ] Websiden viser virksomheden før investeringen og er mærket som fiktiv?
- [ ] Digitale dele er testet på computer og mobil (ingen vandret scroll, ingen konsolfejl)?
- [ ] Backup findes i arkivmappen?

## Rapportformat

Præsentér resultatet som:

```
KONSISTENSTJEK: [Rollespilnavn]

1. KRYDSREFERENCER: ✅ / ❌ [detaljer]
2. STEMMEMATEMATIK: ✅ / ❌ [detaljer]
3. PERSON-PERSPEKTIV: ✅ / ❌ [detaljer]
4. SPROG: ✅ / ❌ [detaljer]
5. BALANCE: ✅ / ❌ [detaljer]
6. DIFFERENTIERING: ✅ / ❌ [detaljer]
7. FACILITERING: ✅ / ❌ [detaljer]
8. BEREGNER OG DIGITALE DELE: ✅ / ❌ / ikke relevant [detaljer]

SAMLET: X af 7 (eller 8) bestået
KRITISKE FEJL: [liste over fejl der SKAL rettes]
ANBEFALINGER: [liste over forbedringer der KAN rettes]
```

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Alle relevante tjek bestået, materialer er klar til print
- **DONE_WITH_CONCERNS** — Tjek gennemført, men med fund der bør adresseres (fx: mindre sprogfejl, svag balancering)
- **BLOCKED** — Kritiske fejl fundet der SKAL rettes før brug (fx: stemmematematik fejler, krydsreferencer er forkerte). Angiv præcist hvilke fejl der skal rettes, og foreslå at køre `rollespil-rollekort-docx` eller `rollespil-laererguide-docx` igen med rettelserne.
- **NEEDS_CONTEXT** — Materialer er ufuldstændige (fx: lærerguide mangler, kun nogle rollekort er genereret). Angiv hvad der mangler før tjekket kan gennemføres.
