from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
window = config.window
canvas = config.canvas

def play_party(entries,window):
    nbTour = 10 # Nombre de tours restant dans la partie

    # Centrer les widgets dans la fenêtre
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    #Affichage du nom du joueur
    lbl_name_player = tkinter.Label(window, text=entries[0].get())
    lbl_name_player.grid(row=1, column=1, padx=10, pady=10)

    #Affichage du nombre de partie
    lbl_nb_tour = tkinter.Label(window, text=" Nombre de tours : " + str(nbTour))
    lbl_nb_tour.grid(row=1, column=6, padx=10, pady=10)

    #Nombre de quille tombé
    lbl_quille = tkinter.Label(window, text="Nombre de quilles tombé")
    entry_quille = ttk.Entry(frame, width=20)
    lbl_quille.grid(row=3, column=3, padx=10, pady=10)
    entry_quille.grid(row=3, column=4, padx=10, pady=10)


    #Score
    lbl_Score = tkinter.Label(window, text="Score : ")
    entry_Score = ttk.Entry(frame, width=20)
    lbl_Score.grid(row=5, column=3, padx=10, pady=10)
    entry_Score.grid(row=6, column=3, padx=10, pady=10)

    #Validation
    btnValider = Button(window, text="Valider" )
    btnValider.grid(row=7, column=3, padx=10, pady=10)


