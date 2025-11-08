class Mietobjekt:
    def __init__(self, top_nr, quadratmeter, miete_pro_quadratmeter):
        self.top_nr=top_nr
        self.quadratmeter=quadratmeter
        self.miete_pro_quadratmeter=miete_pro_quadratmeter

    def miete(self):
        return self.quadratmeter * self.miete_pro_quadratmeter
    
    def __str__(self):
        return f'hat die Nummer: {self.top_nr}, hat {self.quadratmeter} Quadratmeter und kostet {self.miete()}€ pro Monat.'
    
class Garconniere(Mietobjekt):
    def __init__(self, top_nr, quadratmeter, miete_pro_quadratmeter):
        super().__init__(top_nr, quadratmeter, miete_pro_quadratmeter)

    def __str__(self):
        return f'Die Garconniere {super().__str__()}'
    

class Wohnung(Mietobjekt):
    def __init__(self, top_nr, quadratmeter, miete_pro_quadratmeter, anzahl_zimmer):
        super().__init__(top_nr, quadratmeter, miete_pro_quadratmeter)
        self.anzahl_zimmer=anzahl_zimmer

    def miete(self):
        return super().miete() + (self.anzahl_zimmer * 10)
    
    def __str__(self):
        return f'Die Wohnung {super().__str__()} Sie hat {self.anzahl_zimmer} Zimmer.'
    
garconniere1 = Garconniere(15, 35, 15)
wohnung1 = Wohnung(13, 75, 20.14, 3)

print(garconniere1)
print(wohnung1)