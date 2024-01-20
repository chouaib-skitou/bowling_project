from package_party import class_player


# Test for the last frame with a strike
def test_last_frame_scenarios_score_strike():
        player = class_player.Player(1, "Scenarios_score_strike")
        frame_score_list = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 3, 4]]
        assert player.calculateScore(frame_score_list) == 17  # Score total calculé manuellement # 10 (strike) + 3 + 4


# Test for the last frame with a spare
def test_last_frame_scenarios_score_spare():
    player = class_player.Player(1, "Scenarios_score_strike")
    frame_score_list = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [5, 5, 4]]
    assert player.calculateScore(frame_score_list) == 14  # Score total calculé manuellement  # 5 + 5 (spare) + 4

    # Test for the last frame with a spare


def test_last_frame_scenarios_without_score_spareOrStrike():
    player = class_player.Player(1, "Scenarios_score_strike")
    frame_score_list = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [3, 4]]
    assert player.calculateScore(frame_score_list) == 7  # Score total calculé manuellement  # 3 + 4 (spare)

