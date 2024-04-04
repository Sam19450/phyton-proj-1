import csv

from utils.clear import clear_screen


def fungsi_laba():

    # Fungi untuk clear Terminal
    clear_screen()

    # Lokasi DB Nota
    FILE_PATH: str = 'data/nota.csv'

    while True:

        # Akses DB Nota
        with open(FILE_PATH, 'r') as nota_file:
            # Menyalin DB ke Variabel
            nota = csv.reader(nota_file)

            next(nota)  # Melewati header dari baris

            # Deklarasi Variabel awal
            untung: int | str = 0

            # Perulangan setiap baris data
            for row in nota:
                # Menambah Variabel dengan data keuntungan dari setiap baris
                untung += float(row[-1])

            # Handle jika kosong
            if untung == 0:
                untung = 'Belum ada Keuntungan'

            # Menampilkan Total Keuntungan
            print(untung)

            # Input untuk fitur halaman transaksi
            print('Kembali ke menu utama? (y/n) ')
            konfirmasi: str = input().lower()

            # Handle keluar menu
            if konfirmasi == 'y':
                break


# Menjalankan Fungsi untuk debugging
# fungsi_laba()


# Menjalankan Fungsi untuk debugging
# fungsi_laba()
