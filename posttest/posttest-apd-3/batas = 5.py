batas = 5
for i in range(batas):
	print("Perulangan ke-", i)

game = ["Genshin", 7.0, True]
for i in game:
    print(i)

for i in range(1, 3):
    for j in range(1, 4):
        print(f'{i} x {j} = {i * j}')
    print("=" * 60)

jawab = "ya"
hitung = 0

while(jawab == "ya"):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    
print(f"Total Perulangan : {hitung}")

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

angka_benar = 8
 
while True:
    print("== Game Tebak Angka ===")

    angka_input = int(input("Masukkan angka (1-10): "))

    if angka_benar == angka_input:
        print("Angka yang kamu masukkan benar")
        break
    else:
        print("Angka masih salah")


i = int(input("Masukkan angka (1-10): "))

for i in range(10):
    if i % 2 == 0:
        print("Angka Genap")
    else:
        print("Angka Ganjil")
    print(i)