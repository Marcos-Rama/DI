import random
from Heroe import Heroe

class Tesoro:
    beneficios = ["aumento del ataque", "aumento de defensa", "restauración de salud"]


    def encontrar_tesoro(self, heroe):
        """
        Metodo que se ejecuta tras derrotar a un enemigo (en clase mazmorra) y le da al héroe una recompensa

        heroe: objeto sobre el que se va a realizar el metodo

        Retorna:
        Nada, muestra por pantalla que recomensa obtiene (conseguida con un random) y aplica el beneficio.
        """

        beneficio = random.choice(self.beneficios)
        print(f"Héroe ha encontrado un tesoro: {beneficio}.")

        if beneficio == "aumento del ataque":
            heroe.ataque_heroe += 7
            print(f"El ataque de {heroe.nombre_heroe} aumenta a {heroe.ataque_heroe}.")

        elif beneficio == "aumento de defensa":
            heroe.defensa_heroe += 5
            print(f"La defensa de {heroe.nombre_heroe} aumenta a {heroe.defensa_heroe}.")

        elif beneficio == "restauración de salud":
            heroe.salud_heroe = heroe.salud_maxima
            print(f"La salud de {heroe.nombre_heroe} ha sido restaurada a {heroe.salud_heroe}.")