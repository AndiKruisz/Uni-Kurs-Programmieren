import random

liste_mit_zahlen = []

for i in range(0,30):
    zahl = random.randrange(0,101)
    liste_mit_zahlen.append(zahl)

print(liste_mit_zahlen)
liste_mit_zahlen.sort(key=lambda x:int(x), reverse=True)
print(liste_mit_zahlen)