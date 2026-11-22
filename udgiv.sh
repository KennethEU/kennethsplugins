#!/bin/bash
# Udgiver plugins to steder: GitHub (plugins) og Outline (dok.mgai.dk, Fælles → Skills).
#
#   ./udgiv.sh "besked"        tjek, commit, push og opdater Outline
#   ./udgiv.sh --kun-outline   opdater kun Outline (fx når GitHub allerede er opdateret)
#
# Outline-delen viser først en prøvekørsel og spørger, før noget ændres.
set -e
cd "$(dirname "$0")"

echo "1. Tjekker plugins"
claude plugin validate . --strict >/dev/null && echo "   validate: OK"
python3 tjek_arbejdsgang.py | sed 's/^/   /'

if [ "$1" != "--kun-outline" ]; then
  if [ -z "$1" ]; then
    echo 'Skriv en besked, fx: ./udgiv.sh "bloom 1.7.0: nyt trin"'; exit 1
  fi
  echo "2. GitHub"
  git add -A
  if git diff --cached --quiet; then
    echo "   ingen ændringer at committe"
  else
    git commit -q -m "$1" && echo "   commit: $1"
  fi
  git push -q && echo "   push: OK"
fi

echo "3. Outline (prøvekørsel)"
python3 tools/outline/synk.py --slet | sed 's/^/   /'
read -r -p "Gennemfør ændringerne i Outline? [j/N] " svar
if [ "$svar" = "j" ] || [ "$svar" = "J" ]; then
  python3 tools/outline/synk.py --udfoer --slet | tail -2 | sed 's/^/   /'
else
  echo "   Outline er ikke ændret."
fi
