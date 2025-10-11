import random

gewaelte_zahlen = []
zusatzzahl = []
liste_mit_zahlen = []

for i in range(1,46):
    liste_mit_zahlen.append(i)

#print(liste_mit_zahlen)

for i in range(1,7):
    ziehung = random.choice(liste_mit_zahlen)
    liste_mit_zahlen.remove(ziehung)
    gewaelte_zahlen.append(ziehung)

zusatzzahl = gewaelte_zahlen[-1]
gewaelte_zahlen.remove(zusatzzahl)

zahlen_schoen = ' '.join(str(z) for z in gewaelte_zahlen)
   
print(f'Die Glückszahlen sind: {zahlen_schoen} + die Zusatzzahl {zusatzzahl}')
