print("==========================================")
print("   SELAMAT DATANG DI SISTEM MONITORING    ")
print("==========================================")

username_benar = "Ferdika"
password_benar = "039"

login_sukses = False

while not login_sukses:
    print("\n--- SILAHKAN LOGIN ---")
    input_user = input("Masukkan Username: ")
    input_pass = input("Masukkan Password: ")

    if input_user == "" or input_pass == "":
        print("Peringatan: Input ndik kawa kosong!")
        continue
    if input_user == username_benar and input_pass == password_benar:
        print("\nLogin Berhasil! Selamat datang, " + input_user)
        login_sukses = True
    elif input_user != username_benar and input_pass == password_benar:
        print("Username salah! Coba lagi.")
    elif input_user == username_benar and input_pass != password_benar:
        print("Password salah! Coba lagi.")
    else:
        print("Username dan Password salah! Coba lagi.")

total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0

lanjut_input = "Y"

while lanjut_input.upper() == "Y":
    print("\n------------------------------------------")
    print("   INPUT DATA TITIK API (HOTSPOT)         ")
    print("------------------------------------------")
    
    print("\nPilih Wilayah Pulau:")
    print("1. KALIMANTAN")
    print("2. SUMATERA")
    pulau = input("Masukkan nama pulau (Kalimantan/Sumatera): ")
    
    if pulau == "":
        print("Input pulau tidak boleh kosong. Data dilewati.")
        tanya_lanjut = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ")
        if tanya_lanjut.upper() == "Y":
            continue
        else:
            break
            
    pulau_clean = pulau.upper()

    jenis_lahan = ""
    if pulau_clean == "KALIMANTAN":
        print("\nJenis Lahan di Kalimantan:")
        print("1. GAMBUT")
        print("2. MINERAL")
        lahan = input("Masukkan jenis lahan (Gambut/Mineral): ")
        
        if lahan == "":
            print("Input jenis lahan tidak boleh kosong.")
            tanya_lanjut = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ")
            if tanya_lanjut.upper() == "Y":
                continue
            else:
                break
        else:
            jenis_lahan = lahan.upper()
            
    elif pulau_clean == "SUMATERA":
        print("\nJenis Lahan di Sumatera:")
        print("1. GAMBUT")
        print("2. MINERAL")
        lahan = input("Masukkan jenis lahan (Gambut/Mineral): ")
        
        if lahan == "":
            print("Input jenis lahan tidak boleh kosong.")
            tanya_lanjut = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ")
            if tanya_lanjut.upper() == "Y":
                continue
            else:
                break
        else:
            jenis_lahan = lahan.upper()
    else:
        print("Pulau tidak dikenali. Masukkan 'Kalimantan' atau 'Sumatera'.")
        tanya_lanjut = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ")
        if tanya_lanjut.upper() == "Y":
            continue
        else:
            break

    try:
        jumlah_hotspot = int(input("\nMasukkan Jumlah Titik Api (Hotspot): "))
        if jumlah_hotspot < 0:
            print("Jumlah titik api tidak bisa negatif.")
            tanya_lanjut = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ")
            if tanya_lanjut.upper() == "Y":
                continue
            else:
                break
    except ValueError:
        print("Input harus berupa angka!")
        tanya_lanjut = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ")
        if tanya_lanjut.upper() == "Y":
            continue
        else:
            break

    luas_terbakar = jumlah_hotspot * 5
    
    print(f"\nLuas lahan terbakar: {luas_terbakar} Hektare")

    if pulau_clean == "KALIMANTAN":
        if jenis_lahan == "GAMBUT":
            total_kalimantan_gambut = total_kalimantan_gambut + luas_terbakar
        elif jenis_lahan == "MINERAL":
            total_kalimantan_mineral = total_kalimantan_mineral + luas_terbakar
        else:
            print("Jenis lahan tidak dikenali untuk Kalimantan.")
            
    elif pulau_clean == "SUMATERA":
        if jenis_lahan == "GAMBUT":
            total_sumatera_gambut = total_sumatera_gambut + luas_terbakar
        elif jenis_lahan == "MINERAL":
            total_sumatera_mineral = total_sumatera_mineral + luas_terbakar
        else:
            print("Jenis lahan tidak dikenali untuk Sumatera.")

    tanya_lanjut = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ")
    lanjut_input = tanya_lanjut

print("\n\n==========================================")
print("        RINGKASAN LAPORAN AKHIR           ")
print("==========================================")

print("\nWILAYAH KALIMANTAN:")
print(f"   - Lahan Gambut  : {total_kalimantan_gambut} Hektare")
print(f"   - Lahan Mineral : {total_kalimantan_mineral} Hektare")

print("\nWILAYAH SUMATERA:")
print(f"   - Lahan Gambut  : {total_sumatera_gambut} Hektare")
print(f"   - Lahan Mineral : {total_sumatera_mineral} Hektare")

total_semua = total_kalimantan_gambut + total_kalimantan_mineral + total_sumatera_gambut + total_sumatera_mineral
print("\n------------------------------------------")
print(f"TOTAL KESELURUHAN LAHAN TERBAKAR: {total_semua} Hektare")
print("==========================================")