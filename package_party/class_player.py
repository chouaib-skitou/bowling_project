import party_manager

class Player:
    id = 0
    name = ""
    number_of_frame = 0
    number_of_skittles = 0


    def __init__(self, id, name, number_of_frame, number_of_skittles):
        self.id = id
        self.name = name
        self.list_of_party_score = []
        self.current_frame = 0
        self.total_score = 0
        self.number_of_frame = number_of_frame
        self.number_of_skittles = number_of_skittles


    # The function to call at the start of player's frame
    # Should end at the end of the frame
    def next_turn(self, current_frame):
        print("PLAYER ID : ", self.id)
        print("current frame : ", current_frame)
        nbLaunch = 2
        skittlesTouched = 0

        # Display main informations
        print("frame_score_list : ", self.list_of_party_score)
        print(f"Frame {current_frame + 1} :")
        frame_score = []  # stock le nombre de quilles renversées pour

        print("frameNumber (real number before incrementation) : ", current_frame)
        if (current_frame == self.number_of_frame - 1):  # LA DERNIERE FRAME
            print("Derniere frame !")
            print(f"\tLancer 1:")
            skittlesTouched = self.askAndCheckSkittlesInTen()  # demande nombre de quilles renversées
            if (skittlesTouched == 10):  # 1er lancer de la derniere frame
                frame_score.append('X')
                print(f"\t\tVous avez fait un strike au lance 1 de la derniere frame ! Vous avez encore 2 lancer !")
                for e in range(1, 3):  # De 1 à 3 pour garder la continuité des lancers (lancers 2 et 3)
                    print(f"\tLancer {e + 1} :")
                    skittlesTouched = self.askAndCheckSkittlesInTen()
                    if (e == 1):
                        if (skittlesTouched == 10):
                            frame_score.append('X')
                            print(
                                f"\t\tVous avez fait un strike au lance 2 de la derniere frame ! Vous avez encore 1 lancer !")
                        else:
                            frame_score.append(skittlesTouched)
                            print(f"\t\t Vous avez encore 1 lancer !")

                    if (e == 2):  # au 2eme lancer vérifie que c'est coherent avec le precedent
                        skittlesTouched = self.checkCoherentSkittlesLastFrame(skittlesTouched, frame_score, e - 1)
                        if (skittlesTouched == 10):
                            frame_score.append('X')
                            print(f"\t\tVous avez fait un strike au lance 3 de la derniere frame !")
                        elif (frame_score[e - 1] != "X"):  # cas du spare
                            if (frame_score[e - 1] + skittlesTouched == 10):  # cas du spare
                                frame_score.append("|")
                                print(f"\t\tVous avez fait un spare au lance 3 de la derniere frame !")
                        else:
                            frame_score.append(skittlesTouched)


            else:  # 1er lancer de la derniere frame
                frame_score.append(skittlesTouched)
                print(f"\tLancer 2:")
                skittlesTouched = self.askAndCheckSkittlesInTen()
                if (skittlesTouched + frame_score[0] == 10):  # spare
                    frame_score.append("|")
                    print(f"\tLancer 3:")
                    skittlesTouched = self.askAndCheckSkittlesInTen()
                    if (skittlesTouched == 10):
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
                    skittlesTouched = self.checkSkittlesInTen()  # Nombre de quilles entre 0 et 10

                    if (skittlesTouched == 10):  # En cas de strike
                        print(f"\t\tVous avez fait un strike ! On passe à la frame suivante !")
                        frame_score.append("X")
                        frame_score.append("")
                        break  # permet le passage a la frame suivante en quittant le if
                    else:
                        frame_score.append(skittlesTouched)

                if (launchNumber == 1):  # 2EME LANCE
                    skittlesTouched = self.checkSkittlesInTen()  # Nombre de quilles entre 0 et 10
                    skittlesTouched = self.checkCoherentSkittles(skittlesTouched,
                                                            frame_score)  # Nombre de quilles coherent avec lance precedent
                    self.checkSpare(frame_score, skittlesTouched)  # Vérifie si on fait un spare

        self.list_of_party_score.append(frame_score)

    def checkCoherentSkittlesLastFrame(parSkittlesTouched, par_frame_score, counter):
        if (par_frame_score[counter] == "X"):
            pass
        else:
            while (parSkittlesTouched > 10 - par_frame_score[counter]):
                print(f"\t\tAu tour précédent vous avez renversé {par_frame_score[counter]} quilles :")
                parSkittlesTouched = int(input("\t\tVeuillez renseigner un nombre cohérent :"))
        return parSkittlesTouched

    def checkSkittlesInTen(self):
        skittlesTouched = int(input("\t\tIndiquez le nombre de quilles renversées :"))
        while (skittlesTouched > 10 or skittlesTouched < 0):  # Empêche les valeurs incohérentes
            skittlesTouched = int(input("\t\tVeuillez renseigner un nombre entre 0 et 10 :"))
        return skittlesTouched

    def checkCoherentSkittles(self, parSkittlesTouched, par_frame_score):
        while (parSkittlesTouched > 10 - par_frame_score[0]):
            print(f"\t\tAu tour précédent vous avez renversé {par_frame_score[0]} quilles :")
            parSkittlesTouched = int(input("\t\tVeuillez renseigner un nombre cohérent :"))
        return parSkittlesTouched

    def checkSpare(self, par_frame_score, parSkittlesTouched):
        if (par_frame_score[0] + parSkittlesTouched == 10):
            print(f"\t\tVous avez fait un spare ! On passe à la frame suivante !")
            par_frame_score.append("|")
        else:
            par_frame_score.append(parSkittlesTouched)

    # contrary to usual strike check, since we are in the last frame, we keep playing
    def checkStrikeLastFrame(self, par_frame_score, parSkittlesTouched):
        if (parSkittlesTouched == 10):  # En cas de strike
            print(f"\t\tVous avez fait un strike ! On passe à la frame suivante !")
            par_frame_score.append("X")
        else:
            par_frame_score.append(parSkittlesTouched)

    def askAndCheckSkittlesInTen(self):
        skittlesTouched = int(input("\t\tIndiquez le nombre de quilles renversées :"))
        while (skittlesTouched > 10 or skittlesTouched < 0):  # Empêche les valeurs incohérentes
            skittlesTouched = int(input("\t\tVeuillez renseigner un nombre entre 0 et 10 :"))
        return skittlesTouched

    """
        def scoreCalculation(self):
        # CALCUL DU SCORE
        for indexCurrentFrame in range(len(self.list_of_party_score)):
            currentFrame = self.list_of_party_score[indexCurrentFrame]  # liste de score de la frame courante
            # AVANT DERNIERE FRAME
            if (indexCurrentFrame == len(self.list_of_party_score) - 2):
                if ("X" == self.list_of_party_score[indexCurrentFrame][0]):  # STRIKE DANS L'AVANT DERNIER FRAME
                    if ("X" == self.list_of_party_score[indexCurrentFrame + 1][0] and "X" ==
                            self.list_of_party_score[indexCurrentFrame + 1][
                                1]):  # avant derniere frame : Si Strike dans les 2 lancers suivants
                        currentScore += 30
                        print("avant dernier : Strike + 2 strikes")
                    elif ("X" == self.list_of_party_score[indexCurrentFrame + 1][0] and "X" !=
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
                    print("Avan derniere : tir normaux")

            # DERNIERE FRAME
            elif (indexCurrentFrame == len(frame_score_list) - 1):
                if ("X" == frame_score_list[indexCurrentFrame][0]):  # STRIKE DANS LA DERNIERE FRAME
                    if ("X" == frame_score_list[indexCurrentFrame][1] and "X" == frame_score_list[indexCurrentFrame][
                        2]):  # derniere frame : Si Strike dans les 2 lancers suivants
                        currentScore += 30
                        print("dernier : Strike + 2 strikes")
                    elif ("X" == frame_score_list[indexCurrentFrame][1] and "X" != frame_score_list[indexCurrentFrame][
                        2]):  # derniere frame : Si Strike puis normal dans les 2 lancers suivants
                        currentScore += 20 + frame_score_list[indexCurrentFrame][2]
                        print("dernier : Strike + strikes et tir normal")
                    elif ("|" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si un spare
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
                    if ("X" == frame_score_list[indexCurrentFrame][2]):  # derniere frame : Si suivi d'un tir normal
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
                        if ("X" == frame_score_list[indexCurrentFrame + 1][0] and "X" ==
                                frame_score_list[indexCurrentFrame + 2][0]):  # Si Strike dans les 2 lancers suivants
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
                            currentScore += 10 + frame_score_list[indexCurrentFrame + 1][0]  # Si suivi d'un tir normal
                            print("Spare + tir normal")

                else:
                    currentScore += sum(frame_score_list[indexCurrentFrame])

        print("frame_score_list", frame_score_list)
        print("currentScore : ", currentScore)
        """
