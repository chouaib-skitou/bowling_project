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

                    if ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" == frame_score_list[indexCurrentFrame + 1][1]):  # avant derniere frame : STRIKE + frame suivante = 2 Strikes
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 3 #On prend en compte les 2 strikes suivants donc *3
                        print("avant derniere frame : STRIKE + frame suivante = 2 Strikes")
                    elif ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" != frame_score_list[indexCurrentFrame + 1][1]):  # avant derniere frame : STRIKE + frame suivante = strike et un tir normal
                        currentScore += (party_manager.NUMBER_OF_SKITTLES * 2) + frame_score_list[indexCurrentFrame + 1][1]
                        print("avant derniere frame : STRIKE + frame suivante = strike et tir normal")
                    elif ("|" == frame_score_list[indexCurrentFrame + 1][1]):  #avant derniere frame : STRIKE + frame suivante = Spare
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 2
                        print("avant derniere frame : STRIKE + frame suivante = Spare")
                    else:
                        currentScore += party_manager.NUMBER_OF_SKITTLES + frame_score_list[indexCurrentFrame + 1][0] + frame_score_list[indexCurrentFrame + 1][1]  # avant derniere frame : STRIKE + frame suivante = 2 tirs normaux
                        print("avant derniere frame : STRIKE + frame suivante = 2 tirs normaux")

                elif ("|" == frame_score_list[indexCurrentFrame][1]):  # SPARE DANS L'AVANT DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame + 1][0]):  # avant derniere frame : SPARE + frame suivante = Strike
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 2
                        print("avant derniere frame : SPARE + frame suivante = Strike")
                    else:  # Si suivi d'un tir normal
                        currentScore += party_manager.NUMBER_OF_SKITTLES + frame_score_list[indexCurrentFrame + 1][0] # avant derniere frame : SPARE + frame suivante = Tir normal
                        print("avant derniere frame : SPARE + frame suivante = Tir normal")

                else: #TIRS NORMAUX DANS l'AVANT DERNIER FRAME
                    currentScore += sum(frame_score_list[indexCurrentFrame])
                    print("avant derniere frame : 2 tirs normaux")

            # DERNIERE FRAME
            elif (indexCurrentFrame == len(frame_score_list) - 1):
                if ("X" == frame_score_list[indexCurrentFrame][0]):  # STRIKE DANS LA DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame][1] and "X" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : STRIKE + frame suivante = 2 Strikes
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 3
                        print("derniere frame : STRIKE + frame suivante = 2 Strikes")
                    elif ("X" == frame_score_list[indexCurrentFrame][1] and "X" != frame_score_list[indexCurrentFrame][2]):  # derniere frame : STRIKE + STRIKE et tir normal
                        currentScore += (party_manager.NUMBER_OF_SKITTLES * 2) + frame_score_list[indexCurrentFrame][2]
                        print("derniere frame : STRIKE + STRIKE et tir normal")
                    elif ("|" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : STRIKE + SPARE
                        print("frame_score_list !!!!", frame_score_list) #ERREUR
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 2
                        print("derniere frame : STRIKE + SPARE")
                    else:  # derniere frame : Si 2 tirs normaux
                        currentScore += party_manager.NUMBER_OF_SKITTLES + frame_score_list[indexCurrentFrame][1] + frame_score_list[indexCurrentFrame][2]
                        print("dernier : Strike + 2 tirs normaux")
                elif ("|" == frame_score_list[indexCurrentFrame][1]):  # SPARE DANS LA DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : SPARE + STRIKE
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 2
                        print("derniere frame : SPARE + STRIKE")
                    elif ("X" != frame_score_list[indexCurrentFrame][2]):  # derniere frame : SPARE + tir normal #Y AVAIT UNE GROSEE ERREUR ICI
                        currentScore += party_manager.NUMBER_OF_SKITTLES + frame_score_list[indexCurrentFrame][2]
                        print("dernier : Spare + tir normal")
                else:  # Si tir normal
                    currentScore += sum(frame_score_list[indexCurrentFrame])


            # AUTRE FRAME
            else:
                if ("X" == frame_score_list[indexCurrentFrame][0]):  # Si strike, on regarde les 2 frames suivantes
                    if indexCurrentFrame + 2 > len(frame_score_list) - 1:  # pour eviter les dépassements
                        print('Fin')
                    else:
                        if ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" == frame_score_list[indexCurrentFrame + 2][0]):  # STRIKE + 2 STRIKES (Si Strike dans les 2 lancés suivants)
                            currentScore += party_manager.NUMBER_OF_SKITTLES * 3  # car 3 strikes daffilés
                            print("STRIKE + 2 STRIKES")

                        elif ("|" == frame_score_list[indexCurrentFrame + 1][1]):  # STRIKE + SPARE (si un strike et un Spare)
                            currentScore += party_manager.NUMBER_OF_SKITTLES * 2
                            print("STRIKE + SPARE")

                        # precise [0] pour eviter le cas de la dernière frame ou X peut etre en dernier
                        elif ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" != frame_score_list[indexCurrentFrame + 2][0]):  # STRIKE + tir normal
                            currentScore += (party_manager.NUMBER_OF_SKITTLES * 2) + frame_score_list[indexCurrentFrame + 2][0]
                            print("STRIKE + 1 tir normal")

                        else:  # Si 2 tirs normaux
                            currentScore += party_manager.NUMBER_OF_SKITTLES + sum(frame_score_list[indexCurrentFrame + 1])  # STRIKE + 2 tirs normaux (10 plus le score de la frame suivante constituée de 2 lancés)
                            print("STRIKE + 2 tirs normaux")

                elif ("|" == frame_score_list[indexCurrentFrame][1]):
                    if indexCurrentFrame + 1 > len(frame_score_list) - 1:  # pour eviter les dépassements
                        print('Fin')
                    else:
                        if ("X" == frame_score_list[indexCurrentFrame + 1][0]):  # SPARE + STRIKE
                            currentScore += party_manager.NUMBER_OF_SKITTLES * 2
                            print("SPARE + STRIKE")
                        else:
                            currentScore += party_manager.NUMBER_OF_SKITTLES + frame_score_list[indexCurrentFrame + 1][0]  # SPARE + 1 tir normal
                            print("SPARE + 1 tir normal")

                else:
                    currentScore += sum(frame_score_list[indexCurrentFrame])

        return currentScore

    def next_turn(self, current_frame):
        print("PLAYER ID : ", self.id)
        print("current frame : ", current_frame)
        nbLaunch = 2
        skittlesTouched = 0

        # Display main informations
        print("frame_score_list : ", self.list_of_party_score)
        print(f"Frame {current_frame + 1} :")
        frame_score = []  # stock le nombre de quilles renversées pour

        # print("frameNumber (real number before incrementation) : ", current_frame)
        if (current_frame == party_manager.NUMBER_OF_FRAME - 1):  # LA DERNIERE FRAME
            print("Derniere frame !")
            print(f"\tLancer 1:")
            skittlesTouched = self.askAndCheckSkittlesInTen()  # demande nombre de quilles renversées

            if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):  # 1er lancer de la derniere frame
                frame_score.append('X')
                print(f"\t\tVous avez fait un strike au lance 1 de la derniere frame ! Vous avez encore 2 lancer !")

                for e in range(1, 3):  # De 1 à 3 pour garder la continuité des lancers (lancers 2 et 3)
                    print(f"\tLancer {e + 1} :")
                    skittlesTouched = self.askAndCheckSkittlesInTen()
                    if (e == 1):
                        if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):
                            frame_score.append('X')
                            print(
                                f"\t\tVous avez fait un strike au lance 2 de la derniere frame ! Vous avez encore 1 lancer !")
                        else:
                            frame_score.append(skittlesTouched)
                            print(f"\t\t Vous avez encore 1 lancer !")

                    if (e == 2):  # au 2eme lancer vérifie que c'est coherent avec le precedent
                        skittlesTouched = self.checkCoherentSkittlesLastFrame(skittlesTouched, frame_score, e - 1)
                        if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):
                            frame_score.append('X')
                            print(f"\t\tVous avez fait un strike au lance 3 de la derniere frame !")
                        elif (frame_score[e - 1] != "X"):  # cas du spare
                            if (frame_score[
                                e - 1] + skittlesTouched == party_manager.NUMBER_OF_SKITTLES):  # cas du spare
                                frame_score.append("|")
                                print(f"\t\tVous avez fait un spare au lance 3 de la derniere frame !")
                            else:  #GROSSE ERREUR D'IDENTATION ICI AUSSI
                                frame_score.append(skittlesTouched)

            else:  # 1er lancer de la derniere frame
                frame_score.append(skittlesTouched)
                print(f"\tLancer 2:")
                skittlesTouched = self.askAndCheckSkittlesInTen()
                if (skittlesTouched + frame_score[0] == party_manager.NUMBER_OF_SKITTLES):  # spare
                    frame_score.append("|")
                    print(f"\tLancer 3:")
                    skittlesTouched = self.askAndCheckSkittlesInTen()
                    if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):
                        frame_score.append("X")
                    else:
                        frame_score.append(skittlesTouched)
                else:  # cas normal
                    skittlesTouched = self.checkCoherentSkittles(skittlesTouched, frame_score)
                    frame_score.append(skittlesTouched)
                    print(f"\t\tVous n'avez plus de lancers !")

        else:
            for launchNumber in range(nbLaunch):
                print(f"\tLancé {launchNumber + 1} :")  # 1ER LANCE

                if (launchNumber == 0):  # 1ER LANCE
                    skittlesTouched = self.checkSkittlesInTen()  # Nombre de quilles entre 0 et NUMBER_OF_SKITTLES

                    if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):  # En cas de strike
                        print(f"\t\tVous avez fait un strike ! On passe à la frame suivante !")
                        frame_score.append("X")
                        frame_score.append("")
                        break  # permet le passage a la frame suivante en quittant le if
                    else:
                        frame_score.append(skittlesTouched)

                if (launchNumber == 1):  # 2EME LANCE
                    skittlesTouched = self.checkSkittlesInTen()  # Nombre de quilles entre 0 et NUMBER_OF_SKITTLES
                    skittlesTouched = self.checkCoherentSkittles(skittlesTouched,
                                                                 frame_score)  # Nombre de quilles coherent avec lance precedent
                    self.checkSpare(frame_score, skittlesTouched)  # Vérifie si on fait un spare

        self.list_of_party_score.append(frame_score)

    def checkCoherentSkittlesLastFrame(self, parSkittlesTouched, par_frame_score, counter):
        if par_frame_score[counter] == "X":
            pass
        else:
            while (parSkittlesTouched > party_manager.NUMBER_OF_SKITTLES - par_frame_score[counter]):
                print(f"\t\tAu tour précédent vous avez renversé {par_frame_score[counter]} quilles :")
                parSkittlesTouched = int(input("\t\tVeuillez renseigner un nombre cohérent :"))
        return parSkittlesTouched

    def checkSkittlesInTen(self):
        skittlesTouched = int(input("\t\tIndiquez le nombre de quilles renversées :"))
        while (
                skittlesTouched > party_manager.NUMBER_OF_SKITTLES or skittlesTouched < 0):  # Empêche les valeurs incohérentes
            skittlesTouched = int(
                input(f"\t\tVeuillez renseigner un nombre entre 0 et {party_manager.NUMBER_OF_SKITTLES} :"))
        return skittlesTouched

    def checkCoherentSkittles(self, parSkittlesTouched, par_frame_score):
        while (parSkittlesTouched > party_manager.NUMBER_OF_SKITTLES - par_frame_score[0]):
            print(f"\t\tAu tour précédent vous avez renversé {par_frame_score[0]} quilles :")
            parSkittlesTouched = int(input("\t\tVeuillez renseigner un nombre cohérent :"))
        return parSkittlesTouched

    def checkSpare(self, par_frame_score, parSkittlesTouched):
        if (par_frame_score[0] + parSkittlesTouched == party_manager.NUMBER_OF_SKITTLES):
            print(f"\t\tVous avez fait un spare ! On passe à la frame suivante !")
            par_frame_score.append("|")
        else:
            par_frame_score.append(parSkittlesTouched)

    # contrary to usual strike check, since we are in the last frame, we keep playing
    def checkStrikeLastFrame(self, par_frame_score, parSkittlesTouched):
        if (parSkittlesTouched == party_manager.NUMBER_OF_SKITTLES):  # En cas de strike
            print(f"\t\tVous avez fait un strike ! On passe à la frame suivante !")
            par_frame_score.append("X")
        else:
            par_frame_score.append(parSkittlesTouched)

    def askAndCheckSkittlesInTen(self):
        skittlesTouched = int(input("\t\tIndiquez le nombre de quilles renversées :"))
        while (
                skittlesTouched > party_manager.NUMBER_OF_SKITTLES or skittlesTouched < 0):  # Empêche les valeurs incohérentes
            skittlesTouched = int(
                input(f"\t\tVeuillez renseigner un nombre entre 0 et {party_manager.NUMBER_OF_SKITTLES} :"))
        return skittlesTouched
