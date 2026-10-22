import os

# ====================================================
# SISTEM PENCATATAN PERANGKAT KERAS LAB INFORMATIKA
# CRUD pakai nested dictionary
# ====================================================

# dictionary pilihan status -> {nomor: nama status}
status_pilihan = {
    "1": "Tersedia",
    "2": "Dipakai",
    "3": "Rusak",
    "4": "Dalam Servis"
}

# nested dictionary user -> {username: {"password": ..., "role": ...}}
data_user = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

# nested dictionary pc -> {id: {"nama", "spek": {...}, "status", "riwayat": {nomor: keterangan}}}
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

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== SISTEM PENCATATAN PERANGKAT KERAS LAB INFORMATIKA ===")
    print("1. Login")
    print("2. Register")
    print("0. Keluar")
    menu = input("Pilih menu: ")
    os.system("cls" if os.name == "nt" else "clear")

    # LOGIN
    if menu == "1":
        print("=== LOGIN ===")
        user_login = None
        percobaan = 3
        while percobaan > 0:
            username = input("Username: ")
            password = input("Password: ")
            if username in data_user and data_user[username]["password"] == password:
                user_login = username
                break
            percobaan = percobaan - 1
            print("Username atau password salah! Sisa percobaan:", percobaan)

        if user_login == None:
            print("Percobaan habis, kembali ke menu awal.")
            input("Tekan Enter untuk lanjut...")
        else:
            print("Login berhasil, selamat datang", user_login)
            input("Tekan Enter untuk lanjut...")

            # MENU ADMIN
            if data_user[user_login]["role"] == "admin":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== MENU ADMIN ===")
                    print("Login sebagai:", user_login)
                    print("1. Tambah PC baru (Create)")
                    print("2. Lihat semua PC (Read)")
                    print("3. Lihat detail & riwayat servis (Read)")
                    print("4. Update status PC (Update)")
                    print("5. Upgrade spesifikasi PC (Update)")
                    print("6. Hapus PC (Delete)")
                    print("7. Lihat daftar user")
                    print("0. Logout")
                    pilih = input("Pilih menu: ")
                    os.system("cls" if os.name == "nt" else "clear")

                    # CREATE
                    if pilih == "1":
                        print("=== TAMBAH PC BARU ===")
                        nama = input("Nama PC: ")
                        ada = False
                        for id_pc, pc in data_pc.items():
                            if pc["nama"].lower() == nama.lower():
                                ada = True
                        if nama == "":
                            print("Nama tidak boleh kosong!")
                        elif ada == True:
                            print("Nama PC sudah ada!")
                        else:
                            cpu = input("CPU: ")
                            ram = input("RAM (GB): ")
                            storage = input("Storage (GB): ")
                            tanggal = input("Tanggal (contoh 14-10-2026): ")
                            if cpu == "" or tanggal == "":
                                print("Data tidak boleh kosong!")
                            elif ram.isdigit() == False or storage.isdigit() == False:
                                print("RAM dan Storage harus angka!")
                            elif int(ram) < 1 or int(storage) < 1:
                                print("RAM dan Storage minimal 1!")
                            else:
                                id_terakhir = id_terakhir + 1
                                data_pc[id_terakhir] = {
                                    "nama": nama,
                                    "spek": {"cpu": cpu, "ram": int(ram), "storage": int(storage)},
                                    "status": "Tersedia",
                                    "riwayat": {1: tanggal + " : Aset didaftarkan"}
                                }
                                print("Berhasil! PC", nama, "ditambahkan dengan ID", id_terakhir)

                    # READ semua
                    elif pilih == "2":
                        print("=== DAFTAR SEMUA PC ===")
                        print("ID | Nama | CPU | RAM | Storage | Status")
                        print("------------------------------------------------")
                        if len(data_pc) == 0:
                            print("Belum ada data PC.")
                        for id_pc, pc in data_pc.items():
                            spek = pc["spek"]
                            print(str(id_pc) + " | " + pc["nama"] + " | " + spek["cpu"] + " | " + str(spek["ram"]) + " GB | " + str(spek["storage"]) + " GB | " + pc["status"])

                    # READ detail
                    elif pilih == "3":
                        print("=== DETAIL & RIWAYAT SERVIS ===")
                        id_cari = input("Masukkan ID PC (cek ID di menu 2): ")
                        if id_cari.isdigit() == False:
                            print("ID harus berupa angka!")
                        elif int(id_cari) not in data_pc:
                            print("ID tidak ditemukan!")
                        else:
                            pc = data_pc[int(id_cari)]
                            spek = pc["spek"]
                            print("ID      :", id_cari)
                            print("Nama    :", pc["nama"])
                            print("CPU     :", spek["cpu"])
                            print("RAM     :", spek["ram"], "GB")
                            print("Storage :", spek["storage"], "GB")
                            print("Status  :", pc["status"])
                            print("Riwayat :")
                            for nomor, r in pc["riwayat"].items():
                                print(" ", nomor, ".", r)

                    # UPDATE status
                    elif pilih == "4":
                        print("=== UPDATE STATUS PC ===")
                        id_cari = input("Masukkan ID PC (cek ID di menu 2): ")
                        if id_cari.isdigit() == False:
                            print("ID harus berupa angka!")
                        elif int(id_cari) not in data_pc:
                            print("ID tidak ditemukan!")
                        else:
                            pc = data_pc[int(id_cari)]
                            print("Status sekarang:", pc["status"])
                            for nomor, nama_status in status_pilihan.items():
                                print(nomor + ".", nama_status)
                            pilih_status = input("Pilih status baru (1-4): ")
                            if pilih_status not in status_pilihan:
                                print("Pilihan tidak valid!")
                            else:
                                status_baru = status_pilihan[pilih_status]
                                if status_baru == pc["status"]:
                                    print("Status sama dengan sebelumnya!")
                                else:
                                    tanggal = input("Tanggal (contoh 14-10-2026): ")
                                    ket = input("Keterangan (kerusakan/servis): ")
                                    if tanggal == "":
                                        print("Tanggal tidak boleh kosong!")
                                    else:
                                        if ket == "":
                                            ket = "-"
                                        pc["status"] = status_baru
                                        nomor_baru = len(pc["riwayat"]) + 1
                                        pc["riwayat"][nomor_baru] = tanggal + " : " + status_baru + ", " + ket
                                        print("Status", pc["nama"], "berhasil diubah jadi", status_baru)

                    # UPDATE upgrade spek
                    elif pilih == "5":
                        print("=== UPGRADE SPESIFIKASI PC ===")
                        id_cari = input("Masukkan ID PC (cek ID di menu 2): ")
                        if id_cari.isdigit() == False:
                            print("ID harus berupa angka!")
                        elif int(id_cari) not in data_pc:
                            print("ID tidak ditemukan!")
                        else:
                            pc = data_pc[int(id_cari)]
                            spek = pc["spek"]
                            print("Spek sekarang:", spek["cpu"], "|", spek["ram"], "GB RAM |", spek["storage"], "GB Storage")
                            print("(kosongkan kalau tidak ingin diubah)")
                            cpu_baru = input("CPU baru: ")
                            ram_baru = input("RAM baru (GB): ")
                            sto_baru = input("Storage baru (GB): ")
                            if cpu_baru == "" and ram_baru == "" and sto_baru == "":
                                print("Tidak ada yang diubah.")
                            elif (ram_baru != "" and ram_baru.isdigit() == False) or (sto_baru != "" and sto_baru.isdigit() == False):
                                print("RAM dan Storage harus angka!")
                            else:
                                tanggal = input("Tanggal upgrade (contoh 14-10-2026): ")
                                if tanggal == "":
                                    print("Tanggal tidak boleh kosong!")
                                else:
                                    if cpu_baru == "":
                                        cpu_baru = spek["cpu"]
                                    if ram_baru == "":
                                        ram_baru = spek["ram"]
                                    if sto_baru == "":
                                        sto_baru = spek["storage"]
                                    # update langsung isi dictionary spek
                                    spek["cpu"] = cpu_baru
                                    spek["ram"] = int(ram_baru)
                                    spek["storage"] = int(sto_baru)
                                    nomor_baru = len(pc["riwayat"]) + 1
                                    pc["riwayat"][nomor_baru] = tanggal + " : Upgrade jadi " + cpu_baru + " | " + str(ram_baru) + " GB RAM | " + str(sto_baru) + " GB Storage"
                                    print("Spesifikasi", pc["nama"], "berhasil diupgrade!")

                    # DELETE
                    elif pilih == "6":
                        print("=== HAPUS PC ===")
                        id_cari = input("Masukkan ID PC (cek ID di menu 2): ")
                        if id_cari.isdigit() == False:
                            print("ID harus berupa angka!")
                        elif int(id_cari) not in data_pc:
                            print("ID tidak ditemukan!")
                        else:
                            pc = data_pc[int(id_cari)]
                            print("Mau hapus:", pc["nama"], "(status:", pc["status"] + ")")
                            yakin = input("Aset sudah dibuang? Ketik y untuk hapus: ")
                            if yakin == "y" or yakin == "Y":
                                del data_pc[int(id_cari)]
                                print("Data", pc["nama"], "berhasil dihapus!")
                            else:
                                print("Batal menghapus.")

                    # lihat user
                    elif pilih == "7":
                        print("=== DAFTAR USER ===")
                        print("Username | Role")
                        print("------------------")
                        for nama_user, info in data_user.items():
                            print(nama_user + " | " + info["role"])

                    # logout
                    elif pilih == "0":
                        break

                    else:
                        print("Menu tidak valid!")

                    input("Tekan Enter untuk lanjut...")

            # MENU USER BIASA
            else:
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== MENU PENGGUNA ===")
                    print("Login sebagai:", user_login)
                    print("1. Lihat semua PC")
                    print("2. Cek PC yang tersedia")
                    print("3. Lihat detail & riwayat servis")
                    print("0. Logout")
                    pilih = input("Pilih menu: ")
                    os.system("cls" if os.name == "nt" else "clear")

                    if pilih == "1":
                        print("=== DAFTAR SEMUA PC ===")
                        print("ID | Nama | CPU | RAM | Storage | Status")
                        print("------------------------------------------------")
                        if len(data_pc) == 0:
                            print("Belum ada data PC.")
                        for id_pc, pc in data_pc.items():
                            spek = pc["spek"]
                            print(str(id_pc) + " | " + pc["nama"] + " | " + spek["cpu"] + " | " + str(spek["ram"]) + " GB | " + str(spek["storage"]) + " GB | " + pc["status"])

                    elif pilih == "2":
                        print("=== PC YANG TERSEDIA ===")
                        print("ID | Nama | CPU | RAM | Storage | Status")
                        print("------------------------------------------------")
                        jumlah = 0
                        for id_pc, pc in data_pc.items():
                            if pc["status"] == "Tersedia":
                                spek = pc["spek"]
                                print(str(id_pc) + " | " + pc["nama"] + " | " + spek["cpu"] + " | " + str(spek["ram"]) + " GB | " + str(spek["storage"]) + " GB | " + pc["status"])
                                jumlah = jumlah + 1
                        print("Total tersedia:", jumlah, "dari", len(data_pc), "PC")

                    elif pilih == "3":
                        print("=== DETAIL & RIWAYAT SERVIS ===")
                        id_cari = input("Masukkan ID PC (cek ID di menu 1): ")
                        if id_cari.isdigit() == False:
                            print("ID harus berupa angka!")
                        elif int(id_cari) not in data_pc:
                            print("ID tidak ditemukan!")
                        else:
                            pc = data_pc[int(id_cari)]
                            spek = pc["spek"]
                            print("ID      :", id_cari)
                            print("Nama    :", pc["nama"])
                            print("CPU     :", spek["cpu"])
                            print("RAM     :", spek["ram"], "GB")
                            print("Storage :", spek["storage"], "GB")
                            print("Status  :", pc["status"])
                            print("Riwayat :")
                            for nomor, r in pc["riwayat"].items():
                                print(" ", nomor, ".", r)

                    elif pilih == "0":
                        break

                    else:
                        print("Menu tidak valid!")

                    input("Tekan Enter untuk lanjut...")

    # REGISTER
    elif menu == "2":
        print("=== REGISTER AKUN BARU ===")
        username = input("Username (tanpa spasi): ")
        password = input("Password (min 4 karakter): ")
        if username == "" or password == "":
            print("Username dan password tidak boleh kosong!")
        elif " " in username:
            print("Username tidak boleh pakai spasi!")
        elif username in data_user:
            print("Username sudah terdaftar!")
        elif len(password) < 4:
            print("Password minimal 4 karakter!")
        else:
            data_user[username] = {"password": password, "role": "user"}
            print("Register berhasil! Silakan login.")
        input("Tekan Enter untuk lanjut...")

    # KELUAR
    elif menu == "0":
        print("Terima kasih sudah menggunakan program ini.")
        break

    else:
        print("Menu tidak valid!")
        input("Tekan Enter untuk lanjut...")