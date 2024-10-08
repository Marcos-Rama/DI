from Heroe import Heroe
from Monstruo import Monstruo
from Tesoro import Tesoro
from Mazmorra import Mazmorra

def main():
    # Elegimos el nombre de nuestro personaje y creamos un objeto Heroe con ese dato.
    nombre_heroe =input("Introduce el nombre de tu héroe: ")
    heroe = Heroe(nombre_heroe)

    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()


if __name__ == "__main__":
    """
    Este if hace que lo que haya a continuación, en este caso main(), se ejecute solo si se inicia desde el archivo
    llamado main.
    """
    main() #Esto inicia el juego