import tkinter
from interfaces.play_party import *
from package_party.party_manager import *
from package_party.class_player import *
from tkinter import messagebox  
from tkinter import *
from tkinter import ttk

def players(count,nb_tours,nb_skittles, window, callback):

    def verfi_values(entries):
        # Vérification si l'un des Entry est vide
        for entry in entries:
            if entry.get() == "":
                return messagebox.showerror('Erreur ', " Veuillez renseigner nom de joueur !")
        hide_player_list()
        call_play_party(entries,window)

    def show_player_choice():
        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()
        callback()

    def hide_player_list():
        entry.grid_forget()
        btnValidate.grid_forget()
        btnBack.grid_forget()

    def reinit_player_list():
        hide_player_list()
        init_window(window)

    def call_play_party(entries,window):
        for i, entry in enumerate(entries):
            print(f"Player {i + 1}: {entry.get()}")
            create_player(entry.get()) # création de chaque objet Player
        #Affichage des joueurs
        #indice du premier joueur
        current_player_indice =0
        for joueur in party_manager.players_list:
            print(joueur.name)
            print(len(party_manager.players_list))
        if nb_tours == 1:
            LastFrame(nb_tours,nb_skittles,window,party_manager.players_list[current_player_indice],current_player_indice)
        else:
            play_party(nb_tours,nb_skittles,window,party_manager.players_list[current_player_indice],current_player_indice)


    # Centering the widgets in the window
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    entries = []
    for i in range(count):
        ttk.Label(frame, text=f'Player {i + 1}:').grid(row=i, column=0, padx=10, pady=10)
        entry = ttk.Entry(frame, width=20)
        entry.insert(0, f'Player {i + 1}')
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)
    

    btnValidate = ttk.Button(frame, text="Validate", width=20, command=lambda: [verfi_values(entries)])
    btnValidate.grid(row=count, column=0, columnspan=2, pady=10)
    btnBack = ttk.Button(frame, text="Back", width=20, command=show_player_choice)
    btnBack.grid(row=count+1, column=0, columnspan=2, pady=10)