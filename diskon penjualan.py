# Program Kalkulator Diskon Penjualan

# Meminta input dari pengguna
total_belanja = float(input("Masukkan total belanja (Rp): "))

# Menentukan besaran diskon berdasarkan kriteria
if total_belanja < 50000:
    diskon = 0
elif 50000 <= total_belanja <= 100000:
    diskon = 0.10
elif 100001 <= total_belanja <= 200000:
    diskon = 0.15
else:  # total_belanja > 200000
    diskon = 0.20

# Menghitung nilai diskon dan total pembayaran
nilai_diskon = total_belanja * diskon
total_pembayaran = total_belanja - nilai_diskon

# Menampilkan hasil
print("\n==== Rincian Pembayaran ====")
print(f"Total Belanja Awal: Rp{total_belanja:,.2f}")
print(f"Besar Diskon: Rp{nilai_diskon:,.2f} ({diskon * 100:.0f}%)")
print(f"Total Pembayaran Setelah Diskon: Rp{total_pembayaran:,.2f}")