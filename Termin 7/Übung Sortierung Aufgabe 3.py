#Erzeugen Sie wieder eine Liste wie in Aufgabe 2 und geben Sie die unsortierten Zahlen in einer Schleife aus.
#Sortieren Sie mit einer Lambda-Funktion die Zahlen absteigend und geben Sie die Zahlen in einer Schleife wieder aus.

import random

zufallsliste=[random.randint(1,100) for x in range(0,30)]

#def liste_sortieren(liste,richtung):
#    if richtung == 'aufsteigend':
#        liste.sort()
#    elif richtung == 'absteigend':
#        liste.sort(reverse=True)
#    print(liste)
#liste_sortieren(zufallsliste, 'absteigend')


print(zufallsliste)
zufallsliste.sort (key=lambda x:x, reverse=True)
print(zufallsliste)