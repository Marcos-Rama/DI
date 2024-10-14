import tkinter as tk

def seleccion():
    """
    Función para modificar el mensaje de la etiqueta en funcion de la "posición" que marcas con el checkbutton
    hobbies[i] utiliza la lista que has creado para, en función del índice, saber que debe mostrar
    Se crea un bucle que revisa cada una de las i por si hay una selección múltiple que mostrar
    Enumerate permite ir directamente al índice que se asigna mediante la variable (var_check en este caso)
    """
    seleccion = [hobbies[i] for i, position in enumerate(var_check) if position.get()]
    #Modificación de la etiqueta
    etiqueta.config(text=f"Checkbutton: {' '.join(seleccion)}")

root = tk.Tk() #Creamos una ventana
root.title("Ventana ejercicio 2") #Asignamos un título a la ventana
root.geometry("300x200")#Establecemos un tamaño a la ventana

#Creación de la variable que se utilizará para guardar el estado de cada uno de los check
var_check = [tk.BooleanVar() for _ in range(3)]
#Lista para mostar los textos luego en la label
hobbies = ["Leer", "Viajar", "Jugar"]

#Creación de cada uno de los checkbutton
check1= tk.Checkbutton(root,text="Leer",variable=var_check[0], command=seleccion)
check1.pack()
check2= tk.Checkbutton(root,text="Viajar",variable=var_check[1], command=seleccion)
check2.pack()
check3= tk.Checkbutton(root,text="Jugar",variable=var_check[2], command=seleccion)
check3.pack()
#Etiqueta que mostará el estado de las opciones marcadas
etiqueta = tk.Label(root,text="Checkbutton: No seleccionado")
etiqueta.pack()

root.mainloop()