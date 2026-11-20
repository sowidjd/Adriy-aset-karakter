import sys,json,re; sys.path.insert(0,"pipeline"); import perpustakaan_suara as L
S=sys.argv[1]; B=[]; nada=""; fungsi=""
for l in open(f"{S}/batch23.txt"):
    l=l.strip()
    if not l: continue
    if l.startswith("#"): fungsi=l[1:].strip(); continue
    m=re.fullmatch(r"\[(.+?)\]",l)
    if m: nada=m.group(1).strip().lower(); continue
    B.append((nada,fungsi,l))
L.buat([t for _,_,t in B],["adriy","ongky"])
k=L._baca()
for nada,f,t in B:
    for e in k["kalimat"]:
        if e["teks"]==t: e["catatan"]=f"nada {nada}"; e["kategori"]=f; e["fungsi"]=[f]
L._tulis(k); print("katalog diperbarui")
