# Import Modules
from menu import barang, transaksi, laba, nota
import daftar
from utils import clear

# Fungsi Menu


def menu():
    # Handling Pengulangan jika terdapat Error

    while True:

        # Menampilkan Daftar Menu yang disedikan
        for index, menu in enumerate(daftar.list_menu):
            print(f'{index + 1}. {menu}')

        # Input untuk memilih menu
        pilihan: str = input('Masukkan Pilihan : ')

        # Navigasi Menu utama
        if pilihan == '1':
            barang.fungsi_barang()
            clear.clear_screen()
        elif pilihan == '2':
            transaksi.fungsi_transaksi()
            clear.clear_screen()
        elif pilihan == '3':
            nota.fungsi_nota()
            clear.clear_screen()
        elif pilihan == '4':
            laba.fungsi_laba()
            clear.clear_screen()
        elif pilihan == '5':
            konfirmasi: str = input('Keluar dari Aplikasi, lanjutkan? (y/n) ')
            clear.clear_screen()

            if konfirmasi != 'y':
                continue

            break

        else:
            # Handling untuk input tidak sesuai

            print('Input tidak sesuai!')
            print('Silahkan masukkan pilihan lagi')

            continue


menu()
