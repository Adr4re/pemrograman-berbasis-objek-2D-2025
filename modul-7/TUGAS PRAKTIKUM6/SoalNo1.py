from abc import ABC, abstractmethod
import math

class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass
    
    @abstractmethod
    def tampilkan_rumus(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi ** 2
    
    def tampilkan_rumus(self):
        return f"Rumus: sisi × sisi = {self.sisi} × {self.sisi}"

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def luas(self):
        return math.pi * (self.jari_jari ** 2)
    
    def tampilkan_rumus(self):
        return f"Rumus: π × r² = π × {self.jari_jari}²"

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return 0.5 * self.alas * self.tinggi
    
    def tampilkan_rumus(self):
        return f"Rumus: ½ × alas × tinggi = ½ × {self.alas} × {self.tinggi}"

def input_angka_positif(prompt):
    while True:
        try:
            angka = float(input(prompt))
            if angka <= 0:
                print("❌ Masukkan harus lebih besar dari 0")
                continue
            return angka
        except ValueError:
            print("❌ Masukkan harus berupa angka")

def hitung_luas(bangun_datar):
    print(f"\n=== PERHITUNGAN {bangun_datar.__class__.__name__.upper()} ===")
    print(bangun_datar.tampilkan_rumus())
    print(f"Luas = {bangun_datar.luas():.2f}")

def main():
    print("=== PROGRAM HITUNG LUAS BANGUN DATAR ===")
    
    bangun_datar = None
    
    while True:
        print("\nPilih Bangun Datar:")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan (0-3): ")
        
        if pilihan == "1":
            sisi = input_angka_positif("Masukkan panjang sisi: ")
            bangun_datar = Persegi(sisi)
        elif pilihan == "2":
            jari_jari = input_angka_positif("Masukkan jari-jari: ")
            bangun_datar = Lingkaran(jari_jari)
        elif pilihan == "3":
            alas = input_angka_positif("Masukkan alas: ")
            tinggi = input_angka_positif("Masukkan tinggi: ")
            bangun_datar = Segitiga(alas, tinggi)
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("❌ Pilihan tidak valid!")
            continue
        
        hitung_luas(bangun_datar)

main()