import class_player

def init_Number(nb_tours,nb_bowling):
    NUMER_OF_FRAME = nb_tours
    NUMBER_OF_SKITLES = nb_bowling
    players_list = []


def add_player(player):
    players_list.append(player)


def create_player(list_players_names):
    for i in enumerate(list_players_names):
        player = class_player.Player(len(players_list) + 1, list_players_names(i))
        add_player(player)


def next_player_frame(player_id, current_frame):
    players_list[player_id].next_turn(current_frame)


def start_game():
    global current_frame, players_list

    for i in range(NUMER_OF_FRAME):
        for j in range(len(players_list)):
            next_player_frame(j, i)



