# tests/test_class_player.py

from bowling_project.package_party import class_player, party_manager


# Cas de test : ajouter un joueur
def test_add_player():
    
    player1 = class_player.Player(1,"David")
    party_manager.add_player(player1)
    assert len(party_manager.players_list) == 1
    print(party_manager.players_list[0].name)
    assert party_manager.players_list[0].name == "David"

    player2 = class_player.Player(2,"Julien")
    party_manager.add_player(player2)
    assert len(party_manager.players_list) == 2
    assert party_manager.players_list[1].name == "Julien"

