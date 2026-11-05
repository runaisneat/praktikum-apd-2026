import os
from datetime import datetime

import pwinput
from prettytable import PrettyTable
from colorama import init, Fore, Style

# ====================================================
# SISTEM PENCATATAN PERANGKAT KERAS LAB INFORMATIKA
# ====================================================

init(autoreset=True)

#VARIABEL GLOBAL
MAX_PERCOBAAN = 3

status_pilihan = {
    "1": "Tersedia",
    "2": "Dipakai",
    "3": "Rusak",
    "4": "Dalam Servis"
}

data_user = {                         
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

data_pc = {                            
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

id_terakhir = 2                    

daftar_menu_awal = {
    "1": "Login",
    "2": "Register",
    "0": "Keluar"
}

daftar_menu_admin = {
    "1": "Tambah PC baru (Create)",
    "2": "Lihat semua PC (Read)",
    "3": "Lihat detail & riwayat servis (Read)",
    "4": "Update status PC (Update)",
    "5": "Upgrade spesifikasi PC (Update)",
    "6": "Hapus PC (Delete)",
    "7": "Lihat daftar user",
    "0": "Logout"
}

daftar_menu_user = {
    "1": "Lihat semua PC",
    "2": "Cek PC yang tersedia",
    "3": "Lihat detail & riwayat servis",
    "0": "Logout"
}


def buat_id_baru():
    global id_terakhir
    id_terakhir = id_terakhir + 1
    return id_terakhir


def hitung_pc_tersedia():
    jumlah = 0
    for pc in data_pc.values():
        if pc["status"] == "Tersedia":
            jumlah = jumlah + 1
    return jumlah


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def jeda():
    input("\nTekan Enter untuk lanjut...")


def judul(teks):
    print(Fore.CYAN + Style.BRIGHT + "=== " + teks + " ===")


def sukses(teks):
    print(Fore.GREEN + "[OK] " + teks)


def gagal(teks):
    print(Fore.RED + "[!] " + teks)


def info(teks):
    print(Fore.YELLOW + teks)


def warna_status(status):
    if status == "Tersedia":
        return Fore.GREEN + status + Style.RESET_ALL
    if status == "Rusak":
        return Fore.RED + status + Style.RESET_ALL
    return Fore.YELLOW + status + Style.RESET_ALL


def buat_tabel(kolom, judul_tabel=None):
    tabel = PrettyTable()
    tabel.field_names = kolom
    tabel.align = "l"
    if judul_tabel is not None:
        tabel.title = judul_tabel
    return tabel


def tampil_menu(judul_menu, daftar_menu):
    tabel = buat_tabel(["No", "Menu"], judul_menu)
    for nomor, nama in daftar_menu.items():
        tabel.add_row([nomor, nama])
    print(tabel)



def tampil_tabel(daftar_pc, judul_tabel="DAFTAR PC"):
    tabel = buat_tabel(["ID", "Nama", "CPU", "RAM", "Storage", "Status"], judul_tabel)
    for id_pc, pc in daftar_pc.items():
        spek = pc["spek"]
        tabel.add_row([id_pc, pc["nama"], spek["cpu"],
                       str(spek["ram"]) + " GB", str(spek["storage"]) + " GB",
                       warna_status(pc["status"])])
    if len(daftar_pc) == 0:
        info("(tidak ada data)")
    else:
        print(tabel)


def tampil_detail(id_pc, pc):
    spek = pc["spek"]
    tabel = buat_tabel(["Atribut", "Nilai"], "DETAIL PC")
    tabel.add_row(["ID", id_pc])
    tabel.add_row(["Nama", pc["nama"]])
    tabel.add_row(["CPU", spek["cpu"]])
    tabel.add_row(["RAM", str(spek["ram"]) + " GB"])
    tabel.add_row(["Storage", str(spek["storage"]) + " GB"])
    tabel.add_row(["Status", warna_status(pc["status"])])
    print(tabel)

    riwayat = buat_tabel(["No", "Riwayat"], "RIWAYAT SERVIS / UPGRADE")
    for nomor, keterangan in pc["riwayat"].items():
        riwayat.add_row([nomor, keterangan])
    print(riwayat)


def tampil_status_pilihan(daftar_status):
    tabel = buat_tabel(["No", "Status"], "PILIHAN STATUS")
    for nomor, nama in daftar_status.items():
        tabel.add_row([nomor, nama])
    print(tabel)


def tampil_user():
    tabel = buat_tabel(["Username", "Role"], "DAFTAR USER")
    for nama_user, info_user in data_user.items():
        tabel.add_row([nama_user, info_user["role"]])
    print(tabel)


def cari_pc(id_teks):
    try:
        id_pc = int(id_teks)
        return id_pc, data_pc[id_pc]
    except ValueError:
        gagal("ID harus berupa angka!")
    except KeyError:
        gagal("ID tidak ditemukan!")
    return None, None


def input_angka(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < 1:
                raise ValueError("kurang dari 1")
            return nilai
        except ValueError:
            gagal("Input harus berupa angka bulat minimal 1!")


def input_teks(pesan):
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                raise ValueError("kosong")
            return teks
        except ValueError:
            gagal("Input tidak boleh kosong!")


def input_tanggal(pesan):
    while True:
        teks = input(pesan).strip()
        try:
            datetime.strptime(teks, "%d-%m-%Y")
            return teks
        except ValueError:
            gagal("Format tanggal salah! Contoh: 14-10-2026")


def input_password(pesan):
    try:
        return pwinput.pwinput(prompt=pesan, mask="*").strip()
    except Exception:
        return input(pesan).strip()


def tambah_riwayat(pc, keterangan):
    nomor_baru = len(pc["riwayat"]) + 1
    pc["riwayat"][nomor_baru] = keterangan


# ====================================================
# CRUD DATA PC
# ====================================================
#CREATE
def tambah_pc():
    judul("TAMBAH PC BARU")
    nama = input_teks("Nama PC: ")
    for pc in data_pc.values():
        if pc["nama"].lower() == nama.lower():
            gagal("Nama PC sudah ada!")
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


#READ
def lihat_semua():
    tampil_tabel(data_pc, "DAFTAR SEMUA PC")


def lihat_tersedia():
    tersedia = {}
    for id_pc, pc in data_pc.items():
        if pc["status"] == "Tersedia":
            tersedia[id_pc] = pc
    tampil_tabel(tersedia, "PC YANG TERSEDIA")
    info("Total tersedia: " + str(hitung_pc_tersedia()) + " dari " + str(len(data_pc)) + " PC")


def lihat_detail():
    tampil_tabel(data_pc)
    id_pc, pc = cari_pc(input("\nMasukkan ID PC: ").strip())
    if pc is not None:
        print()
        tampil_detail(id_pc, pc)


#UPDATE
def update_status():
    tampil_tabel(data_pc)
    id_pc, pc = cari_pc(input("\nMasukkan ID PC: ").strip())
    if pc is None:
        return
    info("Status sekarang: " + pc["status"])
    tampil_status_pilihan(status_pilihan)
    try:
        status_baru = status_pilihan[input("Pilih status baru (1-4): ").strip()]
    except KeyError:
        gagal("Pilihan tidak valid!")
        return
    if status_baru == pc["status"]:
        gagal("Status sama dengan sebelumnya!")
        return
    tanggal = input_tanggal("Tanggal (contoh 14-10-2026): ")
    ket = input("Keterangan (kerusakan/servis): ").strip()
    if ket == "":
        ket = "-"
    pc["status"] = status_baru
    tambah_riwayat(pc, tanggal + " : " + status_baru + ", " + ket)
    sukses("Status " + pc["nama"] + " berhasil diubah jadi " + status_baru)


def upgrade_spek():
    tampil_tabel(data_pc)
    id_pc, pc = cari_pc(input("\nMasukkan ID PC: ").strip())
    if pc is None:
        return
    spek = pc["spek"]
    info("Spek sekarang: " + spek["cpu"] + " | " + str(spek["ram"]) + " GB RAM | " +
         str(spek["storage"]) + " GB Storage")
    print("(kosongkan kalau tidak ingin diubah)")
    cpu_teks = input("CPU baru: ").strip()
    ram_teks = input("RAM baru (GB): ").strip()
    sto_teks = input("Storage baru (GB): ").strip()
    if cpu_teks == "" and ram_teks == "" and sto_teks == "":
        info("Tidak ada yang diubah.")
        return
    try:
        cpu_baru = cpu_teks if cpu_teks != "" else spek["cpu"]
        ram_baru = int(ram_teks) if ram_teks != "" else spek["ram"]
        sto_baru = int(sto_teks) if sto_teks != "" else spek["storage"]
        if ram_baru < 1 or sto_baru < 1:
            raise ValueError("kurang dari 1")
    except ValueError:
        gagal("RAM dan Storage harus angka bulat minimal 1!")
        return
    tanggal = input_tanggal("Tanggal upgrade (contoh 14-10-2026): ")
    spek["cpu"] = cpu_baru
    spek["ram"] = ram_baru
    spek["storage"] = sto_baru
    tambah_riwayat(pc, tanggal + " : Upgrade jadi " + cpu_baru + " | " +
                   str(ram_baru) + " GB RAM | " + str(sto_baru) + " GB Storage")
    sukses("Spesifikasi " + pc["nama"] + " berhasil diupgrade!")


# ---------------------- DELETE ----------------------
def hapus_pc():
    tampil_tabel(data_pc)
    id_pc, pc = cari_pc(input("\nMasukkan ID PC: ").strip())
    if pc is None:
        return
    info("Mau hapus: " + pc["nama"] + " (status: " + pc["status"] + ")")
    yakin = input("Aset sudah dibuang? Ketik y untuk hapus: ").strip().lower()
    if yakin == "y":
        del data_pc[id_pc]
        sukses("Data " + pc["nama"] + " berhasil dihapus!")
    else:
        info("Batal menghapus.")


# ====================================================
# MENU ADMIN & PENGGUNA
# ====================================================
def menu_admin(username):
    while True:
        bersihkan_layar()
        info("Login sebagai: " + username + " (admin)")
        tampil_menu("MENU ADMIN", daftar_menu_admin)
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
            tampil_user()
        elif pilih == "0":
            break
        else:
            gagal("Menu tidak valid!")
        jeda()


def menu_user(username):
    while True:
        bersihkan_layar()
        info("Login sebagai: " + username + " (pengguna)")
        tampil_menu("MENU PENGGUNA", daftar_menu_user)
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
            gagal("Menu tidak valid!")
        jeda()


# ====================================================
# LOGIN (REKURSIF) & REGISTER
# ====================================================
def cek_login(username, password):
    # fungsi dengan parameter: cek kecocokan username & password
    try:
        return data_user[username]["password"] == password
    except KeyError:
        return False


def login_rekursif(sisa_percobaan):
    # FUNGSI REKURSIF: memanggil dirinya sendiri sampai login benar
    # atau percobaan habis. Mengembalikan username / None.
    if sisa_percobaan == 0:            # base case
        return None
    username = input("Username: ").strip()
    password = input_password("Password: ")
    if cek_login(username, password):  # base case
        return username
    gagal("Username atau password salah! Sisa percobaan: " + str(sisa_percobaan - 1))
    return login_rekursif(sisa_percobaan - 1)   # rekursif


def register():
    judul("REGISTER AKUN BARU")
    username = input("Username (tanpa spasi): ").strip()
    password = input_password("Password (min 4 karakter): ")
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
        gagal(str(pesan_error))
    else:
        data_user[username] = {"password": password, "role": "user"}
        sukses("Register berhasil! Silakan login.")


def login_user():
    judul("LOGIN")
    username = login_rekursif(MAX_PERCOBAAN)
    if username is None:
        gagal("Percobaan habis, kembali ke menu awal.")
        jeda()
        return
    sukses("Login berhasil, selamat datang " + username)
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
        info("SISTEM PENCATATAN PERANGKAT KERAS LAB INFORMATIKA")
        tampil_menu("MENU UTAMA", daftar_menu_awal)
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
            gagal("Menu tidak valid!")
            jeda()
except (KeyboardInterrupt, EOFError):
    print("\nProgram dihentikan paksa.")
finally:
    info("Terima kasih sudah menggunakan program ini.")
