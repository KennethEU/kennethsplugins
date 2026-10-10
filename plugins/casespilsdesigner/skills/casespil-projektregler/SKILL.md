---
name: casespil-projektregler
description: Projektets faste regler for casespil (også kaldet rollespil), der overstyrer de øvrige casespilsskills ved uenighed. Ingen ritualsætninger, kun normalversion af rollekort som standard, ingen faste minuttal, ingen tankestreger, begrænsning af faglige begreber, beregner-tjek, fælles kilde til tal og skjult information, offentlige sider uden modelsvar og backup også ved små rettelser. Læs altid før casespilsmaterialer produceres eller ændres, og sammen med alle andre casespil-skills.
---

# Projektregler for casespil

Disse regler går forud for de generelle casespilsskills, hvor de er uenige.

## Overstyringer

1. **Ingen ritualer eller indramning.** Skriv ikke "I spiller en rolle", "træd ud af rollen", "I er nu jer selv igen", "sig dem højt" eller lignende i materialer til eleverne eller i lærerguiden. Eleverne ved det godt. Det gælder også lærerguidens afsnit om psykologisk sikkerhed: behold indholdet (observatørmulighed, bedøm rollen og ikke personen), men skriv det som konkrete handlinger og ikke som sætninger, læreren skal sige.
2. **Én rollekort-version er nok.** Tre versioner (stærk, normal, støtte) laves kun, hvis læreren beder om det. Fjord Outdoor har kun normalversionen. Konsistenstjek, rollekort-docx og laererguide-docx skal ikke fejle på manglende støtte- og stærkversion.
3. **Faste minuttal** bruges aldrig i elevmaterialer. I lærerguiden kun som rækkefølge og relativ vægt.
4. **Sprog:** dansk, ingen lange tankestreger.
5. **Ordvalg:** skriv casespil i alle tekster, filnavne og overskrifter. Ordet rollespil forstås som det samme, og læreren må gerne bruge begge ord, men materialerne siger casespil.
6. **AI-assistenter følger sprogreglerne.** Systemprompter til elevernes rådgiver og til lærerens assistent indeholder reglerne ovenfor (ingen faste minuttal, ingen rituelle fraser, ingen lange tankestreger) og henter fasenavne, roller og tal fra datasættet i stedet for at gentage dem som tekst. En prompt med egne fasenavne kommer før eller siden til at sige noget andet end materialerne.

## Tillæg til design

1. **Begrænsningsregel for begreber.** Et casespil må ikke bære flere faglige begreber, end eleverne kan overskue på tiden. Hvis en model (fx BCG) kun ændrer sig på grund af forhold, eleverne ikke kan påvirke i spillet, og dermed forvirrer valget mellem "investér mere" og "investér normalt", så skær den ud af selve resultatet og behold den i forberedelsen eller debriefingen.
2. **Beregner-tjek (nyt punkt i konsistenstjek).** Når spillet har penge, grænser og tilfældighed: tjek at (a) pilot- og fuldgrænser står ens overalt, (b) reserveformlen er den samme i elevintro, bilag og casekort, (c) straffen for ikke at forsvare et kerneprodukt er i beregneren, (d) beregnerens parametre og showets parametre er identiske, (e) resultatet ikke kan læses ud af elevmaterialerne.
3. **Fælles kilde.** Hold tal og regler i ét sæt, og kopiér derfra til bilag, rådgiverens casekort, facit og show.
4. **Skjult information:** hvert rollekort med skjult info skal kunne bruges uden at kræve, at eleven siger noget usandt. Regel til eleverne: man må holde noget tilbage, men ikke sige noget usandt.
5. **Rådgiver og rollekort:** rollekortenes overskrifter er faste, fordi en AI-rådgiver læser dem. Ændres de, skal rådgiveren tilpasses.
6. **Offentlige sider afslører ikke svar.** Webside, casespilsside (hub), casekort og introfilm viser aldrig det, eleverne selv skal finde ud af: modelsvar (fx BCG-placering og Ansoff-strategi ved projekterne) og beskrivelser af rollernes holdninger. Roller vises kun med titel, antal stemmer og særlig beføjelse. Roller, titler, stemmetal og beløb hentes fra rollekort og bilag og opfindes aldrig (i Fjord Outdoor var seks bestyrelsesroller opfundet og passede ikke til kortene). Siderne gengiver de regler, der gør spillet forståeligt: stemmeregel, veto, hvad der sker uden flertal, særlige beslutninger og hvad der sker med det ubrugte.

7. **Fælles kode har ingen spilspecifikke fakta.** Kode, der bruges af flere spil (lærer-motor, beregnere, afspillere), indeholder ingen rolle-id'er, projektnavne, antal eller fasenavne. Det står i spillets datasæt. Fælles kode findes i én kopi.
8. **Beregnere har én plan og invarianter.** En gruppeberegner og en printliste bygger på samme plan, og antal elever, pladser og kort skal passe for alle elevtal i et rimeligt interval. Test det med en kørsel over hele intervallet (fx 4 til 80 elever), ikke med to eksempler. Under minimumsantallet vises en advarsel og et råd om en miniversion.
9. **Fortroligt lærermateriale ligger krypteret.** Facit, cheatsheet, hemmeligheder og rollekoder står aldrig i klartekst i en side. Lærerkoden kontrolleres ved selve dekrypteringen (ingen gemt hurtig hash) og er lang og tilfældig.

## Tillæg til produktion

1. **Backup før ændring** i en arkivmappe med sigende navn. Slet aldrig. Det gælder også ved gennemgang og små rettelser, ikke kun ved nybyggeri.
2. **Test** af digitale dele på computer og mobil, med billede, før det kaldes færdigt.
3. **Delt materiale:** hvad der må ligge offentligt (webside, casespilsside, casekort, intro) bestemmes ud fra rollekortenes skjulte information og af reglen om modelsvar under Tillæg til design, punkt 6.
4. **Når en del skæres væk**, ryd også op i resttekster (debriefingsspørgsmål, "hvorfor"-lister, overskrifter).
5. **Layout testes med langt indhold og på smalle skærme.** Prøv et meget langt rollekort eller en lang lærerguide i arbejdsbordet (skrivefeltet skal blive på skærmen), og tjek 320 px (ingen vandret scroll).
