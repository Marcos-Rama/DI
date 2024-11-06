import tkinter as tk
from modelo import GameModel
from vista import GameView, MainMenu
from controlador import GameController


def main():
    root = tk.Tk()
    #¿Ocultar la ventana?

    #Inicialiar con dificultad predefinida y nombre de jugador
    model = GameModel()
    view = GameView(root)
    controlador = GameController(model, view)

    root.mainloop()


if __name__ == '__main__':
    main()
