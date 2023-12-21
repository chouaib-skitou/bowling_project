from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
from interfaces.players_list import players_list,ChoixPlayer,Score
window = config.window
canvas = config.canvas

CANVA_WIDTH = config.CANVA_WIDTH
CANVA_HEIGHT = config.CANVA_HEIGHT
WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT

#################################" Affichage des Scores##########################################"
def window_score():
    global window, canvas
    window = tkinter.Tk()
    window.title('Score final')

    # window gestion
    canvas = tkinter.Canvas(window, width=CANVA_WIDTH, height=CANVA_HEIGHT, bg='white')
    canvas.place(x=10, y=10)
    window_size_str = "{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.geometry(window_size_str)

    #Affichage des scores
    lbl_score_player = tkinter.Label(window, text="Voici les scores :")
    lbl_score_player.pack()

    #dictionnaire contenant le nom de chaque joueur et son score final
    tab_joueur = {"Player1": 50, "Player2": 80, "Player3": 11}

    for player, score in tab_joueur.items():
        lbl_score_player = Label(window, text=f"{player} : {score}")
        lbl_score_player.pack()

    window.mainloop()