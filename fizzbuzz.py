# Meminta pengguna memasukkan angka
angka = int(input("Masukkan sebuah angka: "))

# Memeriksa kondisi
if angka % 3 == 0 and angka % 5 == 0:
    print("FizzBuzz")
elif angka % 3 == 0:
    print("Fizz")
elif angka % 5 == 0:
    print("Buzz")
else:
    print(angka)