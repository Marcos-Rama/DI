
class Monstruo:

    nombre_monstruo = None
    ataque_monstruo = 1
    defensa_monstruo = 1
    salud_monstruo = 1

    def __init__(self, nombre_monstruo, ataque_monstruo, defensa_monstruo, salud_monstruo):
        """
        Constructor de la clase Monstruo.

        nombre_monstruo: El monstruo que le daremos al monstruo
        ataque_monstruo: El ataque que el monstruo nos hará
        defensa_monstruo: La defensa que debe ser superada por el daño del héroe para hacer daño.
        salud_monstruo: La vida del monstruo
        """
        self.nombre_monstruo = nombre_monstruo
        self.ataque_monstruo = ataque_monstruo
        self.defensa_monstruo = defensa_monstruo
        self.salud_monstruo = salud_monstruo

    def atacar(self,heroe):
        """
        Metodo que se usará para realizar una acción en la clase mazmorra, calcula cuanto daño se le hace al héroe
        y se le quita a su vida actual (si el daño es mañor a 0).
        Parámetros
        heroe: objeto que le enviaremos desde la clase Mazmorra, sobre el que se ejecutará el metodo

        Retorna:
        Nada, solo muestra si se ha recibido daño o no y reduce la vida de ser así.
        """
        print(f"El monstruo {self.nombre_monstruo} ataca a {heroe.nombre_heroe}.")
        hit = self.ataque_monstruo - heroe.defensa_heroe
        if hit > 0:
            heroe.salud_heroe-= hit
            print(f"El héroe {heroe.nombre_heroe} ha recibido {hit} puntos de daño.")
        else:
            print("El héroe ha bloqueado el ataque.")

    def esta_vivo(self):
        #Comprueba si la salud del monstruo es mayor a 0, por lo tanto devuelve un true (está vivo) y sigue el combate
        return self.salud_monstruo > 0
