class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen
    
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: Rp{self.gaji:,.2f}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan
    
    def info(self):
        super().info()
        print(f"Tunjangan: Rp{self.tunjangan:,.2f}")
        print("Status: Karyawan Tetap")
        print("-" * 40)

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja
    
    def info(self):
        super().info()
        print(f"Jam Kerja: {self.jam_kerja} jam/hari")
        print("Status: Karyawan Harian")
        print("-" * 40)

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []
    
    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)
        print(f"Karyawan {karyawan.nama} berhasil ditambahkan!\n")
    
    def tampilkan_semua_karyawan(self):
        if not self.daftar_karyawan:
            print("Belum ada karyawan yang terdaftar.\n")
            return
        
        print("\nDaftar Semua Karyawan:")
        print("=" * 40)
        for idx, karyawan in enumerate(self.daftar_karyawan, 1):
            print(f"Karyawan #{idx}")
            karyawan.info()

def input_valid(prompt, tipe='text'):
    while True:
        try:
            data = input(prompt).strip()
            if not data:
                raise ValueError("Input tidak boleh kosong")
            
            if tipe == 'angka':
                data = float(data)
                if data < 0:
                    raise ValueError("Input harus bilangan positif")
            return data
        except ValueError as e:
            print(f"Error: {e}. Silakan coba lagi.")

def input_valid_huruf(prompt, tipe='text'):
    while True:
        try:
            data = input(prompt).strip()
            if not data:
                raise ValueError("Input tidak boleh kosong")
            if not data.isalpha():
                raise ValueError("Input hanya boleh berupa huruf (alfabet)")
            return data
        except ValueError as e:
            print(f"Error: {e}. Silakan coba lagi.")


sistem = ManajemenKaryawan()


while True:
    print("\nSistem Manajemen Karyawan")
    print("1. Tambah Karyawan Tetap")
    print("2. Tambah Karyawan Harian")
    print("3. Lihat Daftar Karyawan")
    print("4. Keluar")
    
    pilihan = input_valid("Pilih menu (1-4): ")
    
    if pilihan == "1":
        print("\n[ Tambah Karyawan Tetap ]")
        nama = input_valid("Nama karyawan: ")
        gaji = input_valid("Gaji pokok: ", 'angka')
        departemen = input_valid_huruf("Departemen: ")
        tunjangan = input_valid("Tunjangan: ", 'angka')
        
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
        sistem.tambah_karyawan(karyawan)
    
    elif pilihan == "2":
        print("\n[ Tambah Karyawan Harian ]")
        nama = input_valid("Nama karyawan: ")
        gaji = input_valid("Gaji per hari: ", 'angka')
        departemen = input_valid_huruf("Departemen: ")
        jam_kerja = input_valid("Jam kerja per hari: ", 'angka')
        
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
        sistem.tambah_karyawan(karyawan)
    
    elif pilihan == "3":
        sistem.tampilkan_semua_karyawan()
    
    elif pilihan == "4":
        print("Terima kasih telah menggunakan sistem ini.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")