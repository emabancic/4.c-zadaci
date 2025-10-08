#definicija klase knjiga
class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
    def _str_(self):
        return f("Knjiga: {self.naslov}, Autor: {self.autor}, Godina izdanja: {self.godina_izdanja}")

# ---- Glavni program ----
# Ovdje kreiramo objekte klase Knjiga i koristimo njihove metode    
knjiga1 = Knjiga("Preobrazba", "Franz kafka", 1912)
knjiga2 = Knjiga("Harry Potter", "J.K Rolling", 1997)
knjiga3 = Knjiga("Zločin i kazna", "Fjodor Dostojevski", 1866) 
print(knjiga1)
print(knjiga2)      
print(knjiga3)




     

