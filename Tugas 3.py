#Nama:M. Daffin surya paundra
#Kelas:XI TKJ 1
#No Absen:17
#Soal 3 : Berat badan ideal'

nama = input("Masukkan nama Anda: ")
jenis_kelamin = input("Masukkan jenis kelamin (Pria/Wanita): ")
tinggi_badan = float(input("Masukkan tinggi badan (cm): "))

# Menghitung berat badan ideal berdasarkan jenis kelamin
if jenis_kelamin == "Pria":
    berat_ideal = tinggi_badan - 100
elif jenis_kelamin == "Wanita":
    berat_ideal = tinggi_badan - 110
else:
    berat_ideal = None

# Menampilkan hasil
print("\n==== Hasil Berat Badan Ideal ====")
print(f"Nama: {nama}")
print(f"Jenis Kelamin: {jenis_kelamin}")
print(f"Tinggi Badan: {tinggi_badan:} cm")

if berat_ideal is not None:
    print(f"Berat Badan Ideal: {berat_ideal:} kg")
else:
    print("Jenis kelamin yang dimasukkan tidak valid.")