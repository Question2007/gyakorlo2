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

def feladat3():
    legidosebb = kutyak[0]
    for i in kutyak:
        if legidosebb.kor < i.kor:
            legidosebb = i
    print(f"4. Ki a legidősebb kutya, és hány éves? {legidosebb.nev} {legidosebb.kor}")

def feladat4():
    gazdi_keres = input("Adj meg egy gazdit: ")
    print("5. Kérjen be a felhasználótól egy gazdi nevét, és listázza ki az ő kutyáit a képernyőre! ")
    with open("eszti.txt", "a", encoding="UTF-8") as f:
        for i in kutyak:
            if i.gazdi == gazdi_keres:
                f.write(i.nev)
                f.write("\n")
                print(i.nev)
        
def feladat5():
    print("7. Listázza ki azokat a kutyákat, akik több mint 8 évesek!")
    for i in kutyak:
        if i.kor > 8:
            print(i)

def feladat6():
    print("8. Listázza ki azokat a kutyákat, akik “keverék” fajtájúak!")
    for i in kutyak:
        if i.fajta == "keverék":
            print(i)


def main():
    beolvasas()
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()

main()