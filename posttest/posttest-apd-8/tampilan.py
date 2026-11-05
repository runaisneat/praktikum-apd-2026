import os
from prettytable import PrettyTable
from colorama import init, Fore, Style

init(autoreset=True)

from data import data_user

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
