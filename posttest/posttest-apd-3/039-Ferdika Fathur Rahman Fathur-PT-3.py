def main():
    nama_benar = "Ferdika Fathur Rahman"
    nim_benar = "39"
    
    biaya_langganan_dasar = 1_500_000
    
    print("=" * 60)
    print("🎵 SELAMAT DATANG DI APLIKASI STREAMING MUSIK 'ANGKASA' 🎵")
    print("=" * 60)
    print()
    
    print("--- PROSES LOGIN ---")
    nama_input = input("Masukkan Nama: ").strip()
    nim_input = input("Masukkan NIM: ").strip()
    
    if nama_input != nama_benar or nim_input != nim_benar:
        print("\n❌ AKSES DITOLAK!")
        print("Data Nama atau NIM tidak terdaftar dalam sistem.")
        return 
    
    print(f"\n✅ Login Berhasil! Selamat datang, {nama_benar}.")
    print()
    
    print("=" * 60)
    print("📋 PILIH PAKET LANGGANAN BULANAN")
    print("=" * 60)
    print("  1. Paket Orbit     (Admin 1%) - Akses Dasar")
    print("  2. Paket Nebula    (Admin 3%) - Premium & Playlist Kustom")
    print("  3. Paket Galaxy    (Admin 5%) - Offline Mode & HD Audio")
    print("  4. Paket Supernova (Admin 7%) - All Access & Eksklusif")
    print("-" * 60)
    
    try:
        pilihan = int(input("Masukkan nomor paket (1-4): "))
    except ValueError:
        print("\n❌ Error: Input harus berupa angka!")
        return

    paket_data = {
        1: {"nama": "Orbit", "admin": 0.01, 
            "fitur": ["Akses lagu populer", "Streaming standar", "Playlist harian"]},
        2: {"nama": "Nebula", "admin": 0.03, 
            "fitur": ["Akses lagu premium", "Playlist kustom", "Audio High Quality", "Bebas Iklan"]},
        3: {"nama": "Galaxy", "admin": 0.05, 
            "fitur": ["Fitur Nebula", "Mode Offline (Download)", "Audio HD", "Prioritas Server"]},
        4: {"nama": "Supernova", "admin": 0.07, 
            "fitur": ["Semua Fitur Premium", "Konten Eksklusif Artis", "Audio Lossless", "Support 24/7"]}
    }

    if pilihan not in paket_data:
        print("\n❌ Pilihan paket tidak tersedia. Silakan pilih 1-4.")
        return

    data_paket = paket_data[pilihan]
    biaya_admin = biaya_langganan_dasar * data_paket["admin"]
    total_bayar = biaya_langganan_dasar + biaya_admin
    
    total_bayar = round(total_bayar)
    biaya_admin = round(biaya_admin)

    print("\n" + "=" * 60)
    print("🧾 STRUK PEMBAYARAN LANGGANAN ANGKASA")
    print("=" * 60)
    print(f"👤 Pelanggan   : {nama_benar}")
    print(f"🆔 NIM         : {nim_benar}")
    print("-" * 60)
    print(f"📦 Paket       : {data_paket['nama']}")
    print(f"💰 Harga Dasar : Rp {biaya_langganan_dasar:,}".replace(',', '.'))
    print(f"📊 Admin Fee   : Rp {biaya_admin:,} ({int(data_paket['admin']*100)}%)".replace(',', '.'))
    print("-" * 60)
    print(f"💳 TOTAL BAYAR : Rp {total_bayar:,}".replace(',', '.'))
    print("=" * 60)
    
    print("\n✨ FITUR YANG ANDA DAPATKAN:")
    for i, fitur in enumerate(data_paket['fitur'], 1):
        print(f"   {i}. {fitur}")
        
    print()
    if pilihan == 1:
        print("Minggir Lu Miskhin 💸𓁉 (dengan nada Speed⚡)")
    elif pilihan == 4:
        print("Selamat Menikmati Musiknya King, Mahkotamu Ketinggalan di DC Cakung 👑")
    else:
        print("🎉 Terima kasih! Musik favoritmu siap menemani harimu.")
        
    print("=" * 60)

if __name__ == "__main__":
    main()