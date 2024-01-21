# tests/test_class_player.py

from package_party import old_class_player_functions, party_manager, class_player

import pytest
from unittest import mock


NUMER_OF_FRAME = 10


@pytest.fixture(autouse=True)
def reset_players_list():
    party_manager.players_list = []


def test_add_player():
    player1 = class_player.Player(1, "David")
    party_manager.add_player(player1)
    assert len(party_manager.players_list) == 1
    assert party_manager.players_list[0].name == "David"

    player2 = class_player.Player(2, "Julien")
    party_manager.add_player(player2)
    assert len(party_manager.players_list) == 2
    assert party_manager.players_list[1].name == "Julien"


# Test sur la fonction permettant d'ajouter des joueurs à la partie depuis une liste de nom
def test_create_player():
    names = "Joueur1"
    party_manager.create_player(names)
    party_manager.create_player("Joueur2")

    assert len(party_manager.players_list) == 2
    assert party_manager.players_list[0].name == "Joueur1"
    assert party_manager.players_list[1].name == "Joueur2"

# Test des ajouts de scores au joueur via la fonction add_scores_to_player()
def test_add_scores_to_player():
    player = class_player.Player(0, "Player")




def test_start_game():
    with mock.patch.object(class_player.Player, 'next_turn') as mock_next_turn:
        player1 = class_player.Player(1, "Matthieu")
        party_manager.add_player(player1)
        player2 = class_player.Player(2, "Altaru")
        party_manager.add_player(player2)

        party_manager.start_game()

        assert all(player.num_current_frame == 0 for player in party_manager.players_list)
        assert mock_next_turn.call_count == party_manager.NUMBER_OF_FRAME * len(party_manager.players_list)


@pytest.fixture
def player():
    return class_player.Player(1, "Matthieu")

# test pour checkCoherentSkittlesLastFrame
def test_checkCoherentSkittlesLastFrame(player):

    assert player.checkCoherentSkittlesLastFrame(5, [5, "X"], 1) == 5
    # Vous pouvez ajouter d'autres assertions pour tester différents scénarios

# test pour checkSpare
def test_checkSpare(player):
    frame_score = [5]
    player.checkSpare(frame_score, 5)
    assert frame_score == [5, "|"]
    # Testez d'autres scénarios

# test pour calculateScore
def test_calculateScore(player):
    frame_scores = [["X", ""], ["X", ""], [5, "|", 5]]
    assert player.calculateScore(frame_scores) == 60
    # Ajoutez d'autres cas de test pour tester différents scénarios
