# tests/test_class_player.py

from package_party import class_player, party_manager

import pytest

NUMER_OF_FRAME = 10


@pytest.fixture(autouse=True)
def reset_players_list():
    party_manager.players_list = []


def test_add_player():
    
    player1 = class_player.Player(1,"David")
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




from unittest import mock

@pytest.fixture(autouse=True)
def reset_players_list():
    party_manager.players_list = []

def test_next_player_frame():
    with mock.patch.object(class_player.Player, 'next_turn') as mock_next_turn:
        player1 = class_player.Player(1, "Hamoudia")
        party_manager.add_player(player1)
        player2 = class_player.Player(2, "Chouaib")
        party_manager.add_player(player2)

        party_manager.next_player_frame(1, 1)
        assert party_manager.players_list[0].num_current_frame == 0
        mock_next_turn.assert_called_once_with(0)

        party_manager.next_player_frame(2,1)
        assert party_manager.players_list[1].num_current_frame == 1
        assert mock_next_turn.call_count == 2

        party_manager.next_player_frame(1, 2)
        assert party_manager.players_list[0].num_current_frame == 2
        assert mock_next_turn.call_count == 3

def test_start_game():
    party_manager.players_list = []
    with mock.patch.object(class_player.Player, 'next_turn') as mock_next_turn:
        player1 = class_player.Player(1, "Matthieu")
        party_manager.add_player(player1)
        player2 = class_player.Player(2, "Altaru")
        party_manager.add_player(player2)

        party_manager.start_game()

        assert all(player.num_current_frame == 0 for player in party_manager.players_list)
        assert mock_next_turn.call_count == party_manager.NUMBER_OF_FRAME * len(party_manager.players_list)
