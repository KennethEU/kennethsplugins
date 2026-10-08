"""Test af generate_csv.py. Kør: python3 plugins/blooket/tests/test_generate_csv.py"""
import csv, io, json, os, subprocess, sys, tempfile

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "skills", "blooket-quizformat", "references", "generate_csv.py")


def run(questions):
    with tempfile.TemporaryDirectory() as d:
        src, out = os.path.join(d, "q.json"), os.path.join(d, "out.csv")
        with open(src, "w", encoding="utf-8") as f:
            json.dump(questions, f)
        r = subprocess.run([sys.executable, SCRIPT, src, out], capture_output=True, text=True)
        data = open(out, "rb").read() if os.path.exists(out) else None
        return r, data


def good(n=8):
    return [{"text": f"Spørgsmål {i}?", "answers": ["a", "b", "c", "d"], "correct": str(i % 4 + 1), "time": 20} for i in range(n)]


def test_format():
    r, data = run(good())
    assert r.returncode == 0, r.stdout + r.stderr
    assert data[:3] == b"\xef\xbb\xbf", "mangler BOM"
    assert b"\r\n" in data and b"\n" not in data.replace(b"\r\n", b"").replace(b'"Blooket\nImport', b"").replace(b"\n(Optional)", b"").replace(b"\n(Max", b"").replace(b"\n(Only", b""), "forkerte linjeskift"
    rows = list(csv.reader(io.StringIO(data.decode("utf-8-sig")), delimiter=";"))
    assert {len(x) for x in rows} == {26}, "ikke 26 kolonner i alle rækker"
    assert rows[2][1] == "Spørgsmål 0?" and rows[2][7] == "1"


def test_rejects_bad_input():
    for bad in ([{"text": "x", "answers": ["a"], "correct": "1"}],
                [{"text": "x", "answers": ["a", "b"], "correct": "3"}],
                [{"text": "a;b", "answers": ["a", "b"], "correct": "1"}],
                [{"text": "x", "answers": ["a", "b"], "correct": "1", "time": 500}]):
        r, _ = run(bad)
        assert r.returncode == 1 and "FEJL" in r.stdout, bad


def test_warns_on_skewed_answers():
    skewed = [{"text": f"q{i}", "answers": ["a", "b"], "correct": "1"} for i in range(10)]
    r, _ = run(skewed)
    assert r.returncode == 0 and "ADVARSEL" in r.stdout


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("OK", name)
