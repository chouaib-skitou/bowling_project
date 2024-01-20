# tests/test_class_player.py

from package_party import class_player, party_manager

import pytest

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

    player.add_scores_to_frame(10, 0)
    player.add_scores_to_frame(7, 3)
    player.add_scores_to_frame(7, 2)
    player.add_scores_to_frame(10, 10, 10)
    player.add_scores_to_frame(10, 5, 2)
    player.add_scores_to_frame(8, 2, 5)
    player.add_scores_to_frame(8, 2, 10)
    player.add_scores_to_frame(10, 3, 7)
    player.add_scores_to_frame(10, 10, 4)
    player.add_scores_to_frame(10, 3, 4)

    assert(player.list_of_party_score[0][0] == "X")
    assert(player.list_of_party_score[0][1] == "")

    assert(player.list_of_party_score[1][0] == 7)
    assert(player.list_of_party_score[1][1] == "|")

    assert(player.list_of_party_score[2][0] == 7)
    assert(player.list_of_party_score[2][1] == 2)

    assert(player.list_of_party_score[3][0] == "X")
    assert(player.list_of_party_score[3][1] == "X")
    assert(player.list_of_party_score[3][2] == "X")

    assert(player.list_of_party_score[4][0] == "X")
    assert(player.list_of_party_score[4][1] == 5)
    assert(player.list_of_party_score[4][2] == 2)

    assert(player.list_of_party_score[5][0] == 8)
    assert(player.list_of_party_score[5][1] == "|")
    assert(player.list_of_party_score[5][2] == 5)

    assert(player.list_of_party_score[6][0] == 8)
    assert(player.list_of_party_score[6][1] == "|")
    assert(player.list_of_party_score[6][2] == "X")

    assert(player.list_of_party_score[7][0] == "X")
    assert(player.list_of_party_score[7][1] == 3)
    assert(player.list_of_party_score[7][2] == "|")

    assert(player.list_of_party_score[8][0] == "X")
    assert(player.list_of_party_score[8][1] == "X")
    assert(player.list_of_party_score[8][2] == 4)

    assert(player.list_of_party_score[9][0] == "X")
    assert(player.list_of_party_score[9][1] == 3)
    assert(player.list_of_party_score[9][2] == 4)

'''
def test_next_player_frame():
    player1 = package_party.class_player.Player(1,"Hamoudia")
    add_player(player1)
    player2 = package_party.class_player.Player(2,"Chouaib")
    add_player(player2)

    next_player_frame(1,0)
    assert package_party.party_manager.players_list[0].current_turn == 1

    next_player_frame(2,1)
    assert package_party.party_manager.players_list[1].current_turn == 1

    next_player_frame(1,0)
    assert package_party.party_manager.players_list[0].current_turn == 2
'''
'''
def test_start_game():
    player1 = package_party.class_player.Player(1,"Matthieu")
    add_player(player1)
    player2 = package_party.class_player.Player(2,"Altaru")
    add_player(player2)

    start_game()

    for player in package_party.party_manager.players_list:
        assert player.current_turn == NUMER_OF_FRAME
'''
