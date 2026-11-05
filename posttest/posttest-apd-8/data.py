#VARIABEL GLOBAL
MAX_PERCOBAAN = 3                      # batas percobaan login

status_pilihan = {                     # pilihan status PC
    "1": "Tersedia",
    "2": "Dipakai",
    "3": "Rusak",
    "4": "Dalam Servis"
}

data_user = {                          # data akun
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

data_pc = {                            # data perangkat
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

id_terakhir = 2                        # ID PC terakhir


#FUNGSI TANPA PARAMETER (mengembalikan nilai)
def buat_id_baru():
    # variabel global dimodifikasi di modul tempat ia didefinisikan
    global id_terakhir
    id_terakhir = id_terakhir + 1
    return id_terakhir


def hitung_pc_tersedia():
    jumlah = 0
    for pc in data_pc.values():
        if pc["status"] == "Tersedia":
            jumlah = jumlah + 1
    return jumlah


#PROSEDUR
def tambah_riwayat(pc, keterangan):
    nomor_baru = len(pc["riwayat"]) + 1
    pc["riwayat"][nomor_baru] = keterangan
