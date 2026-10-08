# Template-kode: Genbrugelige funktioner til rollekort

Denne fil indeholder genbrugelig Node.js-kode til docx-generering af rollekort, lærerguider og elevintroduktioner.

**Vigtigt:** Hvis `/mnt/skills/public/docx/SKILL.md` findes, så læs den først. Den kan have nyere best practices.

## Indhold

- Imports og konstanter
- Hjælpefunktioner
- Farvet boks (central byggeklods)
- Rollekort-header
- Faseguide-tabel
- Støtteversion-specifikke funktioner
- Dokument-bygning
- Lærermateriale / Cheatsheet — Two-table layout
- Validerings- og preview-workflow
- Typiske fejl at undgå

## Imports og konstanter

```javascript
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, PageBreak,
  LevelFormat, VerticalAlign
} = require('docx');
const fs = require('fs');

// ── Sideopsætning (DXA-enheder) ──
const PAGE_W = 11906, PAGE_H = 16838; // A4

// Kompakte margener (rollekort — 1 side pr. kort)
const MH_ROLLE = 1008, MV_ROLLE = 640;
// Standard margener (lærerguide)
const MH_GUIDE = 1440, MV_GUIDE = 1008;
// Medium margener (elevintroduktion)
const MH_INTRO = 1200, MV_INTRO = 900;

// ── Farvepalet ──
const PRIMARY   = "1A3A6B";
const SECONDARY = "2A4A8B";
const ACCENT    = "C0392B";
const LIGHT     = "E8EEF8";
const YELLOW    = "FFF3CC";
const GREEN_BG  = "E8F5E8";
const GREEN_TXT = "1A6B1A";
const WHITE     = "FFFFFF";

// ── Borders ──
const nb = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const NB = { top: nb, bottom: nb, left: nb, right: nb };
const tb = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const TB = { top: tb, bottom: tb, left: tb, right: tb };
```

## Hjælpefunktioner

```javascript
// Halvpunkter: docx TextRun size er i halve punkter
function pt(n) { return Math.round(n * 2); }

// Tom linje med konfigurerbar afstand
function empty(before = 80, after = 80) {
  return new Paragraph({ spacing: { before, after }, children: [new TextRun("")] });
}

// Horisontal skillelinje
function divider(color = "CCCCCC") {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color } }
  });
}

// Brødtekst
function bodyText(text, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.before || 40, after: opts.after || 40 },
    children: [new TextRun({
      text,
      font: "Arial",
      size: pt(opts.size || 9),
      bold: opts.bold || false,
      italics: opts.italic || false,
      color: opts.color || "333333"
    })]
  });
}

// Sektionsoverskrift (blå, fed, caps)
function sectionTitle(text) {
  return new Paragraph({
    spacing: { before: 160, after: 60 },
    children: [new TextRun({
      text: text.toUpperCase(),
      font: "Arial",
      size: pt(9),
      bold: true,
      color: SECONDARY
    })]
  });
}

// Bold label + normal tekst på samme linje
function bold(label, text, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.before || 40, after: opts.after || 40 },
    children: [
      new TextRun({ text: label, font: "Arial", size: pt(opts.size || 9), bold: true, color: opts.labelColor || "333333" }),
      new TextRun({ text, font: "Arial", size: pt(opts.size || 9), color: opts.textColor || "333333" })
    ]
  });
}

// Nummereret punkt
function numberedItem(num, text, opts = {}) {
  return new Paragraph({
    spacing: { before: 30, after: 30 },
    children: [
      new TextRun({ text: `${num}. `, font: "Arial", size: pt(opts.size || 9), bold: true, color: PRIMARY }),
      new TextRun({ text, font: "Arial", size: pt(opts.size || 9), color: "333333" })
    ]
  });
}
```

## Farvet boks (central byggeklods)

```javascript
// Farvet baggrundsboks — bruges til info, advarsler, nødhjælp
function colorBox(children, fill = LIGHT, contentWidth) {
  const w = contentWidth || (PAGE_W - 2 * MH_ROLLE);
  return new Table({
    width: { size: w, type: WidthType.DXA },
    columnWidths: [w],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders: NB,
            shading: { fill, type: ShadingType.CLEAR },
            margins: { top: 100, bottom: 100, left: 140, right: 140 },
            width: { size: w, type: WidthType.DXA },
            children
          })
        ]
      })
    ]
  });
}

// Accent-boks (rød tekst, til særlige beføjelser)
function accentBox(text, contentWidth) {
  return colorBox([
    new Paragraph({
      children: [
        new TextRun({ text: "SÆRLIG BEFØJELSE: ", font: "Arial", size: pt(9), bold: true, color: ACCENT }),
        new TextRun({ text, font: "Arial", size: pt(9), color: ACCENT })
      ]
    })
  ], LIGHT, contentWidth);
}
```

## Rollekort-header

```javascript
// Header med farvet baggrund, hvid tekst
function roleHeader(name, title, org, stemmer, befoejelse, contentWidth) {
  const w = contentWidth || (PAGE_W - 2 * MH_ROLLE);
  const runs = [
    new TextRun({ text: name, font: "Arial", size: pt(14), bold: true, color: WHITE }),
    new TextRun({ text: `\n${title} — ${org}`, font: "Arial", size: pt(10), color: WHITE }),
    new TextRun({ text: `\nStemmer: ${stemmer}`, font: "Arial", size: pt(10), bold: true, color: WHITE })
  ];
  if (befoejelse) {
    runs.push(new TextRun({ text: ` | ${befoejelse}`, font: "Arial", size: pt(9), color: WHITE }));
  }

  return new Table({
    width: { size: w, type: WidthType.DXA },
    columnWidths: [w],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders: NB,
            shading: { fill: PRIMARY, type: ShadingType.CLEAR },
            margins: { top: 160, bottom: 160, left: 200, right: 200 },
            width: { size: w, type: WidthType.DXA },
            children: [
              new Paragraph({
                children: runs
              })
            ]
          })
        ]
      })
    ]
  });
}
```

## Faseguide-tabel

```javascript
// Standard faseguide (normal + støtte version)
function faseGuideTable(phases, contentWidth) {
  // phases = [{ fase: "Fase 1: Forberedelse", handling: "Læs kortet..." }, ...]
  const w = contentWidth || (PAGE_W - 2 * MH_ROLLE);
  const col1 = Math.floor(w * 0.30);
  const col2 = w - col1;

  const headerRow = new TableRow({
    children: [
      new TableCell({
        borders: TB,
        shading: { fill: SECONDARY, type: ShadingType.CLEAR },
        margins: { top: 60, bottom: 60, left: 80, right: 80 },
        width: { size: col1, type: WidthType.DXA },
        children: [new Paragraph({ children: [new TextRun({ text: "FASE", font: "Arial", size: pt(8), bold: true, color: WHITE })] })]
      }),
      new TableCell({
        borders: TB,
        shading: { fill: SECONDARY, type: ShadingType.CLEAR },
        margins: { top: 60, bottom: 60, left: 80, right: 80 },
        width: { size: col2, type: WidthType.DXA },
        children: [new Paragraph({ children: [new TextRun({ text: "DIN HANDLING", font: "Arial", size: pt(8), bold: true, color: WHITE })] })]
      })
    ]
  });

  const dataRows = phases.map((p, i) =>
    new TableRow({
      children: [
        new TableCell({
          borders: TB,
          shading: { fill: i % 2 === 0 ? LIGHT : WHITE, type: ShadingType.CLEAR },
          margins: { top: 50, bottom: 50, left: 80, right: 80 },
          width: { size: col1, type: WidthType.DXA },
          children: [new Paragraph({ children: [new TextRun({ text: p.fase, font: "Arial", size: pt(8), bold: true, color: PRIMARY })] })]
        }),
        new TableCell({
          borders: TB,
          shading: { fill: i % 2 === 0 ? LIGHT : WHITE, type: ShadingType.CLEAR },
          margins: { top: 50, bottom: 50, left: 80, right: 80 },
          width: { size: col2, type: WidthType.DXA },
          children: [new Paragraph({ children: [new TextRun({ text: p.handling, font: "Arial", size: pt(8), color: "333333" })] })]
        })
      ]
    })
  );

  return new Table({
    width: { size: w, type: WidthType.DXA },
    columnWidths: [col1, col2],
    rows: [headerRow, ...dataRows]
  });
}
```

## Støtteversion-specifikke funktioner

```javascript
// Nødhjælpsboks (gul baggrund)
function noedhjælpsBoks(sætninger, contentWidth) {
  // sætninger = ["Jeg vil gerne høre...", "Kan vi finde et kompromis..."]
  const children = [
    new Paragraph({
      spacing: { after: 60 },
      children: [new TextRun({
        text: "HVIS DU ER I TVIVL OM HVAD DU SKAL SIGE:",
        font: "Arial", size: pt(9), bold: true, color: "8B6914"
      })]
    }),
    ...sætninger.map((s, i) =>
      new Paragraph({
        spacing: { before: 20, after: 20 },
        children: [new TextRun({
          text: `→ "${s}"`,
          font: "Arial", size: pt(9), italics: true, color: "8B6914"
        })]
      })
    )
  ];
  return colorBox(children, YELLOW, contentWidth);
}

// Forhandlingssætninger (grøn baggrund)
function forhandlingsBoks(sætninger, contentWidth) {
  const children = [
    new Paragraph({
      spacing: { after: 60 },
      children: [new TextRun({
        text: "FORHANDLINGSSÆTNINGER:",
        font: "Arial", size: pt(9), bold: true, color: GREEN_TXT
      })]
    }),
    ...sætninger.map((s, i) =>
      new Paragraph({
        spacing: { before: 20, after: 20 },
        children: [new TextRun({
          text: `${i + 1}. "${s}"`,
          font: "Arial", size: pt(9), color: GREEN_TXT
        })]
      })
    )
  ];
  return colorBox(children, GREEN_BG, contentWidth);
}

// Alliancetabel (3 kolonner: Hvem? | Hvorfor? | Sig dette)
function allianceTabel(alliancer, contentWidth) {
  // alliancer = [{ hvem: "Henrik", hvorfor: "I deler syn på...", sig: "Henrik, vi burde..." }]
  const w = contentWidth || (PAGE_W - 2 * MH_ROLLE);
  const col1 = Math.floor(w * 0.20);
  const col2 = Math.floor(w * 0.35);
  const col3 = w - col1 - col2;

  const header = new TableRow({
    children: ["HVEM?", "HVORFOR?", "SIG DETTE TIL DEM"].map((label, i) =>
      new TableCell({
        borders: TB,
        shading: { fill: SECONDARY, type: ShadingType.CLEAR },
        margins: { top: 50, bottom: 50, left: 60, right: 60 },
        width: { size: [col1, col2, col3][i], type: WidthType.DXA },
        children: [new Paragraph({ children: [new TextRun({ text: label, font: "Arial", size: pt(8), bold: true, color: WHITE })] })]
      })
    )
  });

  const rows = alliancer.map((a, i) =>
    new TableRow({
      children: [a.hvem, a.hvorfor, a.sig].map((text, j) =>
        new TableCell({
          borders: TB,
          shading: { fill: i % 2 === 0 ? LIGHT : WHITE, type: ShadingType.CLEAR },
          margins: { top: 40, bottom: 40, left: 60, right: 60 },
          width: { size: [col1, col2, col3][j], type: WidthType.DXA },
          children: [new Paragraph({ children: [new TextRun({ text, font: "Arial", size: pt(8), color: "333333" })] })]
        })
      )
    })
  );

  return new Table({
    width: { size: w, type: WidthType.DXA },
    columnWidths: [col1, col2, col3],
    rows: [header, ...rows]
  });
}

// Ordliste (2 kolonner: Begreb | Forklaring)
function ordliste(begreber, contentWidth) {
  // begreber = [{ begreb: "Deliberation", forklaring: "At diskutere..." }]
  const w = contentWidth || (PAGE_W - 2 * MH_ROLLE);
  const col1 = Math.floor(w * 0.30);
  const col2 = w - col1;

  const header = new TableRow({
    children: ["FAGBEGREB", "FORKLARING"].map((label, i) =>
      new TableCell({
        borders: TB,
        shading: { fill: SECONDARY, type: ShadingType.CLEAR },
        margins: { top: 50, bottom: 50, left: 60, right: 60 },
        width: { size: [col1, col2][i], type: WidthType.DXA },
        children: [new Paragraph({ children: [new TextRun({ text: label, font: "Arial", size: pt(8), bold: true, color: WHITE })] })]
      })
    )
  });

  const rows = begreber.map((b, i) =>
    new TableRow({
      children: [
        new TableCell({
          borders: TB,
          shading: { fill: LIGHT, type: ShadingType.CLEAR },
          margins: { top: 40, bottom: 40, left: 60, right: 60 },
          width: { size: col1, type: WidthType.DXA },
          children: [new Paragraph({ children: [new TextRun({ text: b.begreb, font: "Arial", size: pt(8), bold: true, color: PRIMARY })] })]
        }),
        new TableCell({
          borders: TB,
          margins: { top: 40, bottom: 40, left: 60, right: 60 },
          width: { size: col2, type: WidthType.DXA },
          children: [new Paragraph({ children: [new TextRun({ text: b.forklaring, font: "Arial", size: pt(8), color: "333333" })] })]
        })
      ]
    })
  );

  return new Table({
    width: { size: w, type: WidthType.DXA },
    columnWidths: [col1, col2],
    rows: [header, ...rows]
  });
}
```

## Dokument-bygning

```javascript
// Byg et komplet dokument med rollekort
async function buildDocument(sections, marginH, marginV) {
  const doc = new Document({
    styles: {
      default: {
        document: { run: { font: "Arial", size: pt(9) } },
      },
    },
    sections: [{
      properties: {
        page: {
          size: { width: PAGE_W, height: PAGE_H },
          margin: { top: marginH, bottom: marginH, left: marginV, right: marginV },
        },
      },
      children: sections,
    }],
  });

  return await Packer.toBuffer(doc);
}

// Gem og validér
async function saveAndValidate(buffer, filename) {
  fs.writeFileSync(filename, buffer);
  console.log(`✅ ${filename} created (${(buffer.length / 1024).toFixed(0)} KB)`);
}
```

## Lærermateriale / Cheatsheet — Two-table layout

```javascript
// Spørgsmål-svar-par som farvet tabel
function qaBlock(num, question, answer, extras = {}, contentWidth) {
  const w = contentWidth || (PAGE_W - 2 * MH_GUIDE);
  
  // Header-række: Spørgsmål
  const headerRow = new TableRow({
    children: [
      new TableCell({
        borders: TB,
        shading: { fill: PRIMARY, type: ShadingType.CLEAR },
        margins: { top: 100, bottom: 100, left: 140, right: 140 },
        width: { size: w, type: WidthType.DXA },
        children: [
          new Paragraph({
            children: [new TextRun({
              text: `SPØRGSMÅL ${num}: ${question}`,
              font: "Arial", size: pt(10), bold: true, color: WHITE
            })]
          })
        ]
      })
    ]
  });

  // Svar-række: Modelsvar + evt. fagbegreber + typiske fejl
  const answerChildren = [
    new Paragraph({
      spacing: { after: 60 },
      children: [
        new TextRun({ text: "Kernesvar: ", font: "Arial", size: pt(9), bold: true, color: "333333" }),
        new TextRun({ text: answer, font: "Arial", size: pt(9), color: "333333" })
      ]
    })
  ];

  if (extras.fagbegreber) {
    answerChildren.push(new Paragraph({
      spacing: { before: 40, after: 40 },
      children: [
        new TextRun({ text: "Fagbegreber: ", font: "Arial", size: pt(9), bold: true, color: SECONDARY }),
        new TextRun({ text: extras.fagbegreber, font: "Arial", size: pt(9), color: SECONDARY })
      ]
    }));
  }

  if (extras.uddybning) {
    answerChildren.push(new Paragraph({
      spacing: { before: 40, after: 40 },
      children: [
        new TextRun({ text: "Uddybning: ", font: "Arial", size: pt(8), bold: true, color: "666666" }),
        new TextRun({ text: extras.uddybning, font: "Arial", size: pt(8), color: "666666" })
      ]
    }));
  }

  if (extras.typiskeFejl) {
    answerChildren.push(new Paragraph({
      spacing: { before: 40, after: 40 },
      children: [
        new TextRun({ text: "Typiske fejl: ", font: "Arial", size: pt(8), bold: true, italics: true, color: ACCENT }),
        new TextRun({ text: extras.typiskeFejl, font: "Arial", size: pt(8), italics: true, color: ACCENT })
      ]
    }));
  }

  const answerRow = new TableRow({
    children: [
      new TableCell({
        borders: TB,
        margins: { top: 100, bottom: 100, left: 140, right: 140 },
        width: { size: w, type: WidthType.DXA },
        children: answerChildren
      })
    ]
  });

  return new Table({
    width: { size: w, type: WidthType.DXA },
    columnWidths: [w],
    rows: [headerRow, answerRow]
  });
}

// Brug: qaBlock(1, "Hvem er fattig?", "Det afhænger af...", {
//   fagbegreber: "relativ fattigdom, absolut fattigdom, materiel deprivation",
//   uddybning: "Stærke elever nævner også...",
//   typiskeFejl: "Elever forveksler ofte ulighed med fattigdom"
// })
```

## Validerings- og preview-workflow

```bash
# 1. Generér
node rollekort.js

# 2. Validér (skal returnere VALID)
python3 /mnt/skills/public/docx/scripts/office/validate.py output.docx   # kun hvis docx-skillen findes

# 3. Konvertér til PDF
soffice --headless --convert-to pdf output.docx

# 4. Preview (generér JPEG-billeder)
pdftoppm -jpeg -r 200 output.pdf preview

# 5. Visuelt tjek
# Se på preview-1.jpg, preview-2.jpg osv. med view-værktøjet
```

## Typiske fejl at undgå

**Sproglige fejl:** Se `rollespil-sprogtjek`-skillen for komplet dansk retskrivningstjek (æøå, sammensatte ord, genus, person-perspektiv, fagterm-konsistens).

**Tekniske fejl:**
1. **Dobbelt-tekst fra sed:** Undgå at bruge sed til teksterstatning i docx-scripts — det skaber fejl. Skriv altid korrekt tekst direkte i JavaScript-strengen.
2. **Sideoverflow:** Hvert rollekort SKAL passe på præcis 1 A4-side (normal og stærk) eller 2 sider (støtte). Preview ALTID med pdftoppm.
3. **Encoding:** Sørg for at Node.js-filen er gemt som UTF-8. Test med `node -e "console.log('æøå')"` først.
4. **Margin-mismatch:** Brug de korrekte margener for dokumenttypen (MH_ROLLE for rollekort, MH_GUIDE for lærerguide, MH_INTRO for elevintro).
5. **Sidestørrelse:** Sæt altid A4 eksplicit (`11906 x 16838` DXA). Stol ikke på standardværdien.
6. **Tabelbredder:** Angiv bredden i DXA både på `columnWidths` og på hver celle. Summen skal passe til sidebredden minus margener.
7. **Baggrundsfarve:** Brug `ShadingType.CLEAR` med `fill`. `SOLID` kan give sort baggrund.
8. **Linjeskift:** Brug aldrig `\n` i en `TextRun`. Lav et nyt `Paragraph` eller brug `break`.
9. **Punktlister:** Brug en `numbering`-konfiguration (`LevelFormat.BULLET`), ikke et skrevet `•`.
10. **Sideskift:** `PageBreak` skal ligge inde i et `Paragraph`.
11. **Billeder:** `ImageRun` kræver `type` (fx `png`).
12. **Skillelinjer:** Brug en afsnitskant (border) frem for en tom tabel.

(Punkt 5 til 12 er hentet fra Anthropics docx-skill, github.com/anthropics/skills.)
