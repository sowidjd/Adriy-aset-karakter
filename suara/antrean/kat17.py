import sys,json; sys.path.insert(0,"pipeline"); import perpustakaan_suara as L
B=json.load(open(f"{sys.argv[1]}/batch17.json")); k=L._baca(); T={t for _,t in B}
for e in k["kalimat"]:
    if e["teks"] in T: e["kategori"]="humor dan santai"
L._tulis(k); print("kategori batch17 diperbarui")
