import class_player

NUMER_OF_FRAME = 3
NUMBER_OF_SKITTLES = 9
players_list = []


def add_player(player):
    players_list.append(player)


def create_player(list_players_names):
    for i in range(list_players_names):
        player = class_player.Player(len(players_list) + 1, list_players_names(i))
        add_player(player)


def next_player_frame(player_id, current_frame):
    players_list[player_id].next_turn(current_frame)


def start_game():
    global current_frame, players_list

    for i in range(NUMER_OF_FRAME):
        for j in range(len(players_list)):
            next_player_frame(j, i)



