import funktionen as fts

#radius=float(input("Radius: "))
#print(fts.kreisDurchmesser(radius))

#print(fts.groesste_zahl(3,6,7,8))
#print(fts.durchschnitt(3,5,6,8))

zahl=True
while zahl == True:
    zahl = int(input('Gib mir bitte eine Zahl: '))
    ergebnis = fts.ist_primzahl(zahl)
    if ergebnis == True:
        print(f'Deine Zahl {zahl} ist eine Primzahl')
    else:
        print(f'Deine Zahl {zahl} ist keine Primzahl')
    break



#print(fts.ist_primzahl(13))