cel = input("Mire gyűjt Anna: ")
kutyak_szam = int(input("Hány kutyát sétáltat a hétvégén: "))
ido = 20
ora = (ido*kutyak_szam) // 60
perc = (ido * kutyak_szam) % 60 
ar = 700
legalabb = 5000
osszeg = ar * ido
if osszeg < legalabb:
    print(f"Anna {kutyak_szam} kutyát sétáltatott {ora}:{perc} óra alatt, ezért {osszeg} Ft-ot kapott. Ez még nem elég a {cel} ára.")
else:
    print(f"Anna {kutyak_szam} kutyát sétáltatott {ora}:{perc} óra alatt, ezért {osszeg} Ft-ot kapott. Ez még nem elég a {cel} ára.")