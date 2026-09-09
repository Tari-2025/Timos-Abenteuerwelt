# -*- coding: utf-8 -*-
"""Tauscht die Wortpakete in der fertigen Spieldatei aus.
   Nach jeder Änderung an den Listen: erzeuge.py, dann dieses Skript."""
import io, json, re
daten=json.dumps(json.load(open("pakete.json")), ensure_ascii=False, separators=(",",":"))
p="nilo-lernwoerter.html"
s=io.open(p,encoding="utf-8").read()
neu, n = re.subn(r"const PAKETE=.*?;\n", "const PAKETE="+daten+";\n", s, count=1, flags=re.S)
assert n==1, "PAKETE-Zeile nicht gefunden"
io.open(p,"w",encoding="utf-8").write(neu)
pak=json.loads(daten)
print(f"{len(pak)} Pakete, {sum(len(x['woerter']) for x in pak)} Wörter eingesetzt.")
