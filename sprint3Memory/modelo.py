import threading
import time
import random
from datetime import datetime
from recursos import descargar_imagen

class GameModel:

    imagen_hidden = None

    def __init__(self):
    #Inicia el modelo, establece el tamaño del tablero según la dificultad.
    #¿¿¿¿Llama a _generate_board() para crear la estructura del tablero y a _load_images() para cargar las imágenes en segundo plano???
        self.board = []
        self.difficulty = None
        self.player_name = ""
        self.moves = 0 #Contador de movimientos
        self.start_time = 0 #Temporizador de partida
        self.images = {}  # Almacena las imágenes descargadas
        self.images_are_loaded = threading.Event()

    def _generate_board(self,difficulty):
        if difficulty == "facil":
            self.board_size = 4
        elif difficulty == "medio":
            self.board_size = 6
        elif difficulty == "dificil":
            self.board_size = 8
        num_pairs = (self.board_size ** 2) // 2
        card_ids = list(range(num_pairs)) * 2
        self.board = [card_ids[i:i + self.board_size] for i in range(0, len(card_ids), self.board_size)]

    def _load_images(self):
        #inicia hilo para descargar y cargar imágenes mediante una URL base. La imagen oculta se asigna a hidden_image y
        #cada identificador de carta se asigna a una imagen descargada específica.
        def load_images_thread():
            url = 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta1.jpg'
            url2 = "https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta2.jpg"
            #self.imagen_hidden = descargar_imagen(100, hidden_image_url)  # Imagen oculta

            for card_id in range((len(self.board) * len(self.board[0])) // 2):
                image_url = url
                self.images[card_id] = descargar_imagen(65, image_url)
                image2_url = url2
                self.images[card_id] = descargar_imagen(65, image2_url)


            # Todas las imágenes se han descargado, activar el evento
            self.images_are_loaded.set()

        threading.Thread(target=load_images_thread).start()
        pass

    def images_are_loaded(self):
        #verifica si todas la imagenes han sido cargadas, devuelve valor booleano que indica si el evento images_loaded se ha activado(imagenes listas)
        pass

    def start_timer(self):
        #Reinicia el tiempo de inicio del juego para el temporizador, permitiendo un registro del tiempo
        pass
    def get_time(self):
        #calcula y devuelve el timepo en segundos desde el inicio del temporizador
        pass
    def check_match(self, pos1, pos2):
        #Aumenta el contador de movimientos y verifica si 2 posiciones del tablero contienen la misma imagen (coinciden).
        #Si encuentran imagenes coincidentes se incrementa el contador pairs_found
        pass
    def is_game_complete(self):
        #Verifica si se han encontrado todas las parejas del tablero. Si el número de parejas encontradas es igual a la mitad del tamaño total del tablero, juego terminado
        pass
    def save_score(self):
        #Guarda puntuación del juegador en archivo ranking.txt los datos incluyen nombre, dificultad, numero de movimientos y fecha.
        #Solo se guardan las 3 mejores puntuaciones de cada nivel de dificultad, basado en número de movimientos
        pass
    def load_scores(self):
        #Carga y devuelve puntuaciones desde archivo ranking.txt. Si el archivo no existe se devuelve un diccionario vacion con listas para cada nivel
        #Esto será util para mostrar el ranking de los mejors jugadores en una interfaz
        pass



