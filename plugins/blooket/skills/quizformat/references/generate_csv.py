"""
Blooket CSV Generator

Genererer en CSV-fil i Blookets officielle importformat.

Brug:
    python generate_csv.py spoergsmaal.json [output.csv]

spoergsmaal.json er en liste af objekter med text, answers (2-4), correct
(fx "1" eller "1,3") og time (sekunder, valgfri, standard 20).
Scriptet stopper med en tydelig fejl, hvis et spørgsmål bryder reglerne,
og skriver en advarsel, hvis de korrekte svar ligger skævt fordelt.

Output: Blooket-importklar CSV med semikolon-separator, UTF-8 BOM,
Windows-linjeskift, 26 kolonner pr. række, og alle nødvendige headers.
"""

import json
import sys
from collections import Counter


def validate(questions):
    """Returnér (fejl, advarsler) som lister af tekster."""
    errors, warnings = [], []
    if not questions:
        errors.append("Ingen spørgsmål.")
    if len(questions) > 100:
        errors.append(f"{len(questions)} spørgsmål, men Blookets skabelon har plads til 100.")
    first_correct = []
    for i, q in enumerate(questions, 1):
        text = str(q.get("text", "")).strip()
        answers = [str(a).strip() for a in q.get("answers", [])]
        if not text:
            errors.append(f"Spørgsmål {i}: mangler tekst.")
        if not 2 <= len(answers) <= 4:
            errors.append(f"Spørgsmål {i}: har {len(answers)} svarmuligheder, skal have 2 til 4.")
        if any(not a for a in answers):
            errors.append(f"Spørgsmål {i}: et svar er tomt.")
        for field in [text] + answers:
            if ";" in field or "\n" in field:
                errors.append(f"Spørgsmål {i}: semikolon og linjeskift i tekst ødelægger CSV-formatet.")
                break
        try:
            nums = [int(x) for x in str(q.get("correct", "1")).split(",")]
        except ValueError:
            nums = []
            errors.append(f"Spørgsmål {i}: 'correct' skal være tal som \"2\" eller \"1,3\".")
        if nums and (min(nums) < 1 or max(nums) > len(answers)):
            errors.append(f"Spørgsmål {i}: korrekt svar {q.get('correct')} findes ikke, der er {len(answers)} svar.")
        if len(set(nums)) != len(nums):
            errors.append(f"Spørgsmål {i}: samme svarnummer angivet flere gange.")
        if nums:
            first_correct.append(nums[0])
        t = q.get("time", 20)
        if not isinstance(t, int) or not 1 <= t <= 300:
            errors.append(f"Spørgsmål {i}: tid skal være et helt tal mellem 1 og 300 sekunder.")
    if len(first_correct) >= 8:
        pos, n = Counter(first_correct).most_common(1)[0]
        if n / len(first_correct) > 0.5:
            warnings.append(f"Det korrekte svar står på plads {pos} i {n} af {len(first_correct)} spørgsmål. Bland placeringen.")
    return errors, warnings


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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        questions = json.load(f)
    errors, warnings = validate(questions)
    for w in warnings:
        print("ADVARSEL:", w)
    if errors:
        for e in errors:
            print("FEJL:", e)
        sys.exit(1)
    output = sys.argv[2] if len(sys.argv) > 2 else "blooket_output.csv"
    generate_blooket_csv(questions, output)
