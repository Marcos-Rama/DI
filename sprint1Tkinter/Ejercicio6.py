import tkinter as tk
from tkinter import mainloop

def mostrar_fruta():
    """
    Metodo para que se ejecute al pulsar el botón, cambiará el texto en la etiqueta para mostar que fruta hemos elegido
    """
    options = listbox.curselection() #Obtiene la lista de elementos que forman parte de la lista
    elementos = [listbox.get(i) for i in options] #Acepta el valor de lo elegido en la lista
    label.config(text=f"Elegido: {', '.join(elementos)}")

root = tk.Tk() #Creación de la ventana
root.title("Ejercicio 6") #Titutlo de la ventana
root.geometry("300x200") #Tamaño de la ventana

#Etiqueta para mostrar que tenemos eledido
label = tk.Label(root,text="Seleccionaste: Nada")
label.pack()

#Elementos que formarán parte de la lista
frutas =["Manzana", "Plátano", "Naranja"]

#Creación y función de la lista
listbox = tk.Listbox(root,selectmode=tk.SINGLE)
for fruta in frutas:
    listbox.insert(tk.END, fruta)
listbox.pack()

#Botón para cambiar el estado de la label y que muestre que hemos elegido
boton = tk.Button(root, text="Mostrar elegido", command=mostrar_fruta)
boton.pack()

# Inicia el bucle necesario del programa, mientras mantiene la ventana abierta.
root.mainloop()