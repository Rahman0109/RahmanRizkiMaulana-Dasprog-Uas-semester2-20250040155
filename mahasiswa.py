import csv

FILE_NAME = "data_mahasiswa.csv"


def tambah_data():
    nim = input("NIM       : ")
    nama = input("Nama      : ")
    prodi = input("Prodi     : ")
    semester = input("Semester  : ")
    nilai = input("Nilai     : ")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([nim, nama, prodi, semester, nilai])

    print("\nData berhasil ditambahkan.\n")


def tampilkan_data():

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        print("\n============================================================")
        print("DATA MAHASISWA")
        print("============================================================")

        for row in reader:
            print(row)

        print()


def cari_data():

    nim = input("Masukkan NIM yang dicari : ")

    ditemukan = False

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 0 and row[0] == nim:
                print("\nData ditemukan:")
                print(row)
                ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.\n")


def hapus_data():

    nim_hapus = input("Masukkan NIM yang akan dihapus : ")

    data_baru = []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 0 and row[0] != nim_hapus:
                data_baru.append(row)

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data_baru)

    print("Data berhasil dihapus.\n")


def ranking_mahasiswa():

    data = []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    data.sort(key=lambda x: float(x["Nilai"]), reverse=True)

    print("\n===== RANKING MAHASISWA =====")

    no = 1

    for mhs in data:
        print(
            f"{no}. {mhs['Nama']} | {mhs['Prodi']} | Nilai: {mhs['Nilai']}"
        )
        no += 1

    print()