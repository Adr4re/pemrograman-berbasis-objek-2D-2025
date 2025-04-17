class Mahasiswa:
  jumlah_mahasiswa = 0

  def __init__(self, nama, nim, prodi):
    if not self.cek_nim_valid(nim):
      raise ValueError("NIM tidak valid harus dimulai dengan '23' dan '10' digit")
    self.nama = nama
    self.nim = nim
    self.prodi = prodi
    self.daftar_matkul = []
    Mahasiswa.jumlah_mahasiswa += 1

  @staticmethod
  def cek_nim_valid(nim):
    return isinstance(nim, str) and nim.startswith("23") and len (nim) == 10 and nim.isdigit()
  

  
  def tambah_matkul(self, matkul):
    if len(self.daftar_matkul) >= 4:
      print(f"peringatan: {self.nama} sudah mengambil 4 mata kuliah.  Mata kuliah {matkul.nama} tetap ditambahkan")
    self.daftar_matkul.append(matkul)

  
  def tampilkan_biodata(self):
    print(f"\nBiodata Mahasiswa:")
    print(f"Nama: {self.nama}")
    print(f"NIM: {self.nim}")
    print(f"Prodi: {self.prodi}")
    print(f"Mata Kuliah yang diambil:")
    for i, matkul in enumerate(self.daftar_matkul, 1):
      print(f"{i}. {matkul.info_matkul()}")
  
  @classmethod
  def get_jumlah_mahasiswa(cls):
    return cls.jumlah_mahasiswa


class MataKuliah:
  def __init__(self, kodeMT, nama, sks):
    if not self.cek_sks_valid(sks):
      raise ValueError("SKS harus 2 atau 3")
    self.kodeMT = kodeMT
    self.nama = nama
    self.sks = sks

  @staticmethod
  def cek_sks_valid(sks):
    return sks in [2, 3]
  
  def info_matkul(self):
    return f"{self.kodeMT} - {self.nama} - ({self.sks} SKS)"
  

class Kampus:
  jumlah_mahasiswa = 0

  def __init__(self, nama, alamat):
    if not self.cek_namakampus_valid(nama):
      raise ValueError("Nama kampus tidak valid")
    self.nama = nama
    self.alamat = alamat

  @ staticmethod
  def cek_namakampus_valid(nama):
    return isinstance(nama, str) and not any(char.isdigit() for char in nama)
  
  def tampilkan_info_kampus(self):
    print(f"\nInfo Kampus:")
    print(f"Nama Kampus: {self.nama}")
    print(f"Alamat Kampus: {self.alamat}")
    print(f"Total Mahasiswa: {self.__class__.jumlah_mahasiswa}")
    print(f"Cek Nama Kampus Valid: {'ya' if self.cek_namakampus_valid(self.nama) else 'tidak'}")

  @classmethod
  def update_jumlah_mahasiswa(cls, jumlah):
    cls.jumlah_mahasiswa = jumlah

try:
    mhs1 = Mahasiswa("Adrian", "2300000001", "Sistem Informasi")
    mhs2 = Mahasiswa("Arif", "2300000002", "Sistem Informasi")
    mhs3 = Mahasiswa("Edi", "2300000003", "Teknik Informatika")
    mhs4 = Mahasiswa("Dimas", "2300000004", "Teknik Elektro")
    mhs5 = Mahasiswa("Kavi", "2300000005", "Pendidikan Informatika")
    mhs6 = Mahasiswa("Farhan", "2300000006", "Teknik Mesin")

except ValueError as e:
  print(f"Error membuat mahasiswa: {e}")




matkul1 = MataKuliah("MT001", "Pemrograman Berbasis Objek", 3)
matkul2 = MataKuliah("MT002", "Pemrograman Berbasis Web", 3)
matkul3 = MataKuliah("MT003", "Pengantar Basis Data", 3)
matkul4 = MataKuliah("MT004", "Desain Manajemen Jaringan", 3)
matkul5 = MataKuliah("MT005", "E-Business dan E-Commerce", 2)
matkul6 = MataKuliah("MT006", "Analisa Proses Bisnis", 2)
matkul7 = MataKuliah("MT007", "Bahasa Inggris", 2)
matkul8 = MataKuliah("MT008", "Pendidikan Agama Islam", 2)

mhs1.tambah_matkul(matkul1)
mhs1.tambah_matkul(matkul2)
mhs1.tambah_matkul(matkul3)
mhs1.tambah_matkul(matkul8)


mhs2.tambah_matkul(matkul2)
mhs2.tambah_matkul(matkul4)
mhs2.tambah_matkul(matkul6)
mhs2.tambah_matkul(matkul8)

mhs3.tambah_matkul(matkul1)
mhs3.tambah_matkul(matkul3)
mhs3.tambah_matkul(matkul5)
mhs3.tambah_matkul(matkul7)

mhs4.tambah_matkul(matkul2)
mhs4.tambah_matkul(matkul4)
mhs4.tambah_matkul(matkul6)
mhs4.tambah_matkul(matkul7)

mhs5.tambah_matkul(matkul1)
mhs5.tambah_matkul(matkul3)
mhs5.tambah_matkul(matkul5)
mhs5.tambah_matkul(matkul8)

mhs6.tambah_matkul(matkul2)
mhs6.tambah_matkul(matkul4)
mhs6.tambah_matkul(matkul7)
mhs6.tambah_matkul(matkul8)

try:
    kampus = Kampus("Universitas Bina Nusantara", "Jl. Kebon Jeruk Raya No.27")
except ValueError as e:
    print(f"Error membuat kampus: {e}")

daftar_mahasiswa = [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]

for mhs in daftar_mahasiswa:
    if len(mhs.daftar_matkul) < 4:
        print(f"\nPeringatan: {mhs.nama} hanya mengambil {len(mhs.daftar_matkul)} mata kuliah. Program dihentikan.")
        exit() 

Kampus.update_jumlah_mahasiswa(Mahasiswa.get_jumlah_mahasiswa())

print("\n---INFORMASI MAHASISWA ---")

mhs1.tampilkan_biodata()
mhs2.tampilkan_biodata()
mhs3.tampilkan_biodata()
mhs4.tampilkan_biodata()
mhs5.tampilkan_biodata()
mhs6.tampilkan_biodata()

kampus.tampilkan_info_kampus()