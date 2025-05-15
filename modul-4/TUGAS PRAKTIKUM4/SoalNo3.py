class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_nama(self):
        return self.__nama
    
    def get_umur(self):
        return self.__umur
    
    def get_keluhan(self):
        return self.__keluhan


    def update_nama(self, nama_baru):
        self.__nama = nama_baru
    
    def update_umur(self, umur_baru):
        self.__umur = umur_baru
    
    def update_keluhan(self, keluhan_baru):
        self.__keluhan = keluhan_baru


class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.__daftar_pasien.append(pasien)
        print("✅ Data pasien berhasil ditambahkan.")

    def tampilkan_semua_pasien(self):
        if not self.__daftar_pasien:
            print("📭 Belum ada data pasien.")
            return

        print("\n📋 DAFTAR PASIEN")
        print("-" * 72)
        print(f"{'No.':<5}{'Nama':<25}{'Umur':<10}{'Keluhan':<32}")
        print("-" * 72)
        
        for i, pasien in enumerate(self.__daftar_pasien, 1):
            nama = pasien.get_nama()[:22] + "..." if len(pasien.get_nama()) > 25 else pasien.get_nama()
            keluhan = pasien.get_keluhan()[:29] + "..." if len(pasien.get_keluhan()) > 32 else pasien.get_keluhan()
            print(f"{i:<5}{nama:<25}{pasien.get_umur():<10}{keluhan:<32}")
        
        print("-" * 72)
        print(f"Total pasien: {len(self.__daftar_pasien)}")

    def cari_pasien(self, keyword):
        hasil = []
        for pasien in self.__daftar_pasien:
            if (keyword.lower() in pasien.get_nama().lower() or 
                keyword.lower() in pasien.get_keluhan().lower()):
                hasil.append(pasien)
        
        if hasil:
            print(f"\nDitemukan {len(hasil)} pasien:")
            print("-" * 72)
            print(f"{'No.':<5}{'Nama':<25}{'Umur':<10}{'Keluhan':<32}")
            print("-" * 72)
            for i, pasien in enumerate(hasil, 1):
                nama = pasien.get_nama()[:22] + "..." if len(pasien.get_nama()) > 25 else pasien.get_nama()
                keluhan = pasien.get_keluhan()[:29] + "..." if len(pasien.get_keluhan()) > 32 else pasien.get_keluhan()
                print(f"{i:<5}{nama:<25}{pasien.get_umur():<10}{keluhan:<32}")
            print("-" * 72)
            return hasil
        else:
            print("❌ Tidak ditemukan pasien dengan kata kunci tersebut.")
            return None

    def hapus_pasien(self, nama):
        for i, pasien in enumerate(self.__daftar_pasien):
            if pasien.get_nama().lower() == nama.lower():
                del self.__daftar_pasien[i]
                print("✅ Data pasien berhasil dihapus.")
                return True
        print("❌ Pasien tidak ditemukan.")
        return False

    def update_pasien(self, nama_lama):
        pasien_ditemukan = None
        index = -1

        for i, pasien in enumerate(self.__daftar_pasien):
            if pasien.get_nama().lower() == nama_lama.lower():
                pasien_ditemukan = pasien
                index = i
                break
        
        if pasien_ditemukan is None:
            print("❌ Pasien tidak ditemukan.")
            return False
        
        print("\nData pasien yang akan diupdate:")
        print("-" * 40)
        print(f"1. Nama: {pasien_ditemukan.get_nama()}")
        print(f"2. Umur: {pasien_ditemukan.get_umur()}")
        print(f"3. Keluhan: {pasien_ditemukan.get_keluhan()}")
        print("-" * 40)
        
        while True:
            try:
                field = input_validasi_angka_positif(
                    "Pilih data yang akan diupdate (1-3) atau 0 untuk batal: ")
                
                if field == 0:
                    print("Pembaruan data dibatalkan.")
                    return False
                
                if field == 1:
                    nilai_baru = input_validasi_alfabet("Masukkan nama baru: ")
                    pasien_ditemukan.update_nama(nilai_baru)
                elif field == 2:
                    nilai_baru = input_validasi_angka_positif("Masukkan umur baru: ")
                    pasien_ditemukan.update_umur(nilai_baru)
                elif field == 3:
                    nilai_baru = input_validasi_alfabet("Masukkan keluhan baru: ")
                    pasien_ditemukan.update_keluhan(nilai_baru)
                else:
                    print("❌ Pilihan tidak valid. Harap masukkan angka 0-3.")
                    continue
                
                self.__daftar_pasien[index] = pasien_ditemukan
                print("✅ Data pasien berhasil diperbarui.")
                return True
                
            except Exception as e:
                print(f"❌ Terjadi kesalahan: {str(e)}")


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


def main():
    klinik = Klinik()

    while True:
        print("\n===== MENU KLINIK =====")
        print("1. Tambah Data Pasien")
        print("2. Tampilkan Semua Pasien")
        print("3. Cari Pasien")
        print("4. Update Data Pasien")
        print("5. Hapus Data Pasien")
        print("6. Keluar")

        pilihan = input_validasi_angka_positif("Pilih menu (1-6): ")

        if pilihan == 1:
            print("\n📝 Tambah Pasien Baru")
            nama = input_validasi_alfabet("Nama Pasien: ")
            umur = input_validasi_angka_positif("Umur Pasien: ")
            keluhan = input_validasi_alfabet("Keluhan: ")

            pasien = Pasien(nama, umur, keluhan)
            klinik.tambah_pasien(pasien)

        elif pilihan == 2:
            klinik.tampilkan_semua_pasien()

        elif pilihan == 3:
            keyword = input_validasi_alfabet("Masukkan nama/keluhan: ")
            klinik.cari_pasien(keyword)

        elif pilihan == 4:
            print("\nUpdate Data Pasien")
            klinik.tampilkan_semua_pasien()
            nama = input_validasi_alfabet("Nama pasien yang akan diupdate: ")
            klinik.update_pasien(nama)

        elif pilihan == 5:
            print("\n❌ Hapus Data Pasien")
            klinik.tampilkan_semua_pasien()
            nama = input_validasi_alfabet("Nama pasien yang akan dihapus: ")
            klinik.hapus_pasien(nama)

        elif pilihan == 6:
            print("Terima kasih telah menggunakan sistem klinik.")
            break

        else:
            print("❌ Pilihan harus antara 1-6")

main()