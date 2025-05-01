daftar_pengiriman = []

class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def validasi_input(self):
        if not self.asal.strip() or not self.tujuan.strip():
            raise ValueError("Asal dan tujuan tidak boleh kosong.")
        return True

    def estimasi_waktu(self):
        return 5 


class PengirimanDarat(Pengiriman):
    JENIS_KENDARAAN = ['truck', 'pickup', 'kereta']
    ESTIMASI_KENDARAAN = {'truck': 7, 'pickup': 5, 'kereta': 4}

    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan.lower()

    def validasi_input(self):
        super().validasi_input()
        if self.jenis_kendaraan not in self.JENIS_KENDARAAN:
            raise ValueError(f"Jenis kendaraan harus salah satu dari: {', '.join(self.JENIS_KENDARAAN)}")
        return True

    def estimasi_waktu(self):
        return super().estimasi_waktu() + self.ESTIMASI_KENDARAAN[self.jenis_kendaraan]


class PengirimanUdara(Pengiriman):
    MASKAPAI = ['garuda', 'lion', 'singapore airlines']
    ESTIMASI_MASKAPAI = {'garuda': 2, 'lion': 3, 'singapore airlines': 2}

    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai.lower()

    def validasi_input(self):
        super().validasi_input()
        if self.maskapai not in self.MASKAPAI:
            raise ValueError(f"Maskapai harus salah satu dari: {', '.join(self.MASKAPAI)}")
        return True

    def estimasi_waktu(self):
        return super().estimasi_waktu() + self.ESTIMASI_MASKAPAI[self.maskapai]


class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    NEGARA_INTERNASIONAL = ['singapura', 'malaysia', 'jepang', 'amerika']

    def __init__(self, asal, tujuan, jenis_kendaraan=None, maskapai=None, via_darat=True):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan.lower() if jenis_kendaraan else None
        self.maskapai = maskapai.lower() if maskapai else None
        self.via_darat = via_darat

    def validasi_input(self):
        Pengiriman.validasi_input(self)
        if self.tujuan.lower() not in [neg.lower() for neg in self.NEGARA_INTERNASIONAL] and any(neg.lower() in self.tujuan.lower() for neg in self.NEGARA_INTERNASIONAL):
            raise ValueError(f"Tujuan internasional harus salah satu dari: {', '.join(self.NEGARA_INTERNASIONAL)}")
        if self.via_darat:
            if not self.jenis_kendaraan or self.jenis_kendaraan not in PengirimanDarat.JENIS_KENDARAAN:
                raise ValueError(f"Jenis kendaraan harus salah satu dari: {', '.join(PengirimanDarat.JENIS_KENDARAAN)}")
        else:
            if not self.maskapai or self.maskapai not in PengirimanUdara.MASKAPAI:
                raise ValueError(f"Maskapai harus salah satu dari: {', '.join(PengirimanUdara.MASKAPAI)}")
        return True

    def estimasi_waktu(self):
        base = PengirimanDarat.estimasi_waktu(self) if self.via_darat else PengirimanUdara.estimasi_waktu(self)
        return base + 3 


def input_validasi(prompt, valid_opsi=None):
    while True:
        user_input = input(prompt).strip().lower()
        if not user_input:
            print("Input tidak boleh kosong.\n")
            continue
        if valid_opsi and user_input not in valid_opsi:
            print(f"Pilihan harus salah satu dari: {', '.join(valid_opsi)}\n")
            continue
        return user_input


def buat_pengiriman_internasional():
    print("\n=== Buat Pengiriman ===")

    asal = input_validasi("Masukkan kota asal: ")

    tujuan_luar_negeri = input_validasi("Apakah tujuan ke luar negeri? (y/n): ", ['y', 'n'])
    if tujuan_luar_negeri == 'y':
        print("\nDaftar Negara Tujuan Internasional:")
        for negara in PengirimanInternasional.NEGARA_INTERNASIONAL:
            print(f"- {negara.capitalize()}")

        tujuan = input_validasi("Masukkan negara tujuan: ", [negara.lower() for negara in PengirimanInternasional.NEGARA_INTERNASIONAL])
    else:
        tujuan = input_validasi("Masukkan kota tujuan: ")

    via_darat_input = input_validasi("Apakah via darat? (y/n): ", ['y', 'n'])
    via_darat = via_darat_input == 'y'

    if via_darat:
        jenis_kendaraan = input_validasi(
            f"Masukkan jenis kendaraan ({', '.join(PengirimanDarat.JENIS_KENDARAAN)}): ",
            PengirimanDarat.JENIS_KENDARAAN
        )
        maskapai = None
    else:
        maskapai = input_validasi(
            f"Masukkan maskapai ({', '.join(PengirimanUdara.MASKAPAI)}): ",
            PengirimanUdara.MASKAPAI
        )
        jenis_kendaraan = None

    pengiriman = PengirimanInternasional(
        asal=asal,
        tujuan=tujuan,
        jenis_kendaraan=jenis_kendaraan if via_darat else 'truck',
        maskapai=maskapai if not via_darat else 'garuda',
        via_darat=via_darat
    )

    pengiriman.validasi_input()
    estimasi = pengiriman.estimasi_waktu()

    print(f"\nEstimasi waktu pengiriman dari {asal.capitalize()} ke {tujuan.capitalize()}: {estimasi} hari")

    daftar_pengiriman.append({
        "asal": asal.capitalize(),
        "tujuan": tujuan.capitalize(),
        "via_darat": "Darat" if via_darat else "Udara",
        "kendaraan_maskapai": jenis_kendaraan if via_darat else maskapai,
        "estimasi_hari": estimasi
    })


def lihat_daftar_pengiriman():
    print("\n=== Daftar Semua Pengiriman ===")
    if not daftar_pengiriman:
        print("Belum ada pengiriman yang tercatat.")
        return

    print(f"{'No.':<5} {'Asal':<15} {'Tujuan':<20} {'Via':<10} {'Kendaraan/Maskapai':<20} {'Estimasi (hari)':<15}")
    print("-" * 90)
    for idx, data in enumerate(daftar_pengiriman, start=1):
        print(f"{idx:<5} {data['asal']:<15} {data['tujuan']:<20} {data['via_darat']:<10} {data['kendaraan_maskapai']:<20} {data['estimasi_hari']:<15}")

def hapus_pengiriman():
    print("\n=== Hapus Data Pengiriman ===")
    if not daftar_pengiriman:
        print("Belum ada pengiriman untuk dihapus.")
        return

    lihat_daftar_pengiriman()
    while True:
        try:
            nomor = int(input("Masukkan nomor pengiriman yang ingin dihapus: "))
            if 1 <= nomor <= len(daftar_pengiriman):
                data = daftar_pengiriman.pop(nomor - 1)
                print(f"Pengiriman dari {data['asal']} ke {data['tujuan']} berhasil dihapus.")
                break
            else:
                print("Nomor tidak valid.\n")
        except ValueError:
            print("Masukkan angka yang valid.\n")


def programutama():
    while True:
        print("\n=== Sistem Pengiriman ===")
        print("1. Buat Pengiriman Internasional")
        print("2. Lihat Daftar Semua Pengiriman")
        print("3. Hapus Data Pengiriman")
        print("4. Keluar")

        pilihan = input_validasi("Pilih menu (1-4): ", ['1', '2', '3', '4'])

        if pilihan == '1':
            buat_pengiriman_internasional()
        elif pilihan == '2':
            lihat_daftar_pengiriman()
        elif pilihan == '3':
            hapus_pengiriman()
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break

programutama()