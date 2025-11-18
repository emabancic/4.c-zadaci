class Recept:
    def __init__(self, naziv):
        self.naziv = naziv
        self.sastojci = []  # lista rječnika

    def dodaj_sastojak(self, sastojak, kolicina):
        self.sastojci.append({
            'naziv': sastojak,
            'kolicina': kolicina
        })

    def prikazi(self):
        print(f"\nRecept: {self.naziv}")
        print("Sastojci:")
        for s in self.sastojci:
            print(f" - {s['naziv']}: {s['kolicina']}")
        print("-------------------------")


class Kuharica:
    def __init__(self, naziv):
        self.naziv = naziv
        self.recepti = []  # lista objekata klase Recept

    def dodaj_recept(self, recept_objekt):
        self.recepti.append(recept_objekt)

    def pronadi_recept(self, naziv_recepta):
        for recept in self.recepti:
            if recept.naziv.lower() == naziv_recepta.lower():
                recept.prikazi()
                return
        print(f"Recept '{naziv_recepta}' nije pronađen u kuharici.")
# Kreiranje kuharice
moja_kuharica = Kuharica("Moja prva kuharica")

# Kreiranje recepata
palacinke = Recept("Palačinke")
juha = Recept("Juha")

# Dodavanje sastojaka u Palačinke
palacinke.dodaj_sastojak("Brašno", "200 g")
palacinke.dodaj_sastojak("Mlijeko", "300 ml")
palacinke.dodaj_sastojak("Jaje", "2 kom")

# Dodavanje sastojaka u Juhu
juha.dodaj_sastojak("Voda", "1 L")
juha.dodaj_sastojak("Mrkva", "2 kom")
juha.dodaj_sastojak("Kocka za juhu", "1 kom")

# Dodavanje recepata u kuharicu
moja_kuharica.dodaj_recept(palacinke)
moja_kuharica.dodaj_recept(juha)

# Pretraživanje i prikaz recepta
moja_kuharica.pronadi_recept("Palačinke")