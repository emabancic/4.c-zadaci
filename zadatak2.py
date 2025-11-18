class BankovniRacun:
    def __init__(self, ime_vlasnika, broj_racuna):
        self.ime_vlasnika = ime_vlasnika
        self.broj_racuna = broj_racuna
        self.stanje = 0.0

    def uplati(self, iznos):
        if iznos <= 0:
            print("Iznos za uplatu mora biti pozitivan!")
            return
        self.stanje += iznos
        print(f"Uplata uspješna! Uplaćeno: {iznos} EUR. Novo stanje: {self.stanje:.2f} EUR")

    def isplati(self, iznos):
        if iznos <= 0:
            print("Iznos za isplatu mora biti pozitivan!")
            return
        if iznos > self.stanje:
            print("Nedovoljno sredstava na računu!")
            return
        self.stanje -= iznos
        print(f"Isplata uspješna! Isplaćeno: {iznos} EUR. Novo stanje: {self.stanje:.2f} EUR")

    def info(self):
        print("\n--- Podaci o računu ---")
        print("Vlasnik:", self.ime_vlasnika)
        print("Broj računa:", self.broj_racuna)
        print(f"Trenutno stanje: {self.stanje:.2f} EUR")
        print("-------------------------\n")


# TESTIRANJE PROGRAMA

racun = BankovniRacun("Ivan Horvat", "HR12 3456 7890 1234")

racun.info()

# Uplate
racun.uplati(100)
racun.info()

racun.uplati(50.5)
racun.info()

racun.uplati(-20)  # pokušaj neispravne uplate
racun.info()

# Isplate
racun.isplati(30)
racun.info()

racun.isplati(200)  # pokušaj isplate većeg iznosa od stanja
racun.info()

racun.isplati(-10)  # neispravna isplata
racun.info()
