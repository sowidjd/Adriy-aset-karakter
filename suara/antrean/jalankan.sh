#!/bin/bash
# Antrean perpustakaan suara: jalankan batch berurutan, selamatkan rekaman yang sudah jadi, simpan + push tiap batch.
# Pakai: bash video/public/adri/suara/antrean/jalankan.sh 8 9 10 ... (dari folder Aidriy)
cd /home/user/Aidriy || exit 1
A=video/public/adri/suara/antrean
L=$A/log; mkdir -p $L
N="$(git log -1 --format=%an)"; E="$(git log -1 --format=%ae)"
for b in "$@"; do
  [ -f $L/batch$b.selesai ] && continue
  echo "== batch$b mulai $(date +%H:%M)" >> $L/antrean.log
  # selamatkan rekaman dari proses yang terhenti
  python3 - $A $b <<'PY' >> $L/antrean.log 2>&1
import sys,re; sys.path.insert(0,"pipeline"); import perpustakaan_suara as P
A,b=sys.argv[1],sys.argv[2]; nada=""; n=0
for l in open(f"{A}/batch{b}.txt"):
    l=l.strip(); m=re.fullmatch(r"\[(.+?)\]",l)
    if not l or l.startswith("#"): continue
    if m: nada=m.group(1).strip().lower(); continue
    for v in ("adriy","ongky"):
        w=P.LIB/".buat"/f"{P.kid(v,l)}.wav"
        if w.exists() and P.simpan(v,l,w,"",f"nada {nada}","perpustakaan_suara.py"): n+=1
print("diselamatkan",n)
PY
  rm -rf video/public/adri/suara/.buat
  if [ "$b" = 23 ]; then python3 $A/batch23-run.py $A >> $L/batch$b.log 2>&1
  else python3 $A/batch-run.py $A batch$b >> $L/batch$b.log 2>&1; fi
  [ -f $A/kat$b.py ] && python3 $A/kat$b.py $A >> $L/batch$b.log 2>&1
  python3 pipeline/perpustakaan_suara.py tandai >> $L/batch$b.log 2>&1
  (cd video/public/adri && git add suara/adriy suara/ongky suara/katalog.json suara/antrean && \
   git -c user.name="$N" -c user.email="$E" commit -q -m "Perpustakaan suara: batch $b" && git -c push.negotiate=true push -q origin main) >> $L/antrean.log 2>&1
  touch $L/batch$b.selesai
  echo "== batch$b selesai $(date +%H:%M)" >> $L/antrean.log
done
