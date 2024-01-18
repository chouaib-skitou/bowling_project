from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
from interfaces.players_list import *
from interfaces.main_frame import *
from package_party.party_manager import *
from package_party.class_player import *

#################################" Affichage des Scores##########################################"
def window_score(window):
    # Create a frame to hold the widgets
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    #Affichage des scores
    lbl_score_player = tkinter.Label(window, text="Voici les scores :")
    lbl_score_player.pack()

    i = 1
    for player in party_manager.players_list:
        listSum = 0
        for number in player.list_of_party_score:
            for element in number:
                listSum += int(element)
        ttk.Label(frame, text=str(player.name)).grid(row=i, column=0, padx=10, pady=10)
        ttk.Label(frame, text=str(listSum)).grid(row=i, column=1, padx=10, pady=10)
        i = i + 1

    btnBack = ttk.Button(frame, text="Back", width=20, command=window.destroy)
    btnBack.grid(row=i+1, column=0, columnspan=2, pady=10)
    window.mainloop()