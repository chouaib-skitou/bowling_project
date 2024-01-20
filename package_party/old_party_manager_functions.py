NUMBER_OF_FRAME = 10
NUMBER_OF_SKITTLES = 10

def next_player_frame(player_id, current_frame):
    players_list[player_id].next_turn(current_frame)


def start_game():
    global current_frame, players_list

    for i in range(NUMBER_OF_FRAME):
        for j in range(len(players_list)):
            next_player_frame(j, i)
