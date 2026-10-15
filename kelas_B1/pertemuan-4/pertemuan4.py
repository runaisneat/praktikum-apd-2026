a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

# Mencari nilai terbesar menggunakan fungsi max()
nilai_terbesar = max(a, b, c)

# Menampilkan hasil awal
print(f"\nNilai terbesar = {nilai_terbesar}")

# Logika untuk mengecek kesamaan nilai
if a == b and b == c:
    print("A, B, dan C memiliki nilai yang sama")
elif a == b:
    print("A dan B memiliki nilai yang sama")
elif a == c:
    print("A dan C memiliki nilai yang sama")
elif b == c:
    print("B dan C memiliki nilai yang sama")
else:
    print("Semua bilangan memiliki nilai yang berbeda")