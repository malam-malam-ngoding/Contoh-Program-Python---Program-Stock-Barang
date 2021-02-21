import csv
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("==== APLIKASI STOCK BARANG PT.MAJU MUNDUR ====")
    print("[1] Lihat Daftar Barang")
    print("[2] Tambah Data Barang")
    print("[3] Edit Data Barang")
    print("[4] Hapus Data Barang")
    print("[5] Cari Data Barang")
    print("[0] Exit")
    print("------------------------")
    pilih_menu = input("Silahkan Pilih Program yang Ingin dijalankan :  ")
    
    if(pilih_menu == "1"):
        show_data()
    elif(pilih_menu == "2"):
        create_data()
    elif(pilih_menu == "3"):
        edit_data()
    elif(pilih_menu == "4"):
        delete_data()
    elif(pilih_menu == "5"):
        search_data()
    elif(pilih_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah! Silahkan Pilih Program yang Benar !")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_data():
    clear_screen()
    data = []
    with open("gudang.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            data.append(row)

    if (len(data) > 0):
        labels = data.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]} \t {labels[3]}")
        print("-"*50)
        for barang in data:
            print(f'{barang[0]} \t {barang[1]} \t\t {barang[2]} \t {barang[3]}')
    else:
        print("Barang Tidak Ditemukan !")
    back_to_menu()



if __name__ == "__main__":
    while True:
        show_menu()
