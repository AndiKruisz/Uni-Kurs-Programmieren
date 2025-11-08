class BuchBase:
    anzahl=0
    lesedauer=0
    
    def __init__(self, titel, autor):
        self.titel=titel
        self.autor=autor

    def __str__(self):
        return f'Buch: {self.titel}, Autor: {self.autor}'

    #def lesedauer_erhoehen():
        #lesedauer = lesen() + vorlesen()

class Buch(BuchBase):
    def __init__(self, titel, autor, seitenzahl):
        super().__init__(titel, autor)
        self.seitenzahl=seitenzahl
        BuchBase.anzahl+=1
        

    def lesen(self):
        print(f'Das Buch {self.titel} von {self.autor} wird gerade gelesen.')
        BuchBase.lesedauer += self.seitenzahl *2

    def __str__(self):
        return f'{super().__str__()}, Art: Buch'



class Hoerbuch(BuchBase):
    def __init__(self, titel, autor, dauer_in_minuten):
        super().__init__(titel, autor)
        self.dauer_in_minuten=dauer_in_minuten
        BuchBase.anzahl+=1

    def vorlesen(self):
        print(f'Das Buch {self.titel} von {self.autor} wird gerade vorgelesen.')
        BuchBase.lesedauer += self.dauer_in_minuten

    def __str__(self):
        return f'{super().__str__()}, Art: Hörbuch'


buch1=Buch('Dune', 'Frank Herbert', 800)
buch2=Buch('Der Hobbit', 'J.R.Tolkien', 400)

hoerbuch1=Hoerbuch('Das Rad der Zeit', 'Robert Jordan', 180)
hoerbuch2=Hoerbuch('Foundation', 'Isaac Asimov', 160)

print(buch1)
print(buch2)
print(hoerbuch1)
print(hoerbuch2)

buch1.lesen()
buch2.lesen()
hoerbuch1.vorlesen()
hoerbuch2.vorlesen()

print(BuchBase.anzahl)
print(BuchBase.lesedauer)