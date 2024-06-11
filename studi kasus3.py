print("===== Studi Kasus 3 =====")

def input_transaksi():
  """Memasukkan data transaksi."""
  tanggal = input("Masukkan tanggal transaksi (YYYY-MM-DD) : ")
  jenis_transaksi = input("Masukkan jenis transaksi (pemasukan/pengeluaran) : ")
  keterangan = input("Masukkan keterangan transaksi : ")
  jumlah = float(input("Masukkan jumlah transaksi : "))

  return {
    "tanggal" : tanggal,
    "jenis_transaksi" : jenis_transaksi,
    "keterangan" : keterangan,
    "jumlah" : jumlah
  }

def display_transaksi(transaksi):
  """Menampilkan semua transaksi."""
  if not transaksi:
    print("Data transaksi kosong.")
    return

  print("Daftar Transaksi:")
  for t in transaksi:
    print(f"Tanggal : {t['tanggal']}")
    print(f"Jenis : {t['jenis_transaksi']}")
    print(f"Keterangan : {t['keterangan']}")
    print(f"Jumlah : Rp{t['jumlah']:,.2f}")
    print("-------------------------")

def kalkulator_total_pemasukan(transaksi):
  """Menghitung dan menampilkan total pemasukan."""
  total_pemasukan = 0
  for t in transaksi:
    if t["jenis_transaksi"] == "pemasukan":
      total_pemasukan += t["jumlah"]

  print(f"Total Pemasukan : Rp{total_pemasukan:,.2f}")

def kalkulator_total_pengeluaran(transaksi):
  """Menghitung dan menampilkan total pengeluaran."""
  total_pengeluaran = 0
  for t in transaksi:
    if t["jenis_transaksi"] == "pengeluaran":
      total_pengeluaran += t["jumlah"]

  print(f"Total Pengeluaran : Rp{total_pengeluaran:,.2f}")

def kalkulator_saldo_akhir(transaksi):
  """Menghitung dan menampilkan saldo akhir."""
  total_pemasukan = kalkulator_total_pemasukan(transaksi)
  total_pengeluaran = kalkulator_total_pengeluaran(transaksi)
  saldo_akhir = total_pemasukan - total_pengeluaran

  print(f"Saldo Akhir : Rp{saldo_akhir:,.2f}")


transaksi = []

while True:
  print("\nMenu Pengelolaan Keuangan Pribadi :")
  print("1. Tambah Transaksi")
  print("2. Tampilkan Semua Transaksi")
  print("3. Hitung Total Pemasukan")
  print("4. Hitung Total Pengeluaran")
  print("5. Hitung Saldo Akhir")
  print("6. Keluar")

  pilihan = input("Masukkan pilihan Anda : ")

  if pilihan == "1":
    transaksi_baru = input_transaksi()
    transaksi.append(transaksi_baru)
    print("Transaksi baru telah ditambahkan.")
  elif pilihan == "2":
    display_transaksi(transaksi)
  elif pilihan == "3":
    kalkulator_total_pemasukan(transaksi)
  elif pilihan == "4":
    kalkulator_total_pengeluaran(transaksi)
  elif pilihan == "5":
    kalkulator_saldo_akhir(transaksi)
  elif pilihan == "6":
    print("Keluar dari program.")
    break
  else:
    print("Pilihan tidak valid. Silakan masukkan angka 1-6.")

