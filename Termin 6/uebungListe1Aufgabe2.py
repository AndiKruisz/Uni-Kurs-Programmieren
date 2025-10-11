lieblingsgerichte = {
'Pasta': 5,
'Pizza': 6,
'Spargel': 7,
'Schnitzel': 8,
'Palatschinken': 3
}

anzahl_lieblingsgerichte = len(lieblingsgerichte)

while True:
    userinput_name_gericht = int(input(f'Welche Nummer interessiert Sie? Es gibt max {anzahl_lieblingsgerichte} Werte. '))
    if userinput_name_gericht<=anzahl_lieblingsgerichte:
        key = list(lieblingsgerichte)[userinput_name_gericht-1]
        value = lieblingsgerichte[key]
        print(f'Du hast {key} gewählt. Eines davon kostet {value}€.')
        userinput_anzahl_gerichte = int(input('Wie viel willst du davon bestellen? '))
        gesamtpreis = value * userinput_anzahl_gerichte
        print(f'Das wird dich insgesamt {gesamtpreis}€ kosten.')
        break

