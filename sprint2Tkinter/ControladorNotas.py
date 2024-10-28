import tkinter as tk
from tkinter import messagebox
import NotasModel
from NotasModel import Modelo
from VistaNotas import VistaNotas
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading

class Controlador:

    def __init__(self, modelo, vista):
        self.Modelo = modelo
        self.VistaNotas = vista

        #Las siguientes líneas conectarán los botones de la Clase VistaNotas con su funcionalidad, establecida en esta clase
        self.VistaNotas.boton1.config(command=self.agregar_nota)
        self.VistaNotas.boton2.config(command=self.eliminar_nota)
        self.VistaNotas.boton3.config(command=self.guardar_notas)
        self.VistaNotas.boton4.config(command=self.cargar_notas)
        self.VistaNotas.boton5.config(command=self.iniciar_descarga)
        #Crea un evento para captar la posición del ratón y mostarlo enviandolo al metodo mostrar_coordenadas
        self.VistaNotas.root.bind("<Motion>", lambda evento: self.mostrar_coordenadas(evento.x, evento.y))

    #Metodo para actualizar la listbox conforme lo que reciba de obtener_notas(De NotasModel)
    def actualizar_listbox(self):
        self.VistaNotas.listbox.delete(0,tk.END)
        for notas in self.Modelo.obtener_notas():
            self.VistaNotas.listbox.insert(tk.END, notas)

    # Metodo para añadir la nota escrita al listbox
    def agregar_nota(self):
        nueva_nota = self.VistaNotas.entrada.get()
        self.Modelo.agregar_nota(nueva_nota)
        self.actualizar_listbox()

    # Metodo para eliminar la nota seleccionada del listbox
    def eliminar_nota(self):
        selection = self.VistaNotas.listbox.curselection()
        self.Modelo.eliminar_nota(selection[0])
        self.actualizar_listbox()

    # Metodo para guardar las notas que tengamos en el listbox en un fichero de texto
    def guardar_notas(self):
        self.Modelo.guardar_notas()
        messagebox.showinfo("Operación","Notas guardadas")

    # Metodo para mostrar en el listbox las notas que tengamos guardas previamente en el fichero de texto
    def cargar_notas(self):
        self.Modelo.cargar_notas()
        self.actualizar_listbox()

    # Metodo para descargar la imagen y redimensionarla
    def descargar_imagen(self,url, callback):
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            imagen = Image.open(BytesIO(respuesta.content))
            imagen_redimensionada = imagen.resize((200, 200), Image.Resampling.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
            # Programar la actualización de la interfaz en el hilo principal
            self.VistaNotas.root.after(0, callback, imagen_tk)
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen: {e}")
            self.VistaNotas.root.after(0, callback, None)

    # Metodo para modificar la etiqueta de forma que muestre la imagen
    def actualizar_etiqueta(self,imagen_tk):
        if imagen_tk:
            self.VistaNotas.etiqueta3.config(image=imagen_tk)
            self.VistaNotas.etiqueta3.image = imagen_tk  # Mantener una referencia
        else:
            self.VistaNotas.etiqueta3.config(text="Error al descargar la imagen.")

    # Metodo para descargar la imagen mediante otro hilo y así dividir el proceso
    def iniciar_descarga(self):
        url = 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/fototkinter.jpg'
        hilo = threading.Thread(target=self.descargar_imagen, args=(url, self.actualizar_etiqueta))
        hilo.start()

    # Metodo para modificar la etiqueta encargada de mostrar las coordenadas
    def mostrar_coordenadas(self,x, y):
        self.VistaNotas.etiqueta4.config(text=f"Coordenadas: ({x}, {y})")

