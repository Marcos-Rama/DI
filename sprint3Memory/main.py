import tkinter as tk
from tkinter import simpledialog

from modelo import GameModel
from controlador import GameController


def main():
    root = tk.Tk()

    model = GameModel()
    controller = GameController(root, model)

    root.mainloop()

if __name__ == '__main__':
    main()
