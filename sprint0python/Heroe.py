from Monstruo import Monstruo

class Heroe:


    def __init__(self,nombre_heroe):
        """
        Constructor de Héroe

        Parámetros
        nombre_heroe, nombre que le enviamos desde la clase main, donde por teclado elegimos el nombre
        """
        self.nombre_heroe = nombre_heroe
        self.ataque_heroe = 20
        self.defensa_heroe = 12
        self.salud_heroe = 100
        self.salud_maxima=100

    def atacar(self, enemigo):
        """
        Metodo que se usará para realizar una acción en la clase mazmorra, calcula cuanto daño se le hace al monstruo
        y se le quita a su vida actual (si el daño es mañor a 0).
        Parámetros
        enemigo: objeto que le enviaremos desde la clase Mazmorra cuando empiece el programa

        Retorna:
        Nada, solo muestra si se ha recibido daño o no y reduce la vida de ser así.
        """
        print(f"Héroe ataca a {enemigo.nombre_monstruo}.")
        hit = self.ataque_heroe - enemigo.defensa_monstruo
        if hit > 0:
            enemigo.salud_monstruo-= hit
            print(f"El enemigo {enemigo.nombre_monstruo} ha recibido {hit} puntos de daño.")
        else:
            print("El enemigo ha bloqueado el ataque.")

    def curarse(self):
        """
        Metodo invocado desde mazmorra, cuando se elija la opción de curarnos, sobre una cantidad fija que se establece
        se suma al a vida del héroe.

        Parámetros:
        Ninguno, la cantidad de cura es un importe fijo.

        Retorna:
        Nada, simplemente sube el importe de la vida según la cura elegida y muestra el éxito en un print.

        """
        heal = 10
        if self.salud_heroe + heal <= self.salud_maxima:
            self.salud_heroe += heal
        else:
            self.salud_heroe = self.salud_maxima
        print(f"Héroe se ha curado. salud actual: {self.salud_heroe}")

    def defenderse(self):
        """
        Metodo invocado desde mazmorra, cuando se elija la opción de subirnos la defensa, sobre una cantidad fija
        que se establece se suma al a vida del héroe.

        Parámetros:
        Ninguno, la cantidad de defensa subida es un importe fijo.

        Retorna:
        Nada, simplemente sube el importe de la defensa y muestra el éxito en un print.

        """
        self.defensa_heroe += 5
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa_heroe}")

    def reset_defensa(self):
        """
        Metodo invocado desde mazmorra que, tras haber subido la defensa temporalmente, la reestablezca a un valor normal

        Parámetros:
        Ninguno, solo resetea a un valor previo.

        Retorna:
        Nada, simplemente reestablece la defensa al valor previo y muestra el éxito en un print.

        """
        self.defensa_heroe -5
        print(f"La defensa de {self.nombre_heroe} vuelve a la normalidad")

    def esta_vivo(self):
        #Comprueba si la salud del héroes es mayor a 0, por lo tanto devuelve un true (está vivo)
        return self.salud_heroe > 0

