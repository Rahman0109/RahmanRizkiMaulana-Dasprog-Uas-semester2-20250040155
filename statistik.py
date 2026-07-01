import csv

FILE_NAME = "data_mahasiswa.csv"


def statistik_nilai():

    nilai = []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            nilai.append(float(row["Nilai"]))

    if len(nilai) == 0:
        print("Belum ada data.")
        return

    rata = sum(nilai) / len(nilai)

    print("\n===== STATISTIK NILAI =====")
    print("Jumlah Mahasiswa :", len(nilai))
    print("Nilai Tertinggi  :", max(nilai))
    print("Nilai Terendah   :", min(nilai))
    print("Rata-rata Nilai  :", round(rata, 2))
    print()