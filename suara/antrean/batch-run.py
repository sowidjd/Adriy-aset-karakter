import sys,json,re; sys.path.insert(0,"pipeline"); import perpustakaan_suara as L
S,name=sys.argv[1],sys.argv[2]; raw=[l.strip() for l in open(f"{S}/{name}.txt") if l.strip()]
B=[]; nada=""
for l in raw:
    m=re.fullmatch(r"\[(.+?)\]",l)
    if m: nada=m.group(1).strip().lower()
    else: B.append((nada,l))
json.dump(B,open(f"{S}/{name}.json","w"),ensure_ascii=False)
L.buat([t for _,t in B],["adriy","ongky"])
k=L._baca()
for i,(nada,t) in enumerate(B):
    kat="umum" if (name=="batch3" and i>=14) or name in ("batch4","batch5","batch6","batch7","batch8","batch9","batch10","batch11","batch12","batch13","batch14","batch15","batch16","batch17","batch18","batch19","batch20","batch21","batch22") else ("hook" if t.startswith(("Pernah nggak","Pernah terpikir")) else "")
    for e in k["kalimat"]:
        if e["teks"]==t:
            e["catatan"]=f"nada {nada}"
            if kat: e["kategori"]=kat
L._tulis(k); print("katalog diperbarui")
