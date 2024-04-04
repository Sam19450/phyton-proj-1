# import datetime
from typing import List
# from menu import menu

# def menu():
#     # Handling Pengulangan jika terdapat Error

#     while True :

#         # Menampilkan Daftar Menu yang disedikan
#         print('1. satu')
#         print('2. dua')

#         # Input untuk memilih menu
#         pilihan:int = int(input('Masukkan Pilihan : '))

#         # Navigasi Menu utama
#         if pilihan == 1 :
#             satu()
#         elif pilihan == 2 :
#             dua()
#         else :
#             # Handling untuk input tidak sesuai
#             print('Input tidak sesuai!')
#             print('Silahkan masukkan pilihan lagi')

#             # Mengulan perulangan nya
#             continue


# def satu() :
#     while True :
#         print('Pilih Fitur : ')
#         print('1. Print')
#         print('2. Kembali')
#         fitur = input()
#         match fitur :
#             case '1' :
#                 print('satu')
#             case '2' :
#                 break


# def dua() :
#     res = input('Kembali?')


# menu()

# waktu = datetime.datetime.now()
# print(waktu)


# def satu():
#     print('1')


# def dua():
#     print('2')


# def tiga():
#     print('3')


# def empat():
#     print('4')


# fitur: List[str] = [
#     'satu()', 'dua()', 'tiga()', 'empat()'
# ]

# for i in range(len(fitur)):
#     eval(fitur[i])

import csv

from menu.laba import fungsi_laba
from menu.nota import fungsi_nota
from utils.clear import clear_screen


# def baca_nota():

#     # Akses file DB Nota
#     FILE_PATH = 'data/nota.csv'

#     with open(FILE_PATH, 'r') as nota_file:
#         nota = csv.reader(nota_file)

#         # Membaca setiap baris nota
#         for waktu, keranjang, total_harga, total_untung in nota:

#             # print(row)

#             # waktu, keranjang, total_harga, total_untung = row
#             # print('\n')

#             # # Menggunakan CSV untuk membaca list langsung
#             # keranjang = list(csv.reader([keranjang]))[0]
#             # keranjang: List = keranjang[1:-1]

#             # Menampilkan informasi nota
#             print('\n=======================================')
#             print('             NOTA PEMBELIAN              ')
#             print('=======================================')
#             print(f'\nTanggal: {waktu[:11]}')
#             print(f'Waktu: {waktu[11:19]}')
#             print()
#             # print_keranjang(keranjang)  # Menggunakan keranjang langsung tanpa eval atau parsing JSON
#             print(f'{keranjang}')
#             print()
#             print(f'Total Harga: Rp {total_harga}')
#             print(f'Total Keuntungan: Rp {total_untung}')
#             print()
#             print('=======================================')
#             print('              Terimakasih              ')
#             print('            by DagangPraktis           ')
#             print('=======================================\n\n')


# # Panggil fungsi untuk membaca nota
# baca_nota()


# import csv

# FILE_PATH = 'data/nota.csv'


# with open(FILE_PATH, 'r') as nota_file:
#     nota = csv.reader(nota_file)

#     untung = 0
#     for row in nota:
#         untung += float(row[-1])
#         print(untung)

# clear_screen()
# fungsi_laba()

# fungsi_nota()
