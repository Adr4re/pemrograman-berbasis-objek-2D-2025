class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    def get_judul(self):
        return self.__judul
    
    def get_penulis(self):
        return self.__penulis
    
    def get_halaman(self):
        return self.__halaman
    
    def update_judul(self, judul_baru):
        self.__judul = judul_baru
    
    def update_penulis(self, penulis_baru):
        self.__penulis = penulis_baru
    
    def update_halaman(self, halaman_baru):
        self.__halaman = halaman_baru


class Perpustakaan:
    def __init__(self):
        self.__buku_list = []

    def tambah_buku(self, buku):
        self.__buku_list.append(buku)
        print("✅ Buku berhasil ditambahkan.")

    def tampilkan_semua_buku(self):
        if not self.__buku_list:
            print("Belum ada data buku.")
            return

        print("\n📚 DAFTAR BUKU")
        print("-" * 68)
        print(f"{'No.':<5}{'Judul':<32}{'Penulis':<22}{'Halaman':<7}")
        print("-" * 68)
        
        for i, buku in enumerate(self.__buku_list, 1):
            judul = buku.get_judul()[:29] + "..." if len(buku.get_judul()) > 32 else buku.get_judul()
            penulis = buku.get_penulis()[:19] + "..." if len(buku.get_penulis()) > 22 else buku.get_penulis()
            print(f"{i:<5}{judul:<32}{penulis:<22}{buku.get_halaman():<7}")
        
        print("-" * 68)
        print(f"Total buku: {len(self.__buku_list)}")

    def cari_buku(self, keyword):
        hasil = []
        for buku in self.__buku_list:
            if (keyword.lower() in buku.get_judul().lower() or 
                keyword.lower() in buku.get_penulis().lower()):
                hasil.append(buku)
        
        if hasil:
            print(f"\nDitemukan {len(hasil)} buku:")
            print("-" * 68)
            print(f"{'No.':<5}{'Judul':<32}{'Penulis':<22}{'Halaman':<7}")
            print("-" * 68)
            for i, buku in enumerate(hasil, 1):
                judul = buku.get_judul()[:29] + "..." if len(buku.get_judul()) > 32 else buku.get_judul()
                penulis = buku.get_penulis()[:19] + "..." if len(buku.get_penulis()) > 22 else buku.get_penulis()
                print(f"{i:<5}{judul:<32}{penulis:<22}{buku.get_halaman():<7}")
            print("-" * 68)
            return hasil
        else:
            print("❌ Tidak ditemukan buku dengan kata kunci tersebut.")
            return None

    def hapus_buku(self, judul):
        for i, buku in enumerate(self.__buku_list):
            if buku.get_judul().lower() == judul.lower():
                del self.__buku_list[i]
                print("✅ Buku berhasil dihapus.")
                return True
        print("❌ Buku tidak ditemukan.")
        return False

    def update_buku(self, judul_lama):
        buku_ditemukan = None
        index = -1

        for i, buku in enumerate(self.__buku_list):
            if buku.get_judul().lower() == judul_lama.lower():
                buku_ditemukan = buku
                index = i
                break
        
        if buku_ditemukan is None:
            print("❌ Buku tidak ditemukan.")
            return False
        
        print("\nData buku yang akan diupdate:")
        print("-" * 40)
        print(f"1. Judul: {buku_ditemukan.get_judul()}")
        print(f"2. Penulis: {buku_ditemukan.get_penulis()}")
        print(f"3. Halaman: {buku_ditemukan.get_halaman()}")
        print("-" * 40)
        
        while True:
            try:
                field = input_validasi_angka_positif(
                    "Pilih data yang akan diupdate (1-3) atau 0 untuk batal: ")
                
                if field == 0:
                    print("Pembaruan data dibatalkan.")
                    return False
                
                if field == 1:
                    nilai_baru = input_validasi_alfabet("Masukkan judul baru: ")
                    buku_ditemukan.update_judul(nilai_baru)
                elif field == 2:
                    nilai_baru = input_validasi_alfabet("Masukkan penulis baru: ")
                    buku_ditemukan.update_penulis(nilai_baru)
                elif field == 3:
                    nilai_baru = input_validasi_angka_positif("Masukkan jumlah halaman baru: ")
                    buku_ditemukan.update_halaman(nilai_baru)
                else:
                    print("❌ Pilihan tidak valid. Harap masukkan angka 0-3.")
                    continue
                
                self.__buku_list[index] = buku_ditemukan
                print("✅ Data buku berhasil diperbarui.")
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
        return int(angka)


def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n===== MENU PERPUSTAKAAN =====")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Cari Buku")
        print("4. Update Data Buku")
        print("5. Hapus Buku")
        print("6. Keluar")

        pilihan = input_validasi_angka_positif("Pilih menu (1-6): ")

        if pilihan == 1:
            print("\n📝 Tambah Buku")
            judul = input_validasi_alfabet("Judul Buku: ")
            penulis = input_validasi_alfabet("Nama Penulis: ")
            halaman = input_validasi_angka_positif("Jumlah Halaman: ")

            buku = Buku(judul, penulis, halaman)
            perpustakaan.tambah_buku(buku)

        elif pilihan == 2:
            perpustakaan.tampilkan_semua_buku()

        elif pilihan == 3:
            keyword = input_validasi_alfabet("Masukkan judul/penulis: ")
            perpustakaan.cari_buku(keyword)

        elif pilihan == 4:
            print("\nUpdate Data Buku")
            perpustakaan.tampilkan_semua_buku()
            judul = input_validasi_alfabet("Judul buku yang akan diupdate: ")
            perpustakaan.update_buku(judul)

        elif pilihan == 5:
            print("\n❌ Hapus Buku")
            perpustakaan.tampilkan_semua_buku()
            judul = input_validasi_alfabet("Judul buku yang akan dihapus: ")
            perpustakaan.hapus_buku(judul)

        elif pilihan == 6:
            print("Terima kasih!")
            break

        else:
            print("❌ Pilihan harus antara 1-6")

main()