from tampilan import bersihkan_layar, jeda, tampil_menu, tampil_user, gagal, info
from crud import (tambah_pc, lihat_semua, lihat_tersedia, lihat_detail,
                  update_status, upgrade_spek, hapus_pc)

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
