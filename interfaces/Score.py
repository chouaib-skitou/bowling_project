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

    # Affichage des scores

    i = 2
    tabScore = []
    for joueur in party_manager.players_list:
        ttk.Label(frame, text=str(joueur.name)).grid(row=i, column=0, padx=10, pady=10)
        ttk.Label(frame, text="Voici ton score : " + str(joueur.calculateScore(joueur.list_of_party_score))).grid(
            row=i, column=1, padx=10, pady=10)
        i = i + 1
        tabScore.append(joueur.calculateScore(joueur.list_of_party_score))

    if tous_egaux(tabScore):
        lblWinner = ttk.Label(frame, text="Pas de gagnant")
        lblWinner.grid(row=i, column=0, padx=10, pady=10)
    else:
        max_score = max(tabScore)
        winners = [player.name for player, score in zip(party_manager.players_list, tabScore) if score == max_score]
        winner_text = "The Winners are: " + ", ".join(winners)
        lblWinner = ttk.Label(frame, text=winner_text)
        lblWinner.grid(row=i, column=0, padx=10, pady=10)

    btnBack = ttk.Button(frame, text="Back", width=20, command=window.destroy)
    btnBack.grid(row=i + 1, column=0, columnspan=2, pady=10)
    window.mainloop()
