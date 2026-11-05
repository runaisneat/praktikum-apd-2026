from tampilan import bersihkan_layar, jeda, tampil_menu, gagal, info
from auth import login_user, register

daftar_menu_awal = {
    "1": "Login",
    "2": "Register",
    "0": "Keluar"
}

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
