import tkinter as tk
from tkinter import messagebox

def change_label(value):
    """
    Metodo para cambiar el mensaje de la etiqueta que muestra la edad.
    """
    label2.config(text=f"Edad: {value}")

def incorporar_lista():
    """
    Metodo para añadir el usuario que has introducido a la listbox
    """
    name = entrada1.get()
    edad = scale.get()
    sexo = var_radio.get()
    usuario = f"Nombre: {name} Edad: {edad} Sexo: {sexo}"
    listbox.insert(tk.END, usuario)
def eliminar_lista():
    """
    Metodo para eliminar un usuario que ya hayas introducido, seleccionandolo en la listbox directamente para elegirlo.
    Y muestra la operación por consola para saber que has eliminado
    """
    option = listbox.get(listbox.curselection())
    listbox.delete(listbox.curselection())
    print(option)
def salir():
    """
    Metodo para cerrar la ventana (se invocará desde un botón)
    """
    root.quit()
def mensaje_guardado():
    """
    Metodo para mostrar un mensaje por pantalla al elegir la opcion de "guardar lista" en el submenu
    """
    messagebox.showinfo("Guardar lista", "La lista ha sido guardada")

def mensaje_cargado():
    """
    Metodo para mostrar un mensaje por pantalla al elegir la opcion de "cargar lista" en el submenu
    """
    messagebox.showinfo("Cargar lista", "La lista ha sido cargada")

root = tk.Tk() #Creación de la ventana
root.title("Ejercicio 12. Registro de usuario") #Titutlo de la ventana
root.geometry("500x400") #Tamaño de la ventana

#Creación de la lista
lista=[]

#Etiqueta de instrucción
label1=tk.Label(root,text="Nombre de usuario")
label1.pack()
#Entrada para el nombre de usuario
entrada1=tk.Entry(root, width=20)
entrada1.pack()
#Etiqueta de instrucción
label2=tk.Label(root,text="Edad:")
label2.pack()
#Scale para la edad
scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=change_label)
scale.pack()

var_radio = tk.StringVar() #Creamos variable para utilizar en el radio button y guardar el valor
var_radio.set(None) #Elige una opción del radiobutton que vendrá marcada por defecto, uso None para que no hay ninguna

#Creación de los radiobutton, con sus textos y valores correspondientes
radio1 = tk.Radiobutton(root, text="Masculino", variable=var_radio, value="Masculino")
radio1.pack()
radio2 = tk.Radiobutton(root, text="Femenino", variable=var_radio, value="Femenino")
radio2.pack()
radio3 = tk.Radiobutton(root, text="otro", variable=var_radio, value="otro")
radio3.pack()
#Boton para añadir el usuario a la lista, con su llamado al metodo
boton1 = tk.Button(root, text="Añadir a lista", command=incorporar_lista)
boton1.pack()
#Boton para borrar el usuario a la lista, con su llamado al metodo
boton2 = tk.Button(root, text="Borrar seleccionado", command=eliminar_lista)
boton2.pack()


#Creación y función de la lista
listbox = tk.Listbox(root,selectmode=tk.SINGLE)
for user in lista:
    listbox.insert(tk.END, user)
listbox.pack(padx = 15, pady=15, fill='both')

#Creación, y posicionamiento, del scrollbar
scroll_vert =tk.Scrollbar(listbox, orient='vertical', command=listbox.yview)
scroll_vert.pack(fill="y",side="right")
listbox.config(yscrollcommand=scroll_vert.set)

boton3 = tk.Button(root, text="Salir de la ventana", command=salir)
boton3.pack()

#Creamos una barra de menú
menu_inicial = tk.Menu(root)
root.config(menu=menu_inicial)

#Creamos un submenú "Opciones" con las opciones requeridas dentro
menu_opciones = tk.Menu(menu_inicial, tearoff=0)
menu_inicial.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Guardar lista", command=mensaje_guardado)
menu_opciones.add_separator()
menu_opciones.add_command(label="Cargar lista", command= mensaje_cargado)



root.mainloop()