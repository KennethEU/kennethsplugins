"""
Blooket CSV Generator

Genererer en CSV-fil i Blookets officielle importformat.
Tilpas questions-listen nedenfor og kør scriptet.

Output: Blooket-importklar CSV med semikolon-separator, UTF-8 BOM,
Windows-linjeskift, 26 kolonner pr. række, og alle nødvendige headers.
"""

import sys
import os


def generate_blooket_csv(questions, output_path):
    """
    Generér en Blooket-importklar CSV-fil.

    questions: liste af dicts med keys:
        - text (str): Spørgsmålstekst
        - answers (list[str]): 2-4 svarmuligheder
        - correct (str): Korrekte svarnumre, fx "1" eller "1,3"
        - time (int): Tidsbegrænsning i sekunder (default 20, max 300)

    output_path: sti til output CSV-fil
    """
    TOTAL_COLS = 26
    USED_COLS = 8
    DATA_PADDING = ";" * (TOTAL_COLS - USED_COLS)
    FULL_PADDING = ";" * (TOTAL_COLS - 1)

    lines = []

    # Række 1: Header (1 celle + 25 tomme)
    lines.append('"Blooket\nImport Template"' + FULL_PADDING)

    # Række 2: Kolonneoverskrifter (8 celler + 18 tomme)
    headers = [
        "Question #",
        "Question Text",
        "Answer 1",
        "Answer 2",
        '"Answer 3\n(Optional)"',
        '"Answer 4\n(Optional)"',
        '"Time Limit (sec)\n(Max: 300 seconds)"',
        '"Correct Answer(s)\n(Only include Answer #)"',
    ]
    lines.append(";".join(headers) + DATA_PADDING)

    # Datarækker
    for i, q in enumerate(questions, 1):
        answers = list(q["answers"])
        # Pad til 4 svar
        while len(answers) < 4:
            answers.append("")
        time_limit = min(q.get("time", 20), 300)
        correct = q.get("correct", "1")

        row = ";".join([
            str(i),
            q["text"],
            answers[0],
            answers[1],
            answers[2],
            answers[3],
            str(time_limit),
            str(correct),
        ])
        row += DATA_PADDING
        lines.append(row)

    # Tomme nummererede rækker op til 100
    for i in range(len(questions) + 1, 101):
        lines.append(str(i) + FULL_PADDING)

    # Tomme rækker uden nummer (som i Blookets template: ~400 ekstra)
    for _ in range(400):
        lines.append(FULL_PADDING)

    # Skriv fil med UTF-8 BOM og Windows-linjeskift
    content = "\r\n".join(lines)
    with open(output_path, "w", encoding="utf-8-sig", newline="") as f:
        f.write(content)

    print(f"Genereret: {output_path} ({len(questions)} spørgsmål)")


# === TILPAS SPØRGSMÅL HER ===

if __name__ == "__main__":
    # Eksempel — erstat med dine egne spørgsmål
    questions = [
        {
            "text": "Hvad er 2 + 2?",
            "answers": ["4", "3", "1", "Fire"],
            "correct": "1,4",
            "time": 20,
        },
        {
            "text": "Hvad er 3 + 3?",
            "answers": ["3", "6"],
            "correct": "2",
            "time": 15,
        },
    ]

    output = sys.argv[1] if len(sys.argv) > 1 else "blooket_output.csv"
    generate_blooket_csv(questions, output)
