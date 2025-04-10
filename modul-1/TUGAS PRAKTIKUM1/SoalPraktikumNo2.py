class mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        return f"Nama: {self.nama}, Nim: {self.nim}, Jurusan: {self.jurusan}, Alamat: {self.alamat}"

def validasi_input(datamhs):
    while True:
        data = input(datamhs).strip()
        if data:
            return data
        print("Input tidak boleh kosong!")

def input_data_mahasiswa():
    nama = validasi_input("Masukkan nama mahasiswa: ")
    nim = validasi_input("Masukkan NIM mahasiswa: ")
    jurusan = validasi_input("Masukkan jurusan/prodi mahasiswa: ")
    alamat = validasi_input("Masukkan alamat mahasiswa: ")
    return mahasiswa(nama, nim, jurusan, alamat)

def tambah_data():
    while True:
        jawaban = input("Apakah ingin menambahkan data mahasiswa? (ya/tidak): ").strip().lower()
        if jawaban in ["ya", "tidak"]:
            return jawaban == "ya"
        print("Pilihan tidak valid!, silakan masukkan 'ya' atau 'tidak'")

mahasisw4 = []
jumlah_data_awal = 3

for i in range(jumlah_data_awal):
    print(f"\nMasukkan data mahasiswa ke-{i+1}:")
    mhs = input_data_mahasiswa() 
    mahasisw4.append(mhs)

while True:
    if not tambah_data():
        break
    print(f"\nMasukkan data mahasiswa ke-{len(mahasisw4) + 1}:")  
    mhs = input_data_mahasiswa()
    mahasisw4.append(mhs)

print("\nInformasi Mahasiswa:")
for idx, mhs in enumerate(mahasisw4, start=1):
    print(f"Mahasiswa {idx}: {mhs.tampilkan_info()}")