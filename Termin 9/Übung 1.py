class Buch:
    anzahl=0
    lesedauer=0
    
    def __init__(self, titel, autor, seitenzahl):
        self.titel=titel
        self.autor=autor
        self.seitenzahl=seitenzahl
        Buch.anzahl+=1

    def lesen(self):
        print(f'Buch {self.titel} von {self.autor} wird gerade gelesen.')
        Buch.lesedauer += self.seitenzahl *2

    def __str__(self):
        return f'{self.titel} von {self.autor}, Seitenzahl: {self.seitenzahl}'
    

buch1=Buch('Dune', 'Frank Herbert', 800)
buch2=Buch('Der Hobbit', 'J.R.Tolkien', 400)
buch3=Buch('Das Rad der Zeit', 'Robert Jordan', 896)

print(buch1)
print(buch2)
print(buch3)

buch1.lesen()
buch2.lesen()
buch3.lesen()

print(f'AnzahL: {Buch.anzahl}')
print(f'Lesedauer: {Buch.lesedauer} Minuten')