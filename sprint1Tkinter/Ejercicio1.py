import tkinter as tk

def cambiar_boton():
    etiqueta_3.config(text="Texto cambiado")

root = tk.Tk()
root.title("Ventana ejercicio 1")
root.geometry("300x200")
etiqueta_1 = tk.Label(root, text = "Hola, bienvenido")
etiqueta_1.pack()
etiqueta_2 =tk.Label(root, text = "Marcos")
etiqueta_2.pack()
etiqueta_3 = tk.Label(root, text="Mensaje inicial")
etiqueta_3.pack()
boton = tk.Button(root, text="Click aqui para cambiar mensaje", command=cambiar_boton)
boton.pack()

root.mainloop()
