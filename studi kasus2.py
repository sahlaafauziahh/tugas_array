print("===== Studi Kasus 2 =====")

def input_barang():
  """Memasukkan data barang"""
  nama_barang = input("Masukkan nama barang : ")
  kode_barang = input("Masukkan kode barang : ")
  jumlah_barang = int(input("Masukkan jumlah barang : "))

  return {
    "nama_barang" : nama_barang,
    "kode_barang" : kode_barang,
    "jumlah_barang" : jumlah_barang
  }

def display_barang(inventaris):
  """Menampilkan semua barang"""
  if not inventaris:
    print("Data inventaris tidak ada")
    return

  print("Daftar Inventaris Barang :")
  for barang in inventaris:
    print(f"Nama Barang : {barang['nama_barang']}")
    print(f"Kode Barang : {barang['kode_barang']}")
    print(f"Jumlah Barang : {barang['jumlah_barang']}")
    print("-------------------------")

def temukan_barang_dengan_kode(inventaris, kode_barang):
  """Mencari barang berdasarkan kode."""
  for barang in inventaris:
    if barang["kode_barang"] == kode_barang:
      print(f"Nama Barang : {barang['nama_barang']}")
      print(f"Kode Barang : {barang['kode_barang']}")
      print(f"Jumlah Barang : {barang['jumlah_barang']}")
      return

  print(f"Barang dengan kode {kode_barang} tidak ditemukan.")

def hapus_barang_dengan_kode(inventaris, kode_barang):
  """Menghapus barang berdasarkan kode."""
  for i, barang in enumerate(inventaris):
    if barang["kode_barang"] == kode_barang:
      del inventaris[i]
      print(f"Barang dengan kode {kode_barang} telah dihapus.")
      return

  print(f"Barang dengan kode {kode_barang} tidak ditemukan.")


inventaris = []

while True:
  print("\nMenu Inventaris Barang :")
  print("1. Tambah Barang")
  print("2. Tampilkan Semua Barang")
  print("3. Cari Barang Berdasarkan Kode")
  print("4. Hapus Barang Berdasarkan Kode")
  print("5. Keluar")

  pilihan = input("\nMasukkan pilihan Anda [1/2/3/4/5] : ")

  if pilihan == "1":
    barang_baru = input_barang()
    inventaris.append(barang_baru)
    print("Barang baru telah ditambahkan.")
  elif pilihan == "2":
    display_barang(inventaris)
  elif pilihan == "3":
    kode_barang = input("Masukkan kode barang yang ingin dicari: ")
    temukan_barang_dengan_kode(inventaris, kode_barang)
  elif pilihan == "4":
    kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
    hapus_barang_dengan_kode(inventaris, kode_barang)
  elif pilihan == "5":
    print("Keluar dari program.")
    break
  else:
    print("Pilihan tidak valid. Silakan masukkan angka 1-5.")


