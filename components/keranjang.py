def print_keranjang(objek):
    if len(objek) == 0:
        print('Keranjang masih kosong!')
    else:
        print("Daftar barang di keranjang : \n")
        for index, barang in enumerate(objek, 1):
            print(f'{index}. Nama barang : {barang[0]}, Jumlah barang : {barang[1]}, Harga barang : Rp {barang[2]} ')
