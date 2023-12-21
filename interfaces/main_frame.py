from . import config 
import tkinter
from tkinter import *
from tkinter import ttk 
window = config.window
canvas = config.canvas

CANVA_WIDTH = config.CANVA_WIDTH
CANVA_HEIGHT = config.CANVA_HEIGHT
WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT

from interfaces.player_choice import init_window
def main_frame():
    global window, canvas
    window = tkinter.Tk()  # Corrected from ttk.Tk() to tkinter.Tk()
    window.title('Bowling score manager ultimate')

    # Gestion de la fenêtre
    canvas = tkinter.Canvas(window, width=CANVA_WIDTH, height=CANVA_HEIGHT)  # Corrected from ttk.Canvas to tkinter.Canvas
    canvas.place(x=10, y=10)
    window_size_str = "{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.geometry(window_size_str)

    # Centrer les widgets dans la fenêtre
    init_window(window)

    window.mainloop()