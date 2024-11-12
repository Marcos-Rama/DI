from PIL import Image, ImageTk
import requests
import io


def descargar_imagen(width, height, url):
    try:
        respuesta = requests.get(url) #Realiza petición GET
        respuesta.raise_for_status() #Comprueba si tuvo éxito
        imagen = Image.open(io.BytesIO(respuesta.content)) #Abre la imagen desde el flujo de bytes
        imagen_redimensionada = imagen.resize((width, height), Image.Resampling.LANCZOS) #Ajusta al tamaño pedido
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada) #conversión a formato compatible con tkinter
        # Programar la actualización de la interfaz en el hilo principal
        return imagen_tk #Imagen devuelta
    except requests.exceptions.RequestException as e:
        print(f"URL fallida: {e}")
        return None
