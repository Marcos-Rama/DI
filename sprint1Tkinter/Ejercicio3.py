import tkinter as tk


def mostrar_saludo():
    texto =entrada.get()
    etiqueta.config(text = f"Hola, {texto}")

root = tk.Tk() #Creamos una ventana
root.title("Ventana ejercicio 2") #Asignamos un título a la ventana
root.geometry("300x200")#Establecemos un tamaño a la ventana

#Etiqueta que posteriormente cambiará para mostar un saludo personalizado
etiqueta = tk.Label(root, text = "Hola")
etiqueta.pack()
#Forma de introducir mediante un Entry un texto, que luego se usará en el saludo personalizado
entrada = tk.Entry(root, width=20)
entrada.pack()
#Botón para iniciar la modificación de la etiqueta
boton = tk.Button(root, text="Haz click", command=mostrar_saludo)
boton.pack()

root.mainloop()
