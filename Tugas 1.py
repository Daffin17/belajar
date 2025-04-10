
# Nama : M.Daffin Surya Paundra
# No absen : 17
# Kelas : XI TKJ 1
# Soal 1 :Program Daftar Belanja


daftar_belanja = []
print("Masukkan 5 nama barang:")
for i in range(5):
    barang = input(f"Barang {i+1}: ")
    daftar_belanja.append(barang)

print("\nDaftar belanja:")
print(daftar_belanja)

barang_baru = input("\nMasukkan barang baru untuk posisi ke-2: ")
daftar_belanja.insert(1, barang_baru)

print("\nDaftar belanja setelah penambahan:")
print(daftar_belanja)

nomor = int(input("\nMasukkan nomor barang yang ingin dihapus (1-6): "))
del daftar_belanja[nomor - 1]

print("\nDaftar belanja setelah penghapusan:")
print(daftar_belanja)