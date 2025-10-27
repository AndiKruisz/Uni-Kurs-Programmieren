#Erzeugen Sie eine Liste mit 10 Listen, die je 2 Zahlen enthalten.
import random as rnd
import copy


liste = [
    [rnd.randint(0,100),rnd.randint(0,100)]
    for x in range(0,10)
]

print(liste)
alte_liste = liste.copy()
liste.sort(key=lambda x:x[0])
print(alte_liste)