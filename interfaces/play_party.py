from . import config
import tkinter
from tkinter import *
from tkinter import ttk
from package_party.party_manager import init_Number,add_player,next_player_frame,start_game
from package_party.class_player import Player

window = config.window
canvas = config.canvas

def play_party(entries, nb_tours, nb_bowling, window):
    # Create a frame to hold the widgets
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Affichage du nom du joueur
    lbl_name_player = tkinter.Label(frame, text=entries[0].get())
    lbl_name_player.grid(row=1, column=1, padx=10, pady=10)

    # Affichage du nombre de partie
    lbl_nb_tour = tkinter.Label(frame, text=" Nombre de tours : " + str(nb_tours))
    lbl_nb_tour.grid(row=1, column=2, padx=10, pady=10)

    # Nombre de quille tombé
    lbl_quille = tkinter.Label(frame, text="Nombre de quilles tombé")
    lbl_quille.grid(row=2, column=1, padx=10, pady=10)

    # Combobox for the number of fallen bowling pins
    list_of_number_falling_bowling = []
    for i in range(int(nb_bowling), 0, -1):
        list_of_number_falling_bowling.append(i)

    combo_Score = ttk.Combobox(frame, values=list_of_number_falling_bowling, state="readonly")
    combo_Score.grid(row=2, column=2, padx=10, pady=10)

    # Score
    lbl_Score = tkinter.Label(frame, text="Score : ")
    lbl_Score.grid(row=3, column=1, padx=10, pady=10)
    # label contenant le score du joueur au cours de la partie
    lbl_Score_Value = tkinter.Label(frame, width=20, borderwidth=1, relief="solid")
    lbl_Score_Value.grid(row=3, column=2, padx=10, pady=10)

    # Validation
    btnValider = Button(frame, text="Valider", command=lambda: [play_game()])
    btnValider.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
