
from bowling_project.bowling_logic.bowling_logic import askAndCheckSkittlesInTen,checkCoherentSkittles
from bowling_project.bowling_logic import bowling
import pytest

'''
def test_askAndCheckSkittlesInTen(mocker):
    # Simulation d'entrées utilisateur
    mocker.patch('builtins.input', side_effect=["11", "-1", "5"])

    # Appel de la fonction
    result = askAndCheckSkittlesInTen()

    # Vérification du résultat
    assert result == 5, "La fonction doit retourner 5"

    result = askAndCheckSkittlesInTen()

    assert result == 5  # La fonction doit retourner la valeur valide

def test_check_coherent_skittles(mocker):
    # Simuler une séquence d'entrées : d'abord 8 (invalide pour le premier lancer de 3), puis 6 (valide)
    mocker.patch('builtins.input', side_effect=['8', '6'])

    frame_score = [3]  # Premier lancer de la frame a renversé 3 quilles
    result = checkCoherentSkittles(8, frame_score)  # On teste avec 8 quilles au début, qui est invalide

    assert result == 6  # Doit retourner 6, qui est la seconde entrée valide



def test_invalid_input_handling(mocker):
    # Crée une instance de BowlingGame
    game = bowling.BowlingGame()

    # Test avec une entrée négative
    with pytest.raises(ValueError):
        game.roll(-1)

    # Test avec une entrée supérieure au nombre maximum de quilles
    with pytest.raises(ValueError):
        game.roll(11) '''