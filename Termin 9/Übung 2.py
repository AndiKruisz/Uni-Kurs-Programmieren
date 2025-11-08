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
    

def buecherschrank_anzeigen():
    for buch in buecherschrank:
        print(buch)

buch1=Buch('Dune', 'Frank Herbert', 800)
buch2=Buch('Der Hobbit', 'J.R.Tolkien', 400)
buch3=Buch('Das Rad der Zeit', 'Robert Jordan', 896)
buch4=Buch('Foundation', 'Isaac Asimov', 320)

buecherschrank = [buch1, buch2, buch3, buch4]

buecherschrank_anzeigen()

for buch in buecherschrank:
    buch.lesen()

buecherschrank.sort(key=lambda x:x.seitenzahl, reverse=True)
buecherschrank_anzeigen()

buecherschrank.sort(key=lambda x:len(x.titel))
buecherschrank_anzeigen()
