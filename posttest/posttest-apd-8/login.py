from data import data_user, MAX_PERCOBAAN
from tampilan import judul, sukses, gagal, jeda
from validasi import input_password
from menu import menu_admin, menu_user


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
