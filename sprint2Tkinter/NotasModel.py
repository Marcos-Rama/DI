class Modelo:

    def __init__(self):
        self.notas=[]

    def agregar_nota(self,nueva_nota):
        self.notas.append(nueva_nota)

    def eliminar_nota(self,indice):
        del self.notas[indice]

    def obtener_notas(self):
        return self.notas

    def guardar_notas(self):
        with open('notas.txt', 'w') as archivo:
            for nota in self.notas:
                archivo.write(nota  + "\n")

    def cargar_notas(self):
        with open('notas.txt', 'r') as archivo:
            self.notas = [linea.strip() for linea in archivo]
