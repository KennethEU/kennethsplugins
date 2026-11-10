---
name: bloom-planlaeg-time
description: "Planlægger en tre-faset time med lektietjek, arbejdsspørgsmål i par eller grupper og afsluttende diskussion, med Bloom-progression og arbejdsformer. Brug når læreren siger \"planlæg en time\", \"klasseflow\", \"lektionsstruktur\", \"tre faser\", \"hvad skal vi lave i timen\" ud fra en fagtekst. Brug ikke til casespil eller rollespil, gruppearbejdsdagsordener (dagsorden-lav), et sæt spørgsmål uden timeplan (bloom-spoergsmaal-til-tekst) eller en time om et emne uden fagtekst, hvor målet er at få alle med (klasseledelse-planlaeg-lektion) eller en enkelt CL-øvelse (cl-find-oevelse)."
argument-hint: "[fagtekst, emne eller tidsramme]"
allowed-tools:
  - Read
  - Glob
  - Skill
  - Write
---

# Klasseflow: tre-faset time om en fagtekst

Planlæg en time med lektietjek, arbejdsspørgsmål i par eller grupper og en afslutning, hvor alle tager stilling.

**Skal kendes:** teksten eller emnet, og hvor lang timen er. Følg "Arbejdsgang" i `bloom-spoergsmaalsregler`: i hurtig-tilstand springer du Gate 1 og 2 over, skriver antagelserne i én linje og afleverer planen med det samme.

## Standardstruktur

**45 minutter:**

| Fase | Tid | Indhold | Bloom-niveau | Arbejdsform |
|------|-----|---------|--------------|-------------|
| 1. Lektietjek | 7 min | 3 spørgsmål | Huske/Forstå | Alene uden skærm, så sidemand, så opsamling |
| 2. Arbejde | 20 min | 3 til 4 spørgsmål | Anvende/Analysere | Par eller grupper |
| 3. Diskussion | 13 min | 1 spørgsmål | Evaluere/Skabe | Sidemand, klasse, og alle skriver 2 til 3 linjer til sidst |

De sidste 5 minutter går til start og overgange.

**90 minutter:**

| Fase | Tid | Indhold | Bloom-niveau | Arbejdsform |
|------|-----|---------|--------------|-------------|
| 1. Lektietjek | 10 min | 3 spørgsmål | Huske/Forstå | Alene uden skærm, så sidemand, så opsamling |
| 2. Arbejde, runde 1 | 20 min | 2 til 3 spørgsmål | Anvende | Par |
| Pause | 5 til 10 min | | | |
| 3. Arbejde, runde 2 | 25 min | 2 til 3 spørgsmål | Analysere | Grupper, med kort opsamling |
| 4. Diskussion og skrivning | 20 min | 1 spørgsmål | Evaluere/Skabe | Sidemand, klasse, og alle skriver 5 minutter til sidst |

Resten er start, overgange og luft. Læg ikke flere faser ind: højst 4 faser på 90 minutter og højst 3 på 45.

## Regler for planen

- **Lektietjekket er genkaldelse:** alle skriver svar alene, før nogen siger noget. Spørg ikke ud i klassen, hvem der kan svare.
- **Har mange ikke læst,** så lad alle læse et kort uddrag i timen først, og lav tjekket bagefter. Udpeg ikke dem, der ikke har læst.
- **Afslutningen er for alle:** diskussionen slutter med, at hver elev skriver sit eget svar. Den fase må ikke skæres, hvis tiden løber. Skær i stedet et spørgsmål i arbejdsfasen.
- **Lav energi, fx fredag eftermiddag:** gør arbejdsfasen mere aktiv med en case eller en kort debat, ikke med flere faser.
- **Ingen nye ark:** spørgsmålene vises på slide, tavle eller dida-plan.
- **Tider:** regn overgange med, og tjek, at tiderne summer til timens længde.

## Trin

1. **Læs skillen** `${CLAUDE_SKILL_DIR}/../bloom-spoergsmaalsregler/SKILL.md`.

### Gate 1: Afklar rammer (kun uden for hurtig-tilstand, VENT på svar)

Spørg kun om det, der mangler, samlet i én besked: timens længde, om eleverne har læst teksten hjemme, og om der er et begreb eller mål, læreren vil prioritere.

**VENT** på svar.

### Gate 2: Vis strukturen (kun uden for hurtig-tilstand, VENT på OK)

Vis den tilpassede struktur som tabel med én linjes anbefaling, og spørg: "Passer strukturen?"

**VENT** på OK.

### Skriv planen

2. **Lektietjek:** 3 spørgsmål på Huske/Forstå, der viser, om eleverne har læst.
3. **Arbejde:** spørgsmål på Anvende og Analysere til par eller grupper, skrevet færdigt.
4. **Afslutning:** ét åbent spørgsmål på Evaluere/Skabe, og det, eleverne skriver til sidst.
5. **Kvalitetstjek** stille: Bygger faserne på hinanden, følger spørgsmålene reglerne, og summer tiderne?

## Sådan afleverer du

**Kort version (standard):**

- Én linje øverst med antagelserne, fx "Antaget: 90 min. med pause, de fleste har læst."
- Tabellen med faser, tid og arbejdsform.
- Spørgsmålene under hver fase med Bloom-niveau i parentes.
- Én linje: "Kan springes over: [et spørgsmål i arbejdsfasen]."
- Én linje til sidst: "Sig til, hvis noget skal ændres, eller hvis du vil have planen som dida-plan til storskærmen eller en fuld drejebog."

Vil læreren have dida-plan, så start `dida-plan`, og giv den planen, så den ikke spørger igen. Vil læreren have en drejebog med replikker og deltagelseskort, så start `klasseledelse-planlaeg-lektion` med planen. Er en skill ikke tilgængelig, så sig det, og fortsæt uden.

---

## Completion Status

- **DONE**: Timestruktur med spørgsmål leveret
- **DONE_WITH_CONCERNS**: Leveret, men tidsrammen er stram
- **NEEDS_CONTEXT**: Mangler tekst eller emne, eller timens længde
