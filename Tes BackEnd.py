def hitung_gaji():
    # Input jumlah jam kerja dan tarif per jam
    try:
        jam_kerja = float(input("Masukkan jumlah jam kerja: "))
        tarif_per_jam = float(input("Masukkan tarif per jam: "))
    except ValueError:
        print("Masukkan angka yang valid untuk jam kerja dan tarif.")
        return
    
    # Inisialisasi variabel gaji
    gaji_normal = 0
    gaji_lembur = 0

    # Jika jam kerja lebih dari 40 jam, hitung lembur
    if jam_kerja > 40:
        jam_lembur = jam_kerja - 40
        gaji_normal = 40 * tarif_per_jam
        gaji_lembur = jam_lembur * (1.5 * tarif_per_jam)
    else:
        gaji_normal = jam_kerja * tarif_per_jam

    # Total gaji
    total_gaji = gaji_normal + gaji_lembur

    # Menampilkan hasil
    print("\n--- Rincian Gaji ---")
    print(f"Gaji Normal (40 jam pertama): Rp {gaji_normal:.2f}")
    if gaji_lembur > 0:
        print(f"Gaji Lembur: Rp {gaji_lembur:.2f}")
    print(f"Total Gaji Mingguan: Rp {total_gaji:.2f}")

# Panggil fungsi utama
if __name__ == "__main__":
    print("Program Menghitung Gaji Karyawan\n")
    hitung_gaji()
