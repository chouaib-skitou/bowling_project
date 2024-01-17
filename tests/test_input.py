
from bowling_project.bowling_logic.bowling_logic import askAndCheckSkittlesInTen,checkCoherentSkittles
import pytest

def test_ask_and_check_skittles_in_ten(mocker):
    # Simuler une séquence d'entrées : d'abord 11 (invalide), puis 5 (valide)
    mocker.patch('builtins.input', side_effect=['11', '5'])

    result = askAndCheckSkittlesInTen()

    assert result == 5  # La fonction doit retourner la valeur valide

def test_check_coherent_skittles(mocker):
    # Simuler une séquence d'entrées : d'abord 8 (invalide pour le premier lancer de 3), puis 6 (valide)
    mocker.patch('builtins.input', side_effect=['8', '6'])

    frame_score = [3]  # Premier lancer de la frame a renversé 3 quilles
    result = checkCoherentSkittles(8, frame_score)  # On teste avec 8 quilles au début, qui est invalide

    assert result == 6  # Doit retourner 6, qui est la seconde entrée valide



def test_invalid_input_handling(mocker):
    game = BowlingGame()

    # Simuler une séquence d'entrées : d'abord une entrée invalide, puis une entrée valide
    mocker.patch('builtins.input', side_effect=['-1', '11', '5'])

    # Supposons que vous ayez une méthode pour gérer un tour de jeu
    game.play_turn()

    # Vérifiez si la méthode a correctement ignoré les entrées invalides et accepté la valeur valide
    assert game.current_score() == 5  # Supposant que '5' est la première entrée valide
