from datetime import datetime
import pwinput

from data import data_pc
from tampilan import gagal


def cari_pc(id_teks):
    # fungsi dengan parameter: cari PC berdasarkan ID (teks)
    try:
        id_pc = int(id_teks)           # bisa ValueError
        return id_pc, data_pc[id_pc]   # bisa KeyError
    except ValueError:
        gagal("ID harus berupa angka!")
    except KeyError:
        gagal("ID tidak ditemukan!")
    return None, None


def input_angka(pesan):
    # fungsi dengan parameter: angka bulat minimal 1
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < 1:
                raise ValueError("kurang dari 1")
            return nilai
        except ValueError:
            gagal("Input harus berupa angka bulat minimal 1!")


def input_teks(pesan):
    # fungsi dengan parameter: teks tidak boleh kosong
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                raise ValueError("kosong")
            return teks
        except ValueError:
            gagal("Input tidak boleh kosong!")


def input_tanggal(pesan):
    # fungsi dengan parameter: tanggal format dd-mm-yyyy
    while True:
        teks = input(pesan).strip()
        try:
            datetime.strptime(teks, "%d-%m-%Y")
            return teks
        except ValueError:
            gagal("Format tanggal salah! Contoh: 14-10-2026")


def input_password(pesan):
    # library pwinput: password tampil sebagai *****
    try:
        return pwinput.pwinput(prompt=pesan, mask="*").strip()
    except Exception:
        # terminal tidak mendukung mode tersembunyi (mis. input dialihkan
        # dari file / IDE tertentu) -> pakai input biasa
        return input(pesan).strip()
