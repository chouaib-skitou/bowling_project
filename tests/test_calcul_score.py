# import pytest
# from bowling_logic import bowling

# def test_strike_bonus():
#     game = bowling.BowlingGame()
#     game.roll(10)  # Strike
#     game.roll(3)
#     game.roll(4)
#     for _ in range(16):  # Reste de la partie
#         game.roll(0)
#     assert game.score() == 24  # 10 (strike) + 3 + 4 (bonus) + 3 + 4

# def test_spare_bonus():
#     game = bowling.BowlingGame()
#     game.roll(5)
#     game.roll(5)  # Spare
#     game.roll(3)
#     for _ in range(17):  # Reste de la partie
#         game.roll(0)
#     assert game.score() == 16  # 5 + 5 (spare) + 3 (bonus) + 3

# def test_mixed_game():
#     game = bowling.BowlingGame()
#     # Exemple: Strike, 7-2, Spare, 3-0, etc.
#     rolls = [10, 7, 2, 5, 5, 3, 0] + [0] * 12
#     for pins in rolls:
#         game.roll(pins)
#     expected_score = 0 # Calculer le score attendu
#     assert game.score() == expected_score

# def test_normal_game():
#     game = bowling.BowlingGame
#     for _ in range(20):
#         game.roll(4)
#     assert game.score() == 80  # 4 quilles * 20 lancers
