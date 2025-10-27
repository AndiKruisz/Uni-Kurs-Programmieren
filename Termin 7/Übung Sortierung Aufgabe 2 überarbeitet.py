#Erzeugen Sie eine Liste mit 30 Zufallszahlen zwischen 1 und 100.
#Sortieren Sie die Liste aufsteigend und geben Sie in einer Schleife die Zahlen aus.
#Sortieren Sie die Liste absteigend und geben nochmals in einer Schleife die Zahlen aus.

import random

zufallsliste=[random.randint(1,100) for x in range(0,30)]
zufallsliste.sort()
print(zufallsliste)
zufallsliste.sort(reverse=True)
print(zufallsliste)