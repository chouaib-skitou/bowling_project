from package_party import class_player

NUMBER_OF_FRAME = 10
NUMBER_OF_SKITTLES = 10
players_list = []


def add_player(player):
    players_list.append(player)


def create_player(player_name):
    add_player(class_player.Player(len(players_list) + 1, player_name))

