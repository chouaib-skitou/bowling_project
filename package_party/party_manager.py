import class_player

NUMER_OF_FRAME = 10
current_frame = 0
players_list = []


def add_player(player):
    global number_of_players
    players_list.append(player)


def next_player_frame(player_id, current_frame):
    players_list[player_id].next_turn(current_frame)


def start_game():
    global current_frame, players_list, number_of_players

    for i in range(NUMER_OF_FRAME):
        for j in range(len(players_list)):
            next_player_frame(j, i)
