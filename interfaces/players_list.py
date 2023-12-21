from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
window = config.window
canvas = config.canvas


def players_list(count,window):

    # Centrer les widgets dans la fenêtre
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Définir les étiquettes et les entrées pour les joueurs en utilisant une boucle
    for i in range(count):
        ttk.Label(frame, text=f'Player {i + 1}:').grid(row=i, column=0, padx=10, pady=10)
        ttk.Entry(frame, width=20).grid(row=i, column=1, padx=10, pady=10)

    # Ajouter le bouton de validation
    ttk.Button(frame, text="Validate", width=20).grid(row=3, column=0, columnspan=2, pady=10)