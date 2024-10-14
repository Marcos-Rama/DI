import tkinter as tk #Importamos la librería de tkinter para interfaces

def cambiar_boton():
    """
    Este metodo hace una modificación en el texto de la etiqueta3.
    """
    etiqueta_3.config(text="Texto cambiado")

root = tk.Tk() #Creamos una ventana
root.title("Ventana ejercicio 1") #Asignamos un título a la ventana
root.geometry("300x200") #Establecemos un tamaño a la ventana
"""
Aquí vienen una serie de etiquetas de texto, las que indica el ejercicio que hay que realizar
más un botón al final para ejecutar el metodo creado al inicio.
"""
etiqueta_1 = tk.Label(root, text = "Hola, bienvenido")
etiqueta_1.pack()
etiqueta_2 =tk.Label(root, text = "Marcos")
etiqueta_2.pack()
etiqueta_3 = tk.Label(root, text="Mensaje inicial")
etiqueta_3.pack()
boton = tk.Button(root, text="Click aqui para cambiar mensaje", command=cambiar_boton)
boton.pack()
 #Inicia el bucle necesario del programa, mientras mantiene la ventana abierta.
root.mainloop()
