makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000

harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]

biaya_aplikasi = 5000
total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6 + biaya_aplikasi

kurs_eur = 20000
total_bayar_eur = total_bayar / kurs_eur

banyak_data = len(harga_makanan) 
rata_rata = total_bayar / banyak_data

nim = 39 

bolean = nim != rata_rata

print("=== Daftar Harga Makanan 1-6 (Slice Negatif) === ")
print(harga_makanan[-6:])

print("=== Hasil Perhitungan ===")
print("Total Bayar (IDR): Rp{total_bayar}")
print("Total Bayar (EUR): €{total_bayar_eur}")
print("Rata-rata: {rata_rata}")
print("NIM (2 digit terakhir): {nim}")
print("Status Boolean : {bolean}")


