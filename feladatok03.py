class Kutya:
    def __init__(self, sor):
        adatok = sor.split(";")
        self.nev = adatok[0]
        self.fajta = adatok[1]
        self.kor = int(adatok[2])
        self.gazdi = adatok[3]

    def __str__(self):
        return f"Név: {self.nev} Fajta: {self.fajta} Kor: {self.kor} Gazdi: {self.gazdi}"
    


kutyak = []

def beolvasas():
    f = open("kutyak.txt", "r", encoding="UTF-8")
    for sor in f:
        kutya = Kutya(sor.strip())
        kutyak.append(kutya)
    f.close()
    #print(*kutyak)

def feladat1():
    print(f"2. Hány kutya szerepel a listában? {len(kutyak)}")

def feladat2():
    fajtak = {}
    for i in kutyak:
        if not i.fajta in fajtak:
            fajtak[i.fajta] = 0
        fajtak[i.fajta] += 1

    print(f"3. Hány különböző fajta van? {len(fajtak.keys())}")

def main():
    beolvasas()
    feladat1()
    feladat2()

main()