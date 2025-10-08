#definicija klase BankovniRacun
class BankovniRacun:
    def __init__(self, broj_racuna, vlasnik, stanje=0.0):
        self.broj_racuna = broj_racuna
        self.vlasnik = vlasnik
        self.stanje = stanje

    def uplata(self, iznos):
        if iznos > 0:
            self.stanje += iznos
            print(f"INFO: Na račun {self.broj_racuna} izvršena je uplata od {iznos:.2f}. Novo stanje: {self.stanje:.2f}.")
        else:
            print(f"GREŠKA: Iznos uplate mora biti pozitivan. Unijeli ste: {iznos:.2f}.")

    def isplata(self, iznos):
        if iznos > 0:
            if iznos <= self.stanje:
                self.stanje -= iznos
                print(f"INFO: Sa računa {self.broj_racuna} izvršena je isplata od {iznos:.2f}. Novo stanje: {self.stanje:.2f}.")
            else:
                print(f"GREŠKA: Nedovoljno sredstava na računu {self.broj_racuna}. Trenutno stanje: {self.stanje:.2f}, pokušavate isplatiti: {iznos:.2f}.")
        else:
            print(f"GREŠKA: Iznos isplate mora biti pozitivan. Unijeli ste: {iznos:.2f}.")

    def info(self):
        print(f"Račun broj: {self.broj_racuna}, Vlasnik: {self.vlasnik}, Stanje: {self.stanje:.2f}")
        print("-"*30)
# ---- Glavni program ----
# Ovdje kreiramo objekte klase BankovniRacun i koristimo njihove metode
racun1 = BankovniRacun("123-4567890123-45", "Ivan Horvat", 1000.0)
racun2 = BankovniRacun("987-6543210987-65", "Ana Kovač", 500.0) 
# prikaz početnog stanja računa
racun1.info()
racun2.info()