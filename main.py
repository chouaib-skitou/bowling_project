def sum(a, b):
    return a + b



print(sum(2,2))


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter
from tkinter import *
from tkinter import ttk

# Canva and window
window = 0
canvas = 0

CANVA_WIDTH = 200
CANVA_HEIGHT = 50
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Players
num_player_selection = False
num_players = 0
playersScores = []


def players_list(count):
    global window, canvas
    window = tkinter.Tk()  # Corrected from ttk.Tk() to tkinter.Tk()
    window.title('Bowling score manager ultimate')

    # Gestion de la fenêtre
    canvas = tkinter.Canvas(window, width=CANVA_WIDTH, height=CANVA_HEIGHT)  # Corrected from ttk.Canvas to tkinter.Canvas
    canvas.place(x=10, y=10)
    window_size_str = "{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.geometry(window_size_str)

    # Centrer les widgets dans la fenêtre
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Définir les étiquettes et les entrées pour les joueurs en utilisant une boucle
    for i in range(count):
        ttk.Label(frame, text=f'Player {i + 1}:').grid(row=i, column=0, padx=10, pady=10)
        ttk.Entry(frame, width=20).grid(row=i, column=1, padx=10, pady=10)

    # Ajouter le bouton de validation
    ttk.Button(frame, text="Validate", width=20).grid(row=3, column=0, columnspan=2, pady=10)

    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    players_list(2)