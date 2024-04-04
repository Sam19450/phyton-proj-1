from fitur import edit, hapus, tambah


def tampil():
    print('Tampil')

    # Menampilkan daftar barang

    # Variabel untuk error handling
    err: int = 1

    while err:
        err = 0
        # Input untuk fitur halaman Tampil
        print('Pilih Fitur yang dituju (Tambah, Edit, Hapus) : ')
        fitur: str = input().lower()

        match fitur:

            case 'tambah':
                # Fitur tambah
                tambah()
                pass

            case 'edit':
                # Fitur Edit
                edit()
                pass

            case 'hapus':
                # Fitur Hapus
                hapus()
                pass

            case _:
                err = 1
                print('Input tidak sesuai!')
                print('Silahkan berikan input kembali')


def transaksi():
    print('Transaksi')

    # Handle barang transaksi
    keranjang: list = []

    while True:

        # # Tampilkan Keranjang Pembelian
        # print(keranjang)

        # # Input untuk mengisi keranjang
        # nama_barang:str = input('Masukkan nama barang : ')
        # jumlah_barang:int = int(input('Masukkan jumlah barang yang ingin dibeli : '))

        # keranjang.append({'nama barang' : nama_barang, 'jumlah' : jumlah_barang})

        while True:
            # Input untuk fitur halaman transaksi
            print('Pilih fitur yang dituju (Tambah, Hitung, Batalkan) : ')
            fitur: str = input().lower()

            match fitur:

                case 'tambah':
                    break

                case 'hitung':
                    # Fitur Kalkulasi
                    pass

                case 'batalkan':
                    # Fitur batalkan
                    pass

                case _:
                    print('Input tidak sesuai!')
                    print('Silahkan berikan input kembali')

                    continue

    # Buat dan simpan ke DB Nota

    # Tampilkan Nota


def nota():
    print('Nota')

    # Handle data nota

    # Tampilkan Daftar Nota

    pass


def laba():
    print('Laba')

    pass
