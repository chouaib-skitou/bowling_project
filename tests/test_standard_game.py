import pytest
from bowling_logic import bowling

def test_normal_game():
    game = bowling.BowlingGame()
    for _ in range(20):  # 20 lancers dans un jeu normal (10 frames x 2 lancers)
        game.roll(4)  # 4 quilles renversées à chaque lancer

    assert game.score() == 80  # Le score attendu est 80


def test_perfect_game():
    game = bowling.BowlingGame()
    for _ in range(12):  # 12 strikes pour une partie parfaite
        game.roll(10)
    assert game.score() == 300  # Le score d'une partie parfaite est 300


def test_all_spares_game():
    game = bowling.BowlingGame()
    for _ in range(21):  # 20 lancers pour les 10 frames, plus 1 lancer bonus
        game.roll(5)  # 5 quilles par lancer pour faire un spare à chaque fois
    assert game.score() == 150  # Le score total pour ce scénario est 150

'''
def test_alternating_strikes_spares_game():
    game = bowling.BowlingGame()
    for frame in range(1, 11):  # 10 frames au total
        if frame % 2 == 1:  # Frames impaires: strike
            game.roll(10)
        else:  # Frames paires: spare (5 + 5) puis un lancer à zéro
            game.roll(5)
            game.roll(5)
            game.roll(0)

    expected_score = 150 # Calcul du score attendu
    
    Pour calculer expected_score, considérez que chaque strike est suivi de deux lancers de 5 (pour les spares), 
    et chaque spare est suivi d'un lancer de 0. Vous devrez effectuer ce calcul en fonction des règles exactes 
    de scoring que vous utilisez dans votre jeu.
    
    assert game.score() == expected_score'''

