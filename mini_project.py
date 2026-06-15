import os
# ================= MEMBERSIHKAN TERMINAL =================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 40)
print("Nama : Indira Suci Fitriani")
print("NIM  : 552010125006")
print("=" * 40)

# fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== SISTEM NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")

# Fungsi untuk menambahkan data
def tambah_data(data):
    nim = input("Masukkan NIM: ")
    try:
        nilai = float(input("Masukkan nilai: "))
        data[nim] = nilai
        print("Data berhasil ditambahkan.")
    except ValueError:
        print("Nilai harus berupa angka.")

# Fungsi untuk menampilkan data
def tampilkan_data(data):
    if not data:
        print("Data kosong.")
    else:
        for nim, nilai in data.items():
            print(f"{nim} : {nilai}")

# Fungsi untuk menghapus data berdasarkan NIM
def hapus_data(data):
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in data:
        del data[nim]
        print("Data berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")

# PROGRAM UTAMA
def main():
    data = {}

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data(data)
        elif pilihan == "2":
            tampilkan_data(data)
        elif pilihan == "3":
            hapus_data(data)
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
main()