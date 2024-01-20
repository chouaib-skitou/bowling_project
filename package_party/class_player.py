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

    def calculateScore(self, frame_score_list):
        currentScore = 0
        # CALCUL DU SCORE
        for indexCurrentFrame in range(len(frame_score_list)):
            currentFrame = frame_score_list[indexCurrentFrame]  # liste de score de la frame courante
            # AVANT DERNIERE FRAME
            if (indexCurrentFrame == len(frame_score_list) - 2):
                if ("X" == frame_score_list[indexCurrentFrame][0]):  # STRIKE DANS L'AVANT DERNIER FRAME
                    if ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" ==
                            frame_score_list[indexCurrentFrame + 1][
                                1]):  # avant derniere frame : Si Strike dans les 2 lancers suivants
                        currentScore += 30
                        print("avant dernier : Strike + 2 strikes")
                    elif ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" !=
                        frame_score_list[indexCurrentFrame + 1][
                            1]):  # avant derniere frame : Si un strike et un tir normal
                        currentScore += 20 + frame_score_list[indexCurrentFrame + 1][1]
                        print("avant dernier : Strike + strike et tir normal")
                    elif ("|" == frame_score_list[indexCurrentFrame + 1][1]):  # avant derniere frame : Si Spare
                        currentScore += 20
                        print("avant dernier : Strike + 2 strikes")
                    else:
                        currentScore += 10 + frame_score_list[indexCurrentFrame + 1][0] + \
                                        frame_score_list[indexCurrentFrame + 1][
                                            1]  # avant derniere frame : Si 2 tirs normaux
                        print("avant dernier : 2 tirs normaux")

                elif ("|" == frame_score_list[indexCurrentFrame][1]):  # SPARE DANS L'AVANT DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame + 1][0]):  # Si suivi d'un strike
                        currentScore += 20
                        print("avant dernier : Spare + Strike")
                    else:  # Si suivi d'un tir normal
                        currentScore += 10 + frame_score_list[indexCurrentFrame + 1][0]
                        print("avant dernier : Spare + tir normal")

                else:
                    currentScore += sum(frame_score_list[indexCurrentFrame])
                    print("Avant dernier : tir normaux")

            # DERNIERE FRAME
            elif (indexCurrentFrame == len(frame_score_list) - 1):
                if ("X" == frame_score_list[indexCurrentFrame][0]):  # STRIKE DANS LA DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame][1] and "X" ==
                            frame_score_list[indexCurrentFrame][
                                2]):  # derniere frame : Si Strike dans les 2 lancers suivants
                        currentScore += 30
                        print("dernier : Strike + 2 strikes")
                    elif ("X" == frame_score_list[indexCurrentFrame][1] and "X" !=
                        frame_score_list[indexCurrentFrame][
                            2]):  # derniere frame : Si Strike puis normal dans les 2 lancers suivants
                        currentScore += 20 + frame_score_list[indexCurrentFrame][2]
                        print("dernier : Strike + strikes et tir normal")
                    elif ("|" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si un spare
                        print("frame_score_list !!!!", frame_score_list)
                        currentScore += 20
                        print("dernier : Strike + spare")
                    else:  # derniere frame : Si 2 tirs normaux
                        currentScore += 10 + frame_score_list[indexCurrentFrame][1] + \
                                        frame_score_list[indexCurrentFrame][2]
                        print("dernier : Strike + 2 tirs normaux")
                elif ("|" == frame_score_list[indexCurrentFrame][1]):  # SPARE DANS LA DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si spare
                        currentScore += 20
                        print("dernier : Spare + Strike")
                    elif ("X" != frame_score_list[indexCurrentFrame][
                        2]):  # derniere frame : Si suivi d'un tir normal #Y AVAIT UNE GROSEE ERREUR ICI
                        currentScore += 10 + frame_score_list[indexCurrentFrame][2]
                        print("dernier : Spare + tir normal")
                else:  # Si tir normal
                    currentScore += sum(frame_score_list[indexCurrentFrame])


            # AUTRE FRAME
            else:
                if ("X" == frame_score_list[indexCurrentFrame][
                    0]):  # Si strike, on regarde les 2 frames suivantes
                    if indexCurrentFrame + 2 > len(frame_score_list) - 1:  # pour eviter les dépassements
                        print('Fin')
                    else:
                        if ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" ==
                                frame_score_list[indexCurrentFrame + 2][
                                    0]):  # Si Strike dans les 2 lancers suivants
                            currentScore += 30  # car 3 strikes daffilés
                            print("Strike + 2 strike donc +30")

                        elif ("|" == frame_score_list[indexCurrentFrame + 1][1]):  # si un strike et un Spare
                            currentScore += 20
                            print("Strike + spare")

                        # precise [0] pour eviter le cas de la dernière frame ou X peut etre en dernier
                        elif ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" !=
                            frame_score_list[indexCurrentFrame + 2][0]):  # si un strike et un tir normal
                            currentScore += 20 + frame_score_list[indexCurrentFrame + 2][0]
                            print("Strike + normal")

                        else:  # Si 2 tirs normaux
                            currentScore += 10 + sum(frame_score_list[
                                                        indexCurrentFrame + 1])  # 10 plus le score de la frame suivante constituée de 2 lancers
                            print("Strike + 2 tirs normaux")

                elif ("|" == frame_score_list[indexCurrentFrame][1]):
                    if indexCurrentFrame + 1 > len(frame_score_list) - 1:  # pour eviter les dépassements
                        print('Fin')
                    else:
                        if ("X" == frame_score_list[indexCurrentFrame + 1][0]):  # Si suivi d'un strike
                            currentScore += 20
                            print("Spare + Strike")
                        else:
                            currentScore += 10 + frame_score_list[indexCurrentFrame + 1][
                                0]  # Si suivi d'un tir normal
                            print("Spare + tir normal")

                else:
                    currentScore += sum(frame_score_list[indexCurrentFrame])

        return currentScore