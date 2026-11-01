#!/usr/bin/env python3
"""Tjekker en plan-fil til dida.dk/plan. Brug: python3 tjek_plan.py <fil>"""
import json
import re
import sys

FORMS = {"alene", "par", "gruppe", "klassen"}
FIELDS = {"heading", "duration", "type", "workForm", "screen", "instruction", "doneWhen", "note", "teacherNote"}
CLOCK = re.compile(r"\b\d{1,2}\s*-\s*\d{1,2}\s*min|\bkl\.\s*\d", re.I)


def filled(value):
    return isinstance(value, str) and value.strip() != ""


def check(plan):
    errors, warnings = [], []
    if not isinstance(plan, dict) or plan.get("format") != "dida-plan":
        return ['"format" skal være "dida-plan"'], warnings
    if plan.get("version") != 1:
        errors.append('"version" skal være 1')
    if not filled(plan.get("title")):
        errors.append("Planen mangler title")
    steps = plan.get("steps")
    if not isinstance(steps, list) or not 1 <= len(steps) <= 30:
        errors.append("steps skal have 1 til 30 trin")
        return errors, warnings
    total = 0
    for number, step in enumerate(steps, 1):
        label = f"Trin {number}"
        if not isinstance(step, dict):
            errors.append(f"{label} er ikke et objekt")
            continue
        for key in set(step) - FIELDS:
            errors.append(f"{label}: ukendt felt {key}")
        if not filled(step.get("heading")):
            errors.append(f"{label} mangler heading")
        duration = step.get("duration")
        if type(duration) is not int or not 1 <= duration <= 300:
            errors.append(f"{label}: duration skal være hele minutter mellem 1 og 300")
        else:
            total += duration
        if step.get("type") not in (None, "pause"):
            errors.append(f'{label}: type kan kun være "pause"')
        if step.get("type") != "pause" and not filled(step.get("instruction")):
            errors.append(f"{label} mangler instruction")
        if "workForm" in step and step["workForm"] not in FORMS:
            errors.append(f"{label}: workForm skal være alene, par, gruppe eller klassen")
        if "screen" in step and step["screen"] not in ("oppe", "nede"):
            errors.append(f"{label}: screen skal være oppe eller nede")
        for key in ("instruction", "doneWhen", "note"):
            text = step.get(key, "")
            if isinstance(text, str) and "<" in text and ">" in text:
                warnings.append(f"{label}: {key} ser ud til at indeholde HTML, som vises som ren tekst")
            if isinstance(text, str) and CLOCK.search(text):
                warnings.append(f"{label}: {key} ser ud til at indeholde klokkeslæt")
    minutes = plan.get("moduleMinutes")
    if minutes is not None and total != minutes:
        warnings.append(f"Tiderne summer til {total} min, men modulet er {minutes} min")
    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    try:
        with open(sys.argv[1], encoding="utf-8-sig") as handle:
            plan = json.load(handle)
    except (OSError, ValueError) as error:
        print(f"FEJL: filen kan ikke læses: {error}")
        return 1
    errors, warnings = check(plan)
    for warning in warnings:
        print(f"ADVARSEL: {warning}")
    for error in errors:
        print(f"FEJL: {error}")
    if errors:
        return 1
    print(f"OK: {len(plan['steps'])} trin, {sum(s['duration'] for s in plan['steps'])} min")
    return 0


if __name__ == "__main__":
    sys.exit(main())
