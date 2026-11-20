# Aset karakter Adriy

Aset resmi tokoh **Adriy**, burung hantu kecil yang penasaran, maskot Adriy.Project. Dipakai di video TikTok proyek [AdriyMine](https://github.com/sowidjd/AdriyMine).

## Isi

| File | Isi |
|---|---|
| `karakter/adriy-lembar-karakter.png` | Lembar karakter resmi (1080×1920) |
| `karakter/adriy.html` | Sumber lembar karakter (Canvas) |
| `karakter/konsep-karakter.png` | Gambar konsep awal |
| `karakter/konsep.html` | Sumber gambar konsep |
| `_bersama/dasar.js` | Fungsi gambar `adriy(x, y, u, opsi)` (nama lama `clawd()` masih jalan) |
| `_bersama/fonts/` | Font Fredoka (lisensi OFL, lihat `OFL-Fredoka.md`) |

Buka file HTML lewat server lokal (misalnya `python3 -m http.server`), lalu buka `karakter/adriy.html`.

## Ciri wajib (tidak boleh diubah)

- Kacamata bulat besar, syal merah dengan ekor di kanan, jambul telinga, perut krem, paruh & kaki oranye.
- Warna tetap: badan `#A9714B`, sayap `#8A5A3C`, perut `#F1DCC0`, paruh/kaki `#F2A23B`, syal `#D9534F`.
- Gaya animasi hanya mengubah cara goresan (tinta manga, cat air, pensil), bukan bentuk dan warna.
- Ekspresi lewat mata di balik kacamata, ditambah tanda bergambar (!, ?, keringat, awan, lampu ide).
- Tokoh pendamping tidak boleh memakai kacamata bulat + syal merah.

Aturan lengkap ada di `aturan.md` §15 repo AdriyMine. Kalau karakter diubah di AdriyMine, perbarui juga repo ini.
