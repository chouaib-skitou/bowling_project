from package_party import party_manager


class Player:
    id = 0
    name = ""


    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.list_of_party_score = []
        self.num_current_frame = 0


    def add_scores_to_frame(self, score_launch_1, score_launch_2, score_launch_3 = -1):
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
            elif score_to_add2 != "X" and score_to_add2 != "|" and (score_launch_2 + score_launch_3) == party_manager.NUMBER_OF_SKITTLES:
                score_to_add3 = "|"
            else:
                score_to_add3 = score_launch_3

        if score_to_add3 != -1:
            self.list_of_party_score.append([score_to_add1, score_to_add2, score_to_add3])
        else:
            self.list_of_party_score.append([score_to_add1, score_to_add2])

        self.num_current_frame += 1
        print(self.list_of_party_score)


    # The function to call at the start of player's frame
    # Should end at the end of the frame
    #Register the 2 launches of the frame
    def next_turn(self, current_frame):
        print("PLAYER ID : ", self.id)
        print("current frame : ", current_frame)
        nbLaunch = 2
        skittlesTouched = 0

        # Display main informations
        print("frame_score_list : ", self.list_of_party_score)
        print(f"Frame {current_frame + 1} :")
        frame_score = []  # stock le nombre de quilles renversées pour

        #print("frameNumber (real number before incrementation) : ", current_frame)
        if (current_frame == party_manager.NUMBER_OF_FRAME - 1):  # LA DERNIERE FRAME
            print("Derniere frame !")
            print(f"\tLancé 1:")
            skittlesTouched = self.askAndCheckSkittlesInTen()  # demande nombre de quilles renversées

            if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):  # Strike au 1er lancé de la derniere frame
                frame_score.append('X')
                print(f"\t\tVous avez fait un strike au lancé 1 de la derniere frame ! Vous avez encore 2 lancé !")

                for e in range(1, 3):  # De 1 à 3 pour garder la continuité des lancés (lancé 2 et 3)
                    print("for e :", e)
                    print(f"\tLancé {e + 1} :")
                    skittlesTouched = self.askAndCheckSkittlesInTen()
                    if (e == 1):
                        if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):#Si Strike
                            frame_score.append('X')
                            print(f"\t\tVous avez fait un strike au lance 2 de la derniere frame ! Vous avez encore 1 lancé !")
                        else:
                            frame_score.append(skittlesTouched)
                            print(f"\t\t Vous avez encore 1 lancé !")

                    if (e == 2):  # au 3eme lancé vérifie que c'est coherent avec le precedent
                        skittlesTouched = self.checkCoherentSkittlesLastFrame(skittlesTouched, frame_score, e - 1)
                        if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):
                            frame_score.append('X')
                            print(f"\t\tVous avez fait un strike au lance 3 de la derniere frame !")
                        elif (frame_score[e - 1] != "X"):  # cas du spare
                            if (frame_score[e - 1] + skittlesTouched == party_manager.NUMBER_OF_SKITTLES):  # cas du spare
                                frame_score.append("|")
                                print(f"\t\tVous avez fait un spare au lance 3 de la derniere frame !")
                            else: #GROSSE ERREUR D'IDENTATION ICI AUSSI
                                print("Condition 3: Encore 1 lancé")
                                frame_score.append(skittlesTouched)

            else:  # 1er lancé de la derniere frame
                frame_score.append(skittlesTouched)
                print(f"\tLancé 2:")
                skittlesTouched = self.askAndCheckSkittlesInTen()
                if (skittlesTouched + frame_score[0] == party_manager.NUMBER_OF_SKITTLES):  # spare
                    frame_score.append("|")
                    print(f"\tLancé 3:")
                    skittlesTouched = self.askAndCheckSkittlesInTen()
                    if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):
                        frame_score.append("X")
                    else:
                        frame_score.append(skittlesTouched)
                else:  # cas normal
                    skittlesTouched = self.checkCoherentSkittles(skittlesTouched, frame_score)
                    frame_score.append(skittlesTouched)
                    print(f"\t\tVous n'avez plus de lancé !")

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
                    skittlesTouched = self.checkCoherentSkittles(skittlesTouched, frame_score)  # Nombre de quilles coherent avec lance precedent
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
        while (skittlesTouched > party_manager.NUMBER_OF_SKITTLES or skittlesTouched < 0):  # Empêche les valeurs incohérentes
            skittlesTouched = int(input(f"\t\tVeuillez renseigner un nombre entre 0 et {party_manager.NUMBER_OF_SKITTLES} :"))
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
        while (skittlesTouched > party_manager.NUMBER_OF_SKITTLES or skittlesTouched < 0):  # Empêche les valeurs incohérentes
            skittlesTouched = int(input(f"\t\tVeuillez renseigner un nombre entre 0 et {party_manager.NUMBER_OF_SKITTLES} :"))
        return skittlesTouched

    def calculateScore(self, frame_score_list):
        currentScore = 0
        # CALCUL DU SCORE
        for indexCurrentFrame in range(len(frame_score_list)):
            currentFrame = frame_score_list[indexCurrentFrame]  #liste de score de la frame courante
            # AVANT DERNIERE FRAME
            if (indexCurrentFrame == len(frame_score_list) - 2):
                print("AVANT DERNIERE FRAME")
                if ("X" == frame_score_list[indexCurrentFrame][0]):  #STRIKE DANS L'AVANT DERNIER FRAME
                    if ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" == frame_score_list[indexCurrentFrame + 1][1]):  # avant derniere frame : STRIKE + frame suivante = 2 Strikes
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 3 #On prend en compte les 2 strike suivants donc *3
                        print("avant dernier : STRIKE + frame suivante = 2 Strikes")
                    elif ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" !=frame_score_list[indexCurrentFrame + 1][1]):  # avant derniere frame : STRIKE + frame suivante = strike et un tir normal
                        currentScore += (party_manager.NUMBER_OF_SKITTLES * 2) + frame_score_list[indexCurrentFrame + 1][1]
                        print("avant dernier : STRIKE + frame suivante = strike et tir normal")
                    elif ("|" == frame_score_list[indexCurrentFrame + 1][1]):  # avant derniere frame : STRIKE + frame suivante = Spare
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 2
                        print("avant dernier : Strike + frame suivante = Spare")
                    else:
                        currentScore += 10 + frame_score_list[indexCurrentFrame + 1][0] + frame_score_list[indexCurrentFrame + 1][1]  # avant derniere frame : STRIKE + frame suivante = 2 tirs normaux
                        print("avant dernier : Strike + frame suivante = 2 tirs normaux")

                elif ("|" == frame_score_list[indexCurrentFrame][1]):  # SPARE DANS L'AVANT DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame + 1][0]):  # SPARE + frame suivante = Strike
                        currentScore += 20
                        print("avant dernier : SPARE + frame suivante = Strike")
                    else:
                        currentScore += 10 + frame_score_list[indexCurrentFrame + 1][0] # SPARE + frame suivante = Tir Normal
                        print("avant dernier : SPARE + frame suivante = Tir Normal")

                else: # TIR NORMAUX DANS L'AVANT DERNIERE FRAME
                    currentScore += sum(frame_score_list[indexCurrentFrame])
                    print("Avant dernier : 2 tirs normaux")

            # DERNIERE FRAME
            elif (indexCurrentFrame == len(frame_score_list) - 1):
                print("frame_score_list :",frame_score_list)
                print("frame_score_list[indexCurrentFrame]", frame_score_list[indexCurrentFrame])
                if ("X" == frame_score_list[indexCurrentFrame][0]):  # STRIKE DANS LA DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame][1] and "X" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si Strike dans les 2 lancés suivants
                        currentScore += party_manager.NUMBER_OF_SKITTLES * 3
                        print("dernier : Strike + 2 strikes")
                    elif ("X" == frame_score_list[indexCurrentFrame][1] and "X" != frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si Strike puis normal dans les 2 lancés suivants
                        currentScore += 20 + frame_score_list[indexCurrentFrame][2]
                        print("dernier : Strike + strikes et tir normal")
                    elif ("|" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si un spare
                        print("frame_score_list !!!!", frame_score_list) #ERREUR
                        currentScore += 20
                        print("dernier : Strike + spare")
                    else:  # derniere frame : Si 2 tirs normaux
                        currentScore += 10 + frame_score_list[indexCurrentFrame][1] + frame_score_list[indexCurrentFrame][2]
                        print("dernier : Strike + 2 tirs normaux")
                elif ("|" == frame_score_list[indexCurrentFrame][1]):  # SPARE DANS LA DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si spare
                        currentScore += 20
                        print("dernier : Spare + Strike")
                    elif ("X" != frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si suivi d'un tir normal #Y AVAIT UNE GROSEE ERREUR ICI
                        currentScore += 10 + frame_score_list[indexCurrentFrame][2]
                        print("dernier : Spare + tir normal")
                else:  # Si tir normal
                    currentScore += sum(frame_score_list[indexCurrentFrame])


            # AUTRE FRAME
            else:
                if ("X" == frame_score_list[indexCurrentFrame][0]):  # Si strike, on regarde les 2 frames suivantes
                    if indexCurrentFrame + 2 > len(frame_score_list) - 1:  # pour eviter les dépassements
                        print('Fin')
                    else:
                        if ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" == frame_score_list[indexCurrentFrame + 2][0]):  # Si Strike dans les 2 lancés suivants
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
                            currentScore += 10 + sum(frame_score_list[indexCurrentFrame + 1])  # 10 plus le score de la frame suivante constituée de 2 lancés
                            print("Strike + 2 tirs normaux")

                elif ("|" == frame_score_list[indexCurrentFrame][1]):
                    if indexCurrentFrame + 1 > len(frame_score_list) - 1:  # pour eviter les dépassements
                        print('Fin')
                    else:
                        if ("X" == frame_score_list[indexCurrentFrame + 1][0]):  # Si suivi d'un strike
                            currentScore += 20
                            print("Spare + Strike")
                        else:
                            currentScore += 10 + frame_score_list[indexCurrentFrame + 1][0]  # Si suivi d'un tir normal
                            print("Spare + tir normal")

                else:
                    currentScore += sum(frame_score_list[indexCurrentFrame])
        print("frame_score_list :", frame_score_list)
        return currentScore




