import class_player
import party_manager

# Create and add players to the party
player1 = class_player.Player(len(party_manager.players_list) + 1, "AliceGomes", 4, 10)
party_manager.add_player(player1)

player2 = class_player.Player(len(party_manager.players_list) + 1, "JulienMarty", 4, 10)
party_manager.add_player(player2)

print("Players list : ")
for i in range(len(party_manager.players_list)):
    print("id : ", party_manager.players_list[i].id,
          " name : ", party_manager.players_list[i].name)

party_manager.start_game()