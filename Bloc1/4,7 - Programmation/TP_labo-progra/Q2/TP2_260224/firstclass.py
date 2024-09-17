class MaPremiereClass:
    __attribut = 0

    def __int__(self):
        self.__attribut = 0

    def getattribut(self):
        return self.__attribut

    def setattribut(self, valeur):
        self.__attribut = valeur


mon_objet = MaPremiereClass()

print(mon_objet.getattribut())
mon_objet.setattribut(10)
print(mon_objet.getattribut())
