print("   *** STRUKTUR KONDISI *** \n \n")

print("1. IF \n")
nm=raw_input("Nama : ")
gaji = input("gaji : ")
if gaji >= 3500000:
	print("gaji diatas UMR")
	
print(" \n 2. IF ELSE \n")
nm = raw_input("Nama :")
gaji = input("Gaji :")
if gaji >=4000000:
	print("gaji diatas UMR")
else:
	print("gaji dibawah UMR")
	
print("\n 3. IF ELIF ELSE \n ")
nm = raw_input("Nama :")
nilai = input("Nilai :")
if nilai >=80:
	print("nilai huruf : A")
elif nilai >=70:
	print("nilai huruf : B")
elif nilai >=50:
	print("nilai huruf : C")
else:
	print("nilai huruf : D")
	
print("\n 4. NASTED \n")
nm = raw_input("Nama :")
nilai = input("Nilai :")
if nilai <100:
	print("nilai = True")
	if nilai >70:
		print ("lulus")
	else :
		print("tidak lulus")
else :
	print ("false")
