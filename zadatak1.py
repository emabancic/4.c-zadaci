class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja


# Kreiranje dvaju objekata klase Knjiga
knjiga1 = Knjiga("Gospodar prstenova", "J.R.R. Tolkien", 1954)
knjiga2 = Knjiga("Na Drini ćuprija", "Ivo Andrić", 1945)

# Ispis podataka o knjigama
print("Naslov:", knjiga1.naslov, ", Autor:", knjiga1.autor, ", Godina:", knjiga1.godina_izdanja)
print("Naslov:", knjiga2.naslov, ", Autor:", knjiga2.autor, ", Godina:", knjiga2.godina_izdanja)
