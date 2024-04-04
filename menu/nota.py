import csv

from components.nota import print_nota


def fungsi_nota():
    while True:

        FILE_PATH = 'data/nota.csv'

        # Akses DB Nota
        with open(FILE_PATH, 'r') as nota_file:
            reader = csv.reader(nota_file)
            next(reader)  # Melewati header dari baris

            # Perulangan untuk setiap baris
            for row in reader:

                # Fungsi untuk menampilkan nota setiap baris sebagai argumennya
                print_nota(row)

        # Input untuk fitur halaman transaksi
            print('Pilih fitur yang dituju (Reset, Keluar) : ')
            fitur: str = input().lower()

            match fitur:
                case 'reset':
                    with open('data/nota.csv', mode='w', newline='') as nota :
                        write = csv.writer(nota)

                        # Menulis baris data
                        write.writerow('')

                case 'keluar':
                    break


# Menjalankan Fungsi untuk Debugging
# fungsi_nota()
