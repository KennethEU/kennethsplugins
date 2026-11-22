# kennethsplugins

Kenneths plugins til dansk gymnasieundervisning. Se README.md.

## Skills ligger to steder

Denne mappe er den eneste kilde. Skillene udgives både som plugins på GitHub og som sider i Outline (dok.mgai.dk, under Fælles → Skills, én side pr. plugin).

- Efter hver ændring: kør `./udgiv.sh "besked"`, eller sig til Kenneth, at det skal køres. Push og ændringer i Outline kræver hans ja.
- Ret aldrig i Outline-kopien. Den overskrives.
- Skriv stier som nu (`references/x.md`, `${CLAUDE_SKILL_DIR}/../y/SKILL.md`). `tools/outline/konverter.py` laver dem om til Outline-links. Stier inde i kodeblokke og kommandoer ændres ikke.
- Hvilke plugins der kommer i Outline, styres af `I_OUTLINE` og `KUN_PLUGIN` øverst i `tools/outline/konverter.py`.
- `synk.py` ejer kun siderne Skills/<plugin> for plugins i listen og alt under dem. Siden "Skills", "Om vidensbasen" og kollegernes skills i Fælles røres aldrig.
- Test konverteringen uden at røre Outline: `python3 tools/outline/synk.py` (prøvekørsel).
