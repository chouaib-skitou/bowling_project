import tkinter
from interfaces.play_party import play_party
from package_party.party_manager import init_Number,add_player,next_player_frame,start_game,create_player
from package_party.class_player import Player
from tkinter import *
from tkinter import ttk

def players_list(count,nb_tours,nb_bowling, window, callback):
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
        create_player(entries) # création de chaque objet Player
        print(players_list)
        play_party(entries,nb_tours,nb_bowling,window)

    # Centering the widgets in the window
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    entries = []
    for i in range(count):
        ttk.Label(frame, text=f'Player {i + 1}:').grid(row=i, column=0, padx=10, pady=10)
        entry = ttk.Entry(frame, width=20)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    btnValidate = ttk.Button(frame, text="Validate", width=20, command=lambda: [hide_player_list(),call_play_party(entries,window)])
    btnValidate.grid(row=count, column=0, columnspan=2, pady=10)
    btnBack = ttk.Button(frame, text="Back", width=20, command=show_player_choice)
    btnBack.grid(row=count+1, column=0, columnspan=2, pady=10)