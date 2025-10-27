#Erzeugen Sie eine Liste und füllen Sie diese mit 9 weiteren Listen, wobei die inneren Listen jeweils aus einer 
#Artikelbezeichnung (Artikel1, Artikel2, …) und einem zufälligen ganzzahligen Preis bestehen.
#Geben Sie in einer Schleife die Bezeichnung und den Preis aus.
#Sortieren Sie die Liste nach den Preisen aufsteigend und geben Sie die Inhalte wieder in einer Schleife aus.

import random as rnd

zufallspreis = lambda: rnd.randint(1,100)

liste = [
    [f'Artikel{x+1}', zufallspreis()]
    for x in range(0,10)
]
print(liste)

liste.sort(key=lambda x:x[1])

print(liste)