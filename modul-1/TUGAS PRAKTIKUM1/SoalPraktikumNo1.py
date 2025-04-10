class manusia:
  def __init__(self, nama, umur, alamat):
    self.nama = nama
    self.umur = umur
    self.alamat = alamat

  def berjalan(self):
    return f"{self.nama} sedang berjalan"
  
  def berlari(self):
    return f"{self.nama} sedang berlari"
  
manusia1 = manusia("Adrian", 18, "Bangkalan")
manusia2 = manusia("Farhan", 20, "Bangkalan")
manusia3 = manusia("Arif", 60, "Pamekasan")
manusia4 = manusia("Edi", 21, "Sepulu")
manusia5 = manusia("Siska", 19, "Bangkalan")

print(manusia1.berjalan())
print(manusia2.berjalan())
print(manusia3.berjalan())
print(manusia4.berlari())
print(manusia5.berlari())