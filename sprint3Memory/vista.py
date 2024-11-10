import tkinter as tk
from tkinter import simpledialog, Toplevel, Label



class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.window = None
        self.labels = {} #Almacenará las etiquetas de las cartas, representadas por label, cada posición será una label
        #Estas serán funciones de callback que permiten que la vista se comunique con el CONTROLADOR al hacer esas acciones
        self.on_card_click_callback =on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback

    def create_board(self,model):
    #Crea la ventana del juego como instancia TopLevel, con su título y usando el modelo para definir tamaño y contenido
    #Genera un tablero de Labels en función del tamaño, cada una será una imagen oculta, se organizan en cuadrícula y vinculadas a eventos de click que llaman al callback "on_card_click_callback"
    #Añadir etiquetas para contador de movimientos y temporizador
        pass

    def update_board(self, pos, image_id):
        #Actualiza la imagen de una carta en una posición concreta (pos), configurando la imagen que corresponda según el image_id que tenga
        pass

    def reset_cards(selfself, pos1, pos2):
        #Restaura las imágenes de dos cartas a su estado oculto cuando no haya coincidencia entre ambas.
        pass

    def update_move_count(self,moves):
        #Actualiza el contador de movimientos en la interfaz, modificando el texto de la label que muestra los mov. actuales
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

    def ask_player_name(self):
        player_name = simpledialog.askstring("Nombre", "¿Cuál es tu nombre?")

    #Esta función deberá abrir una ventana TopLevel que muestre las etadísticas de los jugadores (puntuaciones organizadas por nivel de dificultad) y muestra nombre-movimientos

    def show_stats(self,stats):
        pass