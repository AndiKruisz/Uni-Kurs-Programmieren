#Sie wollen in einem Dictionary die Information zu Ihren StudienkollegInnen ablegen.
#Die Keys sind die Matrikelnummern und die Werte sind wiederrum Dictionaries, in denen Sie Nachname, Vorname und Alter ablegen.
#Geben Sie die abgelegten Inhalte aus.
#Berechnen Sie das Gesamtalter der abgelegten Personen.

studierende = {}

studierende[12345] = {
    'Nachname' : 'Greiter',
    'Vorname' : 'Michael',
    'Alter' : 55
}

studierende[12346] = {
    'Nachname' : 'Huber',
    'Vorname' : 'Manfred',
    'Alter' : 22
}

studierende[12347] = {
    'Nachname' : 'Kohl',
    'Vorname' : 'Annemarie',
    'Alter' : 55
}

for matrikelnummer, daten in studierende.items():
    print(f"\nMatrikelnummer: {matrikelnummer}")
    for schluessel, wert in daten.items():
        print(f"  {schluessel}: {wert}")

gesamtalter = 0
for matrikelnummer, daten in studierende.items():
    gesamtalter += daten['Alter']
    
print(gesamtalter)
