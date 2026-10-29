import os
from datetime import datetime

# ====================================================
# SISTEM PENCATATAN PERANGKAT KERAS LAB INFORMATIKA
# ====================================================

# ================== VARIABEL GLOBAL ==================
MAX_PERCOBAAN = 3                      # global 1: batas percobaan login

status_pilihan = {                     # global 2: pilihan status PC
    "1": "Tersedia",
    "2": "Dipakai",
    "3": "Rusak",
    "4": "Dalam Servis"
}

data_user = {                          # global 3: data akun
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

data_pc = {                            # global 4: data perangkat
    1: {
        "nama": "PC-01",
        "spek": {"cpu": "Intel Core i5-10400", "ram": 8, "storage": 256},
        "status": "Tersedia",
        "riwayat": {1: "10-01-2026 : Pembelian awal"}
    },
    2: {
        "nama": "PC-02",
        "spek": {"cpu": "Intel Core i3-10100", "ram": 4, "storage": 500},
        "status": "Rusak",
        "riwayat": {1: "10-01-2026 : Pembelian awal", 2: "02-08-2026 : Rusak, PSU mati"}
    }
}

id_terakhir = 2                        # global 5: ID PC terakhir


# ====================================================
# FUNGSI TANPA PARAMETER (mengembalikan nilai)
# ====================================================
def buat_id_baru():
    # fungsi tanpa parameter #1 : membuat ID PC baru
    global id_terakhir                 # mengubah variabel global
    id_terakhir = id_terakhir + 1
    return id_terakhir


def hitung_pc_tersedia():
    # fungsi tanpa parameter #2 : menghitung PC berstatus Tersedia
    jumlah = 0                         # variabel lokal
    for pc in data_pc.values():
        if pc["status"] == "Tersedia":
            jumlah = jumlah + 1
    return jumlah


# ====================================================
# FUNGSI DENGAN PARAMETER (mengembalikan nilai)
# ====================================================
def cari_pc(id_teks):
    # fungsi dengan parameter #1 : mencari PC berdasarkan ID (teks)
    try:
        id_pc = int(id_teks)           # bisa ValueError
        return id_pc, data_pc[id_pc]   # bisa KeyError
    except ValueError:
        print("ID harus berupa angka!")
    except KeyError:
        print("ID tidak ditemukan!")
    return None, None


def cek_login(username, password):
    # fungsi dengan parameter #2 : cek kecocokan username & password
    try:
        return data_user[username]["password"] == password
    except KeyError:
        return False


def login_rekursif(sisa_percobaan):
    # FUNGSI REKURSIF : memanggil dirinya sendiri sampai login benar
    # atau percobaan habis. Mengembalikan username / None.
    if sisa_percobaan == 0:            # base case
        return None
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if cek_login(username, password):  # base case
        return username
    print("Username atau password salah! Sisa percobaan:", sisa_percobaan - 1)
    return login_rekursif(sisa_percobaan - 1)   # rekursif


def input_angka(pesan):
    # fungsi dengan parameter : input angka bulat minimal 1
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < 1:
                raise ValueError("kurang dari 1")
            return nilai
        except ValueError:
            print("Input harus berupa angka bulat minimal 1!")


def input_teks(pesan):
    # fungsi dengan parameter : input teks tidak boleh kosong
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                raise ValueError("kosong")
            return teks
        except ValueError:
            print("Input tidak boleh kosong!")


def input_tanggal(pesan):
    # fungsi dengan parameter : input tanggal format dd-mm-yyyy
    while True:
        teks = input(pesan).strip()
        try:
            datetime.strptime(teks, "%d-%m-%Y")
            return teks
        except ValueError:
            print("Format tanggal salah! Contoh: 14-10-2026")


# ====================================================
# PROSEDUR (tidak mengembalikan nilai)
# ====================================================
def tampil_tabel(daftar_pc):
    # prosedur #1 : menampilkan tabel PC
    print("ID | Nama | CPU | RAM | Storage | Status")
    print("------------------------------------------------")
    if len(daftar_pc) == 0:
        print("(tidak ada data)")
    for id_pc, pc in daftar_pc.items():
        spek = pc["spek"]
        print(str(id_pc) + " | " + pc["nama"] + " | " + spek["cpu"] + " | " +
              str(spek["ram"]) + " GB | " + str(spek["storage"]) + " GB | " + pc["status"])


def tampil_detail(id_pc, pc):
    # prosedur #2 : menampilkan detail & riwayat satu PC
    spek = pc["spek"]
    print("ID      :", id_pc)
    print("Nama    :", pc["nama"])
    print("CPU     :", spek["cpu"])
    print("RAM     :", spek["ram"], "GB")
    print("Storage :", spek["storage"], "GB")
    print("Status  :", pc["status"])
    print("Riwayat :")
    for nomor, keterangan in pc["riwayat"].items():
        print(" ", nomor, ".", keterangan)


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def jeda():
    input("\nTekan Enter untuk lanjut...")


def tambah_riwayat(pc, keterangan):
    nomor_baru = len(pc["riwayat"]) + 1
    pc["riwayat"][nomor_baru] = keterangan


# ---------------------- CREATE ----------------------
def tambah_pc():
    print("=== TAMBAH PC BARU ===")
    nama = input_teks("Nama PC: ")
    for pc in data_pc.values():
        if pc["nama"].lower() == nama.lower():
            print("Nama PC sudah ada!")
            return
    cpu = input_teks("CPU: ")
    ram = input_angka("RAM (GB): ")
    storage = input_angka("Storage (GB): ")
    tanggal = input_tanggal("Tanggal (contoh 14-10-2026): ")
    id_baru = buat_id_baru()
    data_pc[id_baru] = {
        "nama": nama,
        "spek": {"cpu": cpu, "ram": ram, "storage": storage},
        "status": "Tersedia",
        "riwayat": {1: tanggal + " : Aset didaftarkan"}
    }
    print("Berhasil! PC", nama, "ditambahkan dengan ID", id_baru)


# ----------------------- READ -----------------------
def lihat_semua():
    print("=== DAFTAR SEMUA PC ===")
    tampil_tabel(data_pc)


def lihat_tersedia():
    print("=== PC YANG TERSEDIA ===")
    tersedia = {}
    for id_pc, pc in data_pc.items():
        if pc["status"] == "Tersedia":
            tersedia[id_pc] = pc
    tampil_tabel(tersedia)
    print("Total tersedia:", hitung_pc_tersedia(), "dari", len(data_pc), "PC")


def lihat_detail():
    print("=== DETAIL & RIWAYAT SERVIS ===")
    tampil_tabel(data_pc)
    id_pc, pc = cari_pc(input("\nMasukkan ID PC: ").strip())
    if pc is not None:
        print()
        tampil_detail(id_pc, pc)


def lihat_user():
    print("=== DAFTAR USER ===")
    print("Username | Role")
    print("------------------")
    for nama_user, info in data_user.items():
        print(nama_user + " | " + info["role"])


# ---------------------- UPDATE ----------------------
def update_status():
    print("=== UPDATE STATUS PC ===")
    tampil_tabel(data_pc)
    id_pc, pc = cari_pc(input("\nMasukkan ID PC: ").strip())
    if pc is None:
        return
    print("Status sekarang:", pc["status"])
    for nomor, nama_status in status_pilihan.items():
        print(nomor + ".", nama_status)
    try:
        status_baru = status_pilihan[input("Pilih status baru (1-4): ").strip()]
    except KeyError:
        print("Pilihan tidak valid!")
        return
    if status_baru == pc["status"]:
        print("Status sama dengan sebelumnya!")
        return
    tanggal = input_tanggal("Tanggal (contoh 14-10-2026): ")
    ket = input("Keterangan (kerusakan/servis): ").strip()
    if ket == "":
        ket = "-"
    pc["status"] = status_baru
    tambah_riwayat(pc, tanggal + " : " + status_baru + ", " + ket)
    print("Status", pc["nama"], "berhasil diubah jadi", status_baru)


def upgrade_spek():
    print("=== UPGRADE SPESIFIKASI PC ===")
    tampil_tabel(data_pc)
    id_pc, pc = cari_pc(input("\nMasukkan ID PC: ").strip())
    if pc is None:
        return
    spek = pc["spek"]
    print("Spek sekarang:", spek["cpu"], "|", spek["ram"], "GB RAM |", spek["storage"], "GB Storage")
    print("(kosongkan kalau tidak ingin diubah)")
    cpu_teks = input("CPU baru: ").strip()
    ram_teks = input("RAM baru (GB): ").strip()
    sto_teks = input("Storage baru (GB): ").strip()
    if cpu_teks == "" and ram_teks == "" and sto_teks == "":
        print("Tidak ada yang diubah.")
        return
    try:
        cpu_baru = cpu_teks if cpu_teks != "" else spek["cpu"]
        ram_baru = int(ram_teks) if ram_teks != "" else spek["ram"]
        sto_baru = int(sto_teks) if sto_teks != "" else spek["storage"]
        if ram_baru < 1 or sto_baru < 1:
            raise ValueError("kurang dari 1")
    except ValueError:
        print("RAM dan Storage harus angka bulat minimal 1!")
        return
    tanggal = input_tanggal("Tanggal upgrade (contoh 14-10-2026): ")
    spek["cpu"] = cpu_baru
    spek["ram"] = ram_baru
    spek["storage"] = sto_baru
    tambah_riwayat(pc, tanggal + " : Upgrade jadi " + cpu_baru + " | " +
                   str(ram_baru) + " GB RAM | " + str(sto_baru) + " GB Storage")
    print("Spesifikasi", pc["nama"], "berhasil diupgrade!")


# ---------------------- DELETE ----------------------
def hapus_pc():
    print("=== HAPUS PC ===")
    tampil_tabel(data_pc)
    id_pc, pc = cari_pc(input("\nMasukkan ID PC: ").strip())
    if pc is None:
        return
    print("Mau hapus:", pc["nama"], "(status:", pc["status"] + ")")
    yakin = input("Aset sudah dibuang? Ketik y untuk hapus: ").strip().lower()
    if yakin == "y":
        del data_pc[id_pc]
        print("Data", pc["nama"], "berhasil dihapus!")
    else:
        print("Batal menghapus.")


# ---------------------- AKUN & MENU ----------------------
def register():
    print("=== REGISTER AKUN BARU ===")
    username = input("Username (tanpa spasi): ").strip()
    password = input("Password (min 4 karakter): ").strip()
    try:
        if username == "" or password == "":
            raise ValueError("Username dan password tidak boleh kosong!")
        if " " in username:
            raise ValueError("Username tidak boleh pakai spasi!")
        if username in data_user:
            raise ValueError("Username sudah terdaftar!")
        if len(password) < 4:
            raise ValueError("Password minimal 4 karakter!")
    except ValueError as pesan_error:
        print(pesan_error)
    else:
        data_user[username] = {"password": password, "role": "user"}
        print("Register berhasil! Silakan login.")


def menu_admin(username):
    while True:
        bersihkan_layar()
        print("=== MENU ADMIN ===")
        print("Login sebagai:", username)
        print("1. Tambah PC baru (Create)")
        print("2. Lihat semua PC (Read)")
        print("3. Lihat detail & riwayat servis (Read)")
        print("4. Update status PC (Update)")
        print("5. Upgrade spesifikasi PC (Update)")
        print("6. Hapus PC (Delete)")
        print("7. Lihat daftar user")
        print("0. Logout")
        pilih = input("Pilih menu: ").strip()
        bersihkan_layar()

        if pilih == "1":
            tambah_pc()
        elif pilih == "2":
            lihat_semua()
        elif pilih == "3":
            lihat_detail()
        elif pilih == "4":
            update_status()
        elif pilih == "5":
            upgrade_spek()
        elif pilih == "6":
            hapus_pc()
        elif pilih == "7":
            lihat_user()
        elif pilih == "0":
            break
        else:
            print("Menu tidak valid!")
        jeda()


def menu_user(username):
    while True:
        bersihkan_layar()
        print("=== MENU PENGGUNA ===")
        print("Login sebagai:", username)
        print("1. Lihat semua PC")
        print("2. Cek PC yang tersedia")
        print("3. Lihat detail & riwayat servis")
        print("0. Logout")
        pilih = input("Pilih menu: ").strip()
        bersihkan_layar()

        if pilih == "1":
            lihat_semua()
        elif pilih == "2":
            lihat_tersedia()
        elif pilih == "3":
            lihat_detail()
        elif pilih == "0":
            break
        else:
            print("Menu tidak valid!")
        jeda()


def login_user():
    print("=== LOGIN ===")
    username = login_rekursif(MAX_PERCOBAAN)
    if username is None:
        print("Percobaan habis, kembali ke menu awal.")
        jeda()
        return
    print("Login berhasil, selamat datang", username)
    jeda()
    if data_user[username]["role"] == "admin":
        menu_admin(username)
    else:
        menu_user(username)


# ====================================================
# PROGRAM UTAMA
# ====================================================
try:
    while True:
        bersihkan_layar()
        print("=== SISTEM PENCATATAN PERANGKAT KERAS LAB INFORMATIKA ===")
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        menu = input("Pilih menu: ").strip()
        bersihkan_layar()

        if menu == "1":
            login_user()
        elif menu == "2":
            register()
            jeda()
        elif menu == "0":
            break
        else:
            print("Menu tidak valid!")
            jeda()
except (KeyboardInterrupt, EOFError):
    print("\nProgram dihentikan paksa.")
finally:
    print("Terima kasih sudah menggunakan program ini.")