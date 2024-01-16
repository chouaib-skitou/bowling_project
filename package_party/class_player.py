from package_party import party_manager


class Player:
    id = 0
    name = ""


    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.list_of_party_score = []
        self.current_frame = 0
        self.total_score = 0


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
        if (current_frame == party_manager.NUMER_OF_FRAME - 1):  # LA DERNIERE FRAME
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
        if par_frame_score[counter] == "X":
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

