# Tests af rollespilsdesigneren

## Automatiske triggertests (denne mappe)

27 cases i `trigger-*`. Hver sender en besked og tjekker, om den rigtige skill bliver valgt (`tool_used: Skill`).

- `trigger-<emne>-N`: almindelige formuleringer (14 cases).
- `trigger-rodet-N`: rodede, korte formuleringer, som de skrives i travlhed (7 cases).
- `trigger-nej-*` og `trigger-ingen-rollespil`: nære negativer, der deler ord med rollespil men hører til andre skills, fx dagsorden, eksamen, Bloom, videomanuskript og korrektur af elevsvar. Ingen rollespilsskill må udløses (6 cases).

Kør fra repositoryets rod:

```
claude plugin eval plugins/rollespilsdesigner --ablation none -j 6
```

Koster ca. 5 $ for hele suiten. Rapporten ligger i `evals/results/` (ignoreres af git). Kør den igen efter hver ændring af en `description`.

Sidst kørt oktober 2026: alle 27 består. Før beskrivelserne blev gjort skarpere, udløste rodede formuleringer om faseskift ikke lærerguiden.

## Tests, du selv skal køre i Cowork

Brug rigtige opgaver og noter, hvad der går skævt.

1. **Nyt rollespil.** `/nyt-rollespil` med et emne fra din egen undervisning. Gennemfør hele flowet. Tjek: stiller den spørgsmålene i rækkefølge, stopper den ved godkendelsespunkter, ender den med konsistenstjek?
2. **Miniversion.** `/miniversion` på et eksisterende rollespil (fx Fjord Outdoor).
3. **Konsistenstjek af færdigt materiale.** Peg på en mappe med færdige filer. Tjek, at `sprogtjek.py` bliver kørt, og at rapporten har punkt 0 til 8.
4. **Samme som test 1 på Haiku, Sonnet og Opus.** Springer en billigere model faser eller projektregler over?
5. **Installation.** Upload pluginet som zip eller tilføj marketplace'en `KennethEU/kennethsplugins`. Alle 10 skills skal dukke op, og docx-generering og `sprogtjek.py` skal virke.
6. **Efter nogle ugers brug.** Kør `/skill-doctor` og se, hvilke skills der aldrig udløses, og hvad pluginet koster pr. session.
