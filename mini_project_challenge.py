import os
# ================= MEMBERSIHKAN TERMINAL =================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 40)
print("Nama : Indira Suci Fitriani")
print("NIM  : 552010125006")
print("=" * 40)


# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("\n=== SISTEM NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Cari Data")
    print("5. Hitung Rata-rata")
    print("6. Keluar")


# Fungsi untuk menambahkan data mahasiswa
def tambah_data(data):
    # Meminta input NIM
    nim = input("Masukkan NIM: ")

    # Mengecek apakah NIM sudah ada
    if nim in data:
        print("NIM sudah terdaftar!")
        return

    try:
        # Meminta input nilai dan mengubah ke tipe float
        nilai = float(input("Masukkan nilai: "))

        # Menyimpan data ke dictionary
        data[nim] = nilai

        print("Data berhasil ditambahkan.")

    except ValueError:
        # Jika input nilai bukan angka
        print("Nilai harus berupa angka.")


# Fungsi untuk menampilkan seluruh data mahasiswa
def tampilkan_data(data):

    # Mengecek apakah dictionary kosong
    if not data:
        print("Data kosong.")
    else:
        print("\nDaftar Nilai Mahasiswa")

        # Menampilkan setiap pasangan NIM dan nilai
        for nim, nilai in data.items():
            print(f"{nim} : {nilai}")


# Fungsi untuk menghapus data berdasarkan NIM
def hapus_data(data):

    # Meminta NIM yang akan dihapus
    nim = input("Masukkan NIM yang akan dihapus: ")

    # Mengecek apakah NIM ada dalam dictionary
    if nim in data:

        # Menghapus data
        del data[nim]

        print("Data berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")


# Fungsi untuk mencari data mahasiswa berdasarkan NIM
def cari_data(data):

    # Meminta NIM yang dicari
    nim = input("Masukkan NIM yang dicari: ")

    # Mengecek apakah NIM tersedia
    if nim in data:

        # Menampilkan data yang ditemukan
        print(f"NIM   : {nim}")
        print(f"Nilai : {data[nim]}")

    else:
        print("NIM tidak ditemukan.")


# Fungsi untuk menghitung rata-rata nilai mahasiswa
def hitung_rata_rata(data):

    # Mengecek apakah ada data
    if not data:
        print("Data kosong.")
    else:

        # Menjumlahkan seluruh nilai lalu dibagi jumlah mahasiswa
        rata_rata = sum(data.values()) / len(data)

        # Menampilkan hasil rata-rata dengan 2 angka di belakang koma
        print(f"Rata-rata nilai mahasiswa = {rata_rata:.2f}")


# Fungsi utama program
def main():

    # Dictionary untuk menyimpan data mahasiswa
    data = {}

    # Perulangan menu hingga pengguna memilih keluar
    while True:

        # Menampilkan menu
        tampilkan_menu()

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_data(data)
        elif pilihan == "2":
            tampilkan_data(data)
        elif pilihan == "3":
            hapus_data(data)
        elif pilihan == "4":
            cari_data(data)
        elif pilihan == "5":
            hitung_rata_rata(data)
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

# Menjalankan program utama
main()