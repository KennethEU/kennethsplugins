---
name: dida-plan
description: "Omsætter en lektions- eller modulplan til en JSON-fil, der kan uploades på dida.dk/plan og vises på storskærm med køreplan, opgaver og timer, som eleverne følger i de elevaktive faser. Planen bruges ved siden af lærerens slides, som stadig bærer fagbegreber, figurer og billeder. Brug når læreren siger \"lav en dida-plan\", \"lav planen til dida\", \"vis planen på storskærm\", \"JSON til dida.dk/plan\", eller siger ja til tilbuddet fra en anden skill. Brug ikke til at lave selve planen fra bunden (klasseledelse-planlaeg-lektion), til PowerPoint-slides eller til en udretterdagsorden til gruppearbejde på elevernes telefoner (dagsorden-lav i pluginet udretterdagsorden)."
argument-hint: "[plan eller drejebog]"
allowed-tools:
  - Read
  - Glob
  - Write
  - Bash(python3:*)
---

# Plan til dida.dk

Lav en fil, klassen kan følge med i på storskærmen. Planen skal være enkel, og opgaverne skal være præcise. Filen må aldrig indeholde facit eller elevnavne.

## Trin

1. **Find planen.** Brug planen fra samtalen, eller læs filen, hvis du får en. Har du ingen plan, så bed om den, eller tilbyd at lave den med `klasseledelse-planlaeg-lektion`, og stop. Er den en liste over tekster og sider uden faser, så find ikke på faser. Sig det, og spørg.

### Gate 1: Vis trinene (VENT på OK)

Re-ground: "Her er de trin, klassen vil se på skærmen."

2. **Lav trinene efter reglerne nedenfor,** og vis dem:

| # | Overskrift | Min. | Form | Skærm | Opgaven i korte træk |
|---|-----------|------|------|-------|----------------------|

Skriv under tabellen: samlet tid mod modulets længde, og hvad du har slået sammen eller delt op. Mangler planen en tid eller en opgave, så spørg. Find ikke på indhold.

Spørg: "Passer trinene?"

**VENT** på OK.

### Skriv filen

3. **Skriv filen** med Write, efter formatet nedenfor, som `<titel>.dida-plan.json` i lærerens mappe. Kan du ikke skrive filer, så giv JSON'en i én kodeblok.
4. **Tjek filen:** kør `python3 "${CLAUDE_SKILL_DIR}/scripts/tjek_plan.py" "<fil>"`, og ret alle fejl. Kan du ikke køre scriptet, så gennemgå reglerne selv, og sig, at scriptet ikke er kørt.
5. **Aflever:** sig, hvor filen ligger, og at den uploades på dida.dk/plan. Filen bliver i browseren og sendes ikke til serveren. Nævn genvejene: pile skifter trin, mellemrum starter timeren, F giver fuld skærm, og N åbner lærernoter i eget vindue.

## Regler for trinene

- **Ét trin pr. fase i planen,** plus pause. Læg ikke ekstra trin til, og læg overgange ind i det trin, de hører til.
- **Skifter skærmen midt i en fase,** så del fasen i to trin, men kun hvis det ikke giver mere end ca. 6 trin i et modul på 90 minutter. Ellers skriv skiftet i opgaven, fx "Efter 6 minutter: én computer pr. par".
- **Har planen mange flere trin end det,** så sig, at den ser ud til at overskride aktivitetsbudgettet i `klasseledelse-principper`, og spørg, om den skal forenkles først.
- **`instruction` er skrevet til eleverne,** med "du" eller "I", i korte linjer. Det er opgaven, færdigformuleret, så de kan gå i gang uden at spørge.
- **`teacherNote` er til læreren:** replikker, hvad man skal gå efter, og hvad der kan skæres. Alt, hvad klassen ikke skal se, hører til her.
- **`doneWhen`** er noget, eleverne selv kan se, fx "Kædearket er udfyldt".
- **Ingen klokkeslæt** som "26-37". Kun varighed.
- **Tiderne** er hele minutter og summer til modulets længde. Passer de ikke, så sig det i Gate 1.

## Format (version 1)

```json
{
  "format": "dida-plan",
  "version": 1,
  "title": "Kort titel",
  "goal": "Målet eller problemformuleringen",
  "subject": "Fag",
  "moduleMinutes": 90,
  "steps": [
    {
      "heading": "Kort overskrift",
      "duration": 10,
      "workForm": "par",
      "screen": "nede",
      "instruction": "Opgaven til eleverne. \n giver linjeskift.",
      "doneWhen": "Hvornår de er klar",
      "note": "Bemærkning, klassen kan se",
      "teacherNote": "Kun til læreren"
    },
    { "heading": "Pause", "type": "pause", "duration": 5 }
  ]
}
```

- **Påkrævet:** `format`, `version`, `title`, `steps` og i hvert trin `heading`, `duration` og `instruction`. En pause behøver ingen `instruction`.
- **`workForm`:** `alene`, `par`, `gruppe` eller `klassen`.
- **`screen`:** `oppe` eller `nede`.
- Udelad felter, du ikke har indhold til. Filen er ren tekst uden HTML.

Formatet læses af `public/plan/plan.js` på dida.dk. Find ikke på nye felter, for siden viser dem ikke.

---

## Completion Status

- **DONE**: Fil skrevet og tjekket med scriptet
- **DONE_WITH_CONCERNS**: Fil skrevet, men scriptet er ikke kørt, eller tiderne summer ikke
- **NEEDS_CONTEXT**: Mangler en plan, tider eller opgaver
