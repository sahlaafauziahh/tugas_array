print("===== Studi Kasus 1 =====")

def input_mahasiswa():
  """Memasukkan data mahasiswa."""
  mahasiswa = []
  while True:
    nama = input("\nMasukkan nama : ")
    nim = input("Masukkan NIM : ")
    prodi = input("Masukkan Prodi : ")
    nilai = float(input("Masukkan nilai : "))

    mahasiswa.append({
      "nama" : nama,
      "nim" : nim,
      "prodi" : prodi,
      "nilai" : nilai
    })

    tambah_lagi = input("\nTambah data lagi (y/n)? ")
    if tambah_lagi.lower() != "y":
      break

  return mahasiswa

def tampil_mahasiswa(mahasiswa):
  """Menampilkan data mahasiswa."""
  if not mahasiswa:
    print("Data mahasiswa tidak ada.")
    return

  print("Daftar Mahasiswa :")
  for m in mahasiswa:
    print(f"Nama: {m['nama']}")
    print(f"NIM: {m['nim']}")
    print(f"Prodi: {m['prodi']}")
    print(f"Nilai: {m['nilai']}")
    print("-------------------------")

def kalkulator_ratarata_nilai(mahasiswa):
  """Menghitung dan menampilkan rata-rata nilai mahasiswa."""
  if not mahasiswa:
    print("Data mahasiswa tidak ada.")
    return

  total_score = 0
  for m in mahasiswa:
    total_score += m["nilai"]

  ratarata_nilai = total_score / len(mahasiswa)
  print(f"Rata-rata nilai: {ratarata_nilai:.2f}")

def temukan_tertinggi_dan_terendah_skor(mahasiswa):
  """Mencari dan menampilkan mahasiswa dengan nilai tertinggi dan terendah."""
  if not mahasiswa:
    print("Data mahasiswa kosong.")
    return

  tertinggi_skor_murid = mahasiswa[0]
  terendah_skor_murid = mahasiswa[0]

  for m in mahasiswa:
    if m["nilai"] > tertinggi_skor_murid["nilai"]:
     tertinggi_skor_murid = m
    elif m["nilai"] < terendah_skor_murid["nilai"]:
      terendah_skor_murid = m

  print(f"Mahasiswa dengan nilai tertinggi:")
  print(f"Nama: {tertinggi_skor_murid['nama']}")
  print(f"NIM: {tertinggi_skor_murid['nim']}")
  print(f"Nilai: {tertinggi_skor_murid['nilai']}")

  print("\nMahasiswa dengan nilai terendah:")
  print(f"Nama: {terendah_skor_murid['nama']}")
  print(f"NIM: {terendah_skor_murid['nim']}")
  print(f"Nilai: {terendah_skor_murid['nilai']}")

mahasiswa = input_mahasiswa()

tampil_mahasiswa(mahasiswa)
kalkulator_ratarata_nilai(mahasiswa)
temukan_tertinggi_dan_terendah_skor(mahasiswa)


