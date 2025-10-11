import random

gewaelte_zahlen = []
zusatzzahl = []
liste_mit_zahlen = []

for i in range(1,46):
    liste_mit_zahlen.append(i)

random.shuffle(liste_mit_zahlen)
gewaelte_zahlen = liste_mit_zahlen[:7]

zusatzzahl = gewaelte_zahlen[-1]
gewaelte_zahlen.remove(zusatzzahl)

zahlen_schoen = gewaelte_zahlen.sort()
zahlen_schoen = ' '.join(str(z) for z in gewaelte_zahlen)
   
print(f'Die Glückszahlen sind: {zahlen_schoen} + die Zusatzzahl {zusatzzahl}')
