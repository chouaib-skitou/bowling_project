import pytest
from bowling_game import BowlingGame  # Remplacez par le chemin correct de votre classe

def test_last_frame_scenarios():
    # Test pour la dernière frame avec un strike
    game_strike = BowlingGame()
    for _ in range(9):  # Premières 9 frames
        game_strike.roll(0)
        game_strike.roll(0)
    game_strike.roll(10)  # Strike dans la dernière frame
    game_strike.roll(3)   # Lancer supplémentaire 1
    game_strike.roll(4)   # Lancer supplémentaire 2
    score_strike = game_strike.score()

    # Test pour la dernière frame avec un spare
    game_spare = BowlingGame()
    for _ in range(9):  # Premières 9 frames
        game_spare.roll(0)
        game_spare.roll(0)
    game_spare.roll(5)   # Premier lancer de la dernière frame
    game_spare.roll(5)   # Spare dans la dernière frame
    game_spare.roll(4)   # Lancer supplémentaire
    score_spare = game_spare.score()

    # Test pour la dernière frame sans strike ni spare
    game_normal = BowlingGame()
    for _ in range(9):  # Premières 9 frames
        game_normal.roll(0)
        game_normal.roll(0)
    game_normal.roll(3)  # Premier lancer de la dernière frame
    game_normal.roll(4)  # Deuxième lancer de la dernière frame
    score_normal = game_normal.score()

    # Vérifier les scores attendus pour chaque scénario
    assert score_strike == 17  # 10 (strike) + 3 + 4
    assert score_spare == 14   # 5 + 5 (spare) + 4
    assert score_normal == 7   # 3 + 4
