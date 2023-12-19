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


def init_window():
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

    list_of_number_player = [1, 2, 3, 4]
    combo_number_player = ttk.Combobox(window, values=list_of_number_player)

    # Select the current element
    combo_number_player.current(0)
    combo_number_player.pack()

    var = StringVar()
    label = Label(window, textvariable=var, relief=RAISED)
    var.set("Bowling score manager ultimate")
    label.pack()



    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_window()


def score_manager():
    return

