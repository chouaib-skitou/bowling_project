from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
from interfaces.players_list import players_list
window = config.window
canvas = config.canvas

CANVA_WIDTH = config.CANVA_WIDTH
CANVA_HEIGHT = config.CANVA_HEIGHT
WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT

#################################" Choix du nombre de joueurs  ##########################################"
def init_window():
    def AffichageJoueur(nb):
        players_list(nb)
    global window, canvas
    window = tkinter.Tk()
    window.title('Bowling score manager ultimate')

    # window gestion
    canvas = tkinter.Canvas(window, width=CANVA_WIDTH, height=CANVA_HEIGHT, bg='white')
    canvas.place(x=10, y=10)
    window_size_str = "{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.geometry(window_size_str)

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
    window.mainloop()
