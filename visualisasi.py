import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "data_mahasiswa.csv"


def grafik_nilai():

    df = pd.read_csv(FILE_NAME)

    plt.figure(figsize=(10, 5))

    plt.bar(df["Nama"], df["Nilai"])

    plt.title("Grafik Nilai Mahasiswa")
    plt.xlabel("Nama Mahasiswa")
    plt.ylabel("Nilai")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()