from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
from interfaces.players_list import *
from interfaces.main_frame import *
from package_party.party_manager import *
from package_party.class_player import *


def tous_egaux(liste):
    return all(element == liste[0] for element in liste)

def window_score(window):
    # Create a frame to hold the widgets
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    #Affichage des scores

    i = 2
    tabScore = []
    for player in party_manager.players_list:
        listSum = 0
        for number in player.list_of_party_score:
            for element in number:
                listSum += int(element)
        ttk.Label(frame, text=str(player.name)).grid(row=i, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Voici ton score : "+str(listSum)).grid(row=i, column=1, padx=10, pady=10)
        i = i + 1
        tabScore.append(listSum)
    print(max(tabScore))
    index_max_value = tabScore.index(max(tabScore))
    print(index_max_value)
    if tous_egaux(tabScore):
        lblWinner = ttk.Label(frame, text="Pas de gagnant")
        lblWinner.grid(row=i+1, column=0, padx=10, pady=10)
    else:
        lblWinner = ttk.Label(frame, text="The Winner is : "+str(party_manager.players_list[index_max_value].name))
        lblWinner.grid(row=i+1, column=0, padx=10, pady=10)

    btnBack = ttk.Button(frame, text="Back", width=20, command=window.destroy)
    btnBack.grid(row=i+2, column=0, columnspan=2, pady=10)
    window.mainloop()