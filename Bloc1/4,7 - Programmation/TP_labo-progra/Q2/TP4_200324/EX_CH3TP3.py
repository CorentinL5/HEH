import asyncio
from datetime import datetime


async def retirer_puissance_apres(perso, combien=0, delai_sec=1):
    if isinstance(perso, Personnage) and combien != 0:
        await asyncio.sleep(delai_sec)

        perso.puissance -= combien
        print(f"La puissance de {perso.nom} est remise à {perso.puissance}")
    else:
        print("retirer_puissance_apres(); Non effectué car le perso entré n'est pas un personnage")


def date_et_heure():
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    return dt_string


class Personnage:
    def __init__(self, nom, puissance, pv):
        self.nom = nom
        self.puissance = puissance
        self.pv = pv

    def attaquer(self, a_attaquer, degats):
        a_attaquer.perdre_point_de_vie(degats * self.puissance)

    def perdre_point_de_vie(self, degats):
        self.pv -= degats
        if self.pv < 0:
            self.est_ko()
        else:
            print(f"{self.nom} à pris {degats} et à maintenant {self.pv}PV.")
        return self.pv

    def est_ko(self):
        if self.pv < 0:
            print(f"{self.nom} est KO.")
        else:
            print(f"{self.nom} est en vie avec {self.pv}PV restants.")


class SuperHeros(Personnage):
    def __init__(self, nom_secret, nom, puissance, pv, en_vie=True):
        super().__init__(nom, puissance, pv)
        self.nom_secret = nom_secret
        self.en_vie = en_vie

    def attaquer(self, a_attaquer, degats):
        pass

    def utiliser_pouvoir_special(self, puissance_en_plus=10, temps=15):
        self.puissance += puissance_en_plus
        print(f"La puissance de {self.nom} est augmenté à {self.puissance} pour {temps}s")
        retirer_puissance_apres(self, puissance_en_plus, temps)


class SuperVilain(Personnage):
    def __init__(self, nom_de_code, nom, puissance, pv, but="tuer"):
        super().__init__(nom, puissance, pv)
        self.nom_de_code = nom_de_code
        self.but = but
        self.logs_heros = []

    def combat_heros(self, hero):
        if isinstance(hero, SuperHeros):
            self.logs_heros.append((hero.nom, date_et_heure()))


superman = SuperHeros("Clark", "SuperMan", 70, 350)
batman = SuperHeros("Bruce", "Batman", 50, 500)

super_vilain1 = SuperVilain("supvil1", "SuperVilain_N1", 30, 700)
super_vilain2 = SuperVilain("supvil2", "SuperVilain_N2", 100, 150)
