from Monstruo import Monstruo
from Heroe import Heroe
from Tesoro import Tesoro

class Mazmorra:

    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = [
            Monstruo("Goblin", 5, 10, 25),
            Monstruo("Orco", 15, 15, 40)
        ]
        self.tesoro = Tesoro()

    def jugar(self):
        print("Héroe entra en la mazmorra.")
        for monstruo in self.monstruos:
            if not self.heroe.esta_vivo():
                print("Héroe ha sido derrotado en la mazmorra.")
                return
            print(f"Te has encontrado con un {monstruo.nombre_monstruo}.")
            self.enfrentar_enemigo(monstruo)

            if self.heroe.esta_vivo():
                print(f"¡{self.heroe.nombre_heroe} ha derrotado a {monstruo.nombre_monstruo}!")
                self.buscar_tesoro()

        if self.heroe.esta_vivo():
            print(f"¡{self.heroe.nombre_heroe} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")

    def enfrentar_enemigo(self, enemigo):
        defensa = False
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.heroe.atacar(enemigo)
            elif opcion == "2":
                self.heroe.defenderse()
                defensa = True
            elif opcion == "3":
                self.heroe.curarse()
            else:
                print("Opción no válida.")
                continue

            if enemigo.esta_vivo():
                enemigo.atacar(self.heroe)
            if defensa :
                self.heroe.reset_defensa()

        if not self.heroe.esta_vivo():
            print("Héroe ha sido derrotado en la mazmorra.")

    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)
