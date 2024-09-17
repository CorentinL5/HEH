"""
Page 21 - 28

"""

"""
class Numbers:
    def __init__ (self, x = 1, y = 2, z = 3):
        self.__x = x
        self.y = y
        self.z = z

obj = Numbers()
print(vars(obj))
print(obj._Numbers__x)
"""

"""
class MaClasse:
    # Variable de classe
    variable_de_classe = "Je suis une variable de classe"

    # Compteur de classe
    nombre_d_instances = 0

    def __init__(self, nom):
        # Variable d'instance
        self.nom = nom
        self.n_instance = MaClasse.nombre_d_instances

        # Incrémente le compteur de classe lors de la création d'une nouvelle instance
        MaClasse.nombre_d_instances += 1


# Création d'instances de la classe
objet1 = MaClasse("Objet1")
objet2 = MaClasse("Objet2")

# Accès à la variable de classe à partir des instances
print(vars(objet1))
print(vars(objet2))

# Accès au compteur de classe
print("Nombre d'instances de la classe:", MaClasse.nombre_d_instances)  # Affiche "Nombre d'instances de la classe: 2"
"""
"""
xx_xx_xx = input("votre date (yymmdd) > ")
yyy = input("votre nombre après la date (xxx) > ")
zz = 0

#calculs...
zz = int(str(2)+str(xx_xx_xx)+str(yyy))
zz = 97-zz%97


print(f"votre numéro de registre national est celui ci: {xx_xx_xx}-{yyy}.{zz}")
"""