# Program Manajemen Daftar Belanja

# 1. Meminta pengguna memasukkan 5 nama barang
print("Masukkan 5 nama barang yang akan dibeli:")
daftar_belanja = []
for i in range(5):
    barang = input(f"Masukkan barang ke-{i + 1}: ")
    daftar_belanja.append(barang)

# 2. Menampilkan daftar barang yang telah dimasukkan
print("\nDaftar barang yang telah dimasukkan:")
for idx, barang in enumerate(daftar_belanja, start=1):
    print(f"{idx}. {barang}")

# 3. Meminta pengguna memasukkan barang baru untuk ditambahkan pada posisi ke-2
barang_baru = input("\nMasukkan barang baru untuk ditambahkan pada posisi ke-2: ")
daftar_belanja.insert(1, barang_baru)

# Menampilkan daftar setelah penambahan
print("\nDaftar barang setelah penambahan:")
for idx, barang in enumerate(daftar_belanja, start=1):
    print(f"{idx}. {barang}")

# 4. Meminta pengguna memilih barang yang ingin dihapus berdasarkan nomor urut
try:
    nomor_hapus = int(input("\nMasukkan nomor barang yang ingin dihapus: "))
    if 1 <= nomor_hapus <= len(daftar_belanja):
        barang_dihapus = daftar_belanja.pop(nomor_hapus - 1)
        print(f"\nBarang '{barang_dihapus}' telah dihapus.")
    else:
        print("\nNomor yang dimasukkan tidak valid.")
except ValueError:
    print("\nInput harus berupa angka.")

# 5. Menampilkan daftar barang setelah perubahan
print("\nDaftar barang setelah perubahan:")
for idx, barang in enumerate(daftar_belanja, start=1):
    print(f"{idx}. {barang}")