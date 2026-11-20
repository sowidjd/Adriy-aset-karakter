import sys,json; sys.path.insert(0,"pipeline"); import perpustakaan_suara as L
B=json.load(open(f"{sys.argv[1]}/batch9.json"))
k=L._baca()
for i,(n,t) in enumerate(B):
    kat="pengenalan akun" if i<15 else "ajakan" if i<30 else "cta" if i<45 else "peralihan"
    for e in k["kalimat"]:
        if e["teks"]==t: e["kategori"]=kat
L._tulis(k); print("kategori batch9 diperbarui")
