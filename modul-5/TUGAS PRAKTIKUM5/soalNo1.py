from abc import ABC, abstractmethod

class Manusia(ABC):
    @abstractmethod
    def berbicara(self):
        pass
    
    @abstractmethod
    def bekerja(self):
        pass
    
    @abstractmethod
    def makan(self):
        pass

class ManusiaBiasa(Manusia):
    def __init__(self, nama, cara_berbicara, pekerjaan, makanan_favorit):
        self.nama = nama
        self.cara_berbicara = cara_berbicara
        self.pekerjaan = pekerjaan
        self.makanan_favorit = makanan_favorit
    
    def berbicara(self):
        return f"{self.nama} berbicara dengan {self.cara_berbicara}"
    
    def bekerja(self):
        return f"{self.nama} bekerja sebagai {self.pekerjaan}"
    
    def makan(self):
        return f"{self.nama} suka makan {self.makanan_favorit}"

def input_validasi_alfabet(prompt):
    while True:
        teks = input(prompt).strip()
        if not teks:
            print("❌ Input tidak boleh kosong.")
            continue
        if not teks.replace(" ", "").isalpha():
            print("❌ Input hanya boleh huruf dan spasi.")
            continue
        return teks

def input_validasi_angka_positif(prompt):
    while True:
        angka = input(prompt).strip()
        if not angka:
            print("❌ Input tidak boleh kosong.")
            continue
        if not angka.isdigit():
            print("❌ Input harus berupa angka positif.")
            continue
        angka = int(angka)
        if angka <= 0:
            print("❌ Nilai harus lebih dari 0.")
            continue
        return angka

class AplikasiManusia:
    def __init__(self):
        self.daftar_manusia = []
    
    def tambah_manusia(self):
        print("\n=== Tambah Manusia ===")
        nama = input_validasi_alfabet("Masukkan nama: ")
        cara_berbicara = input_validasi_alfabet("Masukkan cara berbicara (contoh: nada tinggi, pelan, logat Jawa): ")
        pekerjaan = input_validasi_alfabet("Masukkan pekerjaan: ")
        makanan_favorit = input_validasi_alfabet("Masukkan makanan favorit: ")
        
        manusia_baru = ManusiaBiasa(nama, cara_berbicara, pekerjaan, makanan_favorit)
        self.daftar_manusia.append(manusia_baru)
        print(f"✅ {nama} berhasil ditambahkan!")
    
    def lihat_semua(self):
        print("\n=== Daftar Semua Manusia ===")
        if not self.daftar_manusia:
            print("❌ Tidak ada data manusia.")
            return
        
        for idx, manusia in enumerate(self.daftar_manusia, 1):
            print(f"{idx}. Nama: {manusia.nama}")
            print(f"   - Berbicara: {manusia.berbicara()}")
            print(f"   - Bekerja: {manusia.bekerja()}")
            print(f"   - Makan: {manusia.makan()}")
            print()
    
    def cari_manusia(self):
        print("\n=== Cari Manusia ===")
        if not self.daftar_manusia:
            print("❌ Tidak ada data manusia.")
            return
        
        nama_cari = input_validasi_alfabet("Masukkan nama yang dicari: ")
        ditemukan = False
        
        for manusia in self.daftar_manusia:
            if nama_cari.lower() in manusia.nama.lower():
                print("\n🔍 Hasil Pencarian:")
                print(f"Nama: {manusia.nama}")
                print(f"- Berbicara: {manusia.berbicara()}")
                print(f"- Bekerja: {manusia.bekerja()}")
                print(f"- Makan: {manusia.makan()}")
                ditemukan = True
        
        if not ditemukan:
            print("❌ Tidak ditemukan manusia dengan nama tersebut.")
    
    def update_manusia(self):
        print("\n=== Update Data Manusia ===")
        if not self.daftar_manusia:
            print("❌ Tidak ada data manusia.")
            return
        
        self.lihat_semua()
        try:
            idx = input_validasi_angka_positif("Pilih nomor manusia yang akan diupdate: ") - 1
            if idx < 0 or idx >= len(self.daftar_manusia):
                print("❌ Nomor tidak valid!")
                return
        except ValueError:
            print("❌ Input harus berupa angka!")
            return
        
        manusia = self.daftar_manusia[idx]
        print(f"\nData saat ini untuk {manusia.nama}:")
        print(f"1. Nama: {manusia.nama}")
        print(f"2. Cara Berbicara: {manusia.cara_berbicara}")
        print(f"3. Pekerjaan: {manusia.pekerjaan}")
        print(f"4. Makanan Favorit: {manusia.makanan_favorit}")
        
        print("\nMasukkan data baru:")
        nama_baru = input_validasi_alfabet(f"Masukkan nama baru ({manusia.nama}): ") or manusia.nama
        cara_berbicara_baru = input_validasi_alfabet(f"Masukkan cara berbicara baru ({manusia.cara_berbicara}): ") or manusia.cara_berbicara
        pekerjaan_baru = input_validasi_alfabet(f"Masukkan pekerjaan baru ({manusia.pekerjaan}): ") or manusia.pekerjaan
        makanan_favorit_baru = input_validasi_alfabet(f"Masukkan makanan favorit baru ({manusia.makanan_favorit}): ") or manusia.makanan_favorit
        
        data_lama = {
            'nama': manusia.nama,
            'cara_berbicara': manusia.cara_berbicara,
            'pekerjaan': manusia.pekerjaan,
            'makanan_favorit': manusia.makanan_favorit
        }
        
        self.daftar_manusia[idx] = ManusiaBiasa(nama_baru, cara_berbicara_baru, pekerjaan_baru, makanan_favorit_baru)
        
        print("\n✅ Data berhasil diupdate!")
        print("\nPerubahan yang dilakukan:")
        print(f"Nama: {data_lama['nama']} → {nama_baru}")
        print(f"Cara Berbicara: {data_lama['cara_berbicara']} → {cara_berbicara_baru}")
        print(f"Pekerjaan: {data_lama['pekerjaan']} → {pekerjaan_baru}")
        print(f"Makanan Favorit: {data_lama['makanan_favorit']} → {makanan_favorit_baru}")
    
    def hapus_manusia(self):
        print("\n=== Hapus Data Manusia ===")
        if not self.daftar_manusia:
            print("❌ Tidak ada data manusia.")
            return
        
        self.lihat_semua()
        try:
            idx = input_validasi_angka_positif("Pilih nomor manusia yang akan dihapus: ") - 1
            if idx < 0 or idx >= len(self.daftar_manusia):
                print("❌ Nomor tidak valid!")
                return
        except ValueError:
            print("❌ Input harus berupa angka!")
            return
        
        nama = self.daftar_manusia[idx].nama
        del self.daftar_manusia[idx]
        print(f"✅ {nama} berhasil dihapus!")
    
    def tampilkan_menu(self):
        print("\n=== APLIKASI MANUSIA ===")
        print("1. Tambah Manusia")
        print("2. Lihat Semua Manusia")
        print("3. Cari Manusia")
        print("4. Update Data Manusia")
        print("5. Hapus Data Manusia")
        print("0. Keluar")

def main():
    app = AplikasiManusia()
    
    while True:
        app.tampilkan_menu()
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            app.tambah_manusia()
        elif pilihan == "2":
            app.lihat_semua()
        elif pilihan == "3":
            app.cari_manusia()
        elif pilihan == "4":
            app.update_manusia()
        elif pilihan == "5":
            app.hapus_manusia()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("❌ Pilihan tidak valid!")

main()