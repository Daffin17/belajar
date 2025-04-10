# password

# Password yang benar
password_benar = "admin123"

#memasukkan password
input_password = input("Masukkan password: ")

# Memeriksa apakah password sesuai
if input_password == password_benar:
    print("Akses diterima")
else:
    print("Akses ditolak")