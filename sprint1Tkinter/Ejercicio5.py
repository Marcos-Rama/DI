import tkinter as tk

def cambio_color():
    """
    Metodo que realiza el cambio de color en función del radio button elegido (que se le carga un valor mediante
    el cual se realiza esta comprobación de ifs)
    """
    if var_radio.get() == "Rojo":
        root.config(bg="red")
    elif var_radio.get() == "Azul":
        root.config(bg="blue")
    elif var_radio.get() == "Verde":
        root.config(bg="green")

root = tk.Tk() #Creamos una ventana
root.title("Ejercicio 5") #Asignamos un título a la ventana
root.geometry("300x200") #Establecemos un tamaño a la ventana

var_radio = tk.StringVar() #Creamos variable para utilizar en el radio button y guardar el valor
var_radio.set("None") #Elige una opción del radiobutton que vendrá marcada por defecto, uso None para que no hay ninguna

#Creación de los radio button, con sus textos y valores correspondientes, así como un command que llame al cambio color
radio1 = tk.Radiobutton(root, text="Rojo", variable=var_radio, value="Rojo", command=cambio_color)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Azul", variable=var_radio, value="Azul", command=cambio_color)
radio2.pack()
radio3 = tk.Radiobutton(root, text="Verde", variable=var_radio, value="Verde", command=cambio_color)
radio3.pack()

# Inicia el bucle necesario del programa, mientras mantiene la ventana abierta.
root.mainloop()