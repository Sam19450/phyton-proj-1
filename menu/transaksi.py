import csv
import datetime
from typing import List

from components.keranjang import print_keranjang
from components.nota import print_nota
from utils.clear import clear_screen


def fungsi_transaksi():
    print('Transaksi')

    transaksi: List[str] = []
    FILE_PATH: str = 'data/barang.csv'

    # Load transaksi dari file ke dalam list saat program dimulai
    if open(FILE_PATH, 'r').read():  # Cek apakah file ada isinya
        file = open(FILE_PATH, 'r')
        reader = csv.reader(file)

        # Filter untuk hanya memuat baris yang sesuai
        transaksi = [row for row in reader if len(row) == 4]
        file.close()

    # Debugging
    # print(transaksi)

    total_harga: float = 0
    totalUntung: float = int(0)
    keranjang: List[List[str, int, float]] = []

    while True:

        # Fungi untuk clear Terminal
        clear_screen()

        # Menampilkan keranjang
        print_keranjang(keranjang)

        # Input untuk fitur halaman transaksi
        print('Pilih fitur yang dituju (Tambah, Hitung, Batalkan) : ')
        fitur: str = input().lower()

        match fitur:

            case 'tambah':
                # Fungi untuk clear Terminal
                clear_screen()

                print(
                    "Masukkan barang yang ingin Anda beli (ketik '0' untuk menyelesaikan belanja) :")

                # Pengulangan menambah barang ke dalam keranjang
                while True:

                    # Menampilkan keranjang
                    print_keranjang(keranjang)

                    # Input barang dari User
                    nama_barang: str = input("Nama barang : ").lower()

                    # Handle untuk menyelesaikan fitur atau
                    if nama_barang == '0':
                        break  # Keluar dari loop jika pengguna memasukkan 'selesai'
                    else:
                        jumlah: int = int(
                            input('Masukkan jumlah barang yang ingin dibeli : '))
                    milih=input("apakah yakin untuk menambahkan barang?[y/n]")
                    if milih=="y":
                        
                    
                    # Mencari harga barang berdasarkan nama barang
                        harga_barang = None
                        for barang, modal, harga, satuan in transaksi:

                            if barang.lower() == nama_barang:
                                harga_barang: float = float(harga) * jumlah
                                untung: float = harga_barang - \
                                    float(modal) * jumlah
                                break

                        if harga_barang is not None:
                            total_harga += harga_barang
                            totalUntung += untung
                            print(f"{nama_barang} berhasil ditambahkan.")
                            keranjang.append([nama_barang, jumlah, harga_barang])
                        else:
                            print(f"{nama_barang} tidak ditemukan di daftar.")
                    elif milih=="n":
                        break
                    else :
                        break

            case 'hitung':
                # Fitur Kalkulasi

                # Fungi untuk clear Terminal
                clear_screen()

                # Waktu Transaksi
                waktu: str = str(datetime.datetime.now())

                # Membuat List data Transaksi
                data: List[str, List[str, float], float, float] = [
                    waktu, keranjang, total_harga, totalUntung
                ]

                # Tampilan Nota
                print_nota(data)

                konfirmasi = input('Simpan transaksi? (y/n) ')
                if konfirmasi == 'y':

                    # Membuka dan menyimpan data Transaksi ke DB Nota
                    with open('data/nota.csv', mode='a', newline='') as nota:
                        write = csv.writer(nota)

                        # Menulis baris data
                        write.writerow(data)

                    print('Transaksi telah disimpan!')

                    break

            case 'batalkan':
                break

            case _:
                # Fungi untuk clear Terminal
                clear_screen()

                print('Input tidak sesuai!')
                print('Silahkan berikan input kembali')

                continue


# fungsi_transaksi()
