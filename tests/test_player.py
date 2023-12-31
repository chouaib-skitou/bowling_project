# tests/test_class_player.py

import pytest
import package_party.class_player
from package_party.party_manager import add_player, next_player_frame, start_game

NUMER_OF_FRAME = 10

def test_add_player():
    player1 = package_party.class_player.Player(1,"David")
    add_player(player1)
    assert len(package_party.party_manager.players_list) == 1
    assert package_party.party_manager.players_list[0].name == "David"

    player2 = package_party.class_player.Player(2,"Julien")
    add_player(player2)
    assert len(package_party.party_manager.players_list) == 2
    assert package_party.party_manager.players_list[1].name == "Julien"
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