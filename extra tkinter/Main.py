import tkinter as tk
from tkinter import messagebox
import random



victorias1 = 0
victorias2 = 0
lista = ["Tijeras", "Papel", "Piedra"]

def salir():
    """
    Metodo para cerrar la ventana (se invocará desde un botón)
    """
    root.quit()


def un_jugador():
    comodin = None
    #Creamos nueva ventana con su nombre y tamaño
    v_uno= tk.Toplevel(root)
    v_uno.title('Single Player')
    v_uno.geometry("300x200")

    #Mostramos un mensaje central
    label1=tk.Label(v_uno,text="Partida de un jugador")
    label1.pack()

    #Opcion y texto indicando que es el lado del jugador 1
    label2=tk.Label(v_uno,text="Opción jugador")
    label2.place(x= 50, y= 50)
    jugador1 = tk.Entry(v_uno,width=7)
    jugador1.place(x= 50, y= 70)

    # Opcion y texto indicando que es el lado del jugador 2 (Máquina en singleplayer)
    label2=tk.Label(v_uno,text="Opción Máquina")
    label2.place(x= 150, y= 50)


    boton1 = tk.Button(v_uno, text="Iniciar ronda", command= lambda: resultado(jugador1.get(),comodin))
    boton1.pack()

    label3 = tk.Label(v_uno, text="Resultado")
    label3.place(x = 75,y = 150)



def dos_jugadores():
    v_dos = tk.Toplevel(root)
    v_dos.title('Multiplayer')
    v_dos.geometry("300x200")
    label1=tk.Label(v_dos,text="Partida de dos jugadores")
    label1.pack()
    # Opcion y texto indicando que es el lado del jugador 1
    label2 = tk.Label(v_dos, text="Opción jugador")
    label2.place(x=50, y=50)
    jugador1 = tk.Entry(v_dos, width=7)
    jugador1.place(x=50, y=70)

    # Opcion y texto indicando que es el lado del jugador 2 (Máquina en singleplayer)
    label2 = tk.Label(v_dos, text="Opción Jugador 2")
    label2.place(x=150, y=50)
    jugador2 = tk.Entry(v_dos, width=7)
    jugador2.place(x=150, y=70)

    boton1 = tk.Button(v_dos, text="Iniciar ronda", command=lambda: resultado(jugador1.get(), jugador2.get()))
    boton1.pack()


def resultado(choice1, choice2):
    global victorias1
    global victorias2
    choice1 = choice1.lower()
    choice2 = random.choice(lista).lower()

    print(choice1)
    print(choice2)

    if choice1 == "papel" and choice2 == "tijeras":
        messagebox.showinfo("Resultado ronda", "El jugador uno saca papel, "
                                               "el jugador dos saca tijera. Gana el jugador dos, "
                                               "Tijera gana a Papel")
        victorias2 +=1

    elif choice1 =="papel" and choice2 == "piedra":
        messagebox.showinfo("Resultado ronda", "El jugador uno saca papel, "
                                               "el jugador dos saca piedra. Gana el jugador uno, "
                                               "Papel gana a Piedra")
        victorias1 += 1
    elif choice1 == "tijeras" and choice2 == "papel":
        messagebox.showinfo("Resultado ronda", "El jugador uno saca tijeras, "
                                               "el jugador dos saca papel. Gana el jugador uno, "
                                               "Tijera gana a Papel")
        victorias1 += 1
    elif choice1 =="tijeras" and choice2 == "piedra":
        messagebox.showinfo("Resultado ronda", "El jugador uno saca tijeras, "
                                               "el jugador dos saca piedra. Gana el jugador dos, "
                                               "Piedra gana a Tijeras")
        victorias2 += 1
    elif choice1 =="piedra" and choice2 == "papel":
        messagebox.showinfo("Resultado ronda", "El jugador uno saca piedra, "
                                               "el jugador dos saca papel. Gana el jugador dos, "
                                               "Papel gana a Piedra")
        victorias2 += 1
    elif choice1 == "piedra" and choice2 == "tijeras":
        messagebox.showinfo("Resultado ronda", "El jugador uno saca piedra, "
                                                "el jugador dos saca tijeras. Gana el jugador uno, "
                                               "Piedra gana a Tijeras")
        victorias1 += 1
    else:
        messagebox.showinfo("Resultado ronda", "Empate, esta ronda no cuenta")
    print(victorias1, " Uno")
    print(victorias2, " Dos")

    if victorias1 == 3:
        messagebox.showinfo("Resultado ronda", "Uno gana")
        victorias1 =0
        victorias2 = 0
        salir()

    elif victorias2 == 3:
        messagebox.showinfo("Resultado ronda", "Dos gana")
        victorias1 = 0
        victorias2 = 0
        salir()


root = tk.Tk() #Creamos la ventana
root.title("Piedra-Papel-Tijera") #Establecemos el título de la ventana
root.geometry("300x200") #Tamaño de la ventana


#Creamos una barra de menú
menu_inicial = tk.Menu(root)
root.config(menu=menu_inicial)

#Creamos un submenú "Opciones" con las opciones requeridas dentro
menu_opciones = tk.Menu(menu_inicial, tearoff=0)
menu_inicial.add_cascade(label="Partida", menu=menu_opciones)
menu_opciones.add_command(label="Un jugador", command=un_jugador)
menu_opciones.add_command(label="Dos jugadores", command=dos_jugadores)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)


root.mainloop()

