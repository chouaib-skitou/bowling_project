import party


class Player:
    id = -1
    name = ""
    total_score = 0
    list_of_score = [[], []]

    def __init__(self, id, name):
        self.id = id
        self.name = "player" + id