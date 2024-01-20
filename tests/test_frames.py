from package_party import class_player


def test_basic_score():
    player = class_player.Player(1, "Basic Player")
    frame_score_list = [[3, 4], [2, 5], [1, 1], [4, 4], [6, 1], [2, 3], [5, 3], [3, 2], [1, 4], [2, 6]]
    assert player.calculateScore(frame_score_list) == 62  # Score total calculé manuellement


def test_strike_score():
    player = class_player.Player(2, "Strike Player")
    frame_score_list = [['X',''], ['X',''], [3, 4], [4, 4], [6, 1], [2, 3], [5, 3], [3, 2], [1, 4], [2, 6]]
    assert player.calculateScore(frame_score_list) == 93  # Score total calculé manuellement



#EN ATTENDANT DE TROUVER UNE SOLUTION
'''
def test_spare_score():
    player = class_player.Player(3, "Spare Player")
    frame_score_list = [[5, 5], [3, 6], [7, 3], [2, 5], [5, 5], [2, 3], [5, 5], [3, 2], [1, 4], [2, 8, 5]]
                                                                                                #[10,3,4]
    assert player.calculateScore(frame_score_list) == 96  # Score total calculé manuellement
'''
