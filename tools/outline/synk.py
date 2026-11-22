#!/usr/bin/env python3
"""Opdaterer collectionen "Kenneths plugins" i Outline (dok.mgai.dk) ud fra plugins/ i dette repo.

Siderne rettes på stedet (samme side-id), så links, kommentarer og historik bevares.
Uden --udfoer vises kun, hvad der ville ske (prøvekørsel).

  python3 tools/outline/synk.py              prøvekørsel: vis ændringer
  python3 tools/outline/synk.py --udfoer     udfør ændringerne
  python3 tools/outline/synk.py --udfoer --slet   slet også sider, der ikke længere findes i repoet
  python3 tools/outline/synk.py --alle       behandl alle sider som ændrede (fx efter ændring i konverteringen)

API-nøglen hentes fra miljøvariablen OUTLINE_API_KEY eller fra Macens nøglering
(tjeneste "outline-mgai"). Læg den i nøgleringen sådan (du bliver bedt om at indsætte nøglen):
  security add-generic-password -a "$USER" -s outline-mgai -w

Kun standardbiblioteket.
"""
import hashlib
import json
import os
import posixpath
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from konverter import byg_sider  # noqa: E402

URL = os.environ.get("OUTLINE_URL", "https://dok.mgai.dk")
COLLECTION = os.environ.get("OUTLINE_COLLECTION", "Kenneths plugins")
REPO_ROD = Path(__file__).resolve().parents[2]
TILSTAND = Path(__file__).resolve().parent / ".synk-tilstand.json"
LINK = re.compile(r"\]\(([^)\s]+?\.md)\)")


def api_noegle():
    if os.environ.get("OUTLINE_API_KEY"):
        return os.environ["OUTLINE_API_KEY"]
    try:
        return subprocess.run(["security", "find-generic-password", "-s", "outline-mgai", "-w"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        sys.exit("Ingen API-nøgle. Lav en i Outline (Indstillinger → API og adgang) og læg den i nøgleringen:\n"
                 '  security add-generic-password -a "$USER" -s outline-mgai -w')


class Outline:
    def __init__(self, noegle):
        self.noegle = noegle

    def kald(self, metode, data):
        req = urllib.request.Request(f"{URL}/api/{metode}", data=json.dumps(data).encode(),
                                     headers={"Authorization": f"Bearer {self.noegle}",
                                              "Content-Type": "application/json",
                                              "Accept": "application/json"})
        for forsoeg in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as svar:
                    return json.loads(svar.read())
            except urllib.error.HTTPError as e:
                if e.code == 429 and forsoeg < 3:
                    time.sleep(5 * (forsoeg + 1))
                    continue
                sys.exit(f"Fejl fra Outline ved {metode}: {e.code} {e.read().decode()[:300]}")

    def collection_id(self, navn):
        offset = 0
        while True:
            data = self.kald("collections.list", {"limit": 100, "offset": offset})["data"]
            for c in data:
                if c["name"] == navn:
                    return c["id"]
            if len(data) < 100:
                sys.exit(f'Fandt ingen collection med navnet "{navn}".')
            offset += 100

    def traeet(self, cid):
        """{(titel, undertitel, ...): id} for alle udgivne sider i collectionen."""
        ud = {}

        def gaa(noder, sti):
            for n in noder:
                noegle = sti + (n["title"],)
                if noegle in ud:
                    print(f"  Advarsel: to sider med samme sti {'/'.join(noegle)}. Bruger den første.")
                else:
                    ud[noegle] = n["id"]
                gaa(n.get("children", []), noegle)

        gaa(self.kald("collections.documents", {"id": cid})["data"], ())
        return ud


def som_noegle(sti):
    return tuple(sti[:-3].split("/"))


def links_til_outline(sti, tekst, ids):
    """Gør relative .md-links til /doc/<id>. Returnerer (tekst, liste over links uden mål)."""
    mappe = posixpath.dirname(sti)
    mangler = []

    def erstat(m):
        href = m.group(1)
        if "://" in href:
            return m.group(0)
        maal = posixpath.normpath(posixpath.join(mappe, urllib.parse.unquote(href)))
        doc = ids.get(som_noegle(maal))
        if not doc:
            mangler.append(href)
            return m.group(0)
        return f"](/doc/{doc})"

    return LINK.sub(erstat, tekst), mangler


def main(argv):
    udfoer, slet, alle = "--udfoer" in argv, "--slet" in argv, "--alle" in argv
    sider = byg_sider(REPO_ROD / "plugins")
    print(f"{len(sider)} sider bygget fra {REPO_ROD / 'plugins'}")

    ol = Outline(api_noegle())
    cid = ol.collection_id(COLLECTION)
    findes = ol.traeet(cid)
    print(f'Outline: "{COLLECTION}" har {len(findes)} sider')

    tilstand = json.loads(TILSTAND.read_text()) if TILSTAND.exists() else {}
    if tilstand.get("collection") != cid:
        tilstand = {"collection": cid, "sider": {}}

    oenskes = {som_noegle(s): s for s in sider}
    nye = sorted((n for n in oenskes if n not in findes), key=len)
    ekstra = [n for n in findes if n not in oenskes]
    # Slet kun de øverste ekstra sider; undersider slettes med dem
    ekstra_top = [n for n in ekstra if n[:-1] not in ekstra]

    # 1. Opret manglende sider (tomme), forælder før barn
    ids = dict(findes)
    for n in nye:
        forælder = ids.get(n[:-1]) if len(n) > 1 else None
        print(f"  + opret   {'/'.join(n)}")
        if udfoer:
            if len(n) > 1 and not forælder:
                sys.exit(f"Mangler forælder til {'/'.join(n)}")
            data = {"title": n[-1], "text": "", "collectionId": cid, "publish": True}
            if forælder:
                data["parentDocumentId"] = forælder
            ids[n] = ol.kald("documents.create", data)["data"]["id"]
            time.sleep(0.2)
        else:
            ids[n] = f"<ny:{'/'.join(n)}>"

    # 2. Opdater tekst, hvor den er ændret
    rettet = uaendret = 0
    alle_mangler = []
    for n, sti in sorted(oenskes.items(), key=lambda x: len(x[0])):
        tekst, mangler = links_til_outline(sti, sider[sti], ids)
        alle_mangler += [(sti, m) for m in mangler]
        sha = hashlib.sha256(tekst.encode()).hexdigest()
        if not alle and n not in nye and tilstand["sider"].get(sti) == sha:
            uaendret += 1
            continue
        rettet += 1
        if n not in nye:
            print(f"  ~ ret     {sti}")
        if udfoer:
            ol.kald("documents.update", {"id": ids[n], "text": tekst, "publish": True})
            tilstand["sider"][sti] = sha
            time.sleep(0.2)

    # 3. Sider i Outline, som ikke længere findes i repoet
    for n in ekstra_top:
        under = sum(1 for e in ekstra if e[:len(n)] == n) - 1
        print(f"  - {'slet' if slet else 'ekstra'}   {'/'.join(n)}" + (f" (+{under} undersider)" if under else ""))
        if udfoer and slet:
            ol.kald("documents.delete", {"id": ids[n]})
            time.sleep(0.2)
    if udfoer and slet:
        tilstand["sider"] = {s: h for s, h in tilstand["sider"].items() if som_noegle(s) in oenskes}

    for sti, href in alle_mangler:
        print(f"  ! link uden mål i {sti}: {href}")

    print(f"\nNye: {len(nye)}. Ændrede: {rettet - len(nye)}. Uændrede: {uaendret}. "
          f"Ekstra i Outline: {len(ekstra)}{' (slettet)' if udfoer and slet else ''}. "
          f"Links uden mål: {len(alle_mangler)}.")
    if udfoer:
        TILSTAND.write_text(json.dumps(tilstand, indent=1, ensure_ascii=False))
        print("Udført.")
    else:
        print("Prøvekørsel. Intet er ændret. Kør med --udfoer for at gennemføre.")


if __name__ == "__main__":
    main(sys.argv[1:])
