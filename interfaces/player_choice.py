import tkinter
from tkinter import *
from tkinter import ttk
from interfaces.players_list import players_list
from package_party.party_manager import *
from package_party.class_player import *

def init_window(window):
    def hide_player_choice():
        lbl_number_player.pack_forget()
        combo_number_player.pack_forget()
        lbl_number_tours.pack_forget()
        combo_number_tours.pack_forget()
        lbl_number_bowling.pack_forget()
        combo_number_bowling.pack_forget()
        btnValider.pack_forget()

    def reinit_player_choice():
        hide_player_choice()
        init_window(window)

    def AffichageJoueur(nb_player,nb_tours,nb_bowling):
        nb_player = int(nb_player)
        party_manager.NUMBER_OF_SKITLES = nb_bowling
        party_manager.NUMER_OF_FRAME = nb_tours
        players_list(nb_player,nb_tours,nb_bowling, window, reinit_player_choice)
        


    # Selection of the number of players
    lbl_number_player = tkinter.Label(window, text="Choisissez le nombre de joueurs 😊")
    lbl_number_player.pack()

    list_of_number_player = [1, 2, 3, 4]
    combo_number_player = ttk.Combobox(window, values=list_of_number_player, state="readonly")
    combo_number_player.current(0)
    combo_number_player.pack()

    # Selection of the number of frame
    lbl_number_tours = tkinter.Label(window, text="Choisissez le nombre de tours 😊")
    lbl_number_tours.pack()

    list_of_number_tours = [10,9,8,7,6,5,4,3,2,1]
    combo_number_tours = ttk.Combobox(window, values=list_of_number_tours, state="readonly")
    combo_number_tours.current(0)
    combo_number_tours.pack()

    # Selection of the number of bowling
    lbl_number_bowling = tkinter.Label(window, text="Choisissez le nombre de quilles 😊")
    lbl_number_bowling.pack()

    list_of_number_bowling = [10,9,8,7,6,5,4,3,2,1]
    combo_number_bowling = ttk.Combobox(window, values=list_of_number_bowling, state="readonly")
    combo_number_bowling.current(0)
    combo_number_bowling.pack()

    btnValider = Button(window, text="Bowling score manager ultimate", command=lambda: [hide_player_choice(), AffichageJoueur(combo_number_player.get(),combo_number_tours.get(),combo_number_bowling.get())])
    btnValider.pack()