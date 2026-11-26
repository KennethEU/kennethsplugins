#!/bin/bash
# Kører triggertests for ét plugin. Testene ligger her (tools/evals/<plugin>/), uden for pluginet,
# så lærerne ikke ser dem. `claude plugin eval` kræver dem inde i pluginet, så de kopieres ind
# midlertidigt og fjernes igen bagefter. Resultater havner i tools/evals/<plugin>/results/.
#
#   tools/evals/koer.sh bloom                 alle tests for bloom
#   tools/evals/koer.sh bloom --case 'trigger-*' --runs 1
set -e
cd "$(dirname "$0")/../.."
p="$1"; shift || true
[ -d "tools/evals/$p" ] || { echo "Ingen tests: tools/evals/$p"; exit 1; }
[ -e "plugins/$p/evals" ] && { echo "plugins/$p/evals findes allerede. Fjern den først."; exit 1; }
cp -R "tools/evals/$p" "plugins/$p/evals"
trap 'if [ -d "plugins/$p/evals/results" ]; then mkdir -p "tools/evals/$p/results"; cp -R "plugins/$p/evals/results/." "tools/evals/$p/results/"; fi; rm -rf "plugins/$p/evals"' EXIT
claude plugin eval "plugins/$p" "$@"
