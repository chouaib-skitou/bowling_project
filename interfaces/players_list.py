from . import config 
from interfaces.play_party import play_party
import tkinter
from tkinter import *
from tkinter import ttk 
window = config.window
canvas = config.canvas

#fonction de récupération du pseudo du joueur
def call_play_party(entries,window):
        for i, entry in enumerate(entries):
            print(f"Player {i + 1}: {entry.get()}")
        play_party(entries,window)

def players_list(count,window):

    # Centrer les widgets dans la fenêtre
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Liste pour stocker les objets Entry
    entries = []

    # Définir les étiquettes et les entrées pour les joueurs en utilisant une boucle
    for i in range(count):
        ttk.Label(frame, text=f'Player {i + 1}:').grid(row=i, column=0, padx=10, pady=10)
        entry = ttk.Entry(frame, width=20)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    # Ajouter le bouton de validation
    ttk.Button(frame, text="Validate", width=20,command = lambda:call_play_party(entries,window)).grid(row=3, column=0, columnspan=2, pady=10)
