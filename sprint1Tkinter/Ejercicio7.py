import tkinter as tk

def modificar_canvas():
    """
    Metodo que dibuja las formas en el canvas con las coordenadas que obtiene de los entry
    """
    cX =int(coordX.get()) #Corrdenadas de arriba izquierda
    cY = int(tam.get()) #Corrdenadas de abajo derecha
    canvas.create_oval(cX,cX, cY, cY,outline="red")
    canvas.create_rectangle(cX,cX, cY, cY,outline="green")

root = tk.Tk() #Creación de la ventana
root.title("Ejercicio 7") #Titutlo de la ventana
root.geometry("300x200") #Tamaño de la ventana

#Entrys para obtener los valores de las cooredenadas
coordX = tk.Entry(root, width=20)
coordX.pack()
tam = tk.Entry(root, width=20)
tam.pack()

#Botón para ejecutar el dibujado
boton = tk.Button(root, text="Haz click", command=modificar_canvas)
boton.pack()
canvas = tk.Canvas(root, width=250, height= 200, bg="white")
canvas.pack()

root.mainloop()