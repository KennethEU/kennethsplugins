---
name: rollespil-laererguide-docx
description: Genererer lærerguider til rollespil med alle obligatoriske sektioner. Brug når brugeren beder om en lærerguide, facilitatorguide eller lærervejledning til et rollespil. Trigger også ved "lærerguide", "facilitering", "debriefing-spørgsmål" eller "hvad gør læreren". Skillen sikrer at ingen obligatoriske sektioner glemmes — især rammen, faseovergange og RAS-debriefing.
allowed-tools:
  - Read
  - Glob
  - Bash
  - Write
---

# Lærerguide-generering

**Projektregler:** `rollespil-projektregler` gælder altid og går forud, hvor den er uenig med denne skill.

Denne skill sikrer at alle obligatoriske sektioner kommer med i lærerguiden. Brug `rollespil-rollekort-docx`-skillen for selve docx-produktionen.

## Fase 0: Saml kontekst (automatisk — FØR alt andet)

1. Læs CLAUDE.md for at forstå lærerens fag og hold
2. Scan projektmappen for eksisterende rollekort og rollespilsdesign — lærerguiden SKAL matche rollekortene
3. Læs `rollespil-designprincipper`-skillen for at sikre debriefing og facilitering følger de 10 principper
4. Identificér faget og fagets fagbegreber — de skal bruges i debriefing-sektionen

**HÅRD REGEL:** Lærerguiden skrives ALTID efter rollekortene er færdige. Aldrig før.

---

## Obligatoriske sektioner (udelad ALDRIG nogen)

### 1. Oversigt
- Fag, niveau, varighed, klassestørrelse
- Læringsmål (konkrete, målbare)

### 2. Ramme og tryghed (kort, uden ritualer)
Læreren italesætter selv rammen, så guiden indeholder INGEN indramningssætninger (ikke "I spiller en rolle", "I er nu jer selv igen", "time-out" eller lignende). Skriv kun de praktiske valg:
- Observatørrolle-mulighed for utrygge elever
- Hvad læreren holder øje med (personangreb, en elev der trækker sig)
- Hvad der evalueres: argumenter og valg, ikke personer

### 3. Differentiering
- Normalversionen er standard. Hvis der også findes støtte- og/eller stærkversion: tabel over versionerne, råd til diskret uddeling og "bland versioner INDEN FOR gruppen, giv aldrig alle støttekort til én gruppe"
- Hvis der kun er en normalversion: skriv det kort som et bevidst valg. Nævn evt., at en AI-rådgiver pr. rolle kan være støtte til de svageste elever

### 4. Roller og stemmefordeling
Tabel med: Rolle | Organisation | Stemmer | Særlig beføjelse

### 5. Forberedelse (lærer)
Tjekliste med:
- [ ] Print elevintroduktion (1 pr. elev)
- [ ] Print rollekort (de versioner, der er lavet)
- [ ] Stil lokalet op
- [ ] Test evt. digitalt værktøj
- [ ] Elevintroduktion uddeles FØR rollekort

### 6. Tidsplan (UDEN minuttal)
"Du styrer selv tempoet — skemaet viser rækkefølge og relativ vægtning."

| Fase | Aktivitet | Lærers rolle |
|------|-----------|-------------|
| Intro | Præsentér scenarie | Facilitator |
| Fase 1 | Forberedelse | Cirkulér |
| Fase 2 — R1 | Åbningsstatements | Tidstager |
| Fase 2 — R2 | Fri forhandling | Observér |
| Fase 2 — R3 | Forslag + afstemning | Hold styr |
| Fase 3 | Debriefing (RAS) | Facilitator |
| Afslutning | Exit-ticket | Uddel |

### 7. Faseovergangssignaler
Konkrete sætninger med **fed** og *kursiv* til HVER overgang:
- Intro → Fase 1: "I har nu fået jeres rollekort..."
- Fase 1 → Fase 2: "Forberedelsen er slut. Nu går vi ind i [scenarienavn]..."
- Runde → Runde: "[Ordstyrer], forhandlingstiden er udløbet..."
- Fase 2 → Fase 3: "Forhandlingen er slut. Nu går vi i gang med debriefingen..."

### 8. Faciliterings-indikatorer

**Godt flow (lad det være!):**
- Elever taler højlydt i karakter
- Der grines og gestikuleres
- Elever forhandler i krogene

**Dårligt flow (intervener!):**
- Elever kigger på telefonen
- Ingen opsøger andre grupper
- For hurtig konsensus

**Interventioner uden at bryde flow:**
- Brug rollens navn, ikke elevens
- Stil åbne spørgsmål
- Aktivér stille grupper direkte

### 9. Inject drama (2-3 stk., brug HØJST ét)
| Type | Indhold | Hvornår |
|------|---------|---------|
| Nye data | "Ny rapport viser..." | Energien daler |
| Budgetpres | "Beregninger viser at..." | Konsensus for hurtigt |
| Eksternt deadline | "EU/regeringen kræver at..." | Manglende urgency |

### 10. Debriefing (RAS-modellen)

**R = Reaktion** (kort, formål: lade følelser komme ud)
- "Hvordan føltes det at spille jeres rolle?"
- "Hvad overraskede jer?"
- Rollespecifikke spørgsmål (wildcard, blokerer, kompromis, ordstyrer)

**A = Analyse** (lang, formål: koble oplevelse til fagbegreber)
- Advocacy-inquiry teknik: "Jeg lagde mærke til at... Hvordan skete det?"
- Magt, alliancer, argumentation
- Skriv nøgleord på tavlen

**Overgangssætning:** "OK — nu har vi analyseret hvad der skete. Men hvad med den virkelige verden?"

**S = Sammenfatning** (medium, formål: transfer til virkelighed)
- Teori-kobling: "Hvordan relaterer dette til [begreb]?"
- Virkelighedstransfer: "Hvor ser I denne dynamik i virkeligheden?"
- Meta-læring: "I har nu OPLEVET på egen krop at..."

### 11. Typiske problemer og løsninger
| Problem | Tegn | Løsning |
|---------|------|---------|
| Elever forstår ikke reglerne | Spørger konstant | Bedre intro, visuel guide |
| Én gruppe dominerer | Andre er passive | Justér stemmevægte |
| Deadlock | Ingen kan blive enige | Kompromisrolle, sænk flertal |
| For personligt | Elev virker ked | Stop, adressér, genopbyg |

### 12. Variationer
Beskriv mindst 2 variationer af rollespillet:
- **Kort version:** Hvilke faser/roller kan skæres væk og stadig bevare kernekonflikt?
- **Lang version:** Hvad kan tilføjes for at uddybe (ekstra runder, flere roller, bilag)?
- **Alternativt scenarie:** Kan samme rollespilsstruktur bruges med et andet emne i faget?

Variationerne hjælper læreren med at tilpasse rollespillet til forskellige holdstørrelser og tidsrammer.

---

## Completion Status

Afslut ALTID med én af:

- **DONE** — Lærerguide genereret med alle 12 obligatoriske sektioner
- **DONE_WITH_CONCERNS** — Guide leveret, men med mangler (fx: inject drama-kort mangler fordi scenariet er for kort, eller debriefing er generisk)
- **BLOCKED** — Kan ikke generere guide (fx: rollekort er ikke færdige endnu, rollespil-designprincipper-skill ikke tilgængelig)
- **NEEDS_CONTEXT** — Mangler information (fx: "Hvor lang tid har du til rollespillet?")
