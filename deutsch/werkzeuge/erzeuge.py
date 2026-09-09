# -*- coding: utf-8 -*-
"""Zu jedem Wort die orthografische Stolperstelle finden und daraus
   die Luecke sowie glaubwuerdige Fehlschreibungen ableiten.
   Grundsatz: lieber nur eine falsche Variante als eine unsinnige."""
import re, json
D=json.load(open("woerter.json"))

ECHTE={"ihn","ihm","fiel","seid","dass","wider","wahr","war","den","dem","man","mann",
       "meer","lehre","leere","mahl","mal","wen","wenn","stadt","statt","tot","tod",
       "lied","litt","rat","rad","isst","hüte","hütte","stille","stiele","waise","weise",
       "leib","laib","seite","saite","malen","mahlen","wahl","wal","lehren","leeren"}
for w in D["haeufig"]: ECHTE.add(w.lower())
for t in D["trainings"].values():
    for e in t: ECHTE.add(e.split()[-1].lower())

VOK="aeiouäöü"

def regeln(w):
    """(Priorität, Fehlschreibung, Stolperstelle) – nur typische Kinderfehler."""
    r=[]; k=w.lower()

    i=k.find("ß")                                   # ß -> ss / s
    if i>=0:
        r.append((1, w[:i]+"ss"+w[i+1:], (i,i+1)))
        r.append((1, w[:i]+"s"+w[i+1:],  (i,i+1)))

    m=re.search(r"([bdfgklmnprstz])\1", k)          # Doppelkonsonant vereinfacht
    if m:
        i=m.start(); r.append((2, w[:i]+w[i]+w[i+2:], (i,i+2)))

    i=k.find("ck")                                  # ck -> k / kk
    if i>=0:
        r.append((3, w[:i]+w[i+1:],      (i,i+2)))
        r.append((3, w[:i]+"kk"+w[i+2:], (i,i+2)))

    i=k.find("ie")                                  # ie -> i
    if i>=0:
        r.append((4, w[:i]+w[i]+w[i+2:], (i,i+2)))

    i=k.find("tz")                                  # tz -> z
    if i>=0:
        r.append((5, w[:i]+w[i+1:], (i,i+2)))

    m=re.search(r"(["+VOK+r"])h", k)                # stummes h weggelassen
    if m:
        i=m.start()+1; r.append((6, w[:i]+w[i+1:], (m.start(),i+1)))

    # h eingefuegt, wo keins hingehoert (langer Vokal in offener Silbe)
    m=re.search(r"^([^"+VOK+r"]*)(["+VOK+r"])([bdfgklmnprst])(e|en)$", k)
    if m and not re.search(r"["+VOK+r"]h", k):
        i=m.start(2)+1
        r.append((6, w[:i]+"h"+w[i:], (m.start(2), i+1)))

    if k.endswith("ig"):                            # -ig -> -ich
        r.append((7, w[:-2]+"ich", (len(w)-2,len(w))))
    if k.endswith("d"):                             # Auslaut d -> t
        r.append((8, w[:-1]+"t", (len(w)-1,len(w))))
    if k.endswith("g") and not k.endswith("ig"):    # Auslaut g -> k
        r.append((8, w[:-1]+"k", (len(w)-1,len(w))))
    if k.endswith("b"):                             # Auslaut b -> p
        r.append((8, w[:-1]+"p", (len(w)-1,len(w))))

    i=k.find("äu")                                  # äu -> eu
    if i>=0: r.append((9, w[:i]+("Eu" if w[i].isupper() else "eu")+w[i+2:], (i,i+2)))
    i=k.find("eu")                                  # eu -> oi
    if i>=0: r.append((9, w[:i]+("Oi" if w[i].isupper() else "oi")+w[i+2:], (i,i+2)))

    # Konsonant faelschlich verdoppelt (haeufigster Fehler ueberhaupt)
    m=re.search(r"["+VOK+r"]([bdfgklmnprst])["+VOK+r"]", k)
    if m and not re.search(r"([bdfgklmnprstz])\1", k):
        i=m.start(1); r.append((9, w[:i]+w[i]+w[i:], (max(0,i-1),i+1)))

    if k.startswith("v"):                           # v -> f
        r.append((10, ("F" if w[0].isupper() else "f")+w[1:], (0,1)))

    for u,e in (("ä","e"),("ö","o"),("ü","u")):     # Umlaut vereinfacht
        i=k.find(u)
        if i>=0:
            r.append((11, w[:i]+e+w[i+1:], (i,i+1))); break
    return sorted(r, key=lambda x:x[0])

def luecke_span(w):
    """Was verdeckt wird: erst der echte Stolperstein, dann ein Vokalpaar,
       sonst die Wortmitte."""
    k=w.lower()
    for muster in ("ß",):
        i=k.find(muster)
        if i>=0: return (i,i+1)
    m=re.search(r"([bdfgklmnprstz])\1", k)
    if m: return (m.start(), m.start()+2)
    for muster in ("ck","ie","tz","sch","pf"):
        i=k.find(muster)
        if i>=0: return (i,i+len(muster))
    m=re.search(r"(["+VOK+r"])h", k)
    if m: return (m.start(), m.start()+2)
    for muster in ("ei","au","eu","äu","ai","ä","ö","ü"):
        i=k.find(muster)
        if i>=0: return (i,i+len(muster))
    if k.endswith(("ig","d","g","b")):
        return (len(w)-1-(1 if k.endswith("ig") else 0), len(w))
    m=max(1,(len(w)-2)//2)
    return (m, min(m+2,len(w)))

def baue(eintrag):
    teile=eintrag.split()
    artikel=teile[0] if len(teile)>1 and teile[0] in ("der","die","das") else ""
    w=teile[-1]
    falsch=[]
    for _,f,_sp in regeln(w):
        if f==w or f.lower() in ECHTE or f in falsch: continue
        falsch.append(f)
        if len(falsch)==2: break
    span=luecke_span(w)
    luecke=list(range(span[0],min(span[1],len(w)))) if len(w)>=4 else []
    d={"a":artikel,"w":w,"l":luecke}
    if falsch: d["f"]=falsch
    return d

pakete=[]
for nr in sorted(D["trainings"], key=int):
    pakete.append({"id":f"lw{nr}","name":f"Lernwörter {nr}",
                   "woerter":[baue(e) for e in D["trainings"][nr]]})
h=D["haeufig"]
for i in range(0,len(h),28):
    pakete.append({"id":f"hw{i//28+1}","name":f"Häufigkeitswörter {i//28+1}",
                   "woerter":[baue(e) for e in h[i:i+28]]})
json.dump(pakete, open("pakete.json","w"), ensure_ascii=False)

alle=[x for p in pakete for x in p["woerter"]]
for p in pakete[:4]+pakete[11:13]:
    print(f"\n--- {p['name']} ---")
    for x in p["woerter"]:
        lk="".join("_" if i in x["l"] else x["w"][i] for i in range(len(x["w"]))) or "(zu kurz)"
        print(f"  {(x['a']+' '+x['w']).strip():18} {lk:15} {', '.join(x.get('f',[])) or '– keine Auswahl –'}")
print("\nWörter gesamt:", len(alle))
print("ohne Auswahlübung:", sum(1 for x in alle if not x.get("f")))
print("mit nur einer falschen Variante:", sum(1 for x in alle if len(x.get("f",[]))==1))
