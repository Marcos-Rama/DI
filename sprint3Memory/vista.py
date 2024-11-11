import time
import tkinter as tk
from tkinter import simpledialog, Toplevel, Label

from modelo import GameModel
from recursos import descargar_imagen


class GameView(Toplevel):
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        super().__init__()
        self.moves = 0
        self.window = None
        self.model = GameModel
        self.labels = {} #Almacenará las etiquetas de las cartas, representadas por label, cada posición será una label
        #Estas serán funciones de callback que permiten que la vista se comunique con el CONTROLADOR al hacer esas acciones
        self.on_card_click_callback =on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.hidden_image = descargar_imagen(65, "https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta3.jpg")

    def create_board(self,model):
    #Crea la ventana del juego como instancia TopLevel, con su título y usando el modelo para definir tamaño y contenido
    #Genera un tablero de Labels en función del tamaño, cada una será una imagen oculta, se organizan en cuadrícula y vinculadas a eventos de click que llaman al callback "on_card_click_callback"
    #Añadir etiquetas para contador de movimientos y temporizador
        print("Haciendo tablero")
        for i, row in enumerate(model.board):
            for j, card in enumerate(row):
                lbl = Label(self, text="*", width=65, height=75,image=model.imagen_hidden , relief="raised", bg="grey")
                lbl.grid(row=i+1,column = j)
                self.labels[(i,j)] = lbl
                lbl.bind("<Button-1>", lambda event, pos=(i,j): self.on_card_click_callback(event,pos))


    def update_board(self, pos, image):
        #Actualiza la imagen de una carta en una posición concreta (pos), configurando la imagen que corresponda según el image_id que tenga
        row, col = pos
        label = self.labels[(row, col)]  # Obtener la etiqueta de la carta
        label.config(image=image, width=80, heigh= 50)  # Actualizar la imagen
        label.image = image  #Mantener una referencia de la imagen

    def delay(self, pos1, pos2):
        self.after(1000, lambda: self.reset_cards(pos1, pos2))

    def reset_cards(self, pos1, pos2):
        # Obtener las etiquetas de las cartas

        print('RESET CARDS')
        # self.delay(pos1, pos2)
        label1 = self.labels[pos1]
        label2 = self.labels[pos2]

        # Restaurar las cartas al estado oculto
        label1.config(image=self.hidden_image)
        label2.config(image=self.hidden_image)

        # Mantener las referencias para evitar que las imágenes sean recolectadas
        label1.image = self.hidden_image
        label2.image = self.hidden_image

    def update_move_count(self,moves):
        #Actualiza el contador de movimientos en la interfaz, modificando el texto de la label que muestra los mov. actuales
        print("Movimientos", moves)
        pass

    def update_time(self, time):
        #Actualiza el temporizador de la interfaz para reflejar el tiempo pasado
        pass

    def destroy(self):
        #Cierra la ventana del tablero y limpia los elementos almacenados en labels. Esto sirve para restablecer la interfaz al terminar le juego o vovler al menu principal
        pass



class MainMenu:
    def __init__(self,root, start_game_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.title("Juego de memoria")
        (tk.Button(self.window, text="Jugar", command = start_game_callback).pack(pady = 10))
        (tk.Button(self.window, text="Estadisticas", command=show_stats_callback).pack(pady=10))
        (tk.Button(self.window, text="Salir", command=quit_callback).pack(pady=10))


    #Esta función deberá abrir una ventana TopLevel que muestre las etadísticas de los jugadores (puntuaciones organizadas por nivel de dificultad) y muestra nombre-movimientos

    def show_stats(self,stats):
        pass