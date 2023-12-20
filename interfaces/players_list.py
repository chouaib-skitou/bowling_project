from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
window = config.window
canvas = config.canvas

CANVA_WIDTH = config.CANVA_WIDTH
CANVA_HEIGHT = config.CANVA_HEIGHT
WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT


def players_list(count):
    global window, canvas
    window = tkinter.Tk()  # Corrected from ttk.Tk() to tkinter.Tk()
    window.title('Bowling score manager ultimate')

    # Gestion de la fenêtre
    canvas = tkinter.Canvas(window, width=CANVA_WIDTH, height=CANVA_HEIGHT)  # Corrected from ttk.Canvas to tkinter.Canvas
    canvas.place(x=10, y=10)
    window_size_str = "{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.geometry(window_size_str)

    # Centrer les widgets dans la fenêtre
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Définir les étiquettes et les entrées pour les joueurs en utilisant une boucle
    for i in range(count):
        ttk.Label(frame, text=f'Player {i + 1}:').grid(row=i, column=0, padx=10, pady=10)
        ttk.Entry(frame, width=20).grid(row=i, column=1, padx=10, pady=10)

    # Ajouter le bouton de validation
    ttk.Button(frame, text="Validate", width=20).grid(row=3, column=0, columnspan=2, pady=10)

    window.mainloop()