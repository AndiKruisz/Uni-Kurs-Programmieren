#dein Code

while True:
    max_punkte = int(input('Wie viele Punkte gibt es maximal? '))
    erreichte_punkte = float(input('Wie viele Punkte hast du geschafft? '))

    if erreichte_punkte > max_punkte:
        print('Das kann nicht stimmen. Bitte probiere es nochmal.')
        
    else:
        prozent = (erreichte_punkte / max_punkte )* 100

        if erreichte_punkte < 60:
            note = 'Nicht genügend'
        elif erreichte_punkte < 70:
            note = 'Genügend'
        elif erreichte_punkte < 80:
            note = 'Befriedigend'
        elif erreichte_punkte < 90:
            note = 'Gut'
        else:
            note = 'Sehr gut'
        print(f'Du hast {erreichte_punkte} von {max_punkte} erreicht. Das sind {prozent}% und somit ein {note}.')
        break