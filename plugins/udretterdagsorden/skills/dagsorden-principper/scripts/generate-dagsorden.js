#!/usr/bin/env node
/**
 * generate-dagsorden.js
 * 
 * Genererer en udretterdagsorden som .docx med præcist layout.
 * 
 * Brug:
 *   node generate-dagsorden.js --input dagsorden.json --output dagsorden.docx
 *   echo '{ ... }' | node generate-dagsorden.js --output dagsorden.docx
 * 
 * Designet er ekstraheret fra udretterdagsorden_polkom.docx og kan justeres
 * i DESIGN-objektet nedenfor uden at røre resten af koden.
 */

const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, BorderStyle, WidthType, ShadingType,
        VerticalAlign, HeadingLevel } = require("docx");

// ═══════════════════════════════════════════════════════════════════════
// DESIGN — Ret her for at ændre udseendet. Rør ikke koden nedenunder.
// ═══════════════════════════════════════════════════════════════════════

const DESIGN = {
  // Sidelayout (A4, smalle marginer)
  page: {
    width: 11906,       // A4 bredde i DXA
    height: 16838,      // A4 højde i DXA
    margins: { top: 720, right: 720, bottom: 720, left: 720 }
  },

  // Font
  font: "Arial",

  // Overskrifter
  title: {
    size: 36,            // "Gruppedagsorden"
    color: "1B3A5C",     // Mørkeblå
    bold: true
  },
  subtitle: {
    size: 26,            // Emne-tekst
    color: "2E75B6",     // Mellemblå
    bold: true
  },
  meta: {
    size: 19,            // "Fag: ... Klasse: ... Total tid: ..."
    color: "333333",
    labelBold: true
  },
  divider: {
    color: "2E75B6",     // Streg under meta-linjen
    size: 6
  },

  // Rolletabel
  roles: {
    headingColor: "2E75B6",
    headingSize: 22,
    cellBg: "D6E4F0",   // Lyseblå baggrund
    textSize: 19,
    textColor: "333333",
    labelColor: "1B3A5C",
    columnWidths: [2400, 8066],  // Sum = 10466
  },

  // Hovedtabel
  table: {
    totalWidth: 10466,
    columnWidths: [550, 2200, 7066, 650],  // Nr, Hvad, Hvordan, Tid
    borderColor: "B0C4DE",
    cellMargins: { top: 60, bottom: 60, left: 100, right: 100 },

    // Header-række
    header: {
      bg: "1B3A5C",
      textColor: "FFFFFF",
      textSize: 20,
      bold: true
    },

    // Indholdsrækker
    content: {
      textSize: 19,
      textColor: "333333",
      nrBold: true,
      hvadBold: true,
      tidColor: "2E75B6",
      tidBold: true,
      rowEvenBg: "FFFFFF",       // Hvid
      rowOddBg: "EDF2F8",       // Meget lys blå
    },

    // Pause-række
    pause: {
      bg: "FFF3CD",              // Lys gul
    },

    // OBS-linjer
    obs: {
      labelColor: "C00000",     // Rød, fed
      labelBold: true,
      textColor: "333333",
    },

    // TOTAL-række
    total: {
      bg: "1B3A5C",
      textColor: "FFFFFF",
      textSize: 22,
      bold: true
    }
  }
};

// ═══════════════════════════════════════════════════════════════════════
// NORMALISERING — Accepterer både nyt (kanonisk) og gammelt feltformat
// ═══════════════════════════════════════════════════════════════════════

function normalize(data) {
  return {
    emne: data.title || data.titel || data.topic || data.emne,
    fag: data.subject || data.fag,
    klasse: data.klasse || '',
    total_tid: data.totalTime || data.totalTid || data.total_tid,
    roller: data.roles || data.roller,
    trin: (data.steps || data.trin || []).map((t, i) => {
      // Flet docInstruction ind i instruction hvis det er nyt format
      let hvordan = t.hvordan || t.instruction || t.instruktion || '';
      const doc = t.docInstruction || t.docInstruktion;
      if (!t.hvordan && doc) {
        hvordan += '\n\n' + doc;
      }
      return {
        nr: t.nr || (i + 1),
        type: t.type === 'individuel' ? 'normal' : (t.type || 'normal'),
        hvad: t.hvad || t.heading || t.overskrift || '',
        hvordan,
        obs: t.note || t.obs || null,
        docInstruktion: t.hvordan ? (t.docInstruction || t.docInstruktion || null) : null,
        tid: t.duration || t.tid,
      };
    }),
  };
}

// ═══════════════════════════════════════════════════════════════════════
// HJÆLPEFUNKTIONER — Generisk, bruger DESIGN-værdier
// ═══════════════════════════════════════════════════════════════════════

const font = (text, opts = {}) => new TextRun({
  text,
  font: DESIGN.font,
  size: opts.size || DESIGN.table.content.textSize,
  color: opts.color || DESIGN.table.content.textColor,
  bold: opts.bold || false,
});

const border = { style: BorderStyle.SINGLE, size: 1, color: DESIGN.table.borderColor };
const borders = { top: border, bottom: border, left: border, right: border };

const cellMargins = {
  top: DESIGN.table.cellMargins.top,
  bottom: DESIGN.table.cellMargins.bottom,
  left: DESIGN.table.cellMargins.left,
  right: DESIGN.table.cellMargins.right,
};

function makeCell(children, opts = {}) {
  const paragraphs = Array.isArray(children) ? children : [children];
  return new TableCell({
    width: { size: opts.width, type: WidthType.DXA },
    borders,
    shading: { fill: opts.bg || "FFFFFF", type: ShadingType.CLEAR },
    margins: cellMargins,
    verticalAlign: opts.vAlign || VerticalAlign.TOP,
    children: paragraphs.map(p => {
      if (p instanceof Paragraph) return p;
      // Nyt format: { spacing: 100, runs: [...] }
      if (p && typeof p === "object" && !Array.isArray(p) && p.runs) {
        return new Paragraph({
          spacing: { before: p.spacing || 0, after: 0 },
          alignment: opts.align || AlignmentType.LEFT,
          children: p.runs,
        });
      }
      // Gammelt format: [TextRun, TextRun, ...]
      const runs = Array.isArray(p) ? p : [p];
      return new Paragraph({
        spacing: { before: 0, after: 0 },
        alignment: opts.align || AlignmentType.LEFT,
        children: runs,
      });
    }),
  });
}

// ═══════════════════════════════════════════════════════════════════════
// DOKUMENTBYGGER
// ═══════════════════════════════════════════════════════════════════════

function buildDocument(data) {
  const D = DESIGN;
  const T = D.table;
  const cw = T.columnWidths;

  // ── Overskrift ──
  const titlePara = new Paragraph({
    spacing: { after: 40 },
    children: [font("Gruppedagsorden", { size: D.title.size, color: D.title.color, bold: D.title.bold })],
  });

  const subtitlePara = new Paragraph({
    spacing: { after: 20 },
    children: [font(data.emne, { size: D.subtitle.size, color: D.subtitle.color, bold: D.subtitle.bold })],
  });

  // ── Meta-linje (Fag | Klasse | Tid) ──
  const metaPara = new Paragraph({
    spacing: { before: 80, after: 60 },
    children: [
      font("Fag: ", { size: D.meta.size, color: D.meta.color, bold: D.meta.labelBold }),
      font(`${data.fag}   `, { size: D.meta.size, color: D.meta.color }),
      font("Klasse: ", { size: D.meta.size, color: D.meta.color, bold: D.meta.labelBold }),
      font(`${data.klasse}   `, { size: D.meta.size, color: D.meta.color }),
      font("Total tid: ", { size: D.meta.size, color: D.meta.color, bold: D.meta.labelBold }),
      font(`${data.total_tid} min`, { size: D.meta.size, color: D.meta.color }),
    ],
  });

  // ── Divider ──
  const dividerPara = new Paragraph({
    spacing: { before: 40, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: D.divider.size, color: D.divider.color, space: 1 } },
    children: [],
  });

  // ── Roller-overskrift ──
  const rollerHeading = new Paragraph({
    spacing: { before: 0, after: 60 },
    children: [font("Roller", { size: D.roles.headingSize, color: D.roles.headingColor, bold: true })],
  });

  // ── Rolletabel ──
  const rcw = D.roles.columnWidths;
  const rolleRows = data.roller.map(rolle =>
    new TableRow({
      children: [
        makeCell([[
          font(rolle.navn, { size: D.roles.textSize, color: D.roles.labelColor, bold: true }),
        ]], { width: rcw[0], bg: D.roles.cellBg, vAlign: VerticalAlign.CENTER }),
        makeCell([[
          font(rolle.beskrivelse, { size: D.roles.textSize, color: D.roles.textColor }),
        ]], { width: rcw[1], bg: D.roles.cellBg }),
      ]
    })
  );

  const rolleTable = new Table({
    width: { size: T.totalWidth, type: WidthType.DXA },
    columnWidths: rcw,
    rows: rolleRows,
  });

  // ── Dagsorden-overskrift ──
  const dagsordenHeading = new Paragraph({
    spacing: { before: 200, after: 60 },
    children: [font("Dagsorden", { size: D.roles.headingSize, color: D.roles.headingColor, bold: true })],
  });

  // ── Header-række i hovedtabel ──
  const headerLabels = ["Nr.", "Hvad", "Hvordan", "Tid"];
  const headerAligns = [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.CENTER];
  const headerRow = new TableRow({
    children: headerLabels.map((label, i) =>
      makeCell([[font(label, {
        size: T.header.textSize, color: T.header.textColor, bold: T.header.bold
      })]], {
        width: cw[i], bg: T.header.bg, align: headerAligns[i], vAlign: VerticalAlign.CENTER
      })
    ),
  });

  // ── Indholdsrækker ──
  const contentRows = [];
  let rowIndex = 0;

  for (const trin of data.trin) {
    const isPause = trin.type === "pause";
    const bg = isPause
      ? T.pause.bg
      : (rowIndex % 2 === 0 ? T.content.rowEvenBg : T.content.rowOddBg);

    // Byg "Hvordan"-cellens indhold (kan have flere linjer + OBS)
    const hvordanRuns = [];

    // Hovedtekst — opdel på \n for separate paragraffer
    // Dobbelt \n giver ekstra afstand (som i originalen)
    const blocks = (trin.hvordan || "").split("\n\n");
    for (let bi = 0; bi < blocks.length; bi++) {
      const lines = blocks[bi].split("\n").filter(l => l.trim());
      for (let li = 0; li < lines.length; li++) {
        const isFirstInBlock = li === 0 && bi > 0;
        hvordanRuns.push({
          spacing: isFirstInBlock ? 100 : 0,
          runs: [font(lines[li], { size: T.content.textSize, color: T.content.textColor })],
        });
      }
    }

    // OBS-linje (med afstand før)
    if (trin.obs) {
      hvordanRuns.push({
        spacing: 100,
        runs: [
          font("OBS: ", { size: T.content.textSize, color: T.obs.labelColor, bold: T.obs.labelBold }),
          font(trin.obs, { size: T.content.textSize, color: T.obs.textColor }),
        ],
      });
    }

    // Pas-på-doc instruktion (med afstand før)
    if (trin.docInstruktion) {
      hvordanRuns.push({
        spacing: 100,
        runs: [font(trin.docInstruktion, { size: T.content.textSize, color: T.content.textColor })],
      });
    }

    const row = new TableRow({
      children: [
        // Nr.
        makeCell([[font(`${trin.nr}`, {
          size: T.content.textSize, color: T.content.textColor, bold: T.content.nrBold
        })]], { width: cw[0], bg, align: AlignmentType.CENTER, vAlign: VerticalAlign.CENTER }),

        // Hvad
        makeCell([[font(trin.hvad, {
          size: T.content.textSize, color: T.content.textColor, bold: T.content.hvadBold
        })]], { width: cw[1], bg }),

        // Hvordan (multiple paragraphs)
        makeCell(hvordanRuns.length > 0 ? hvordanRuns : [{ spacing: 0, runs: [font("")] }], { width: cw[2], bg }),

        // Tid
        makeCell([[font(`${trin.tid} min`, {
          size: T.content.textSize, color: T.content.tidColor, bold: T.content.tidBold
        })]], { width: cw[3], bg, align: AlignmentType.CENTER, vAlign: VerticalAlign.CENTER }),
      ],
    });

    contentRows.push(row);
    rowIndex++;
  }

  // ── TOTAL-række ──
  const totalRow = new TableRow({
    children: [
      makeCell([[font("")]], { width: cw[0], bg: T.total.bg }),
      makeCell([[font("")]], { width: cw[1], bg: T.total.bg }),
      makeCell([[font("TOTAL:", {
        size: T.total.textSize, color: T.total.textColor, bold: T.total.bold
      })]], { width: cw[2], bg: T.total.bg, align: AlignmentType.RIGHT }),
      makeCell([[font(`${data.total_tid} min`, {
        size: T.total.textSize, color: T.total.textColor, bold: T.total.bold
      })]], { width: cw[3], bg: T.total.bg, align: AlignmentType.CENTER, vAlign: VerticalAlign.CENTER }),
    ],
  });

  // ── Saml hovedtabel ──
  const mainTable = new Table({
    width: { size: T.totalWidth, type: WidthType.DXA },
    columnWidths: cw,
    rows: [headerRow, ...contentRows, totalRow],
  });

  // ── Saml dokument ──
  return new Document({
    styles: {
      default: {
        document: {
          run: { font: DESIGN.font, size: 22 }
        }
      }
    },
    sections: [{
      properties: {
        page: {
          size: { width: D.page.width, height: D.page.height },
          margin: D.page.margins,
        }
      },
      children: [
        titlePara,
        subtitlePara,
        metaPara,
        dividerPara,
        rollerHeading,
        rolleTable,
        dagsordenHeading,
        mainTable,
      ]
    }]
  });
}

// ═══════════════════════════════════════════════════════════════════════
// MAIN — Læs input, generer dokument
// ═══════════════════════════════════════════════════════════════════════

async function main() {
  // Parse argumenter
  const args = process.argv.slice(2);
  let inputPath = null;
  let outputPath = "dagsorden.docx";

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--input" && args[i + 1]) inputPath = args[++i];
    if (args[i] === "--output" && args[i + 1]) outputPath = args[++i];
  }

  // Læs data
  let data;
  if (inputPath) {
    data = JSON.parse(fs.readFileSync(inputPath, "utf-8"));
  } else {
    // Læs fra stdin
    const chunks = [];
    for await (const chunk of process.stdin) chunks.push(chunk);
    data = JSON.parse(Buffer.concat(chunks).toString());
  }

  // Normalisér til internt format (accepterer både nyt og gammelt)
  data = normalize(data);

  // Generer og gem
  const doc = buildDocument(data);
  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(outputPath, buffer);
  console.log(`✅ Genereret: ${outputPath}`);
}

main().catch(err => {
  console.error("Fejl:", err.message);
  process.exit(1);
});
