#masukkan umur
umur = int(input("masukkan umur anda:"))

#mengecek umur 
if umur < 13:
	print("anak-anak")
elif umur < 20:
	print("remaja")
elif umur < 40:
	print("dewasa")
else : 
	print("lansia")