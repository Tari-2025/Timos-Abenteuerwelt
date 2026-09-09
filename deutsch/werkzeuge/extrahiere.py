import zlib, re, json
d=open("/root/.claude/uploads/3b584eed-df4b-5006-a2f1-06115eb1d8ee/5ceefecd-Lernw_rter_H_ufigkeitsw_rter.pdf","rb").read()
streams=[]
for s in re.findall(rb"stream\r?\n(.*?)endstream", d, re.S):
    try: r=zlib.decompress(s)
    except Exception: r=s
    if b"TJ" in r or b"Tj" in r: streams.append(r)

def dec(roh):
    out=bytearray(); i=0
    while i<len(roh):
        c=roh[i]
        if c==0x5c:
            n=roh[i+1:i+2]
            if n.isdigit():
                okt=roh[i+1:i+4]; out.append(int(okt,8)); i+=1+len(okt); continue
            out+=n; i+=2; continue
        out.append(c); i+=1
    return out.decode("cp1252","replace")

seiten=[]
for st in streams:
    eintraege=[]
    for m in re.finditer(rb"1 0 0 1 ([\d.]+) ([\d.]+) Tm\s*(.*?)ET", st, re.S):
        x,y=float(m.group(1)), float(m.group(2))
        teile=re.findall(rb"\((.*?)(?<!\\)\)", m.group(3), re.S)
        t="".join(dec(p) for p in teile).strip()
        if t: eintraege.append((x,y,t))
    seiten.append(eintraege)

# --- Seiten 1-3: je vier Bloecke (2 Spalten x 2 Bloecke) ---
trainings={}
for si in range(3):
    e=seiten[si]
    kopf=[(x,y,t) for x,y,t in e if t.startswith("Lernwörtertraining")]
    kopf.sort(key=lambda k:(-k[1], k[0]))
    for kx,ky,kt in kopf:
        nr=int(re.search(r"(\d+)", kt).group(1))
        # Woerter derselben Spalte, unterhalb dieser Ueberschrift
        kandidaten=[(x,y,t) for x,y,t in e
                    if abs(x-kx)<40 and y<ky-5 and not t.startswith("Lernwörtertraining")
                    and not t.startswith("Lernwörter zweites")]
        # nur bis zur naechsten Ueberschrift derselben Spalte
        naechste=[ky2 for kx2,ky2,_ in kopf if abs(kx2-kx)<40 and ky2<ky-5]
        grenze=max(naechste) if naechste else -1
        woerter=[(y,t) for x,y,t in kandidaten if y>grenze]
        woerter.sort(key=lambda w:-w[0])
        trainings[nr]=[t for _,t in woerter]

# --- Seite 4: Haeufigkeitswoerter, vier Spalten ---
e=seiten[3]
raus={"111 Häufigkeits","-","/Merkwörter","des","Grundwortschatzes NRW"}
posten=[(x,y,t) for x,y,t in e if t not in raus]
spalten=sorted(set(round(x) for x,_,_ in posten))
gruppen=[]
for x in spalten:
    if gruppen and x-gruppen[-1][-1]<40: gruppen[-1].append(x)
    else: gruppen.append([x])
def spalte(x):
    for i,g in enumerate(gruppen):
        if round(x) in g: return i
    return 99
posten.sort(key=lambda p:(spalte(p[0]), -p[1]))
haeufig=[t for x,y,t in posten]

print("Trainings:", sorted(trainings))
for nr in sorted(trainings):
    print(f"  {nr}: ({len(trainings[nr])}) " + ", ".join(trainings[nr]))
print(f"\nHäufigkeitswörter ({len(haeufig)}):")
print(", ".join(haeufig))
json.dump({"trainings":trainings,"haeufig":haeufig}, open("woerter.json","w"), ensure_ascii=False, indent=1)
