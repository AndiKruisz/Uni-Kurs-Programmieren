import random as rnd

# Ein Würfelspiel. Es wird gewürfelt, wenn keine 1 oder 5 gewürfelt wird hat man verloren. Ansonsten kann man einen Würfel rauslegen.
# 1er sind 100 Punkte wert.
# 5er sind 50 Punkte wert. 
# Wenn man einen Würfel rauslegt, ist ein Würfel weniger im Pool. Man muss keinen Würfel rauslegen.
# Versuche so viele Punkte wie möglich zu bekommen.

def random_wuerfel ():
    return rnd.randrange(1,6)


PUNKTE_WENN_1 = 100
PUNKTE_WENN_5 = 50
punkte_gesamt = 0

wuerfel_noch_im_spiel = 5
rausgelegt = []

while wuerfel_noch_im_spiel > 0:
    print(f'Es sind noch {wuerfel_noch_im_spiel} Würfel im Spiel.')
    
    gewuerfelt = [random_wuerfel() for i in range(wuerfel_noch_im_spiel)]
    gewuerfelt.sort()
    print(gewuerfelt)

    if 1 in gewuerfelt or 5 in gewuerfelt:

        weitermachen = input('Willst du weiterspielen? y or n ' )

        if weitermachen == 'y':
            
            wuerfel_rausnehmen = int(input('Welchen Würfel willst du rausnehmen? '))
            
            if wuerfel_rausnehmen in gewuerfelt:
                wuerfel_noch_im_spiel -= 1

                rausgelegt.append(wuerfel_rausnehmen)
                print(f'Du hast die Zahlen {rausgelegt} rausgelegt.')
                
                punkte_gesamt = (rausgelegt.count(1)*PUNKTE_WENN_1) + (rausgelegt.count(5)*PUNKTE_WENN_5)
                print(f'Du stehst bei {punkte_gesamt} Punkten')
            else:
                print('Bitte wähle einen 1er oder 5er Würfel aus dem Pool.')

        else:
            print(f'Gratuliere, du hast {punkte_gesamt} erreicht.')
            break

    else: 
        print(f'Du hast leider verloren.')
        break