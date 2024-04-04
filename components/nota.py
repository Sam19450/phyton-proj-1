def print_barang_str(barang):
    # Menghilangkan tanda kurung siku dan spasi pada awal dan akhir string
    barang_list_str = barang[1][2:-2].split("], [")

    for idx, barang_str in enumerate(barang_list_str, 1):
        # Mengonversi setiap elemen string menjadi list
        barang = barang_str.split(", ")

        # Pastikan barang adalah list dan memiliki setidaknya 3 elemen
        if len(barang) >= 3:
            nama_barang, jumlah, harga_barang = barang[0], barang[1], barang[2]
            # print(f"{idx}. Nama barang: {nama_barang}, Jumlah: {
            #       jumlah}, Harga: {harga_barang}")
            print(f"{nama_barang[1:-1]}\n x{jumlah} : Rp {harga_barang}")
        else:
            print("Data barang tidak valid.")


def print_barang_list(barang):
    for data in barang:
        nama_barang, jumlah, harga_barang = data[0], data[1], data[2]

        print(f"{nama_barang}\n x{jumlah} : Rp {harga_barang}")


def print_nota(nota_data):
    print("\n=======================================")
    print("             NOTA PEMBELIAN")
    print("=======================================\n")

    print(f"Tanggal: {nota_data[0]}\n")

    if type(nota_data[1]) == list:
        print_barang_list(nota_data[1])
    else:
        print_barang_str(nota_data)

    print(f"\nTotal Harga: Rp {nota_data[2]}")
    print(f"Total Keuntungan: Rp {nota_data[3]}\n")

    print("=======================================")
    print("              Terimakasih")
    print("            by DagangPraktis")
    print("=======================================\n")
