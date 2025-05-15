class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo=0):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    def setor(self, jumlah):
        self.__saldo += jumlah
        print(f"✅ Setor sebesar Rp {jumlah:,.2f} berhasil.")
        return True

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"✅ Penarikan sebesar Rp {jumlah:,.2f} berhasil.")
            return True
        else:
            print("❌ Saldo tidak mencukupi.")
            return False

    def get_info(self):
        return f"No Rekening: {self.__no_rek}, Nama: {self.__nama_pemilik}, Saldo: Rp {self.__saldo:,.2f}"

    def get_no_rek(self):
        return self.__no_rek


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)

    def cari_rekening(self, no_rek):
        for rekening in self.rekening_list:
            if rekening.get_no_rek() == no_rek:
                return rekening
        return None

    def setor_uang(self, no_rek, jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            return rekening.setor(jumlah)
        else:
            print("❌ Rekening tidak ditemukan.")
            return False

    def tarik_uang(self, no_rek, jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            return rekening.tarik(jumlah)
        else:
            print("❌ Rekening tidak ditemukan.")
            return False

    def tampilkan_semua_rekening(self):
        if not self.rekening_list:
            print("Belum ada data rekening.")
        else:
            print("\nDaftar Semua Rekening:")
            for r in self.rekening_list:
                print(r.get_info())


def input_validasi_no_rek(prompt):
    while True:
        nilai = input(prompt).strip()
        if not nilai:
            print("Input tidak boleh kosong.\n")
            continue
        if not nilai.isdigit():
            print("No rekening harus berupa angka.\n")
            continue
        if len(nilai) < 10:
            print("No rekening minimal 10 digit.\n")
            continue
        return nilai

def input_validasi_angka(prompt):
    while True:
        nilai = input(prompt).strip()
        if not nilai:
            print("Input tidak boleh kosong.\n")
            continue
        try:
            return float(nilai)
        except ValueError:
            print("Input harus berupa angka.\n")

def input_validasi_alfabet(prompt):
    while True:
        teks = input(prompt).strip()
        if not teks:
            print("Input tidak boleh kosong.\n")
            continue
        if not teks.replace(" ", "").isalpha():
            print("Input hanya boleh huruf dan spasi.\n")
            continue
        return teks

def konfirmasi_ya_tidak(prompt):
    while True:
        konfirmasi = input(prompt).strip().lower()
        if konfirmasi in ['y', 'n']:
            return konfirmasi == 'y'
        print("❌ Pilih hanya 'y' (ya) atau 'n' (tidak).")


def main():
    bank = Bank()

    while True:
        print("\n===== MENU BANK =====")
        print("1. Tambah Rekening")
        print("2. Setor Uang")
        print("3. Tarik Uang")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            print("\n🔹 Tambah Rekening Baru 🔹")
            no_rek = input_validasi_no_rek("Masukkan No Rekening (min 10 digit): ")
            if bank.cari_rekening(no_rek):
                print("❌ Rekening sudah ada.")
                continue

            nama = input_validasi_alfabet("Masukkan Nama Pemilik: ")
            saldo_awal = input_validasi_angka("Masukkan Saldo Awal: ")

            rekening = RekeningBank(no_rek, nama, saldo_awal)
            bank.tambah_rekening(rekening)
            print("✅ Rekening berhasil ditambahkan.")

        elif pilihan == "2":
            print("\n- Setor Uang -")
            no_rek = input_validasi_no_rek("Masukkan No Rekening: ")
            jumlah = input_validasi_angka("Masukkan Jumlah Setoran: ")

            if bank.cari_rekening(no_rek):
                if konfirmasi_ya_tidak(f"Apakah Anda yakin ingin menyetor Rp {jumlah:,.2f} ke rekening {no_rek}? (y/n): "):
                    bank.setor_uang(no_rek, jumlah)
                else:
                    print("❎ Setoran dibatalkan.")
            else:
                print("❌ Rekening tidak ditemukan.")

        elif pilihan == "3":
            print("\n- Tarik Uang -")
            no_rek = input_validasi_no_rek("Masukkan No Rekening: ")
            jumlah = input_validasi_angka("Masukkan Jumlah Penarikan: ")

            if bank.cari_rekening(no_rek):
                if konfirmasi_ya_tidak(f"Apakah Anda yakin ingin menarik Rp {jumlah:,.2f} dari rekening {no_rek}? (y/n): "):
                    bank.tarik_uang(no_rek, jumlah)
                else:
                    print("❎ Penarikan dibatalkan.")
            else:
                print("❌ Rekening tidak ditemukan.")

        elif pilihan == "4":
            bank.tampilkan_semua_rekening()

        elif pilihan == "5":
            print("👋 Terima kasih telah menggunakan sistem bank.")
            break

        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.\n")

main()