import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    """
    Meotodo para mostrar una ventana emergente al seleccionar 'Acerca de '
    """
    messagebox.showinfo("Acerca de", "Mensaje informativo sobre Acerca de")

def salir_app():
    """
    Metodo para cerrar la ventana
    """
    root.quit()

root = tk.Tk() #Creación de la ventana
root.title("Ejercicio 9") #Titutlo de la ventana
root.geometry("300x200") #Tamaño de la ventana

#Creamos una barra de menú
menu_inicial = tk.Menu(root)
root.config(menu=menu_inicial)


#Creamos un submenú "Archivo" con las opciones requeridas dentro
menu_archivo = tk.Menu(menu_inicial, tearoff=0)
menu_inicial.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_app)

#Creamo el submenu Ayuda con la opcion requerida dentro
menu_ayuda = tk.Menu(menu_inicial, tearoff=0)
menu_inicial.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label = "Acerca de", command= mostrar_mensaje)

root.mainloop()



