# Én spilfil: opbygning af et casespils data

Et casespil findes i flere udgaver: elevpakke, lærerpakke, miniside, lærercockpit, storskærm og AI-prompter. De bygges alle af én spilfil. Generatorerne laver kun layout. Erfaringen fra Strafudvalget (2026) var, at regeltekster, der stod direkte i generatorerne, skulle rettes tre til fem steder, og at det, der blev glemt ét sted, blev fundet af hvert review igen.

## Filer

```
produktion/
  spil.cjs          # den eneste kilde: data, tekster og små beregninger
  elev.cjs          # layout: elevpakke (docx og pdf)
  laerer.cjs        # layout: lærerpakke
  byg_web.cjs       # layout: miniside, spildata.js og krypteret lærerbundt
tests/<spil>.cjs    # tjekker blandt andet, at generatorerne ikke har egne spiltekster
```

Spilfilen er en `.cjs`-fil med rene data (som JSON, men med kommentarer), så små beregninger som elevfordeling og facit kan ligge ved siden af dataene og bruges af både papir, cockpit og test.

## Opbygning af spil.cjs

```js
module.exports = {
  // 1. Identitet. slug ændres aldrig (står i webadresser, mapper, nøgler og bogmærker).
  meta: { navn: "Strafudvalget", slug: "strafudvalget", fag: "Samfundsfag", niveau: "C", klasse: "1.g" },

  // 2. Regler som data. Bruges både til tekst og til beregning.
  regler: {
    stemmer: 5, flertal: 3,
    faldback: { fri: true },                 // hvad der sker uden flertal
    genafstemning: true, makkerparDelerStemme: true,
  },
  valg: { straffe: [...], tillaeg: [...] },  // det, udvalget vælger imellem

  // 3. Roller. Hovedkrav er data, ikke kun tekst:
  roller: [{
    id: "R", navn: "Den retfærdige straf",
    hovedkrav: { minAar: 6 },                // storskærm og facit regner med dette
    hovedkravTekst: "Straffen skal være mindst 6 år.",
    oenske: "...", notat: "...", argumenter: [...], dilemma: "...", taktik: [...],
  }],

  // 4. Fælles tekster, som står flere steder (intro-regler, stopregel, fri fod).
  tekster: {
    stopregel: "Når læreren stopper forhandlingen, og intet forslag har tre stemmer, går han fri.",
    ...
  },

  // 5. Tekster pr. kanal: kun det, der hører hjemme ét sted.
  elev:       { intro: [...], bilag: [...], skema: {...} },
  laerer:     { guide: [...], cheatsheet: [...], typiskeProblemer: [...] },
  web:        { lead: "...", lektie: [...] },   // offentligt: aldrig hovedkrav, notater eller facit
  cockpit:    { introIndtastning: "..." },
  storskaerm: { udenFlertal: "Uden flertal: han går fri", ingenJa: "Ingen ja-stemmer endnu", ... },

  // 6. Beregninger, som flere dele bruger.
  fordeling(elever) { ... },   // elever pr. rolle og udvalg
  pakker() { ... },            // facit ud fra regler.hovedkrav
};
```

## Regler

1. **Generatorerne skriver ingen spiltekst.** Står en sætning om spillet i `elev.cjs`, `laerer.cjs`, `byg_web.cjs` eller i storskærmens kode, flyttes den til spilfilen. Layoutord som "Side", "Navn" og kolonneoverskrifter må gerne stå i generatoren.
2. **En regel skrives én gang.** En tekst, der står to steder (fx stopreglen i intro og på minisiden), ligger i `tekster` og hentes begge steder.
3. **Krav, der skal beregnes, er data.** Hovedkrav, grænser og afkald udledes af den samme struktur, som teksten på kortet laves af. Storskærm, facit og test bruger den samme funktion.
4. **Offentlig og fortrolig adskilles i filen.** `web` og det, `byg_web.cjs` lægger i `spildata.js`, må kun hente fra offentlige felter. En test fejler, hvis hovedkrav, notater, facit eller dommen findes i den offentlige udgave.
5. **Viste navne og teknisk nøgle er adskilt.** `meta.navn` kan ændres ét sted. `meta.slug` ligger fast.
6. **Test af, at det holder.** En test bygger alle udgaver og tjekker:
   - samme regeltekst står ens i elevpakke, lærerpakke, miniside og cockpit
   - ingen kendte spiltekster står direkte i generatorerne (søg efter sætninger fra `tekster` og `storskaerm`)
   - facit fra `pakker()` passer med det, storskærmen beregner, for alle kombinationer
7. **Ved et eksisterende spil** flyttes teksterne over, når man alligevel arbejder i spillet, ikke dagen før det skal bruges.
