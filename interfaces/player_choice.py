from interfaces.players_list import players_list
import tkinter
from tkinter import *
from tkinter import ttk 
def init_window(window):
    def AffichageJoueur(nb):
        nb = int(nb)
        players_list(nb,window)

    # Selection of the numbers of players
    lbl_number_player = tkinter.Label(window, text="Choisissez le nombre de joueurs :")
    lbl_number_player.pack()

    list_of_number_player = [1,2, 3, 4]
    combo_number_player = ttk.Combobox(window, values=list_of_number_player, state="readonly")

    # Select the current element
    combo_number_player.current(0)
    combo_number_player.pack()

    # dès que le bouton est cliqué on renvoie le nombre de joueur choisit
    btnValider = Button(window, text="Bowling score manager ultimate",command = lambda:AffichageJoueur(combo_number_player.get()) )
    btnValider.pack()
