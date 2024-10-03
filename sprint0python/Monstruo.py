
class Monstruo:

    nombre_monstruo = None
    ataque_monstruo = 1
    defensa_monstruo = 1
    salud_monstruo = 1

    def __init__(self, nombre_monstruo, ataque_monstruo, defensa_monstruo, salud_monstruo):
        self.nombre_monstruo = nombre_monstruo
        self.ataque_monstruo = ataque_monstruo
        self.defensa_monstruo = defensa_monstruo
        self.salud_monstruo = salud_monstruo

    def atacar(self,heroe):
        print(f"El monstruo {self.nombre_monstruo} ataca a {heroe.nombre_heroe}.")
        hit = self.ataque_monstruo - heroe.defensa_heroe
        if hit > 0:
            heroe.salud_heroe-= hit
            print(f"El héroe {heroe.nombre_heroe} ha recibido {hit} puntos de daño.")
        else:
            print("El héroe ha bloqueado el ataque.")

    def esta_vivo(self):
        return self.salud_monstruo > 0
