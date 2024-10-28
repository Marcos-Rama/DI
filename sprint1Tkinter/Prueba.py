import tkinter as tk

#req_ancho = 0
#req_alto = 0
a = 0
an = 0
def mostrar_saludo():
    texto =entrada.get()
    etiqueta.config(text = f"Hola, {texto}")

root = tk.Tk() #Creamos una ventana
root.title("Ventana ejercicio 2")#Asignamos un título a la ventana
#root.eval('tk::PlaceWindow . center')
#Establecemos un tamaño a la ventana

ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
print(f"Resolución de pantalla: {ancho_pantalla}x{alto_pantalla}")

def obtener_dimensiones_reales():
    root.update_idletasks()
    ancho = root.winfo_width()
    alto = root.winfo_height()

    return f"{ancho}x{alto}"


#Etiqueta que posteriormente cambiará para mostar un saludo personalizado
etiqueta = tk.Label(root, text = "Hola")
etiqueta.pack()
#Forma de introducir mediante un Entry un texto, que luego se usará en el saludo personalizado
entrada = tk.Entry(root, width=20)
entrada.pack()
#Botón para iniciar la modificación de la etiqueta
boton = tk.Button(root, text="Haz click", command=mostrar_saludo)
boton.pack()


root.update_idletasks()
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
x = int(root.winfo_screenwidth()/2 - windowWidth/2)
y =  int(root.winfo_screenheight()/2 - windowHeight/2)
#root.geometry("+{}+{}".format(x,y))
root.geometry(obtener_dimensiones_reales() + (x,y))



root.mainloop()