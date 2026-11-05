from data import data_pc, status_pilihan, buat_id_baru, hitung_pc_tersedia, tambah_riwayat
from tampilan import (judul, sukses, gagal, info, tampil_tabel, tampil_detail,tampil_status_pilihan)
from validasi import cari_pc, input_angka, input_teks, input_tanggal


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
    sukses("PC " + nama + " ditambahkan dengan ID " + str(id_baru))


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


#DELETE
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
