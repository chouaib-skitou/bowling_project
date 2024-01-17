from package_party import party_manager,class_player

def test_start_game():
    player1 = class_player.Player(1, "David")
    party_manager.add_player(player1)
    assert len(party_manager.players_list) == 1
    assert party_manager.players_list[0].name == "David"

    player2 = class_player.Player(2, "Julien")
    party_manager.add_player(player2)
    assert len(party_manager.players_list) == 2
    assert party_manager.players_list[1].name == "Julien"

    party_manager.start_game()