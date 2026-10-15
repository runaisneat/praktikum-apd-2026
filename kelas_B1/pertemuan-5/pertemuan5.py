# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# formula1.append("Spa-Francorchamps")
# formula1.extend(["Verstappen", "Interlagos"])
# formula1.insert(4, "Max")
# formula1.insert(3, "Alpine")
# formula1[0] = "Steelball"
# formula1[0:2] = ["Monza", "Silverstone"]
# del formula1[2]
# formula1.remove("Interlagos")
# ambil_formula1 = formula1.pop(6)

# team1 = ["Mercedes", "Ferrari", "MacLaren"]
# team2 = ["Red Bull", "Alpine", "Aston Martin"]
# gabung_team = team1 + team2
# print(gabung_team)

# line_up = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4]
# ]

# for i in line_up:
#     for j in i:
#         print(j, end=" ")

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# # listchara = list(chara)
# # print(chara[4][1])
# # listchara.insert(3, 19)
# # chara = tuple(listchara)
# print(chara[1:5])

# chara = ("Yukari", "Yukino", "Odette", "Senku")
# (Persona, Oregairu, Genshin, DrStone) = chara
# print(Persona)
# print(Oregairu)

# # print(ambil_formula1)
# print(formula1[0:6:2])
# # print(formula1[3])
# # print(formula1[4][0])
# # print(formula1)

# Studi Kasus1
data_harian = ["Senin", 36.5, "Selasa", 37.1, "Rabu", 36.8, "Kamis", 37.0, "Jumat", 36.6]
data_suhu = data_harian[1::2]
print(data_suhu)

# # Studi Kasus2
profil_karakter = ("Arthur", 50, True, ["Pedang Suci", "Tameng Naga"])
profil_tebalik = profil_karakter[4::-1]
print(profil_tebalik)