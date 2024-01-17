from . import config
import tkinter
from tkinter import *
from tkinter import ttk
from package_party.party_manager import *
from package_party.class_player import *

window = config.window
canvas = config.canvas
def verif_Skittles(entries, nb_tours, nb_skittles, window,nb):
    if nb == len(party_manager.players_list)-1:
        nb = -1
    if nb_tours == 0:
        print("FIN")
    play_party(entries,nb_tours-1,nb_skittles,window,party_manager.players_list[nb+1],nb+1)

def play_party(entries, nb_tours, nb_skittles, window,current_player,current_player_indice):
    # Create a frame to hold the widgets
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Affichage du nom du joueur
    lbl_name_player = tkinter.Label(frame, text=str(current_player.name))
    lbl_name_player.grid(row=1, column=1, padx=10, pady=10)

    # Affichage du nombre de partie
    lbl_nb_tour = tkinter.Label(frame, text="Nombre de tours : " + str(nb_tours))
    lbl_nb_tour.grid(row=1, column=2, padx=10, pady=10)

    # Nombre de quille tombées
    lbl_quille = tkinter.Label(frame, text="Nombre de quilles tombées")
    entry_quille = tkinter.Entry(frame, width=20)
    lbl_quille.grid(row=2, column=1, padx=10, pady=10)


    # Combobox for the number of fallen skittles pins
    list_of_number_falling_skittles = []
    for i in range(int(nb_skittles), 0, -1):
        list_of_number_falling_skittles.append(i)

    combo_Score = ttk.Combobox(frame, values=list_of_number_falling_skittles, state="readonly")
    combo_Score.grid(row=2, column=2, padx=10, pady=10)

    # Score
    lbl_Score = tkinter.Label(frame, text="Score : ")
    lbl_Score.grid(row=3, column=1, padx=10, pady=10)
    # label contenant le score du joueur au cours de la partie
    lbl_Score_Value = tkinter.Label(frame, width=20, borderwidth=1, relief="solid")
    lbl_Score_Value.grid(row=3, column=2, padx=10, pady=10)

    # Validation
    btnValider = Button(frame, text="Valider", command=lambda: [verif_Skittles(entries, int(nb_tours), nb_skittles, window,int(current_player_indice))]) #verif_Skittles(combo_Score.get())
    btnValider.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

