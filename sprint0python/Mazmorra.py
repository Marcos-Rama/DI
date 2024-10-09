from Monstruo import Monstruo
from Heroe import Heroe
from Tesoro import Tesoro

class Mazmorra:

    def __init__(self, heroe):
        """
        Constructor de la clase  Mazmorra, sobre la que se ejecutará el ciclo normal del juego.

        heroe: El objeto que le enviamos desde main, que será el "personaje".
        monstruos: Una lista de los que serán los enemigos del heroe, con sus valores de estadísticas predefinidos.
        tesoro: Objeto de la clase Tesoro para dar las recompensas si se gana el combate.

        """
        self.heroe = heroe
        self.monstruos = [
            Monstruo("Goblin", 105, 10, 25),
            Monstruo("Orco", 15, 15, 40)
        ]
        self.tesoro = Tesoro()

    def jugar(self):
        """
        Metodo que inicia el juego, donde habrá condiciones para saber si se continua o si hay que tomar un
        desvío, ya sea por game over, finalización etc.

        Parámetros:
        No se le envía ninguno, pero consulta los objetos definidos necesarios para sus condiciones.
        Monstruos: Donde están contenidos los monstruos del juego y sus atributos, así como que monstruo esta ahora
        miso "activo".
        Tesoro: Para buscar un premio si el héroe gana el combate.
        Héroe: Será el que realice las acciones junto a monstruo, y se debe comprobar su estado (vida).
        """
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
        """
        Metodo para tomar las decisiones del héroe durante el juego, donde se decide que acción realizar (y esto
        llamará a los métodos de las otras clases de manera oportuna).

        Parámetros:

        enemigo: objeto que se comprueba si el monstruo está vivo, se traen sus valores, así como el nombre,
        del metodo anterior.

        Retorna:
        Nada, realiza las acciones elegidas y va modificando los valores y mostrando por pantalla la información
        de acuerdo al metodo concreto que llame.

        """
        #Utilizo un boolean defensa para que solo llame al metodo reset() si antes se llamo al metodo defenderse()
        defensa = False
        #Bucle que se repite siempre que se cumplan las condiciones de que tanto heroe como monstruo estén vivos.
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            #Aquí se elige una de las opciónes del menú anterior.
            opcion = input("Elige una opción: ")

#           #Según la elección anterior se ejecuta un metodo u otro.
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
            #Si el monstruo aún está vivo realiza  su ataque contra el héroe.
            if enemigo.esta_vivo():
                enemigo.atacar(self.heroe)
            #Si se ejecutó el metodo defenderse(), se reestablece la defensa a un valor por defecto.
            if defensa :
                self.heroe.reset_defensa()

    #Metodo que si el heroe ha derrotado al monstruo le da un tesoro (mediante random).
    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)
