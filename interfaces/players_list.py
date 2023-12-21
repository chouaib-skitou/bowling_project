import tkinter
from tkinter import *
from tkinter import ttk

def players_list(count, window, callback):
    def show_player_choice():
        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()
        callback()

    def playParty(entries):
        for i, entry in enumerate(entries):
            print(f"Player {i + 1}: {entry.get()}")

    # Centering the widgets in the window
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    entries = []
    for i in range(count):
        ttk.Label(frame, text=f'Player {i + 1}:').grid(row=i, column=0, padx=10, pady=10)
        entry = ttk.Entry(frame, width=20)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    ttk.Button(frame, text="Validate", width=20, command=lambda: playParty(entries)).grid(row=count, column=0, columnspan=2, pady=10)
    ttk.Button(frame, text="Back", width=20, command=show_player_choice).grid(row=count+1, column=0, columnspan=2, pady=10)
