import random

#Aufgabe 1:
java_kurs={'Anna', 'Bernd', 'Klara', 'David', 'Eva'}
python_kurs={'Bernd', 'Eva', 'Frank', 'Gina', 'Hannah'}

schnittmenge = java_kurs & python_kurs
summe_beide_kurse = java_kurs | python_kurs
differenzmenge_nur_im_java_kurs = java_kurs - python_kurs
differenzmenge_nur_im_python_kurs = python_kurs - java_kurs


print(f'An beiden Kursen haben/hat {schnittmenge} teilgenommen.')
print(f'An zumindestest einem Kurs haben/hat {summe_beide_kurse} teilgenommen.')
print(f'Nur im Java Kurs teilgenommen haben/hat {differenzmenge_nur_im_java_kurs}.')
print(f'Nur im Python Kurs teilgenommen haben/hat {differenzmenge_nur_im_python_kurs}.')

java_kurs.add('Iris')
print(f'Im Java Kurs sind aktuell {java_kurs}.')

python_kurs.remove('Eva')
python_kurs.discard('Jochen')
print(f'Im Python Kurs sind aktuell {python_kurs}.')

#Aufgabe 2
zahlen = set()

while len(zahlen)<10:
    zusaetzliche_zahl = random.randint(1,40)
    zahlen.add(zusaetzliche_zahl)

print(zahlen)

if 10 in zahlen:
    print('Ja, 10 ist in der Liste Zahlen enthalten.')
else:
    print('Nein, 10 ist nicht enhalten.')

print(sum(zahlen))
print(sum(zahlen)/len(zahlen))
print(min(zahlen))
print(max(zahlen))
print(sorted(zahlen))