import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label
from modelo import GameModel
from vista import GameView, MainMenu


class GameController:
    def __init__(self, root, model):
        self.root = root #Ventana principal
        self.model = model #Intancia del model del juego
        self.selected = [] #Lista que almacena posiciones de las cartas
        self.timer_started = False #Booleando que indica si el temporizador ha comenzado
        self.main_menu = MainMenu(root,self.show_difficulty_selection, self.show_stats, root.quit) #Crear menu con sus callbacks

    def show_difficulty_selection(self):
        difficulty = simpledialog.askstring("¿Dificultad?", "Elige una dificultad (facil, medio o dificil)")
        if difficulty in ["facil", "medio", "dificil"]:
            player_name = simpledialog.askstring("¿Nombre?", "Elige un nombre para el jugador")
            if player_name:
                self.model.difficulty = difficulty
                self.model.player_name = player_name
                self.start_game(difficulty)

    def start_game(self, difficulty):
        #Muestra ventana de carga y crear una instancia GameModel con dificultad y nombre elegidos, llama a check_images_loaded
        pass

    def show_loading_window(self, message):
        #Crea una ventana de carga temporal para indicar que el tablero está siendo preparado, esto impide interactuar con otras partes de la interfaz mientras dure la carga
        pass

    def check_images_loaded(self):
        #Comprueba si las imágenes se han cargado completamente en el modelo, una vez listas destruye la ventana de carga y crea una instancia GameModel para el tablero y controles de juego
        #Si las imágenes no están listas, vuelve a comprobar tras un breve tiempo
        pass

    def on_card_click(self):
        #Maneja evento de clic en una carta, si el temporizador no ha compezado, lo inicia y actualiza el temporizador en interfaz
        #Almacena la posición de la carta clicada y, si hay dos cargas en self.selected, llama a handle_card_selection para verificar si coinciden
        pass

    def handle_card_selection(self):
        #Verifica si 2 cartas forman pareja mediante metodo check_match del modelo, si coinciden mentiene la visualización de ambas, sino las oculta tras un breve tiempo
        #Actualzia el contador de movimientos en interfaz y llama a check_game_complete para comprobar si ha terminado el juego
        pass

    def update_move_count(self,moves):
        #Actualiza el contador de movimientos en GameView par reflejar número actual de movimientos
        pass

    def check_game_complete(self):
        #Verifica si el juego está completo llamando a is_game_complete del modelo. Si se han encontrado todas las parejas muestra un mensaje de victoria y vuelve al main_menu
        pass

    def return_to_main_menu(self):
        #Cierra la vista del juego actual y vuelve al menú principal, permitiendo que el jugador inicie nueva partida o salga
        pass

    def show_stats(self):
        #Obtiene estadísitcas de puntuaciones desde el modelo y las muestra en el menú principal
        pass

    def update_time(self):
        #Actualiza el temporizador de la vista del juego. Se llama a sí misma cada segundo mientras el juego esté activo
        pass

