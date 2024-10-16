import tkinter as tk

def change_label(value):

    label.config(text=f"Valor: {value}")

root = tk.Tk() #Creación de la ventana
root.title("Ejercicio 11") #Titutlo de la ventana
root.geometry("300x200") #Tamaño de la ventana

#Creamos el scale

scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=change_label)
scale.pack()

#Etiquieta que se irá modificando según desplacemos el scale

label = tk.Label(root, text="Valor 0")
label.pack()

#Bucle para iniciarl a ventana

root.mainloop()
