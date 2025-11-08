class Elektrobass:
    anzahl = 0
    
    def __init__(self, marke, anzahl_der_saiten, hat_bundstege):
        self.marke=marke
        self.anzahl_der_saiten=anzahl_der_saiten
        self.hat_bundstege=hat_bundstege
        Elektrobass.anzahl+=1

    @property
    def marke(self):
        return self.__marke
    
    @marke.setter
    def marke(self,value):
        self.__marke=value

    @property
    def anzahl_der_saiten(self):
        return self.__anzahl_der_saiten
    
    @anzahl_der_saiten.setter
    def anzahl_der_saiten(self,value):
        self.__anzahl_der_saiten=value

    @property
    def hat_bundstege(self):
        return self.__hat_bundstege
    
    @hat_bundstege.setter
    def hat_bundstege(self,value):
        self.__hat_bundstege=value

    def spielen(self):
        print('Der Bass wird gespielt.')

    def bundsteg_ja_nein(self):
        if self.hat_bundstege == True:
            return 'hat Bundstege'
        elif self.hat_bundstege == False:
            return 'hat keine Bundstege'

    def __str__(self):
        return f'Der Bass ist von {self.marke}, hat {self.anzahl_der_saiten} Saiten und {self.bundsteg_ja_nein()}.'
    
bass1 = Elektrobass('Fender', 4, True)
bass2 = Elektrobass('Ibanez', 5, False)

print(bass1)
print(bass2)
print(f'{Elektrobass.anzahl} Objekte')