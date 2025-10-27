# Sie sitzen mit Ihren Freunden zusammen und planen die Getränkeliste für kommenden Samstag abend.
# Ihr Programm fragt immer nach dem Getränk und der Anzahl und legt diese in einem Dictionary ab.
# Danach kommt die Frage, ob noch etwas benötigt wird.
# Wird ein Getränk mehrmals erwähnt, so wird der entsprechende Wert im Dictionary erhöht.
# Am Ende geben Sie die Getränkeliste aus.

getraenkeliste = {}

while True:
    getraenk = input('Getränk: ')
    anzahl_getraenk = int(input('Anzahl: '))
    if getraenk in getraenkeliste.keys() == False:
        getraenkeliste.setdefault[getraenk,anzahl_getraenk]
    else:
        getraenkeliste[getraenk] = getraenkeliste.get(getraenk, 0) + anzahl_getraenk
        
    print(getraenkeliste)

    entscheidung=input('Brauchen wir noch etwas? (j oder n) ')
    if entscheidung == 'n':
        break

