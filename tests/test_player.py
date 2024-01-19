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

    player2 = class_player.Player(2,"Julien")
    party_manager.add_player(player2)
    assert len(party_manager.players_list) == 2
    assert party_manager.players_list[1].name == "Julien"

# Test sur la fonction permettant d'ajouter des joueurs à la partie depuis une liste de nom
def test_create_player():
    names = ["Joueur1", "Joueur2"]
    party_manager.create_player(names)

    assert len(party_manager.players_list) == 2
    assert party_manager.players_list[0].name == "Joueur1"
    assert party_manager.players_list[1].name == "Joueur2"
