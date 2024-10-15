import tkinter as tk

def mostrar_entry():
    """
    Metodo que cambia la etiqueta 2 para mostar lo que hayas introducido en entry

    """
    option = entry.get()
    label2.config(text=option)
    pass

def borrar_entry():
    """
    Metodo que cambia la etiqueta 2 para borrar lo que hayas introducido en entry y mostrar pendiente de nuevo

    """
    entry.delete(0,tk.END) #Borra el entry desde la posicion 0 hasta el final que sea
    label2.config(text="Pendiente")
    pass

root = tk.Tk() #Creación de la ventana
root.title("Ejercicio 7") #Titutlo de la ventana
root.geometry("400x300") #Tamaño de la ventana

#Creación frame 1
frame1 = tk.Frame(root, bg="lightblue", bd=2)
frame1.pack(padx=10, pady=10, fill='both', expand=True)

#Etiquetas para mostrar mensajes
label1 = tk.Label(frame1, text="¿Mensaje?", bg="lightgrey")
label1.pack()
label2 = tk.Label(frame1, text="Pendiente", bg="lightgrey")
label2.pack()
#Entry donde escribir lo que se quiera mostrar luego
entry = tk.Entry(frame1, width=20)
entry.pack()

#Segundo frame
frame2 =tk.Frame(root, bg="lightgrey", bd=2, relief="sunken")
frame2.pack(padx=10, pady=10, fill='both', expand=True)
#Botón que ejecuta el cambio en la label para mostrar la información del entry
boton1 = tk.Button(frame2, text="Mostrar", command=mostrar_entry)
boton1.pack()
#Botón que ejecuta el cambio en la label para eliminar la información del entry y volver al estado base
boton2 = tk.Button(frame2, text="eliminar", command=borrar_entry)
boton2.pack()


root.mainloop()