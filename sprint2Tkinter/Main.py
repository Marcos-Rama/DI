import tkinter as tk
from NotasModel import Modelo
from VistaNotas import VistaNotas
from ControladorNotas import Controlador

def main():
    root = tk.Tk()
    model = Modelo()
    view = VistaNotas(root)
    controlador = Controlador(model, view)

    root.mainloop()

if __name__ == "__main__":
    main()