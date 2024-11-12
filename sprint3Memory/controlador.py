import time
import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label
from modelo import GameModel
from vista import GameView, MainMenu


class GameController:
    def __init__(self, root, model):
        self.loading_window = None
        self.root = root #Ventana principal
        self.model = model #Intancia del model del juego
        self.view = GameView(
            on_card_click_callback=self.on_card_click,
            update_move_count_callback=self.update_move_count,
            update_time_callback=self.update_time
        )
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
        self.model.difficulty = difficulty
        self.model._generate_board(difficulty)  # Generar el tablero
        self.model._load_images()  # Cargar las imágenes de las cartas

        # Mostrar ventana de carga
        self.show_loading_window("Cargando")

        # Iniciar la verificación de la carga de imágenes
        self.check_images_loaded()

        pass

    def show_loading_window(self, message):
        #Crea una ventana de carga temporal para indicar que el tablero está siendo preparado, esto impide interactuar con otras partes de la interfaz mientras dure la carga
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Cargando")
        tk.Label(self.loading_window, text=message).pack(padx=20, pady=20)
        self.loading_window.transient(self.root)
        self.loading_window.grab_set()
        pass

    def check_images_loaded(self):
        #Comprueba si las imágenes se han cargado completamente en el modelo, una vez listas destruye la ventana de carga y crea una instancia GameModel para el tablero y controles de juego
        #Si las imágenes no están listas, vuelve a comprobar tras un breve tiempo
        if self.model.images_are_loaded.is_set():
            self.view.create_board(self.model)
            self.loading_window.destroy()
        else:
            # Repetir la comprobación después de un breve intervalo
            self.root.after(100, self.check_images_loaded)
        pass

    def on_card_click(self,event, pos):
        #Maneja evento de clic en una carta, si el temporizador no ha compezado, lo inicia y actualiza el temporizador en interfaz
        #Almacena la posición de la carta clicada y, si hay dos cargas en self.selected, llama a handle_card_selection para verificar si coinciden
        #Si el timer parado empiezalo


        if not self.timer_started:
            self.timer_started = True
            self.model.start_timer()

        #Obtener el id de la carta
        row, col = pos
        card_id = self.model.board[row][col]

        id_image, image = self.model.images[card_id]  # Obtener la imagen correspondiente
        self.view.update_board(pos, image)  #Actualizar la vista de la carta

        self.selected += [(id_image, pos)]
        if len(self.selected) == 2:
            self.handle_card_selection()
        self.update_time()
        print(f"Carta clic: {pos}")
        print(card_id)

    def handle_card_selection(self):
        #Verifica si 2 cartas forman pareja mediante metodo check_match del modelo, si coinciden mentiene la visualización de ambas, sino las oculta tras un breve tiempo
        #Actualzia el contador de movimientos en interfaz y llama a check_game_complete para comprobar si ha terminado el juego
        selection1, selection2 = self.selected
        id_image1, pos1 = selection1
        id_image2, pos2 = selection2
        is_same_card = self.model.check_match(id_image1, id_image2)
        if not is_same_card:
            print('Is not the same card')
            self.view.delay(pos1, pos2)
        self.update_move_count()
        self.selected = []
        self.check_game_complete()

    def update_move_count(self):
        #Actualiza el contador de movimientos en GameView par reflejar número actual de movimientos
        self.view.moves += 1
        self.view.update_move_count(self.view.moves)


    def check_game_complete(self):
        #Verifica si el juego está completo llamando a is_game_complete del modelo. Si se han encontrado todas las parejas muestra un mensaje de victoria y vuelve al main_menu
        if self.model.is_game_complete():
            print("Terminado game")

    def return_to_main_menu(self):
        #Cierra la vista del juego actual y vuelve al menú principal, permitiendo que el jugador inicie nueva partida o salga
        pass

    def show_stats(self):
        #Obtiene estadísitcas de puntuaciones desde el modelo y las muestra en el menú principal
        pass

    def update_time(self):
        #Actualiza el temporizador de la vista del juego. Se llama a sí misma cada segundo mientras el juego esté activo
        time_elapsed = self.model.get_time()
        self.view.update_time(time_elapsed)
        # Llama a `update_time` cada segundo mientras el juego esté activo

        self.root.after(1000, self.update_time)
        pass
