class Modelo:

    def __init__(self):
        self.notas=[]

#Creación de los métodos que se invocarán desde los botones

    #Metodo que añade las notas que escribamos a una listbox
    def agregar_nota(self,nueva_nota):
        self.notas.append(nueva_nota)
    #Metodo que elimina las notas que seleccionemos de la listbox
    def eliminar_nota(self,indice):
        del self.notas[indice]
    #Metodo que añade las notas que tengamos en la lista.
    def obtener_notas(self):
        return self.notas
    #Metodo que añade las notas que tengamos a un documento de texto
    def guardar_notas(self):
        with open('notas.txt', 'w') as archivo:
            for nota in self.notas:
                archivo.write(nota  + "\n")
    #Metodo que carga las notas que tengamos en un fichero de texto para visualizarlo en la listbox
    def cargar_notas(self):
        with open('notas.txt', 'r') as archivo:
            self.notas = [linea.strip() for linea in archivo]
