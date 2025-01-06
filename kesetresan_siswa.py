

def prediksi_stres(jumlah_tugas, lama_belajar, waktu_tidur, aktivitas_relaksasi):
    """
    Memprediksi tingkat stres mahasiswa berdasarkan parameter tertentu.

    Args:
        jumlah_tugas (int): Jumlah tugas yang harus diselesaikan.
        lama_belajar (int): Lama belajar per hari dalam jam.
        waktu_tidur (int): Waktu tidur rata-rata per hari dalam jam.
        aktivitas_relaksasi (int): Lama aktivitas relaksasi per hari dalam jam.

    Returns:
        str: Tingkat stres ("Rendah", "Sedang", "Tinggi").
    """
    skor_stres = 0

    if jumlah_tugas > 10:
        skor_stres += 20
    elif 6 <= jumlah_tugas <= 10:
        skor_stres += 10
    elif 1 <= jumlah_tugas <= 5:
        skor_stres += 5

    if lama_belajar > 8:
        skor_stres += 15
    elif 4 <= lama_belajar <= 8:
        skor_stres += 10
    elif lama_belajar < 4:
        skor_stres += 5

    if waktu_tidur >= 7:
        skor_stres -= 15
    elif 5 <= waktu_tidur < 7:
        skor_stres -= 10
    elif waktu_tidur < 5:
        skor_stres += 10


    if aktivitas_relaksasi >= 2:
        skor_stres -= 10
    elif 1 <= aktivitas_relaksasi < 2:
        skor_stres -= 5
    elif aktivitas_relaksasi < 1:
        skor_stres += 5

   
    if skor_stres < 20:
        return "Rendah"
    elif 20 <= skor_stres <= 40:
        return "Sedang"
    else:
        return "Tinggi"

def main():
    print("Sistem Prediksi Tingkat Stres Mahasiswa")
    jumlah_tugas = int(input("Masukkan jumlah tugas yang harus diselesaikan: "))
    lama_belajar = int(input("Masukkan lama belajar per hari (jam): "))
    waktu_tidur = int(input("Masukkan rata-rata waktu tidur per hari (jam): "))
    aktivitas_relaksasi = int(input("Masukkan rata-rata lama aktivitas relaksasi per hari (jam): "))

    tingkat_stres = prediksi_stres(jumlah_tugas, lama_belajar, waktu_tidur, aktivitas_relaksasi)
    print(f"Tingkat stres Anda: {tingkat_stres}")


if __name__ == "__main__":
    main()
