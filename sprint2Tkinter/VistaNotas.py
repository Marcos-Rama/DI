import tkinter as tk


class VistaNotas:

    def __init__(self, root):
        self.root = root
        self.root.title("Practica 2")

        self.etiqueta1 = tk.Label(self.root, text="Aplicación para notas")
        self.etiqueta1.pack()

        self.etiqueta2 = tk.Label(self.root, text="Posición del ratón:")
        self.etiqueta2.pack()

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()

        self.entrada = tk.Entry(self.root)
        self.entrada.pack()

        self.boton1 = tk.Button(self.root, text="Agregar Nota")
        self.boton1.pack()

        self.boton2 = tk.Button(self.root, text="Eliminar Nota")
        self.boton2.pack()

        self.boton3 = tk.Button(self.root, text="Guardar Notas")
        self.boton3.pack()

        self.boton4 = tk.Button(self.root, text="Cargar notas")
        self.boton4.pack()

        self.boton5 = tk.Button(self.root, text="Descargar Imagen")
        self.boton5.pack()

        self.etiqueta3 = tk.Label(self.root)
        self.etiqueta3.pack()
        self.etiqueta4 = tk.Label(self.root, text= "Coordenadas:")
        self.etiqueta4.pack()