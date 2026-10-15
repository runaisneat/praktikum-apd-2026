# kartu = {"merah", "merah", "biru", "hijau"} 
# deck = list(kartu)
# print(kartu)

# angka_ganjil = {1, 3, 5, 7, 9}

# for angka in angka_ganjil:
#     print(angka)

# kelas = {"a", "b", "c", "d"}
# kelas.add("e")
# print(kelas)

# kelas_b1 = {"luvi", "rasya", "eza", "ferdika"}
# print(kelas_b1)
# kelas_b1.remove("ferdika")
# print(kelas_b1)
# kelas_b1.discard("alam")
# print(kelas_b1)

# aslab1 = {"Fina", "shasha", "risma"} 
# aslab2 = {"larry", "attar", "haekal"} 
# gabung = aslab1.union(aslab2) 
# print(gabung) 

# angka1 = {1, 2, 3, 4, 5} 
# angka2 = {2, 4,, 6, 8, 10} 
# irisan = angka1.intersection(angka2) 
# print(irisan)

# angka1 = {1, 2, 3, 4, 5} 
# angka2 = {2, 4, 6, 8, 10} 
# angka1.update(angka2) 
# print(angka1)

# praktikum = {
#     "apd" : "belajar dictionary",
#     "orsikom" : "belajar logism"
# }

# print(praktikum)
# print(praktikum["orsikom"])


# biodata = {
#     "nama" : "ferdika",
#     "nim" : "039",
#     "pacar" : ["laptop", "jojo"],
#     "sosmed" : "@fvrdka"
# }

# biodata["matkul"] = "kalkulus"
# print(biodata)

# biodata.update({"warna" : "biru"})

# for i in biodata:
#     print(i)

# for i in biodata.keys():
#     print(i)

# for i in biodata.values():
#     print(i)

# for i, j in biodata.items():
#     print(i, ":", j)

# print(biodata.get("sosmed"))
# print(biodata.get("alamat", "alamat tidak ditemukan"))
# print(f'nama saya adalah {biodata["nama"]}')
# print(f'pacar nomor 1 saya adalah {biodata["pacar"][1]}')
# print = (biodata)

# list_game = dict(genshin = "odette", meler = "seber", hayday = "ayam")
# print(list_game)


# game = { 
#     "pou" : "chill", 
#     "genshin impact" : "action", 
#     "valorant" : "fps", 
#     "minecraft" : "sandbox", 
#     "mobile legend" : "moba" 
# } 

# print('panjang dari dictionary:', len(game))

# game_copy = game.copy()
# game_copy["mobile legend"] = "moba analog"

# key = "A", "B", "C"
# value = "anak infor"

# akt26 = dict.fromkeys(key, value)

# game["valorant"] = "kutukan"
# print(game)

# print(game) 
# del game["valorant"] 
# print(game) 
# print(game.get("minecraft")) 

# cache = game.pop("mobile legend")
# print(cache.get ("mobile legend"))

# tambah = game.setdefault("resident evil", "horror") 
# print(game) 
# print("Tipe game", game.setdefault("grow a garden", "gardening"))

# menu = { 
#     "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"], 
#     "nasi" : ["nasi goreng", "nasi uduk"], 
#     "mie" : ["mie goreng rendang", "mie goreng aceh"], 
#     "kuah" : ["soto", "rawon", "sop iga"] 
# }

# for i, j in menu.items(): 
#     print(f"Kategori {i} memiliki menu :") 
#     for kategori in j: 
#         print(kategori) 
#     print("")

# studi kasus
poli_umum = {"Andi", "Budi", "Citra", "Doni"}  
poli_gigi = {"Citra", "Doni", "Eka", "Fani"}  

gabung = poli_umum.union(poli_gigi) 
print(gabung)