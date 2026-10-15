import os
import datetime

# ==========================================================
# SISTEM PENCATATAN PERANGKAT KERAS LAB INFORMATIKA BOSKYUH
# ==========================================================

STATUS_PILIHAN = ("Tersedia", "Dipakai", "Rusak", "Dalam Servis")

# Nested list pengguna: [username, password, role]
data_user = [
    ["admin", "admin123", "admin"],
    ["user", "user123", "user"],
]

# Nested list perangkat:[id, nama, (cpu, ram_gb, storage_gb), status, [[tanggal, keterangan], ...]]
data_pc = [
    [1, "PC-01", ("Intel Core i5-10400", 8, 256), "Tersedia",
     [["2026-01-10", "Pembelian awal"]]],
    [2, "PC-02", ("Intel Core i3-10100", 4, 500), "Rusak",
     [["2026-01-10", "Pembelian awal"], ["2026-08-02", "Status -> Rusak: PSU mati"]]],
]
id_terakhir = 2

# buat nyimpan data user yang lagi login (None = belum login)
user_login = None

while True:
    os.system("cls" if os.name == "nt" else "clear")
    aksi = ""

    #TAMPILAN MENU
    if user_login is None:
        print("=" * 52)
        print(" SISTEM PENCATATAN PERANGKAT KERAS LAB INFORMATIKA")
        print("=" * 52)
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            aksi = "login"
        elif pilih == "2":
            aksi = "register"
        elif pilih == "0":
            os.system("cls" if os.name == "nt" else "clear")
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("  [!] Menu tidak valid.")
            input("\nTekan Enter untuk lanjut...")
            continue

    elif user_login[2] == "admin":
        print(f"=== MENU ADMIN | Login sebagai: {user_login[0]} ===")
        print("1. Tambah PC baru                  (Create)")
        print("2. Lihat semua perangkat           (Read)")
        print("3. Detail & riwayat servis         (Read)")
        print("4. Update status kerusakan/servis  (Update)")
        print("5. Upgrade spesifikasi             (Update)")
        print("6. Hapus aset                      (Delete)")
        print("7. Lihat daftar pengguna")
        print("0. Logout")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            aksi = "tambah"
        elif pilih == "2":
            aksi = "semua"
        elif pilih == "3":
            aksi = "detail"
        elif pilih == "4":
            aksi = "status"
        elif pilih == "5":
            aksi = "upgrade"
        elif pilih == "6":
            aksi = "hapus"
        elif pilih == "7":
            aksi = "user"
        elif pilih == "0":
            user_login = None
            continue
        else:
            print("  [!] Menu tidak valid.")
            input("\nTekan Enter untuk lanjut...")
            continue

    else:
        print(f"=== MENU PENGGUNA | Login sebagai: {user_login[0]} ===")
        print("1. Lihat semua perangkat")
        print("2. Cek ketersediaan PC")
        print("3. Detail & riwayat servis")
        print("0. Logout")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            aksi = "semua"
        elif pilih == "2":
            aksi = "tersedia"
        elif pilih == "3":
            aksi = "detail"
        elif pilih == "0":
            user_login = None
            continue
        else:
            print("  [!] Menu tidak valid.")
            input("\nTekan Enter untuk lanjut...")
            continue

    os.system("cls" if os.name == "nt" else "clear")
    idx = -1

    #LOGIN
    if aksi == "login":
        print("=== LOGIN ===")
        for percobaan in range(3, 0, -1):
            username = ""
            while username == "":
                username = input("Username: ").strip()
                if username == "":
                    print("  [!] Username tidak boleh kosong.")
            password = ""
            while password == "":
                password = input("Password: ").strip()
                if password == "":
                    print("  [!] Password tidak boleh kosong.")
            for u in data_user:
                if u[0] == username and u[1] == password:
                    user_login = u
            if user_login is not None:
                print(f"\n  Login berhasil. Selamat datang, {username}!")
                break
            print(f"  [!] Username/password salah. Sisa percobaan: {percobaan - 1}")
        if user_login is None:
            print("  Terlalu banyak percobaan gagal.")

    #REGISTER
    if aksi == "register":
        print("=== REGISTER AKUN BARU ===")
        username = ""
        while username == "":
            username = input("Username (tanpa spasi)   : ").strip()
            if username == "":
                print("  [!] Username tidak boleh kosong.")
        username_ada = False
        for u in data_user:
            if u[0] == username:
                username_ada = True
        if " " in username:
            print("  [!] Username tidak boleh mengandung spasi.")
        elif username_ada:
            print("  [!] Username sudah terdaftar.")
        else:
            password = ""
            while password == "":
                password = input("Password (min. 4 karakter): ").strip()
                if password == "":
                    print("  [!] Password tidak boleh kosong.")
            if len(password) < 4:
                print("  [!] Password terlalu pendek.")
            else:
                data_user.append([username, password, "user"])
                print(f"\n  Registrasi berhasil! Silakan login sebagai '{username}'.")

    #CREATE: tambah PC
    if aksi == "tambah":
        print("=== TAMBAH PC BARU (CREATE) ===")
        nama = ""
        while nama == "":
            nama = input("Nama/label PC      : ").strip()
            if nama == "":
                print("  [!] Input tidak boleh kosong.")
        nama_ada = False
        for pc in data_pc:
            if pc[1].lower() == nama.lower():
                nama_ada = True
        if nama_ada:
            print(f"  [!] Nama '{nama}' sudah dipakai.")
        else:
            cpu = ""
            while cpu == "":
                cpu = input("CPU                : ").strip()
                if cpu == "":
                    print("  [!] Input tidak boleh kosong.")
            while True:
                teks = input("RAM (GB)          : ").strip()
                if teks.isdigit() and int(teks) >= 1:
                    break
                print("  [!] Harus berupa angka bulat positif.")
            ram = int(teks)
            while True:
                teks = input("Storage (GB)      : ").strip()
                if teks.isdigit() and int(teks) >= 1:
                    break
                print("  [!] Harus berupa angka bulat positif.")
            storage = int(teks)
            id_terakhir += 1
            data_pc.append([
                id_terakhir, nama, (cpu, ram, storage), "Tersedia",
                [[str(datetime.date.today()), "Aset didaftarkan"]],
            ])
            print(f"\n  Berhasil! PC '{nama}' ditambahkan dengan ID {id_terakhir}.")

    #READ: tabel perangkat
    if aksi in ("semua", "tersedia", "detail", "status", "upgrade", "hapus"):
        if aksi == "tersedia":
            print("=== PC YANG TERSEDIA ===")
            daftar = [pc for pc in data_pc if pc[3] == "Tersedia"]
        else:
            print("=== DAFTAR PERANGKAT ===")
            daftar = data_pc
        print(f"{'ID':<4}{'Nama':<10}{'CPU':<24}{'RAM':<8}{'Storage':<10}{'Status':<14}")
        print("-" * 70)
        if len(daftar) == 0:
            print("(tidak ada data)")
        for pc in daftar:
            cpu, ram, storage = pc[2]
            print(f"{pc[0]:<4}{pc[1]:<10}{cpu:<24}{str(ram) + ' GB':<8}"
                  f"{str(storage) + ' GB':<10}{pc[3]:<14}")
        if aksi == "tersedia":
            print(f"\nTotal tersedia: {len(daftar)} dari {len(data_pc)} perangkat.")

    #Pilih PC berdasarkan ID (untuk detail/update/hapus)
    if aksi in ("detail", "status", "upgrade", "hapus"):
        if len(data_pc) == 0:
            print("\n  Belum ada data perangkat.")
        else:
            while True:
                teks = input("\nMasukkan ID PC: ").strip()
                if teks.isdigit():
                    break
                print("  [!] Harus berupa angka bulat positif.")
            id_pc = int(teks)
            for i in range(len(data_pc)):
                if data_pc[i][0] == id_pc:
                    idx = i
            if idx == -1:
                print(f"  [!] PC dengan ID {id_pc} tidak ditemukan.")

    #READ: detail & riwayat
    if aksi == "detail" and idx != -1:
        pc = data_pc[idx]
        cpu, ram, storage = pc[2]
        print("\n=== DETAIL & RIWAYAT SERVIS ===")
        print(f"ID      : {pc[0]}")
        print(f"Nama    : {pc[1]}")
        print(f"CPU     : {cpu}")
        print(f"RAM     : {ram} GB")
        print(f"Storage : {storage} GB")
        print(f"Status  : {pc[3]}")
        print("\nRiwayat:")
        for no, r in enumerate(pc[4], start=1):
            print(f"  {no}. [{r[0]}] {r[1]}")

    #UPDATE: status kerusakan/servis
    if aksi == "status" and idx != -1:
        pc = data_pc[idx]
        print(f"\n=== UPDATE STATUS: {pc[1]} (sekarang: {pc[3]}) ===")
        for i in range(len(STATUS_PILIHAN)):
            print(f"  {i + 1}. {STATUS_PILIHAN[i]}")
        while True:
            teks = input("Pilih status baru: ").strip()
            if teks.isdigit() and 1 <= int(teks) <= len(STATUS_PILIHAN):
                break
            print("  [!] Pilihan tidak valid.")
        status_baru = STATUS_PILIHAN[int(teks) - 1]
        if status_baru == pc[3]:
            print("  [!] Status sama dengan sebelumnya, tidak ada perubahan.")
        else:
            ket = input("Keterangan (boleh kosong): ").strip()
            if ket == "":
                ket = "-"
            pc[3] = status_baru
            pc[4].append([str(datetime.date.today()), f"Status -> {status_baru}: {ket}"])
            print(f"\n  Status {pc[1]} diubah menjadi '{status_baru}'.")

    #UPDATE: upgrade spesifikasi
    if aksi == "upgrade" and idx != -1:
        pc = data_pc[idx]
        cpu, ram, storage = pc[2]
        print(f"\n=== UPGRADE SPESIFIKASI: {pc[1]} ===")
        print(f"Spek sekarang: {cpu} | {ram} GB RAM | {storage} GB Storage")
        print("(Kosongkan input jika tidak ingin mengubah)")
        cpu_baru = input("CPU baru          : ").strip()
        while True:
            ram_teks = input("RAM baru (GB)     : ").strip()
            if ram_teks == "" or (ram_teks.isdigit() and int(ram_teks) >= 1):
                break
            print("  [!] Harus berupa angka bulat positif.")
        while True:
            sto_teks = input("Storage baru (GB) : ").strip()
            if sto_teks == "" or (sto_teks.isdigit() and int(sto_teks) >= 1):
                break
            print("  [!] Harus berupa angka bulat positif.")
        if cpu_baru == "" and ram_teks == "" and sto_teks == "":
            print("\n  Tidak ada perubahan.")
        else:
            if cpu_baru == "":
                cpu_baru = cpu
            if ram_teks != "":
                ram = int(ram_teks)
            if sto_teks != "":
                storage = int(sto_teks)
            pc[2] = (cpu_baru, ram, storage)
            pc[4].append([str(datetime.date.today()),
                          f"Upgrade: {cpu_baru} | {ram} GB RAM | {storage} GB Storage"])
            print(f"\n  Spesifikasi {pc[1]} berhasil diperbarui.")

    #DELETE: hapus aset
    if aksi == "hapus" and idx != -1:
        pc = data_pc[idx]
        print(f"\nAnda akan menghapus: ID {pc[0]} - {pc[1]} ({pc[3]})")
        yakin = input("Aset sudah dibuang? Ketik 'y' untuk hapus: ").strip().lower()
        if yakin == "y":
            data_pc.pop(idx)
            print(f"\n  Data {pc[1]} berhasil dihapus.")
        else:
            print("\n  Penghapusan dibatalkan.")

    #Daftar pengguna (khusus admin)
    if aksi == "user":
        print("=== DAFTAR PENGGUNA ===")
        print(f"{'No':<4}{'Username':<16}{'Role':<10}")
        print("-" * 30)
        for no, u in enumerate(data_user, start=1):
            print(f"{no:<4}{u[0]:<16}{u[2]:<10}")

    input("\nTekan Enter untuk lanjut...")