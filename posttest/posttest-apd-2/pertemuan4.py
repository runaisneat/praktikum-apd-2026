#Percabangan IF
angka = 6

if angka < 10:
    print("Angka kurang dari 10")

#Percabangan IF/ELSE
    umur = int(input("Masukkan umur: ")) 

if umur >= 17:
    print("Kamu sudah bisa membuat KTP") 
else:
    print("Kamu belum bisa membuat KTP") 

#Percabangan IF/ELIF/ELSE
kendaraan = input("Masukkan jenis kendaraan anda: ")

if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000

print("Tarif parkir yang harus dibayar:", tarif_parkir)

#poin
#programnya harus input nilai
#kalo nilai1
nilai = input("Masukkan nilai: ")
nilai = float(nilai)

if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
elif nilai >= 50 and nilai <= 69:
    print("Nilai D")
else:
    print("Nilai E")

#Ternary Operator (Percabangan Satu Baris)
# Bentuk Awal Percabangan IF/ELSE
#umur = 20
#if umur >= 18:
#status = "Dewasa"
#else:
#status = "Belum Dewasa"

# Bentuk Akhir Percabangan IF/ELSE (Ternary Operator)
umur = 20
status = "Dewasa" if umur >= 18 else "Belum Dewasa"

#Studi Kasus
# Studi Kasus 1
umur = input("Masukkan umur: ")
umur = float(umur)
if umur >= 16:
    print("boleh masuk")
else:
    print("tidak boleh masuk")

#Studi Kasus 2
total_belanja = int(input("Masukkan total belanja: "))
if total_belanja >= 200000:
    print("Anda mendapatkan diskon 30%")
elif total_belanja >= 100000:
    print("Anda mendapatkan diskon 10%")
else:
    print("Anda tidak mendapatkan diskon")