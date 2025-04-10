# Meminta pengguna memasukkan sebuah angka
angka = float(input("Masukkan sebuah angka: "))

# Memeriksa kondisi angka
if angka > 0:
    print("Angka positif")
elif angka < 0:
    print("Angka negatif")
else:
    print("Angka nol")