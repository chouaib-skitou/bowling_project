from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
window = config.window
canvas = config.canvas

def play_party(entries, window):
    nbTour = 10  # Nombre de tours restant dans la partie

    # Create a frame to hold the widgets
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Affichage du nom du joueur
    lbl_name_player = tkinter.Label(frame, text=entries[0].get())
    lbl_name_player.grid(row=1, column=1, padx=10, pady=10)

    # Affichage du nombre de partie
    lbl_nb_tour = tkinter.Label(frame, text=" Nombre de tours : " + str(nbTour))
    lbl_nb_tour.grid(row=1, column=2, padx=10, pady=10)

    # Nombre de quille tombé
    lbl_quille = tkinter.Label(frame, text="Nombre de quilles tombé")
    entry_quille = tkinter.Entry(frame, width=20)
    lbl_quille.grid(row=2, column=1, padx=10, pady=10)
    entry_quille.grid(row=2, column=2, padx=10, pady=10)

    # Score
    lbl_Score = tkinter.Label(frame, text="Score : ")
    entry_Score = tkinter.Entry(frame, width=20)
    lbl_Score.grid(row=3, column=1, padx=10, pady=10)
    entry_Score.grid(row=3, column=2, padx=10, pady=10)

    # Validation
    btnValider = Button(frame, text="Valider")
    btnValider.grid(row=4, column=1, columnspan=2, padx=10, pady=10)


