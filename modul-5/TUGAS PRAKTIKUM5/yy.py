from abc import ABC, abstractmethod

# a. Abstract class
class AlatMusik(ABC):
    @abstractmethod
    def mainkan(self):
        pass

    @abstractmethod
    def suara(self):
        pass

# b. Subclass
class Gitar(AlatMusik):
    def mainkan(self):
        print("Memetik senar gitar.")

    def suara(self):
        print("Suara gitar: jreng jreng")

# c. Pembuatan objek dan pemanggilan method
gitar1 = Gitar()
gitar1.mainkan()
gitar1.suara()