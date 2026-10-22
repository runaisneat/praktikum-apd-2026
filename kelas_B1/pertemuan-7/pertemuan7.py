# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas

# print("Luas persegi panjang:", luas_persegi_panjang())

# def luas_persegi(sisi, lebar=5):
#     luas = sisi * lebar
#     return luas
# sisi = int(input("Masukkan panjang sisi persegi: "))
# hasil = luas_persegi(sisi)
# print("Luas persegi:", hasil)
# print("Luas persegi:", luas_persegi(7))


# Pemanggilan Prosedur
# def pengumuman():
#     print("Hari ini Pengujian Proyek Akhir")
# #Pemanggilan Prosedur
# pengumuman()

# def pengumuman(nama):
#     print(f"Selamat datang, {nama}!")

# pengumuman("Ler")


#Membuat variabel global
nama = "Larry"
prodi = "Informatika"

#Membuat variabel lokal
def data():
    global nama, prodi
    nama = "Teknik Kedokteran"
    prodi = "Kedokteran Lanjut"
    print("Nama:", nama)
    print("Prodi:", prodi)

data()
#Mengakses variabel global
print("Nama:", nama)
print("Prodi:", prodi)