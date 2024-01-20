from . import config
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox  
from interfaces.Score import *
from package_party.party_manager import *
from package_party.class_player import *

window = config.window
canvas = config.canvas

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#Passe au joueur suivant, pour le moment changement à chaque lancer au lieu de laisser 2 lancer pour chaque joueur
def change_player(nb_tours, nb_skittles, window,current_player_indice):
    if current_player_indice == len(party_manager.players_list)-1:#si on atteint le dernier joueur de la liste, on reprends au début, et un tours est passé
        current_player_indice = -1
        nb_tours = nb_tours - 1
    if nb_tours == 0:
        clear_frame(window)
        return window_score(window)
    if nb_tours == 1: #dernier tours
        clear_frame(window)
        return LastFrame(nb_tours,nb_skittles,window,party_manager.players_list[current_player_indice+1],current_player_indice+1)
    play_party(nb_tours,nb_skittles,window,party_manager.players_list[current_player_indice+1],current_player_indice+1)

#mise à jour des Score, pour le moment il ne marche que pour un lancer
def majScore(nb_skittles_fallen,current_player_indice):
    party_manager.players_list[current_player_indice].list_of_party_score.append(nb_skittles_fallen)
    print(" - " + party_manager.players_list[current_player_indice].name + " : " + str(party_manager.players_list[current_player_indice].list_of_party_score))

#on vérifie les valeurs de quilles tombées entrés dans le formulaire 
def verfi_values_void(first,second):
    if((first == "" and second == "") or (first == "") or (second == "")):
        return messagebox.showerror('Erreur ', " Veuillez renseigner toutes les valeurs !!! ")


def play_party(nb_tours, nb_skittles, window,current_player,current_player_indice):
    # Create a frame to hold the widgets
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Affichage du nom du joueur
    lbl_name_player = tkinter.Label(frame, text=str(current_player.name))
    lbl_name_player.grid(row=1, column=1, padx=10, pady=10)

    # Affichage du nombre de partie
    lbl_nb_tour = tkinter.Label(frame, text="Nombre de tours : " + str(nb_tours))
    lbl_nb_tour.grid(row=1, column=2, padx=10, pady=10)

    # Nombre de quille tombées
    lbl_quille_first = tkinter.Label(frame, text="Nombre de quilles tombées, premier lancé")
    entry_quille = tkinter.Entry(frame, width=20)
    lbl_quille_first.grid(row=2, column=1, padx=10, pady=10)


    # Combobox for the number of fallen skittles pins
    list_of_number_falling_skittles_first = []
    for i in range(int(nb_skittles), -1, -1):
        list_of_number_falling_skittles_first.append(i)

    combo_Score_value = StringVar()
    combo_Score_first = ttk.Combobox(frame, values=list_of_number_falling_skittles_first, state="readonly", textvariable=combo_Score_value)
    combo_Score_first.grid(row=2, column=2, padx=10, pady=10)

    # Nombre de quille tombées
    lbl_quille_second = tkinter.Label(frame, text="Nombre de quilles tombées, deuxième lancé")
    entry_quille_second = tkinter.Entry(frame, width=20)
    lbl_quille_second.grid(row=3, column=1, padx=10, pady=10)

    # Création de la deuxième ComboBox
    combo_Score_second = ttk.Combobox(frame, values=list_of_number_falling_skittles_first, state="readonly")
    combo_Score_second.grid(row=3, column=2, padx=10, pady=10)

    # Vérification de la valeur de la première ComboBox
    def check_first_combo_value(*args):
        if combo_Score_value.get() == str(nb_skittles): #strike donc pas de second lancé
            combo_Score_second.config(values = "0",state="disabled")
            combo_Score_second.current(0)
        else:
            list_of_number_falling_skittles_second = []
            for i in range((int(nb_skittles)-int(combo_Score_value.get())), -1, -1): #on donne un nombre de quilles restantes cohérents avec le premier lancé
                list_of_number_falling_skittles_second.append(i)
            combo_Score_second.config(values=list_of_number_falling_skittles_second,state="readonly")

    # Associer la fonction de vérification au changement de la valeur de la première ComboBox
    combo_Score_value.trace_add("write", check_first_combo_value)
    
    listSum = 0
    for number in current_player.list_of_party_score:
        for element in number:
            if isinstance(element, int):
                listSum += element
    

    # Score
    lbl_Score = tkinter.Label(frame, text="Score : ")
    lbl_Score.grid(row=4, column=1, padx=10, pady=10)
    # label contenant le score du joueur au cours de la partie
    lbl_Score_Value = tkinter.Label(frame, width=20, borderwidth=1, relief="solid",text=str(listSum))
    lbl_Score_Value.grid(row=4, column=2, padx=10, pady=10)

    # Validation
    btnValider = Button(frame, text="Valider", command=lambda: [verfi_values_void(combo_Score_first.get(),combo_Score_second.get()),current_player.add_scores_to_frame(int(combo_Score_first.get()),int(combo_Score_second.get())),change_player(int(nb_tours), nb_skittles, window,int(current_player_indice))]) #verif_Skittles(combo_Score.get())
    btnValider.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

def LastFrame(nb_tours, nb_skittles, window,current_player,current_player_indice):
    print("LASTFRAME")
    # Create a frame to hold the widgets
    frame = ttk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Affichage du nom du joueur
    lbl_name_player = tkinter.Label(frame, text=str(current_player.name))
    lbl_name_player.grid(row=1, column=1, padx=10, pady=10)

    # Affichage du nombre de partie
    lbl_nb_tour = tkinter.Label(frame, text="Nombre de tours : " + str(nb_tours))
    lbl_nb_tour.grid(row=1, column=2, padx=10, pady=10)

    # Nombre de quille tombées
    lbl_quille_first = tkinter.Label(frame, text="Nombre de quilles tombées, premier lancé")
    entry_quille = tkinter.Entry(frame, width=20)
    lbl_quille_first.grid(row=2, column=1, padx=10, pady=10)


    # Combobox for the number of fallen skittles pins
    list_of_number_falling_skittles_first = []
    for i in range(int(nb_skittles), -1, -1):
        list_of_number_falling_skittles_first.append(i)

    combo_Score_value = StringVar()
    combo_Score_first = ttk.Combobox(frame, values=list_of_number_falling_skittles_first, state="readonly", textvariable=combo_Score_value)
    combo_Score_first.grid(row=2, column=2, padx=10, pady=10)

    # Nombre de quille tombées
    lbl_quille_second = tkinter.Label(frame, text="Nombre de quilles tombées, deuxième lancé")
    entry_quille_second = tkinter.Entry(frame, width=20)
    lbl_quille_second.grid(row=3, column=1, padx=10, pady=10)

    # Création de la deuxième ComboBox
    combo_Score_second_value = StringVar()
    combo_Score_second = ttk.Combobox(frame, values=list_of_number_falling_skittles_first, state="readonly", textvariable=combo_Score_second_value)
    combo_Score_second.grid(row=3, column=2, padx=10, pady=10)

    num_additional_combos = 0
    combo_Score_third = None
    validation_button_visible = False
    # Vérification de la valeur de la première ComboBox
    def check_first_combo_value(*args):
        global validation_button_visible
        value_first = int(combo_Score_value.get()) if combo_Score_value.get() else 0
        value_second = int(combo_Score_second_value.get()) if combo_Score_second_value.get() else 0
        nonlocal num_additional_combos,combo_Score_third
        if value_first + value_second == nb_skittles: # s'il y a un SPARE
            if num_additional_combos < 1:
                num_additional_combos += 1

                # Ajouter une nouvelle ComboBox et une entrée
                lbl_quille_third = tkinter.Label(frame, text="Nombre de quilles tombées, troisième lancé")
                lbl_quille_third.grid(row=4, column=1, padx=10, pady=10)

                combo_Score_third_value = StringVar()
                combo_Score_third = ttk.Combobox(frame, values=list_of_number_falling_skittles_first, state="readonly", textvariable=combo_Score_third_value)
                combo_Score_third.grid(row=4, column=2, padx=10, pady=10)

            #nouveau bouton valider
            validation_button_visible = True
            btnValidation = Button(frame, text="Validation", command=lambda: [verfi_values_void(combo_Score_first.get(), combo_Score_second.get()),current_player.add_scores_to_frame(int(combo_Score_first.get()), int(combo_Score_second.get()),int(combo_Score_third.get())), change_player(int(nb_tours), nb_skittles, window, int(current_player_indice))])
            btnValidation.grid(row=6 + num_additional_combos, column=1, columnspan=2, padx=10, pady=10)


        if combo_Score_value.get() == str(nb_skittles):  # s'il y a un STRIKE
            if num_additional_combos < 1:
                num_additional_combos += 1

               # Ajouter une nouvelle ComboBox et une entrée
                lbl_quille_second = tkinter.Label(frame, text="SPARE : troisième lancé")
                entry_quille_second = tkinter.Entry(frame, width=20)
                lbl_quille_second.grid(row=4, column=1, padx=10, pady=10)
                combo_Score_third_value = StringVar()
                combo_Score_third = ttk.Combobox(frame, values=list_of_number_falling_skittles_first, state="readonly", textvariable=combo_Score_third_value)
                combo_Score_third.grid(row=4, column=2, padx=10, pady=10)

            #nouveau bouton valider
            validation_button_visible = True
            btnValidation = Button(frame, text="Validation", command=lambda: [verfi_values_void(combo_Score_first.get(), combo_Score_second.get()),current_player.add_scores_to_frame(int(combo_Score_first.get()), int(combo_Score_second.get()),int(combo_Score_third.get())), change_player(int(nb_tours), nb_skittles, window, int(current_player_indice))])
            btnValidation.grid(row=6 + num_additional_combos, column=1, columnspan=2, padx=10, pady=10)
        if validation_button_visible:
            btnValider.grid_remove()  # Masquer le bouton btnValider
            

    # Associer la fonction de vérification au changement de la valeur de la première ComboBox
    combo_Score_value.trace_add("write", check_first_combo_value)
    combo_Score_second_value.trace_add("write", check_first_combo_value)
    #calcul du score
    listSum = 0
    for number in current_player.list_of_party_score:
        for element in number:
            if isinstance(element, int):
                listSum += element

    # Score
    lbl_Score = tkinter.Label(frame, text="Score : ")
    lbl_Score.grid(row=5, column=1, padx=10, pady=10)
    # label contenant le score du joueur au cours de la partie
    lbl_Score_Value = tkinter.Label(frame, width=20, borderwidth=1, relief="solid",text=str(listSum))
    lbl_Score_Value.grid(row=5, column=2, padx=10, pady=10)

# Validation
    btnValider = Button(frame, text="Valider", command=lambda: [verfi_values_void(combo_Score_first.get(), combo_Score_second.get()),current_player.add_scores_to_frame(int(combo_Score_first.get()), int(combo_Score_second.get())), change_player(int(nb_tours), nb_skittles, window, int(current_player_indice))])
    btnValider.grid(row=6 + num_additional_combos, column=1, columnspan=2, padx=10, pady=10)
