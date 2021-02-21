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

def search_data():
    data = []
    with open ("gudang.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)

    cari = input ("Cari berdasarkan nama barang : ")
    kolom = [x[1] for x in data]

    if cari in kolom:
        for x in range (0, len(data)):
            if cari == data[x][1]:
                print (data[x])
    
    else:
        print ("Masukan nama barang dengan benar !")
            
    
    back_to_menu()

    

if __name__ == "__main__":
    while True:
        show_menu()
