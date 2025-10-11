lieblingsgerichte = [
['Pasta', 5],
['Pizza', 6],
['Spargel', 7],
['Schnitzel', 8],
['Palatschinken', 3]
]

weiteres_gericht = input('Auf welches Gericht hast du sonst noch Lust? ')
weiterer_preis = int(input('Was soll das gericht kosten? '))

lieblingsgerichte.append([weiteres_gericht,weiterer_preis])

while True:
    erster_wert = lieblingsgerichte[0]
    letzter_wert = lieblingsgerichte[-1]
    auswahl_user = input('Vorwärts (v), Rückwärts(r) oder Exit (e)? ')
    if auswahl_user == 'v':
        lieblingsgerichte.append(erster_wert)
        del lieblingsgerichte[0]
        print(lieblingsgerichte)
    elif auswahl_user == 'r':
        lieblingsgerichte.insert(0,letzter_wert)
        del lieblingsgerichte[-1]
        print(lieblingsgerichte)
    else:
        break