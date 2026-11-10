"""Test af sprogtjek.py. Kør: python3 plugins/casespilsdesigner/tests/test_sprogtjek.py"""
import os, subprocess, sys, tempfile, zipfile

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "skills", "casespil-sprogtjek", "scripts", "sprogtjek.py")


def run(files):
    """files: {relativ sti: tekst eller bytes}. Returnerer (returkode, output)."""
    with tempfile.TemporaryDirectory() as d:
        for rel, content in files.items():
            path = os.path.join(d, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                f.write(content if isinstance(content, bytes) else content.encode("utf-8"))
        r = subprocess.run([sys.executable, SCRIPT, d], capture_output=True, text=True)
        return r.returncode, r.stdout


def docx(body, header=None):
    path = tempfile.mktemp(suffix=".docx")
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("word/document.xml", f"<w:document><w:p><w:t>{body}</w:t></w:p></w:document>")
        if header:
            z.writestr("word/header1.xml", f"<w:hdr><w:p><w:t>{header}</w:t></w:p></w:hdr>")
    data = open(path, "rb").read()
    os.remove(path)
    return data


def test_filnavne_er_ikke_ascii_fejl():
    code, out = run({"guide.txt": "Print kun denne ene: Laererpakke_Fjord_Samlet.docx og laerer-motor.js"})
    assert code == 0 and "ASCII" not in out, out
    code, out = run({"guide.txt": "Laereren siger noget."})
    assert code == 1 and "ASCII" in out, out


def test_tankestreg_er_fejl():
    code, out = run({"guide.txt": "OK — nu har vi analyseret."})
    assert code == 1 and "tankestreg" in out, out


def test_ritual_er_advarsel():
    code, out = run({"guide.txt": "I spiller en rolle i dag."})
    assert code == 0 and "ADVARSEL" in out and "ritualsætning" in out, out


def test_bindestreg_i_sammensat_ord():
    code, out = run({"guide.txt": "Åbn lærer-assistenten. AI-rådgiveren og 1-klik linket er fine."})
    assert code == 0 and out.count("bindestreg") == 1, out


def test_arkiv_og_node_modules_springes_over():
    code, out = run({"arkiv_2026-11-01/gammel.txt": "max. 5", "_arkiv/x.txt": "max. 5",
                     "node_modules/pakke/index.js": 'const t = "Budget forhandling er max. 5 runder";',
                     "ny.txt": "Alt er fint."})
    assert code == 0 and "1 fil(er) tjekket" in out, out


def test_spilfil_laeses_men_kode_goer_ikke():
    spil = ('module.exports = { meta: { slug: "laerer-test", paa: 1 },\n'
            '  tekster: { stopregel: "Budget forhandling slutter — max. 5 runder for alle" },\n'
            '  css: "width: 100%" };\n')
    code, out = run({"produktion/spil.cjs": spil})
    assert code == 1 and "tankestreg" in out and "max." in out and "budget forhandling" in out, out
    assert "linje 2" in out and "ASCII" not in out and "60 %" not in out, out


def test_sidehoved_i_docx_laeses():
    code, out = run({"pakke.docx": docx("Alt er fint her.", header="Fortroligt — kun til læreren")})
    assert code == 1 and "tankestreg" in out, out
    code, out = run({"pakke.docx": docx("Alt er fint her.")})
    assert code == 0, out


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("OK", name)
