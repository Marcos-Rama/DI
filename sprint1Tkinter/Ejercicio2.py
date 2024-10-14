import tkinter as tk
from tkinter import messagebox

def mostar_mensaje():
    """
    Metodo para mostrar un mensaje al utilizar un botón creado posteriormente.

    """
    messagebox.showinfo("Mensaje","Click con éxito" )
def cerrar_ventana():
    """
    Metodo que ejecuta el quit, que sirve para cerrar la ventana

    """
    root.quit()


root = tk.Tk() #Creamos una ventana
root.title("Ventana ejercicio 2") #Asignamos un título a la ventana
root.geometry("300x200")#Establecemos un tamaño a la ventana
#botón que "llama" al metodo que muestra un mensaje
boton1 = tk.Button(root, text="Haz click", command=mostar_mensaje)
boton1.pack()
#Botón que llama al metodo declarado arriba que cierra la ventana
boton2 = tk.Button(root, text="Haz click para cerrar", command=cerrar_ventana)
boton2.pack()

root.mainloop()