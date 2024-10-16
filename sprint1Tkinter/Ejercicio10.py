import tkinter as tk

def introducir_líneas():
    """
    Metodo que al final introducirá las líneas para comprobar la funcionalidad del scrollbar
    """
    for i in range(1,200):
        cuadro_texto.insert(tk.END, f"Línea {i}\n")

root = tk.Tk() #Creación de la ventana
root.title("Ejercicio 10") #Titutlo de la ventana
root.geometry("300x200") #Tamaño de la ventana

#Se crea un frame donde contener tanto el textbox como el scrollbar
frame=tk.Frame(root)
frame.pack(fill='both', expand=True)

#Creación, y posicionamiento, del cuadro donde estará el texto
cuadro_texto = tk.Text(frame, height=10, width=40)
cuadro_texto.grid(row=0, column=0, sticky='nsew')

#Creación, y posicionamiento, del scrollbar
scroll_vert =tk.Scrollbar(frame, orient='vertical', command=cuadro_texto.yview)
scroll_vert.grid(row=0, column=1,sticky='ns')
cuadro_texto.config(yscrollcommand=scroll_vert.set)

#Configuración del frame para el tamaño de la ventana
frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(0,weight=1)

#Ejecutamos el metodo que rellenará el texto
introducir_líneas()

root.mainloop()