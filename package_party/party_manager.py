from package_party import class_player

NUMBER_OF_FRAME = 10
NUMBER_OF_SKITTLES = 10
players_list = []


def add_player(player):
    players_list.append(player)


def create_player(player_name):
    add_player(class_player.Player(len(players_list) + 1, player_name))


def next_player_frame(player_id, current_frame):
    players_list[player_id - 1].next_turn(current_frame)


def start_game():
    global current_frame, players_list

    for i in range(NUMBER_OF_FRAME):
        for j in range(len(players_list)):
            next_player_frame(j, i)

