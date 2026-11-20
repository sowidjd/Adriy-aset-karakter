# Aset karakter ADRIY (privat)

Gambar karakter ADRIY untuk video Adriy.project. Repo ini sengaja privat: berisi wajah ADRIY. Tokoh resmi video AdriyMine (menggantikan burung hantu Adriy).

- `santai/` — outfit santai (sweater abu-abu ADRIY, celana hitam, sneaker)
  - `00-penuh-berdiri.webp`, `lembar-01..09.png` — lembar asli badan penuh (4 pose per lembar)
  - `dekat/` — lembar asli close-up dan setengah badan, termasuk 5 bentuk mulut (`dekat-09.png`)
  - `aset.json` — daftar pose per lembar
  - `pose/` — hasil potong: satu PNG transparan per pose (dibuat `scripts/adri_aset.py` di repo Aidriy)
  - `peta.json` — peta pose ADRI -> gambar, dibaca video

- `travel/` — outfit travel (jaket abu-abu, ransel, tas pinggang ADRIY, headphone, botol, bantal leher, celana kargo)
  - `lembar-01..09.png` badan penuh, `dekat/` close-up, setengah badan, dan lembar bentuk mulut
  - `tata.json` — tata letak lembar dan peta pose khusus outfit ini

- `arkeolog/` — outfit arkeolog/petualang lapangan (topi rimba, kemeja khaki ADRIY, rompi, ransel), 85 pose
  siap pakai di `pose/`; dipakai otomatis untuk video bertopik sejarah/arkeologi

- `formal/` (69 pose) jas formal — investasi, ekonomi, bisnis, berita; juga style bisnis
- `angkasa/` (69 pose) astronot — luar angkasa, planet, atmosfer
- `penyelam/` (41 pose + 4 rusak di `rusak/`) penyelam — laut, hewan laut; ada siklus jalan dan bentuk mulut badan penuh
- `lab/` (78 pose) jas lab — sains, kimia, biologi, kedokteran; juga style sains

Outfit dipilih otomatis per video dari topik (lihat `art_direct` di pipeline.py repo Aidriy).

## Dipakai di repo Aidriy

```bash
bash video/scripts/ambil_aset.sh        # salin repo ini ke video/public/adri/ (tidak masuk git Aidriy)
```

Menambah aset baru: taruh lembar di folder outfit, tambah tata letaknya di `scripts/adri_aset.py` (repo Aidriy),
jalankan skrip itu, lalu commit hasilnya di sini.

## sfx/ — sound effect bebas pakai

Sound effect gratis dari internet yang boleh dipakai di video (termasuk dimonetisasi):

- `sfx/opengameart/<paket>/` — paket CC0 dari OpenGameArt.org (tanpa kredit)
- `sfx/soundbible/` — SoundBible.com, hanya Public Domain dan CC BY 3.0
- `sfx/wikimedia/<hewan>/` — suara hewan dari Wikimedia Commons (CC0 / Public Domain / CC BY)

Semua sudah diubah ke mp3 (44,1 kHz, 160 kbps). `sfx/katalog.json` mencatat judul, pembuat, lisensi, dan
sumber tiap file; `sfx/KREDIT.md` mendaftar file CC BY yang wajib dikredit di deskripsi video.

## objek/benda/ — 385 gambar benda

Benda sehari-hari untuk adegan objek (dapur, rumah, elektronik, uang, sains, tubuh, alam, luar angkasa,
transportasi, sejarah). Semua dari Openclipart.org, lisensi CC0 (bebas tanpa kredit). Latar transparan,
maks. 800 px. Terdaftar di `objek/katalog.json` (kategori "benda", kolom `kelompok`, `kata`, `sumber`):
gambar muncul otomatis bila naskah menyebut salah satu `kata`.

## Catatan

- Disalin dari `adriyarfiyfadilclash-lang/adriy-karakter-aset` (commit 22539ca). Folder `suara/` (perpustakaan suara VoxCPM) tidak ikut disalin, karena aturan AdriyMine: file tiruan suara pemilik tidak diunggah ke GitHub.
- Di AdriyMine, ambil aset dengan `bash projects/karakter/ambil_aset.sh` (disalin ke `projects/karakter/aset/`, tidak masuk git).
