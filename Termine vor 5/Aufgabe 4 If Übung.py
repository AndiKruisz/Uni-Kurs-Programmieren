while True:
    zahl1 = input('Was ist deine erste Zahl? ')
    zahl2 = input('Was ist deine zweite Zahl? ') 

    if zahl1 % 2 == 0 & zahl2 % 2 == 0:
        print('Beide Zahlen sind gerade.')
    elif zahl1 % 2 == 0 & zahl2 % 2 != 0:
        print('Nur erste Zahl gerade.')
    elif zahl1 % 2 != 0 & zahl2 % 2 == 0:
        print('Nur zweite Zahl gerade.')
    else:
        print('Beide Zahlen sind ungerade.')

    print('Ich bin fertig')
