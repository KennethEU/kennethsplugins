---
name: rollespil-designprincipper
description: "De 10 universelle designprincipper og 8 rollespilsformater til dansk gymnasieundervisning. Brug ALTID denne skill når du designer et nyt rollespil, brainstormer idéer til simulationer, vælger rollespilsformat, eller rådgiver om rollespilsdesign. Trigger også ved 'rollespil', 'simulation', 'forhandlingsspil', 'lev-et-liv', 'krisehåndtering' eller lignende. Skillen er den faglige rygrad — den styrer HVAD der designes, mens rollespil-rollekort-docx styrer HVORDAN det produceres."
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Designprincipper for Rollespil i Gymnasieundervisning

**Næste skills:** produktion i `rollespil-rollekort-docx`, `rollespil-laererguide-docx` og `rollespil-laerermateriale`; digitale værktøjer i `rollespil-digitale-tillaeg`; kort version i `rollespil-mini`; kvalitetssikring i `rollespil-konsistenstjek`.

**Projektregler:** `rollespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill er den faglige rygrad i pluginet. Den indeholder principper, formater og designmønstre. Til uddybning, læs reference-filerne:

- **`references/cases.md`** — 14 afprøvede cases med roller, stemmer, knaphed og fagbegreber
- **`references/masterguide-kompakt.md`** — Teori (Kolb, Englund), skabeloner, koalitionsmatematik, evaluering, avancerede designmønstre

## De 10 universelle designprincipper

Disse gælder for ALLE rollespil uanset emne eller format:

| # | Princip | Kerneregel | Tjek-spørgsmål |
|---|---------|-----------|----------------|
| 1 | **Ægte ressourceknaphed** | Der er ALDRIG nok til alle | Er efterspørgslen > udbuddet? |
| 2 | **Magtasymmetri** | Ikke alle har lige magt | Har rollerne forskellige stemmevægte/beføjelser? |
| 3 | **Perspektiv-diversitet** | Roller ≠ elevernes eget perspektiv | Oplever eleverne noget ANDERLEDES? |
| 4 | **Progressiv kompleksitet** | Byg i lag, ikke alt på én gang | Er der en klar fase 1 → 2 → 3 struktur? |
| 5 | **Transparens og feedback** | Eleverne SER konsekvenserne | Får eleverne real-time feedback på valg? |
| 6 | **Struktureret dialog** | Faciliteret samtale, ikke fri-for-alle | Er der talerliste, runder, afstemning? |
| 7 | **Tryg ramme** | Fejl er OK i spillet. Læreren italesætter selv rammen, så materialerne bruger ingen ritualsætninger | Kan en utryg elev trække sig til en observatørrolle? |
| 8 | **Skjult information** | Udvalgte roller ved noget andre ikke ved | Er der mindst 1-2 roller med skjult info? |
| 9 | **Krydsreferencer** | Dilemmaer nævner andre roller eksplicit | Refererer hvert rollekort til mindst 2-3 andre? |
| 10 | **Differentieret materiale** | Normalversionen er standard. Støtte- og stærkversion laves kun, hvis læreren ønsker det. Støtte kan også være en AI-rådgiver, som de svage elever kan spørge | Er der støtte til de elever, der har brug for det, uanset om det er en støttekort-version eller en rådgiver? |

## Rollespilsformater

### A: Forhandling & Afstemning
Interessegrupper forhandler om fælles beslutning → formel afstemning.
- **Egnet til:** Demokrati, magtforhold, politisk beslutningstagning, EU
- **Knaphed:** Ressourcer (penge, stemmer, tid)
- **Nøgleprincipper:** P1 (knaphed), P2 (magtasymmetri), P6 (struktureret dialog)

### B: Krisehåndtering
Akut krise i realtid med injicerede begivenheder og tidspres.
- **Egnet til:** International politik, sikkerhedspolitik, krisekommunikation
- **Knaphed:** Tid, information, handlemuligheder
- **Nøgleprincipper:** P8 (skjult info), P5 (feedback), læreren som "nyhedsredaktør"

### C: Lev-et-Liv (livssimulation)
Elever lever et fiktivt liv med givne betingelser over flere runder.
- **Egnet til:** Social ulighed, velfærdsstat, empati, strukturelle forklaringer
- **Knaphed:** Penge, tid, muligheder (individuelt)
- **Nøgleprincipper:** P3 (perspektiv-diversitet), P5 (feedback via budget)

### D: Konsekvens-kredsløb
Politiske/økonomiske beslutninger → konsekvenser → nye problemer → nye beslutninger.
- **Egnet til:** Makroøkonomi, finanspolitik, systemtænkning
- **Knaphed:** Budgetter, kapacitet, tid (kumulativt)
- **Nøgleprincipper:** P5 (transparens), feedback-loops, trade-offs

### E: Retssag / Tribunal
Struktureret argumentation og bevisførelse med dommer, anklager, forsvar, vidner.
- **Egnet til:** Retsstat, retsprincipper, etik, argumentation
- **Knaphed:** Taletid, bevismateriale
- **Nøgleprincipper:** P6 (struktureret dialog er bærende)

### F: Virksomhedsbestyrelse / Strategimøde
Strategisk beslutning med modstridende analyser og stakeholder-pres.
- **Egnet til:** Erhvervsøkonomi, strategi, CSR, finansiering
- **Knaphed:** Kapital, markedsandel, omdømme
- **Nøgleprincipper:** Data-asymmetri, ekstern stakeholder-pres

### G: Parlamentarisk Lovproces
Fuld lovgivningsproces: partigrupper, udvalg, behandlinger, ændringsforslag, korridorpolitik.
- **Egnet til:** Lovgivning, parlamentarisme, EU's beslutningsproces
- **Knaphed:** Stemmetal, politisk kapital
- **Nøgleprincipper:** Partidisciplin, modulære lovforslag, korridorpolitik-fase

### H: Interaktiv Virksomhedssimulation (digital)
Webapp + Excel-regnskab, elever udforsker investeringer og ser finansielle konsekvenser.
- **Egnet til:** Erhvervsøkonomi, virksomhedsstrategi, regnskab
- **Knaphed:** Investeringsbudget, kapacitet
- **Nøgleprincipper:** Teori-tagging direkte i materialer, P5 (transparens)

## Kombination af formater

Formater kan kombineres for dybere læring. Maks. 2 formater per lektion. Eksempler:
- **C → A:** Lev som fattig → stem om velfærdspolitik (levede erfaringer → politik)
- **D → A:** Kør økonomien → forhandl krisepakke (konsekvenser → løsninger)
- **H → F:** Digital simulation → bestyrelsespræsentation (analyse → beslutning)

## Vigtige designmønstre

### Kompromisrollen
Design mindst én rolle hvis position bygger bro. Høj troværdighed, konkrete elementer fra 2-3 positioner.

### Wildcard-rollen
0 stemmer, stor moralsk autoritet. Stærke personlige argumenter i 1. person. En anden rolle kan "aktivere" wildcarden.

### Korridorpolitik
Uformel forhandlingsfase EFTER positioner er kendte, FØR endelig afstemning. 5-10 minutter.

### Teori-tagging
Navngiv fagbegreber direkte i materialer (stærk-version): [NEO], [REAL], [LIB] osv.

## Pointsystemer

ALDRIG i deliberative rollespil (Format A, E, G). Fjerner fokus fra argumentation. Talbaserede konsekvenser (budget, likviditet) er OK i Format C, D, H — men aldrig som leaderboard.

## Debriefing: RAS-modellen

| Trin | Formål | Varighed | Fokus |
|------|--------|----------|-------|
| R = Reaktion | Lade følelserne komme ud | Kort | Ventilere, ikke diskutere |
| A = Analyse | Koble oplevelse til fagbegreber | Lang | Kernen. "Hvorfor"-spørgsmål |
| S = Sammenfatning | Overføre til virkelighed | Medium | Teori + eksamensrelevans |

Eksplicit overgangssætning mellem A og S: "OK — nu har vi analyseret hvad der skete. Men hvad med den virkelige verden?"

## Reference-filer

Når du designer et nyt rollespil:

1. **Læs `references/cases.md`** — find et lignende case og brug det som udgangspunkt for roller, stemmematematik og fagbegreber
2. **Læs `references/masterguide-kompakt.md`** — for teori-begrundelser (Kolb, Englund), avancerede designmønstre (modulært scenarie-design, bilag-system), koalitionsmatematik, evaluering og rollekort-skabelon

Pluginet er selvstændigt. Den fulde masterguide (MASTERGUIDE_Rollespil_Samfundsfag_Erhvervsoekonomi_v3.md) kan lægges i arbejdsmappen som ekstra reference, men er ikke påkrævet.

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Rollespil designet med roller, konflikt, stemmematematik og format valgt
- **DONE_WITH_CONCERNS** — Design leveret, men med forbehold (fx: kun ét dilemma pr. rolle, eller balancen er skæv)
- **BLOCKED** — Kan ikke designe rollespil (fx: emnet har ingen naturlig konflikt, eller faget egner sig ikke til formatet)
- **NEEDS_CONTEXT** — Mangler information (fx: "Hvor mange elever er der?" eller "Hvilket fagligt emne?")
