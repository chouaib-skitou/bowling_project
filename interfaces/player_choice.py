import tkinter
from tkinter import *
from tkinter import ttk
from interfaces.players_list import players_list

def init_window(window):
    def hide_player_choice():
        lbl_number_player.pack_forget()
        combo_number_player.pack_forget()
        btnValider.pack_forget()

    def reinit_player_choice():
        hide_player_choice()
        init_window(window)

    def AffichageJoueur(nb):
        nb = int(nb)
        players_list(nb, window, reinit_player_choice)

    # Selection of the number of players
    lbl_number_player = tkinter.Label(window, text="Choisissez le nombre de joueurs 😊")
    lbl_number_player.pack()

    list_of_number_player = [1, 2, 3, 4]
    combo_number_player = ttk.Combobox(window, values=list_of_number_player, state="readonly")
    combo_number_player.current(0)
    combo_number_player.pack()

    btnValider = Button(window, text="Bowling score manager ultimate", command=lambda: [hide_player_choice(), AffichageJoueur(combo_number_player.get())])
    btnValider.pack()