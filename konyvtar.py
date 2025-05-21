from nagykonyv import konyv

class Konyvtar:
    def __init__(self):
        self.konyvek = []
        self.fajl_beolvasas()

    def fajl_beolvasas(self):
        with open("konyvek.txt", "r", encoding="utf-8") as forrasfajl:
            # fejléc kihagyása
            next(forrasfajl)
            for sor in forrasfajl:
                adatok = sor.strip().split(";")
                nev = adatok[0]
                szul_ev = adatok[1]
                hal_ev = adatok[2]
                nemzetiseg = adatok[3]
                cim = adatok[4]
                helyezes = adatok[5]

                konyvek.append(konyv(nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes))