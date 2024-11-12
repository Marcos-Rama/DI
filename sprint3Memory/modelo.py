import os
import threading
import time
import random
from datetime import datetime

from recursos import descargar_imagen

class GameModel:


    def __init__(self):
        """
        Inicia el modelo, establece el tamaño del tablero según la dificultad y declara los atributos que vaya a necesitar
        """

        self.board = []
        self.difficulty = None
        self.player_name = ""
        self.pairs_found = 0
        self.total_time = 0
        self.moves = 0 #Contador de movimientos
        self.start_time = 0 #Temporizador de partida
        self.images = {}  # Almacena las imágenes descargadas
        self.images_are_loaded = threading.Event()
        self.imagen_hidden = None
        self.timer_running = False
        self.images_loaded = threading.Event()

    def _generate_board(self,difficulty):
        """
        Genera las caracteristicas que tendrá el tablero en función de la dificultad elegida
        """
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

        """
        Inicia hilo para descargar y cargar imágenes mediante unas URL. La imagen oculta se asigna a hidden_image y
        cada identificador de carta se asigna a una imagen descargada específica.
        """
        def load_images_thread():
            urls = [
                'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta1.jpg',
                'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta2.jpg',
                 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta5.png',
                 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta4.jpg',
            ]
            url_hidden = 'https://raw.githubusercontent.com/Marcos-Rama/DI/refs/heads/main/carta3.jpg'
            #self.imagen_hidden = descargar_imagen(100, hidden_image_url)  # Imagen oculta
            images_download = []
            total_items_to_duplicate = int((self.board_size * self.board_size) / len(urls))
            for count, url in enumerate(urls):
                print('url', url)
                downloaded_image = descargar_imagen(80,120, url)
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

            self.imagen_hidden = descargar_imagen(80,120,url_hidden)

            # Todas las imágenes se han descargado, activar el evento
            self.images_loaded.set()

        threading.Thread(target=load_images_thread).start()


    def images_are_loaded(self):
        #verifica si todas la imagenes han sido cargadas, devuelve valor booleano que indica si el evento images_loaded se ha activado(imagenes listas)
        return self.images_loaded.is_set()

    def start_timer(self):
        #Reinicia el tiempo de inicio del juego para el temporizador, permitiendo un registro del tiempo
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True

    def stop_timer(self):
        if self.timer_running:
            self.total_time = int(time.time() - self.start_time)
            self.timer_running = False


    def get_time(self):
        #calcula y devuelve el timepo en segundos desde el inicio del temporizador
        if self.start_time is None:
            return 0
        elapsed_time = int(time.time() - self.start_time)  # Devuelve el tiempo en segundos
        return elapsed_time

    def check_match(self, id_image1, id_image2):

        """
        Verifica si 2 posiciones del tablero contienen la misma imagen (coinciden).
        Si encuentran imagenes coincidentes se incrementa el contador pairs_found
        """

        print(f'Is same card? {id_image1}, {id_image2} ----- {id_image1 == id_image2}')
        if id_image1 == id_image2:
            self.pairs_found += 1
            print("Parejas encontradas: ", self.pairs_found)
        return id_image1 == id_image2

    def is_game_complete(self):
        #Verifica si se han encontrado todas las parejas del tablero. Si el número de parejas encontradas es igual a la mitad del tamaño total del tablero, juego terminado
        total_pairs = ((self.board_size * self.board_size)/ 2)
        print("total_pairs:", total_pairs)
        return self.pairs_found == total_pairs

    def reset_game(self):
        #Resetea los valores siguientes para un nuevo juego
        self.pairs_found = 0
        self.start_time = None
        self.timer_running = False
        self.board = []
        self.images_loaded.clear()


    def save_score(self):

        """
        Guarda puntuación del juegador en archivo ranking.txt los datos incluyen nombre, dificultad, numero de movimientos y fecha.
        Solo se guardan las 3 mejores puntuaciones de cada nivel de dificultad, basado en número de movimientos
        """

        current_date = datetime.now().strftime("%Y-%m-%d") #Obtenemos la fecha actual en formato año-mes-dia
        score_entry = f"{self.player_name}, {self.moves} movimientos, {current_date}" #Creamos lo que será el mensaje que se guardará para cada player

        #Si no existe el archivo lo crea
        if not os.path.exists("ranking.txt"):
            with open("ranking.txt", "w") as f:
                f.write("Nombre, Dificultad, Movimientos, Fecha\n")

        with open("ranking.txt", "a") as f:
            f.write(f"{self.player_name}, {self.difficulty}, {self.moves}, {current_date}\n")


        with open("ranking.txt", 'r') as f:
            lines = f.readlines()

        scores_by_difficulty = {"facil": [], "medio": [], "dificil": []}

        for line in lines:

            parts = line.strip().split(", ")
            if len(parts) == 4:  # Verifica que la línea tenga el formato
                name, difficulty, moves, date = parts
                # Asegurarse de que 'difficulty' tenga un valor esperado
                if difficulty in scores_by_difficulty:
                    scores_by_difficulty[difficulty].append((name, difficulty, int(moves), date))

        for difficulty in scores_by_difficulty:
            scores_by_difficulty[difficulty] = sorted(scores_by_difficulty[difficulty], key=lambda x: x[2])

        with open("ranking.txt", 'w') as f:
            f.write("Nombre, Dificultad, Movimientos, Fecha\n")  # Escribir la cabecera
            for difficulty in scores_by_difficulty:
                for score in scores_by_difficulty[difficulty][:3]:  # Solo las tres mejores
                    f.write(f"{score[0]}, {score[1]}, {score[2]}, {score[3]}\n")

    def load_scores(self):
        """
        Carga y devuelve puntuaciones desde archivo ranking.txt. Si el archivo no existe se devuelve un diccionario vacion con listas para cada nivel
        Esto será util para mostrar el ranking de los mejors jugadores en una interfaz"""

        ranking_file = "ranking.txt"
        scores_by_difficulty = {"facil": [], "medio": [], "dificil": []}

        #Si existe, abrimos el fichero en lectura

        if os.path.exists(ranking_file):
            with open(ranking_file, 'r') as f:
                lines = f.readlines()
            # Eliminar la primera línea
            header = lines.pop(0)

            for line in lines:
                parts = line.strip().split(", ")
                if len(parts) == 4:  # Verifica que la línea esté bien formateada
                    name, difficulty, moves, date = parts
                    if difficulty in scores_by_difficulty:
                        scores_by_difficulty[difficulty].append((name, difficulty, int(moves), date))
            for difficulty in scores_by_difficulty:
                scores_by_difficulty[difficulty] = sorted(scores_by_difficulty[difficulty], key=lambda x: x[2])
        return scores_by_difficulty
