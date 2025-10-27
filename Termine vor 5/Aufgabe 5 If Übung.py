artikel = str(input('Was willst du kaufen? '))
stückpreis = float(input('Was ist der Stückpreis? '))
anzahl = int(input('Wie viel willst du davon bestellen? '))
gesamtpreis = (anzahl*stückpreis)


if gesamtpreis >= 100:
    gesamtpreis = gesamtpreis/100*90
elif anzahl > 10 and gesamtpreis <= 100:
    gesamtpreis = gesamtpreis/100*95

print(f'Du hast {anzahl} {artikel} gekauft. Eines kostet {stückpreis}, somit zahlst du {gesamtpreis}€.') 