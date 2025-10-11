import random

liste_mit_zahlen = []

for i in range(0,30):
    zahl = random.randrange(0,101)
    liste_mit_zahlen.append(zahl)

liste_mit_zahlen.sort()
print(liste_mit_zahlen)
liste_mit_zahlen.sort(reverse=True)
print(liste_mit_zahlen)