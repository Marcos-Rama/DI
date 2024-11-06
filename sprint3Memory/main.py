import tkinter as tk
from modelo import GameModel
from vista import GameView, MainMenu
from controlador import GameController


def main():
    root = tk.Tk()
    model = GameModel()
    view = GameView(root)
    controlador = GameController(model, view)

    root.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
