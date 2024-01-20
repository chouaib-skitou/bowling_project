from package_party import party_manager


class Player:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.list_of_party_score = []
        self.num_current_frame = 0

    def add_scores_to_frame(self, score_launch_1, score_launch_2, score_launch_3=-1):
        score_to_add3 = -1

        # First and second launch of two launches
        if score_launch_3 == -1:
            # First launch
            if score_launch_1 == party_manager.NUMBER_OF_SKITTLES:
                score_to_add1 = "X"

                self.list_of_party_score.append([score_to_add1, ""])
                self.num_current_frame += 1
                return
            else:
                score_to_add1 = score_launch_1

            # Second launch
            if (score_launch_1 + score_launch_2) == party_manager.NUMBER_OF_SKITTLES \
                    and score_to_add1 != "X":
                score_to_add2 = "|"
            else:
                score_to_add2 = score_launch_2

        # First, second and third launch of three launches
        if 0 <= score_launch_3 <= 10:
            # First launch
            if score_launch_1 == party_manager.NUMBER_OF_SKITTLES:
                score_to_add1 = "X"
            else:
                score_to_add1 = score_launch_1

            # Second launch
            if (score_launch_1 + score_launch_2) == party_manager.NUMBER_OF_SKITTLES \
                    and score_to_add1 != "X":
                score_to_add2 = "|"
            elif score_to_add1 == "X" and score_launch_2 == party_manager.NUMBER_OF_SKITTLES:
                score_to_add2 = "X"
            else:
                score_to_add2 = score_launch_2

            # Third launch
            if score_launch_3 == party_manager.NUMBER_OF_SKITTLES:
                score_to_add3 = "X"
            elif score_to_add2 != "X" and score_to_add2 != "|" and (
                    score_launch_2 + score_launch_3) == party_manager.NUMBER_OF_SKITTLES:
                score_to_add3 = "|"
            else:
                score_to_add3 = score_launch_3

        if score_to_add3 != -1:
            self.list_of_party_score.append([score_to_add1, score_to_add2, score_to_add3])
        else:
            self.list_of_party_score.append([score_to_add1, score_to_add2])

        self.num_current_frame += 1
