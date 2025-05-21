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
                hal_ev = adatok[2] if adatok[2] else "2005"
                nemzetiseg = adatok[3]
                cim = adatok[4]
                helyezes = adatok[5]

                self.konyvek.append(konyv(nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes))

    def konyvek_db(self):
        print(len(self.konyvek))

konyvtar = Konyvtar()
konyvtar.konyvek_db()

for i in konyvtar.konyvek:
    print(i.nev, "-", i.cim)
