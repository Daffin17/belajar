
keranjang = []

def tampilkan_menu():
    
    print("===== APLIKASI KASIR SEDERHANA =====")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Hitung Total Harga")
    print("4. Keluar")

def tambah_barang():
    
    nama = input("Masukkan nama barang: ")
    try:
        harga = float(input("Masukkan harga barang: "))
        if harga < 0:
            print("Harga tidak boleh negatif!")
            return
        keranjang.append((nama, harga))
        print(f"{nama} seharga Rp{harga:.2f} telah ditambahkan ke keranjang.")
    except ValueError:
        print("Masukkan harga yang valid!")

def lihat_keranjang():
    
    if not keranjang:
        print("Keranjang masih kosong.")
        return
    print("===== Isi Keranjang =====")
    for i, (nama, harga) in enumerate(keranjang, start=1):
        print(f"{i}. {nama} - Rp{harga:.2f}")

def hitung_total():
    
    if not keranjang:
        print("Keranjang masih kosong.")
        return
    total = sum(harga for _, harga in keranjang)
    if total > 100000:
        diskon = total * 0.10
        total_setelah_diskon = total - diskon
        print(f"Total harga: Rp{total:.2f}")
        print(f"Diskon 10%: Rp{diskon:.2f}")
        print(f"Total setelah diskon: Rp{total_setelah_diskon:.2f}")
    else:
        print(f"Total harga: Rp{total:.2f} (Tidak mendapatkan diskon)")

def main():
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            lihat_keranjang()
        elif pilihan == "3":
            hitung_total()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi kasir. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-4.")

if __name__ == "__main__":
    main()