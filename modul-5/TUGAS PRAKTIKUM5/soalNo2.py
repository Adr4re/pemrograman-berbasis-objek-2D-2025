from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100  
        self.status_nyala = False
    
    @abstractmethod
    def nyalakan(self):
        pass
    
    @abstractmethod
    def matikan(self):
        pass
    
    @abstractmethod
    def gunakan(self, jam: int):
        pass
    
    def status(self):
        return f"{self.__class__.__name__} - Energi: {self.energi_tersisa}% | Status: {'Nyala' if self.status_nyala else 'Mati'}"

class Laptop(PerangkatElektronik):
    def __init__(self):
        super().__init__()
        self.jam_penggunaan = 0

    def nyalakan(self):
        self.status_nyala = True
        return f"{self.__class__.__name__} dinyalakan"
    
    def matikan(self):
        if not self.status_nyala:
            return f"{self.__class__.__name__} belum dinyalakan!"
        self.status_nyala = False
        return f"{self.__class__.__name__} dimatikan. Total penggunaan: {self.jam_penggunaan} jam"
    
    def gunakan(self, jam: int):
        if not self.status_nyala:
            return f"{self.__class__.__name__} harus dinyalakan dulu!"
        
        self.jam_penggunaan += jam
        pengurangan_energi = 10 * jam
        energi_sebelum = self.energi_tersisa
        self.energi_tersisa = max(0, self.energi_tersisa - pengurangan_energi)
        energi_terpakai = energi_sebelum - self.energi_tersisa
        
        pesan = f"Laptop digunakan {jam} jam. Energi berkurang {energi_terpakai}%"
        
        if self.energi_tersisa == 0:
            pesan += "\n🔋 Baterai habis!"
            self.status_nyala = False 
            
        return pesan

class Kulkas(PerangkatElektronik):
    def __init__(self):
        super().__init__()
        self.jam_penggunaan = 0

    def nyalakan(self):
        self.status_nyala = True
        return f"{self.__class__.__name__} dinyalakan"
    
    def matikan(self):
        if not self.status_nyala:
            return f"{self.__class__.__name__} belum dinyalakan!"
        self.status_nyala = False
        return f"{self.__class__.__name__} dimatikan. Total penggunaan: {self.jam_penggunaan} jam"
    
    def gunakan(self, jam: int):
        if not self.status_nyala:
            return f"{self.__class__.__name__} harus dinyalakan dulu!"
        
        self.jam_penggunaan += jam
        pengurangan_energi = 5 * jam
        energi_sebelum = self.energi_tersisa
        self.energi_tersisa = max(0, self.energi_tersisa - pengurangan_energi)
        energi_terpakai = energi_sebelum - self.energi_tersisa
        
        pesan = f"Kulkas digunakan {jam} jam. Energi berkurang {energi_terpakai}%"
        
        if self.energi_tersisa < 20:
            pesan += "\n⚠️ Energi rendah, kulkas butuh daya tambahan!"
            if self.energi_tersisa == 0:
                self.status_nyala = False 
                pesan += "\n❌ Kulkas mati karena kehabisan energi!"
                
        return pesan

def input_validasi_jam(prompt):
    while True:
        jam = input(prompt).strip()
        if not jam:
            print("❌ Input tidak boleh kosong")
            continue
        if not jam.isdigit():
            print("❌ Input harus berupa angka positif")
            continue
        jam = int(jam)
        if jam <= 0:
            print("❌ Durasi harus lebih dari 0 jam")
            continue
        return jam

def main():
    print("=== PROGRAM PERANGKAT ELEKTRONIK ===")
    
    laptop = Laptop()
    kulkas = Kulkas()
    
    while True:
        print("\nMenu:")
        print("1. Operasikan Perangkat")
        print("2. Matikan Perangkat")
        print("3. Lihat Status")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            print("\nPilih Perangkat:")
            print("1. Laptop")
            print("2. Kulkas")
            
            perangkat = input("Pilih perangkat (1/2): ")
            
            if perangkat == "1":
                print(laptop.nyalakan())
                if laptop.status_nyala:
                    jam = input_validasi_jam("Durasi penggunaan (jam): ")
                    print(laptop.gunakan(jam))
            elif perangkat == "2":
                print(kulkas.nyalakan())
                if kulkas.status_nyala:
                    jam = input_validasi_jam("Durasi penggunaan (jam): ")
                    print(kulkas.gunakan(jam))
            else:
                print("Pilihan tidak valid!")
        
        elif pilihan == "2":
            print("\nPilih Perangkat yang akan dimatikan:")
            print("1. Laptop")
            print("2. Kulkas")
            
            perangkat = input("Pilih perangkat (1/2): ")
            
            if perangkat == "1":
                print(laptop.matikan())
            elif perangkat == "2":
                print(kulkas.matikan())
            else:
                print("Pilihan tidak valid!")
        
        elif pilihan == "3":
            print("\nStatus Perangkat:")
            print(laptop.status())
            print(kulkas.status())
        
        elif pilihan == "0":
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid!")

main()