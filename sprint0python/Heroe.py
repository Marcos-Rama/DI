from Monstruo import Monstruo

class Heroe:


    def __init__(self,nombre_heroe):
        self.nombre_heroe = nombre_heroe
        self.ataque_heroe = 20
        self.defensa_heroe = 12
        self.salud_heroe = 100
        self.salud_maxima=100

    def atacar(self, enemigo):
        print(f"Héroe ataca a {enemigo.nombre_monstruo}.")
        hit = self.ataque_heroe - enemigo.defensa_monstruo
        if hit > 0:
            enemigo.salud_monstruo-= hit
            print(f"El enemigo {enemigo.nombre_monstruo} ha recibido {hit} puntos de daño.")
        else:
            print("El enemigo ha bloqueado el ataque.")

    def curarse(self):
        heal = 10
        if self.salud_heroe + heal <= self.salud_maxima:
            self.salud_heroe += heal
        else:
            self.salud_heroe = self.salud_maxima
        print(f"Héroe se ha curado. salud actual: {self.salud_heroe}")

    def defenderse(self):
        self.defensa_heroe += 5
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa_heroe}")

    def reset_defensa(self):
        self.defensa_heroe -5
        print(f"La defensa de {self.nombre_heroe} vuelve a la normalidad")

    def esta_vivo(self):
        return self.salud_heroe > 0

