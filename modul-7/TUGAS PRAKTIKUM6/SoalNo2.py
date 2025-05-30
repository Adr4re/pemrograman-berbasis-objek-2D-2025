from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama):
        self.nama = nama
    
    @abstractmethod
    def hitung_gaji(self):
        pass
    
    def tampilkan_gaji(self):
        print(f"Gaji {self.__class__.__name__} {self.nama}: Rp {self.hitung_gaji():,.2f}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan
    
    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, upah_per_jam, jam_kerja):
        super().__init__(nama)
        self.upah_per_jam = upah_per_jam
        self.jam_kerja = jam_kerja
    
    def hitung_gaji(self):
        return self.upah_per_jam * self.jam_kerja

def input_angka_positif(prompt, default=None):
    while True:
        try:
            angka = input(prompt)
            if not angka and default is not None:
                return default
            angka = float(angka)
            if angka <= 0:
                print("❌ Masukkan harus lebih besar dari 0")
                continue
            return angka
        except ValueError:
            print("❌ Masukkan harus berupa angka")

def input_teks(prompt, default=None):
    while True:
        teks = input(prompt).strip()
        if not teks and default is not None:
            return default
        if not teks:
            print("❌ Input tidak boleh kosong")
            continue
        if not teks.replace(" ", "").isalpha():
            print("❌ Input hanya boleh berisi huruf")
            continue
        return teks

def tampilkan_daftar(daftar_karyawan):
    if not daftar_karyawan:
        print("Belum ada data karyawan")
        return False
    print("\nDaftar Karyawan:")
    for i, karyawan in enumerate(daftar_karyawan, 1):
        print(f"{i}. {karyawan.nama} ({karyawan.__class__.__name__})")
    return True

def main():
    print("=== PROGRAM HITUNG GAJI KARYAWAN ===")
    daftar_karyawan = []
    
    while True:
        print("\nMenu:")
        print("1. Tambah Karyawan Tetap")
        print("2. Tambah Karyawan Kontrak")
        print("3. Lihat Daftar Karyawan")
        print("4. Update Data Karyawan")
        print("5. Hapus Karyawan")
        print("0. Keluar")
        
        pilihan = input("Pilih menu (0-5): ")
        
        if pilihan == "1":
            print("\nTambah Karyawan Tetap")
            nama = input_teks("Nama karyawan: ")
            gaji_pokok = input_angka_positif("Gaji pokok: Rp ")
            tunjangan = input_angka_positif("Tunjangan: Rp ")
            
            daftar_karyawan.append(KaryawanTetap(nama, gaji_pokok, tunjangan))
            print(f"✅ {nama} berhasil ditambahkan sebagai karyawan tetap")
            
        elif pilihan == "2":
            print("\nTambah Karyawan Kontrak")
            nama = input_teks("Nama karyawan: ")
            upah_per_jam = input_angka_positif("Upah per jam: Rp ")
            jam_kerja = input_angka_positif("Total jam kerja: ")
            
            daftar_karyawan.append(KaryawanKontrak(nama, upah_per_jam, jam_kerja))
            print(f"✅ {nama} berhasil ditambahkan sebagai karyawan kontrak")
            
        elif pilihan == "3":
            print("\nDaftar Karyawan:")
            if not daftar_karyawan:
                print("Belum ada data karyawan")
                continue
                
            for i, karyawan in enumerate(daftar_karyawan, 1):
                print(f"{i}. {karyawan.nama} ({karyawan.__class__.__name__})")
                karyawan.tampilkan_gaji()
                print()
                
        elif pilihan == "4":
            if not tampilkan_daftar(daftar_karyawan):
                continue
                
            try:
                index = int(input("Pilih nomor karyawan yang akan diupdate: ")) - 1
                if index < 0 or index >= len(daftar_karyawan):
                    print("❌ Nomor tidak valid")
                    continue
                    
                karyawan = daftar_karyawan[index]
                print(f"\nUpdate data {karyawan.nama} ({karyawan.__class__.__name__})")
                
                if isinstance(karyawan, KaryawanTetap):
                    nama = input_teks(f"Nama ({karyawan.nama}): ", karyawan.nama)
                    gaji_pokok = input_angka_positif(f"Gaji pokok (Rp {karyawan.gaji_pokok:,.2f}): ", karyawan.gaji_pokok)
                    tunjangan = input_angka_positif(f"Tunjangan (Rp {karyawan.tunjangan:,.2f}): ", karyawan.tunjangan)
                    daftar_karyawan[index] = KaryawanTetap(nama, gaji_pokok, tunjangan)
                else:
                    nama = input_teks(f"Nama ({karyawan.nama}): ", karyawan.nama)
                    upah_per_jam = input_angka_positif(f"Upah per jam (Rp {karyawan.upah_per_jam:,.2f}): ", karyawan.upah_per_jam)
                    jam_kerja = input_angka_positif(f"Jam kerja ({karyawan.jam_kerja}): ", karyawan.jam_kerja)
                    daftar_karyawan[index] = KaryawanKontrak(nama, upah_per_jam, jam_kerja)
                    
                print("✅ Data berhasil diupdate")
                
            except ValueError:
                print("❌ Input harus berupa angka")
                
        elif pilihan == "5":
            if not tampilkan_daftar(daftar_karyawan):
                continue
                
            try:
                index = int(input("Pilih nomor karyawan yang akan dihapus: ")) - 1
                if index < 0 or index >= len(daftar_karyawan):
                    print("❌ Nomor tidak valid")
                    continue
                    
                nama = daftar_karyawan[index].nama
                daftar_karyawan.pop(index)
                print(f"✅ {nama} berhasil dihapus")
                
            except ValueError:
                print("❌ Input harus berupa angka")
                
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program!")
            break
            
        else:
            print("❌ Pilihan tidak valid!")

main()