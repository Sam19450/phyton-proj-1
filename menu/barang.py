import csv

from utils.clear import clear_screen


def fungsi_barang():

    databarang = []
    FILE_PATH = 'data/barang.csv'

    # Membaca data dari file CSV dan memuatnya ke dalam databarang saat program dimulai
    with open(FILE_PATH, 'r', newline='') as file_csv:
        databarang = list(csv.reader(file_csv))

    while True:

        # Fungi untuk clear Terminal
    

        # Tampilkan Daftar Barang
        print("\nData:")
        for idx, (nama_barang, modal_harga, total_harga, Jenis_barang) in enumerate(databarang, 1):
            print(f"{idx}. Barang: {nama_barang}, Harga modal: {modal_harga}, Harga jual: {total_harga}, Jenis barang: {Jenis_barang}")

        # Tampilkan setiap fitur yang disediakan
        print("\nPilih yang mana nih?:")
        print("1. Tambah Barang")
        print("2. Hapus Data Barang")
        print("3. Ganti Detail Barang")
        print("4. Kembali ke menu utama")
        print("5. Clear Screen")
        # Variabel fitur yang dipilih User
        pilihan = input("Pilih nomor berapa?: ")

        if pilihan == "1":
            x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            nama_barang = input("\nNama barang?: ")
            angka_ditemukan = False

            for i in x:
                if i in nama_barang:
                    angka_ditemukan = True
            if angka_ditemukan == True:
                print(" --------------------------------------------")
                print("| Angka terdeteksi !, Tidak bisa melanjutkan |")
                print(" --------------------------------------------")
                continue
            z = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            modal_harga = input("Harga modalnya berapa?:")
            angka_ditemukan2 = False

            for huruf in z:
                if huruf in modal_harga:
                    angka_ditemukan2 = True
            if angka_ditemukan2 == True:
                print(" --------------------------------------------")
                print("| Huruf terdeteksi !, Tidak bisa melanjutkan |")
                print(" --------------------------------------------")
                continue
            total_harga = input("Harga jualnya berapa?: ")
            for huruf in z:
                if huruf in total_harga:
                    angka_ditemukan2 = True
            if angka_ditemukan2 == True:
                print(" --------------------------------------------")
                print("| Huruf terdeteksi !, Tidak bisa melanjutkan |")
                print(" --------------------------------------------")
                continue
            Jenis_barang = input("Jenis apa nih? Pcs/Kg:")

            if Jenis_barang in ["PCS", "Pcs", "pCs", "pcS", "PCs", "pCS", "PcS", "pcs"]:
                Jenis_barang = "Pcs"
            if Jenis_barang in ["KG", "kg", "Kg", "kG"]:
                Jenis_barang = "Kg"
            elif Jenis_barang != "Pcs" and Jenis_barang != "Kg":
                print(" -------------------------------------")
                print("| Waduh jenis apaantuh, saya gk paham |")
                print(" -------------------------------------")
                continue
            databarang.append(
                [nama_barang, modal_harga, total_harga, Jenis_barang])

            # Simpan setiap databarang ke dalam file setelah ditambahkan
            file = open(FILE_PATH, 'w', newline='')
            writer = csv.writer(file)
            writer.writerows(databarang)
            file.close()
            print(" --------------------------------")
            print("| Udah masuk tuh Data Barangnya! |")
            print(" --------------------------------")
            while True:
                print("\nLanjut menambahkan atau tidak?")
                print("1. Lanjut")
                print("2. tidak")
                lanjut = input("Pilih nomor berapa?: ")
                if lanjut == "1":
                    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                    nama_barang = input("\nNama barang?: ")
                    angka_ditemukan = False

                    for i in x:
                        if i in nama_barang:
                            angka_ditemukan = True
                    if angka_ditemukan == True:
                        print(" --------------------------------------------")
                        print("| Angka terdeteksi !, Tidak bisa melanjutkan |")
                        print(" --------------------------------------------")
                        continue
                    modal_harga = input("Harga modalnya berapa?:")
                    total_harga = input("Harga jualnya berapa?: ")
                    Jenis_barang = input("Jenis apa nih? Pcs/Kg:")
                    if Jenis_barang in ["PCS", "Pcs", "pCs", "pcS", "PCs", "pCS", "PcS", "pcs"]:
                        Jenis_barang = "Pcs"
                    if Jenis_barang in ["KG", "kg", "Kg", "kG"]:
                        Jenis_barang = "Kg"
                    elif Jenis_barang != "Pcs" and Jenis_barang != "Kg":
                        print(" -------------------------------------")
                        print("| Waduh jenis apaantuh, saya gk paham |")
                        print(" -------------------------------------")
                        continue

                    databarang.append(
                        [nama_barang, modal_harga, total_harga, Jenis_barang])

                    # Simpan setiap databarang ke dalam file setelah ditambahkan
                    file = open(FILE_PATH, 'w', newline='')
                    writer = csv.writer(file)
                    writer.writerows(databarang)
                    file.close()
                    print(" --------------------------------")
                    print("| Udah masuk tuh Data Barangnya! |")
                    print(" --------------------------------")

                if lanjut == "2":
                    print(" ----------------------------------------------")
                    print("| Selamat !, Barang-barangmu sudah ditambahkan |")
                    print(" ----------------------------------------------")
                    break
                elif lanjut != "1" and lanjut != "2":
                    print(" -------------------------------")
                    print("| Eror, Masukkan angka 1 atau 2 |")
                    print(" -------------------------------")
                    continue

        elif pilihan == "2":
            # Tampilkan databarang saat ini

            nomor = int(input("Pilih nomor Data barang yang mau dihapus?: "))

            if 0 <= nomor <= len(databarang):
                del databarang[nomor - 1]
                # Simpan setelah databarang dihapus
                file = open(FILE_PATH, 'w', newline='')
                writer = csv.writer(file)
                writer.writerows(databarang)
                file.close()
                print(" --------------------------")
                print("| Data barang sudah di Hapus |")
                print(" --------------------------")

            else:
                print(" -----------------------------")
                print("| Nomor Data barang tidak valid |")
                print(" -----------------------------")

        elif pilihan == "3":
            print("\nAyo dipilih mau ganti apa:")
            print("1.Modal barang")
            print("2.Harga jual")
            print("3.Jenis barang")
            print("Kalau milih lebih dari 1 pilihan, ngisinya urut ya, cth:123")
            b = input("Masukkan pilihanmu:")



            def simpenan(): 
                file = open(FILE_PATH, 'w', newline='')
                writer = csv.writer(file)
                writer.writerows(databarang)
                file.close()

            def ganti_modal():
                if 1 <= nomorr <= len(databarang):
                    modal_baru = int(input("Masukkan harga modal yang baru:"))
                    data_baru = (databarang[nomorr - 1][0], modal_baru, databarang[nomorr - 1][2], databarang[nomorr - 1][3])
                    databarang[nomorr - 1] = data_baru
                    
                else :
                    print(" -----------------------------------")
                    print("| Nomor yang dimasukkan tidak valid |")
                    print(" -----------------------------------")

            def ganti_harga():
                if 1 <= nomorr <= len(databarang):
                    harga_baru = int(input("Masukkan harga jual yang baru:"))
                    data_baru = (databarang[nomorr - 1][0], databarang[nomorr - 1][1], harga_baru, databarang[nomorr - 1][3])
                    databarang[nomorr - 1] = data_baru
                else:
                    print(" -----------------------------------")
                    print("| Nomor yang dimasukkan tidak valid |")
                    print(" -----------------------------------")

            def ganti_jenis():
                if 1 <= nomorr <= len(databarang):
                    jenis_baru = input("Masukkan jenis baru. Pcs/Kg:")
                    # if jenis_baru.upper() in ["PCS", "KG"]:
                    if jenis_baru in ["PCS","Pcs","pCs","pcS","PCs","pCS","PcS","pcs"]:
                        jenis_baru = "Pcs"
                        data_baru = (databarang[nomorr - 1][0], databarang[nomorr - 1][1], databarang[nomorr - 1][2], jenis_baru)
                        databarang[nomorr - 1] = data_baru
                    if jenis_baru in ["KG","kg","Kg","kG"]:
                        jenis_baru = "Kg"
                        data_baru = (databarang[nomorr - 1][0], databarang[nomorr - 1][1], databarang[nomorr - 1][2], jenis_baru)
                        databarang[nomorr - 1] = data_baru               
                    elif jenis_baru != "Pcs" and jenis_baru != "Kg":
                        print(" -----------------------------------")
                        print("| Jenis yang dimasukkan tidak valid |")
                        print(" -----------------------------------")
                else :
                    print(" -----------------------------------")
                    print("| Nomor yang dimasukkan tidak valid |")
                    print(" -----------------------------------") 

            if b == "1":
                nomorr = int(
                    input("Pilih nomor databarang yang mau diganti?: "))
                ganti_modal()
                simpenan()

            elif b == "2":
                nomorr = int(
                    input("Pilih nomor databarang yang mau diganti?: "))
                ganti_harga()
                simpenan()

            elif b == "3":
                nomorr = int(
                    input("Pilih nomor databarang yang mau diganti?: "))
                ganti_jenis()
                simpenan()

            elif b == "12":
                nomorr = int(
                    input("Pilih nomor databarang yang mau diganti?: "))
                ganti_modal()
                ganti_harga()
                simpenan()

            elif b == "123":
                nomorr = int(
                    input("Pilih nomor databarang yang mau diganti?: "))
                ganti_modal()
                ganti_harga()
                ganti_jenis()
                simpenan()

            elif b == "23":
                nomorr = int(
                    input("Pilih nomor databarang yang mau diganti?: "))
                ganti_harga()
                ganti_jenis()
                simpenan()

            elif b == "13":
                nomorr = int(
                    input("Pilih nomor databarang yang mau diganti?: "))
                ganti_modal()
                ganti_jenis()
                simpenan()

            else:
                print(" -----------------------------------")
                print("| Intruksi yang dipilih tidak valid |")
                print(" -----------------------------------")

        elif pilihan == '4':
            break
        elif pilihan == '5':
            clear_screen()
        else:
            print(" -----------------------------------")
            print("| Intruksi yang dipilih tidak valid |")
            print(" -----------------------------------")


# fungsi_barang()
