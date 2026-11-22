# Formater

Tre formater: forløbsteksten på forløbssiden (som i Lectio), oversigten på holdsiden og UVM's skabelon, hvis skolen ikke bruger Lectio.

## 1. Forløbsteksten på forløbssiden

Lægges under modultabellen, fx lige over "Fælles filer i mappen". Felterne er Lectios felter for et forløb. Alt over boksen "Til læreren" skal kunne kopieres ind i Lectio og læses af eleverne.

```markdown
## Til undervisningsbeskrivelsen

*Tekst til forløbet i Lectio, felt for felt. Skrevet af Claude <dato> ud fra forløbssiden og modulsiderne. Tjek og ret. Noter til læreren står i boksen nederst og kommer ikke i Lectio. Krav: [Undervisningsbeskrivelse: vejledning og skabelon](<link>).*

**Forløb:** <titel>

**Periode:** <datoer eller "ikke angivet">. **Estimat:** <antal> moduler á <min> min (<timer> timer).

**Forløbsbeskrivelse**

<Problemstillingen som spørgsmål. 2 til 3 sætninger til eleven: hvad du lærer, og hvad forløbet ender med.>

Emner og begreber:

* <emne: begreber og teorier>

Materiale:

* Kernestof: <bog>, <afsnit>
* Supplerende stof: <artikler, tal, cases, video>

**Faglige mål**

Kernestof:

* <Disciplin>: <ordret punkt fra læreplanen 2.2>

Mål:

* <ordret mål fra læreplanen 2.1>

**Særlige fokuspunkter** (det skal du kunne)

* <verbum + indhold, bygget på modulernes mål>

**Arbejdsformer**

<De væsentligste arbejdsformer i hele sætninger.>

**Skriftligt arbejde**

<Titel og frist pr. aflevering, eller "Ingen afleveringer registreret i forløbet.">

> **Til læreren (kommer ikke i Lectio)**
>
> * Afholdt: modul <x-y>. Planlagt: modul <z> (<hvad>). Tag det ud, der ikke bliver til noget, før den endelige beskrivelse.
> * <Tjek: noget, der måske hører til et kernestofpunkt, med grund>
> * Sider mangler. <Engelsk materiale, fordybelsestid, internet til prøven, hvis det er relevant.>
```

## 2. Oversigten på holdsiden

```markdown
## Undervisningsbeskrivelse: forløbene

*Oversigt over holdets forløb (UVM's punkt 1). Teksten til Lectio står på hver forløbsside under "Til undervisningsbeskrivelsen". Opdateret af Claude <dato>.*

1. [<Forløb>](<link>): modul <x-y> afholdt, modul <z> planlagt
2. <Forløb, der kun ligger i Lectio> (ligger kun i Lectio)

## Mangler i læreplanen

*Kernestof og mål, som intet afholdt modul dækker endnu. <Forløb, der ikke er tjekket.>*

* **Kernestof:** <punkter>
* **Mål:** <punkter, kort>
* **Andet:** <omfang i sider, engelsk materiale, projekter og andre tværgående krav fra læreplanen>
```

Deler to hold siden, så lav en oversigt pr. hold.

## 3. UVM's skabelon

Bruges kun, hvis skolen ikke bruger Lectio. Forsiden laves én gang:

```text
Termin: <fx maj-juni 2027> (skoleår <2026/27>)
Institution: <skole>
Uddannelse: <stx/hhx/htx/hf>
Fag og niveau: <fag og niveau, som i bekendtgørelsen>
Lærer(e): <navn>
Hold: <holdbetegnelse>

Oversigt over gennemførte forløb:
Forløb 1: <titel>
```

Derefter én blok pr. forløb med felterne Forløbets indhold og fokus, Faglige mål, Kernestof, Anvendt materiale (kernestof og supplerende stof med omfang, undervisningstid og fordybelsestid) og Arbejdsformer. Indholdet er det samme som i afsnit 1.
