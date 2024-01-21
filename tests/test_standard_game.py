
from package_party import class_player


def test_normal_game():
    player = class_player.Player(3, "Normal game")
    frame_score_list = [[4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4], [4, 4]]
    assert player.calculateScore(frame_score_list) == 80  # Score total calculé manuellement

def test_perfect_game():
    player = class_player.Player(3, "Perfect game")
    frame_score_list = [['X',''], ['X',''], ['X',''], ['X',''], ['X',''], ['X',''], ['X',''], ['X', ''], ['X', ''], ['X', 'X','X']]
    assert player.calculateScore(frame_score_list) == 300  # Score total calculé manuellement

def test_spare_game():
    player = class_player.Player(3, "Spare game")
    frame_score_list = [[5,'|'], [5,'|'], [5,'|'], [5,'|'], [5,'|'], [5,'|'], [5,'|'], [5,'|'], [5,'|'], [5,'|',5]]
    assert player.calculateScore(frame_score_list) == 150  # Score total calculé manuellement


def test_half_strikes_half_spares_game():
    player = class_player.Player(3, "Alternating Strikes and Spares")
    frame_score_list = [['X', ''], ['X', ''], ['X', ''], ['X', ''], ['X', ''], [5, '|'], [5, '|'], [5, '|'], [5, '|'], [5, '|', 0]]  # Alternance de strikes et spares
    # Alternance de strikes et spares
    # Pour les frames impaires (strikes), nous utilisons ['X', ''],
    # et chaque spare est suivi d'un lancer de 0.
    expected_score = 205  # Score total calculé manuellement
    assert player.calculateScore(frame_score_list) == expected_score



def test_alternating_strikes_spares_game():
    player = class_player.Player(3, "Alternating Strikes and Spares")
    frame_score_list = [['X', ''],[5, '|'], ['X', ''],[5, '|'] ,['X', ''],[5, '|'] ,['X', ''],[5, '|'], ['X', ''],[5,'|',0]]  # Alternance de strikes et spares
    # Alternance de strikes et spares
    # Pour les frames impaires (strikes), nous utilisons ['X', ''],
    # et pour les frames paires (spares), nous utilisons [5, 5] suivi d'un lancer supplémentaire à 0 dans la dernière frame.

    # Calcul du score attendu : chaque strike est suivi de deux lancers de 5 (pour les spares),
    # et chaque spare est suivi d'un lancer de 0.
    expected_score = 190  # Score total calculé manuellement

    assert player.calculateScore(frame_score_list) == expected_score

