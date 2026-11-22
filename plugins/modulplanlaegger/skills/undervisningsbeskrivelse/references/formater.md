# Formater

Tre formater: afsnittet på forløbssiden, dækningstabellen på holdsiden og den færdige tekst. Felterne følger UVM's skabelon.

## 1. Afsnittet på forløbssiden

Lægges under modultabellen, fx lige over "Fælles filer i mappen". Rækker i tabeller starter med ordet "Modul", ikke med et tal. Så forveksles de ikke med modultabellen.

```markdown
## Til undervisningsbeskrivelsen

*Udkast af Claude <dato> ud fra siden her (hold <hold>). Tjek og ret. Opdatér, når et modul er afholdt. Kun afholdte moduler tæller som dækket. Læreplanen: [<titel>](<link>).*

**Titel:** <forløbets titel>

**Indhold og fokus:** <2 til 4 sætninger: problemstilling, hvad eleverne har arbejdet med. "Planlagt:" for det, der mangler.>

**Faglige mål (læreplan 2.1, ordret):**

* "<ordret mål>": afholdt i modul <x–y>, planlagt i modul <z>

**Kernestof (læreplan 2.2, ordret):**

* <Disciplin>: "<ordret punkt>": afholdt i modul <x>
* Tjek: <noget, der måske hører til et punkt, med grund>

**Materiale** (samlet fra modulsiderne <dato>. Sider: læreren udfylder):

| Modul | Kernestof: <bogens titel> | Supplerende stof | Sider |
|-------|---------------------------|------------------|-------|
| Modul 1 (afholdt) | <afsnit> | <artikler, tal, cases, video> | ? |

* Engelsk materiale: <hvad, eller "ikke registreret">  (kun hvis læreplanen kræver det)
* Tid: <antal> afholdte moduler á <min> min, i alt <timer> timer undervisningstid (planlagte moduler tælles ikke med). Fordybelsestid: <timer eller "ikke opgjort">.
* Tilladt at tilgå via internettet: <materiale, eller "intet markeret">

**Arbejdsformer:** <de væsentligste, med modul: klasseundervisning, gruppearbejde, oplæg, skriftligt arbejde, projekt, it, udadvendte aktiviteter. "Planlagt:" for resten.>
```

## 2. Dækningstabellen på holdsiden

```markdown
## Dækning af læreplanen

*Udkast af Claude <dato>, samlet fra forløbssiderne. "Afholdt" tæller som dækket. "Planlagt" er ikke dækket endnu.*

*<Forløb, der ikke er kortlagt, fx fordi de kun ligger i Lectio.>*

**Faglige mål (læreplan 2.1)**

| Mål | <Forløb 1> | <Forløb 2> |
|-----|------------|------------|
| <målets første ord …> | afholdt (modul 2–4) | – |

**Kernestof (læreplan 2.2)**

| Kernestof | <Forløb 1> | <Forløb 2> |
|-----------|------------|------------|
| <Disciplin: punktets første ord …> | planlagt (7) | – |

**Mangler:** <kernestof og mål uden afholdt modul, og tværgående krav som omfang, engelsk materiale og projekter.>
```

Brug "–" for ikke dækket, "afholdt (modul)" og "planlagt (modul)". Alle mål og alle kernestofpunkter fra læreplanen skal være rækker, også dem uden dækning.

## 3. Teksten til Lectio eller UVM's skabelon

Én blok pr. forløb, kun gennemført undervisning, uden "Planlagt:" og uden Claudes noter. Felterne er dem fra UVM's skabelon. Læreren kopierer selv teksten ind i Lectio, hvor felterne passer, eller i skabelonen.

Forsiden og oversigten laves én gang for hele beskrivelsen:

```text
Termin: <fx maj-juni 2027> (skoleår <2026/27>)
Institution: <skole>
Uddannelse: <stx/hhx/htx/hf>
Fag og niveau: <fag og niveau, som i bekendtgørelsen>
Lærer(e): <navn>
Hold: <holdbetegnelse>

Oversigt over gennemførte forløb:
Forløb 1: <titel>
Forløb 2: <titel>
```

Derefter én blok pr. forløb:

```text
<Forløb nr.>: <titel>

Forløbets indhold og fokus:
<resumé med centrale problemstillinger>

Faglige mål:
- <ordret mål>

Kernestof:
- <Disciplin>: <ordret punkt>

Anvendt materiale:
Kernestof:
- <bog>, <afsnit> (<sider> sider)
Supplerende stof:
- <materiale> (<omfang>)
[TILLADT AT TILGÅ VIA INTERNETTET: <materiale>, kun hvis læreren har besluttet det]
Omfang i alt: <summen af siderne ovenfor>. Undervisningstid: <timer> timer (kun afholdte moduler). Fordybelsestid: <timer> timer.

Arbejdsformer:
<de væsentligste arbejdsformer>
```
