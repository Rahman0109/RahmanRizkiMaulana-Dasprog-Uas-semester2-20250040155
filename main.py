from mahasiswa import *
from statistik import *
from visualisasi import *

while True:

    print("\n================================================")
    print(" SISTEM PENGELOLAAN DATA MAHASISWA ")
    print("================================================")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Cari Data")
    print("4. Hapus Data")
    print("5. Statistik Nilai")
    print("6. Ranking Mahasiswa")
    print("7. Grafik Nilai")
    print("8. Keluar")
    print("================================================")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        tambah_data()

    elif pilihan == "2":
        tampilkan_data()

    elif pilihan == "3":
        cari_data()

    elif pilihan == "4":
        hapus_data()

    elif pilihan == "5":
        statistik_nilai()

    elif pilihan == "6":
        ranking_mahasiswa()

    elif pilihan == "7":
        grafik_nilai()

    elif pilihan == "8":
        print("Terima kasih.")
        break

    else:
        print("Menu tidak tersedia.")