import math

'''Mehrere Funktionen aus der Übung Programmieren'''
def kleinste_zahl(*args):
    '''Aus zwei oder mehr Zahlen wird die kleinste Zahl definiert.'''
    ergebnis=min(*args)
    return ergebnis


def kreis_durchmesser(radius):
    '''Es wird der Durchmesser eines Radius berechnet.'''
    return radius * 2

def groesste_zahl(*args):
    '''Es wird die größte Zahl angegeben.'''
    ergebnis=max(args)
    return ergebnis


def durchschnitt(*args):
    '''Es wird der Durchschnitt zwischen mindestens 2 Zahlen berechnet.'''
    ergebnis = sum(args)/len(args)
    return ergebnis

def ist_primzahl(zahl):
    """Prüft, ob eine gegebene Zahl eine Primzahl ist.
    Eine Primzahl ist eine natürliche Zahl größer als 1, 
    die nur durch 1 und sich selbst teilbar ist.
    Args:
        zahl (int): Die zu prüfende Zahl.
    Returns:
        bool: True, wenn die Zahl eine Primzahl ist, False sonst.
    """
    # Primzahlen müssen größer als 1 sein
    if zahl <= 1:
        return False
    
    # Die Zahl 2 ist die einzige gerade Primzahl
    if zahl == 2:
        return True
    
    # Alle geraden Zahlen größer als 2 sind keine Primzahlen
    if zahl % 2 == 0:
        return False
        
    # Wir müssen nur bis zur Wurzel der Zahl prüfen,
    # da wenn ein Teiler 'a' > sqrt(zahl) existiert, 
    # muss auch ein Teiler 'b' < sqrt(zahl) existieren (da a*b = zahl).
    # Wir starten bei 3 und springen in 2er-Schritten (alle ungeraden Zahlen),
    # da wir gerade Zahlen bereits ausgeschlossen haben.
    
    # math.isqrt ist effizienter für Integer-Wurzeln, 
    # aber math.floor(math.sqrt(zahl)) funktioniert auch.
    limit = int(math.isqrt(zahl)) 
    
    for i in range(3, limit + 1, 2):
        if zahl % i == 0:
            return False  # Gefundenes Vielfaches, keine Primzahl
        
    return True  # Wenn keine Vielfachen gefunden wurden, ist es eine Primzahl

def main():
    radius=100
    print(kreis_durchmesser(radius))
    durchmesser=kreis_durchmesser(radius)
    print(durchmesser)
    groesste_zahl(3,5,9,2,7)

if __name__=="__main__":
    main()