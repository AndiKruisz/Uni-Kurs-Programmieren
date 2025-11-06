import random
print("Würfelspiel")

while True:
    print("Neue Runde")
    augen=[]
    print("Erster Versuch")
    for i in range(5):
        augen+=[random.randint(1,6)]    
    print(augen)    
    while True:
        wuerfel=int(input("Welche Zahl wollen Sie entfernen (0 für keine): "))
        if wuerfel==0:
            break
        if wuerfel in augen:
            del augen[augen.index(wuerfel)]
        print(augen)
    
    print("Zweiter Versuch")
    anzahlRest=len(augen)
    for i in range(5-anzahlRest):
        augen+=[random.randint(1,6)]    
    print(augen)
    while True:
        wuerfel=int(input("Welche Zahl wollen Sie entfernen (0 für keine): "))
        if wuerfel==0:
            break
        if wuerfel in augen:
            del augen[augen.index(wuerfel)]
        print(augen)
    print("Dritter Versuch")
    anzahlRest=len(augen)
    for i in range(5-anzahlRest):
        augen+=[random.randint(1,6)]    
    print(augen)
    neueRunde=input("Noch eine Runde (j oder n): ")
    if neueRunde=="n":
        break
