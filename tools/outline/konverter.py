"""Laver plugins om til sider til Outline (dok.mgai.dk).

Plugins er skrevet til Claude med filstier (`references/x.md`, `${CLAUDE_SKILL_DIR}/../y/SKILL.md`).
I Outline skal de samme henvisninger være links mellem sider. Dette modul bygger alle sider som
markdown med relative `.md`-links. `synk.py` laver bagefter de relative links om til Outline-links.

Sidernes stier (nøglerne i det, `byg_sider` returnerer):
  Skills.md                                oversigt
  Skills/<plugin>.md                       plugin-side
  Skills/<plugin>/<skill>.md               SKILL.md
  Skills/<plugin>/<skill>/<fil>.md         references, scripts m.m. (fladt)

Kun standardbiblioteket.
"""
import json
import re
from pathlib import Path

# Plugins, der lægges i Outline. Andre plugins lægges kun ind som en kort side, der henviser til GitHub.
I_OUTLINE = ["bloom", "blooket", "cl-oevelser", "dida", "klasseledelse",
             "modulplanlaegger", "udretterdagsorden"]
KUN_PLUGIN = {
    "casespilsdesigner": "Casespilsdesigneren er stor og har mange scripts og digitale dele. "
                         "Den bruges derfor som plugin og ligger ikke i Outline.",
}
SPRING_OVER = {".gitignore", "package-lock.json", ".DS_Store"}
SPRING_OVER_MAPPER = {"node_modules", "__pycache__", "evals", "tests"}
SPROG = {".py": "python", ".js": "javascript", ".json": "json", ".txt": "text",
         ".csv": "csv", ".sh": "bash"}
MAPPER = ("references", "scripts", "resources", "examples", "assets")
STI_I_KODE = re.compile(r"`\"?((?:\$\{CLAUDE_SKILL_DIR\}/)?(?:\.\./)?[A-Za-z0-9_./-]+?)\"?`")
REPO = "KennethEU/kennethsplugins"


def frontmatter(tekst):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", tekst, re.S)
    if not m:
        return {}, tekst
    data, noegle = {}, None
    for linje in m.group(1).splitlines():
        hit = re.match(r"^([A-Za-z_-]+):\s*(.*)$", linje)
        if hit:
            noegle = hit.group(1)
            data[noegle] = hit.group(2).strip().strip('"').strip("'").replace('\\"', '"')
        elif noegle and linje.strip() and not linje.lstrip().startswith("- "):
            data[noegle] = (data[noegle] + " " + linje.strip()).strip()
    return data, tekst[m.end():]


def uden_h1(tekst):
    """Gør en indledende H1 til fed tekst, så titlen kommer fra filnavnet."""
    linjer = tekst.lstrip("\n").split("\n")
    if linjer and linjer[0].startswith("# "):
        linjer[0] = "**" + linjer[0][2:].strip() + "**"
    return "\n".join(linjer)


def md_navn(relsti):
    navn = relsti.replace("/", "-")
    return navn if navn.endswith(".md") else navn + ".md"


def omskriv_links(tekst, skill, plugin_skills):
    """Rigtige markdown-links til egne underfiler og til skills i samme plugin."""
    tekst = re.sub(r"\]\((?:\./)?(?:references|scripts|resources|examples|assets)/([^)#\s]+)",
                   lambda m: f"]({skill}/{md_navn(m.group(1))}", tekst)
    tekst = re.sub(r"\]\(\.\./([a-z0-9-]+)/SKILL\.md\)",
                   lambda m: f"]({m.group(1)}.md)" if m.group(1) in plugin_skills else m.group(0), tekst)
    return tekst


def find_maal(sti, skill, sider):
    """Finder siden for en sti i `kode`. sider: {skill: {sidenavne}}.
    Returnerer (skill, sidenavn eller None for selve skill-siden) eller None."""
    sti = sti.replace("${CLAUDE_SKILL_DIR}/", "")
    if sti.startswith("./"):
        sti = sti[2:]
    dele = sti.split("/")
    if len(dele) == 1:
        if dele[0] == "SKILL.md":
            return (skill, None)
        return (dele[0], None) if dele[0] in sider and dele[0] != skill else None
    if dele[0] == ".." and len(dele) > 1:
        maal, rest = dele[1], dele[2:]
    elif dele[0] in sider:
        maal, rest = dele[0], dele[1:]
    else:
        maal, rest = skill, dele
    if maal not in sider:
        return None
    if rest in ([], [""], ["SKILL.md"]):
        return (maal, None) if maal != skill or rest == ["SKILL.md"] else None
    if rest[0] not in MAPPER or len(rest) < 2 or not rest[-1]:
        return None
    navn = md_navn("/".join(rest[1:]))
    if navn in sider[maal]:
        return (maal, navn)
    andre = [s for s, navne in sider.items() if navn in navne]
    return (andre[0], navn) if len(andre) == 1 else None


def stier_til_links(tekst, skill, sider, plugin_af, dybde):
    """Gør stier i `kode` (uden for kodeblokke) til relative links.
    dybde 0: skill-side (Skills/<plugin>/), 1: underside (Skills/<plugin>/<skill>/)."""
    op = "../" * dybde
    plugin = plugin_af[skill]

    def erstat(m):
        hit = find_maal(m.group(1), skill, sider)
        if not hit:
            return m.group(0)
        maal, navn = hit
        sti = op if plugin_af[maal] == plugin else op + f"../{plugin_af[maal]}/"
        if navn is None:
            return f"[{maal}]({sti}{maal}.md)"
        return f"[{navn[:-3]}]({sti}{maal}/{navn})"

    ud, i_blok = [], False
    for linje in tekst.split("\n"):
        if linje.lstrip().startswith("```"):
            i_blok = not i_blok
        ud.append(linje if i_blok else STI_I_KODE.sub(erstat, linje))
    return "\n".join(ud)


def som_markdown(sti):
    if sti.suffix == ".md":
        return uden_h1(sti.read_text(encoding="utf-8"))
    sprog = SPROG.get(sti.suffix, "")
    indhold = sti.read_text(encoding="utf-8")
    return (f"Filen `{sti.name}` fra pluginet. Kopier den til en fil med samme navn, "
            f"og kør den derfra.\n\n```{sprog}\n{indhold.rstrip()}\n```\n")


def underfiler(skilldir):
    for f in sorted(skilldir.rglob("*")):
        rel = f.relative_to(skilldir)
        if any(del_ in SPRING_OVER_MAPPER or del_.startswith(".") for del_ in rel.parts):
            continue
        if f.is_file() and f.name != "SKILL.md" and f.name not in SPRING_OVER:
            if len(rel.parts) > 1:  # kun filer i undermapper (references/, scripts/ ...)
                yield f, md_navn(str(Path(*rel.parts[1:])))


def byg_sider(plugins_dir):
    """Returnerer {sti: markdown} for alle sider. Stierne er relative til collectionen."""
    plugins_dir = Path(plugins_dir)
    sider_idx, plugin_af = {}, {}
    for plugin in I_OUTLINE:
        for s in sorted((plugins_dir / plugin / "skills").glob("*/SKILL.md")):
            s = s.parent
            plugin_af[s.name] = plugin
            sider_idx[s.name] = {navn for _, navn in underfiler(s)}

    ud = {}
    oversigt = ["Kenneths egne plugins som skills. Kilden er udviklingsmappen og GitHub-repoet "
                f"`{REPO}`. Ret ikke her: ændringer overskrives ved næste udgivelse.",
                "", "Hver plugin er en underside. Hver skill er en underside til sit plugin. "
                "Filer, som skill'en henviser til (references, scripts), ligger som undersider til skill'en.",
                "", "| Plugin | Skills | Beskrivelse |", "| :--- | :--- | :--- |"]

    for plugin in I_OUTLINE:
        pdir = plugins_dir / plugin
        meta = json.loads((pdir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        skills = sorted(p.parent for p in (pdir / "skills").glob("*/SKILL.md"))
        navne = [s.name for s in skills]
        beskrivelse = meta.get("description", "")
        oversigt.append(f"| [{plugin}](Skills/{plugin}.md) | {len(skills)} | {beskrivelse} |")

        side = [beskrivelse, "", f"Version {meta.get('version', '?')}.", "", "**Skills:**", ""]
        for s in skills:
            fm, _ = frontmatter((s / "SKILL.md").read_text(encoding="utf-8"))
            side.append(f"- [{s.name}]({plugin}/{s.name}.md): {fm.get('description', '')}")
        ud[f"Skills/{plugin}.md"] = "\n".join(side) + "\n"

        for s in skills:
            fm, krop = frontmatter((s / "SKILL.md").read_text(encoding="utf-8"))
            hoved = [f"> **Skill:** `{s.name}` fra pluginet {plugin}.", ">",
                     f"> **Beskrivelse:** {fm.get('description', '')}", "", ""]
            krop = omskriv_links(uden_h1(krop), s.name, navne)
            krop = stier_til_links(krop, s.name, sider_idx, plugin_af, 0)
            ud[f"Skills/{plugin}/{s.name}.md"] = "\n".join(hoved) + krop
            for f, navn in underfiler(s):
                indhold = som_markdown(f)
                if f.suffix == ".md":
                    indhold = stier_til_links(indhold, s.name, sider_idx, plugin_af, 1)
                ud[f"Skills/{plugin}/{s.name}/{navn}"] = indhold

    for plugin, grund in KUN_PLUGIN.items():
        pj = plugins_dir / plugin / ".claude-plugin" / "plugin.json"
        beskrivelse = json.loads(pj.read_text(encoding="utf-8")).get("description", "") if pj.exists() else ""
        oversigt.append(f"| [{plugin}](Skills/{plugin}.md) | (plugin) | {beskrivelse} |")
        ud[f"Skills/{plugin}.md"] = (
            f"{beskrivelse}\n\n**Bruges som plugin.** {grund}\n\n"
            f"Tilføj marketplacet `{REPO}` i Claude, og installer pluginet `{plugin}`.\n")

    ud["Skills.md"] = "\n".join(oversigt) + "\n"
    return ud
