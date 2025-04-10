
barang = ["Buku", "Pensil", "Penghapus", "Penggaris", "Spidol"]
stok = [10, 0, 5, 3, 0]

indeks = 0

while indeks < len(barang):
    
    if stok[indeks] > 0:
        status = "Tersedia"
    else:
        status = "Habis"
    
    
    print(f"Barang: {barang[indeks]} - {status} (Stok: {stok[indeks]})")
   
    indeks += 1