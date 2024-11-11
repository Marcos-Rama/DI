import threading
import time
import random
from datetime import datetime
from email.contentmanager import raw_data_manager

from recursos import descargar_imagen

class GameModel:


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
        self.imagen_hidden = None

    def _generate_board(self,difficulty):
        if difficulty == "facil":
            self.board_size = 4
        elif difficulty == "medio":
            self.board_size = 6
        elif difficulty == "dificil":
            self.board_size = 8
        num_pairs = (self.board_size ** 2) // 2
        card_ids = list(range(num_pairs)) * 2
        random.shuffle(card_ids)
        self.board = [card_ids[i:i + self.board_size] for i in range(0, len(card_ids), self.board_size)]

    def _load_images(self):
        #inicia hilo para descargar y cargar imágenes mediante una URL base. La imagen oculta se asigna a hidden_image y
        #cada identificador de carta se asigna a una imagen descargada específica.
        def load_images_thread():
            urls = [
                'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta1.jpg',
                'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta2.jpg',
                # 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta3.jpg',
                 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta4.jpg',
            ]
            url_hidden = 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta3.jpg'
            #self.imagen_hidden = descargar_imagen(100, hidden_image_url)  # Imagen oculta
            images_download = []
            total_items_to_duplicate = int((self.board_size * self.board_size) / len(urls))
            for count, url in enumerate(urls):
                print('url', url)
                downloaded_image = descargar_imagen(65, url)
                images_download += [(count, downloaded_image)] * total_items_to_duplicate

            len_board = self.board_size * self.board_size
            banned_positions = []
            for image in images_download:
                print(' Image ')
                random_position = None
                while random_position is None:
                    random_position = random.randint(0, (len_board-1))
                    print(' pos:', random_position)
                    if random_position in banned_positions:
                        print('\t - banned')
                        random_position = None
                        continue
                    banned_positions += [random_position]
                self.images[random_position] = image
            print(self.images)

            self.imagen_hidden = descargar_imagen(65,url_hidden)
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

    def check_match(self, id_image1, id_image2):
        #Aumenta el contador de movimientos y verifica si 2 posiciones del tablero contienen la misma imagen (coinciden).
        #Si encuentran imagenes coincidentes se incrementa el contador pairs_found
        print(f'Is same card? {id_image1}, {id_image2} ----- {id_image1 == id_image2}')
        return id_image1 == id_image2

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



