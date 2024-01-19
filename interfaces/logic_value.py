from . import config
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox  
from package_party.party_manager import *
from package_party.class_player import *
from interfaces.play_party import play_party


# def verif_Skittles(nb_skittles_fallen):
#     #messagebox.showerror('Erreur ', "\t\tVeuillez renseigner un nombre cohérent :")
#     return nb_skittles_fallen

def verif_Skittles(nb):
    play_party(entries,nb_tours,nb_skittles,window,party_manager.players_list[nb+1],nb+1)