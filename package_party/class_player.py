import party_manager


class Player:
    id = 0
    name = ""
    current_frame = 0
    total_score = 0
    list_of_party_score = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

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

        print("frameNumber : ", current_frame)
        if (current_frame == party_manager.NUMER_OF_FRAME - 1):  # LA DERNIERE FRAME
            print("Derniere frame !")
            finalLaunchNumber = 0  # determine le nombre de lance effectue dans la derniere frame
            counter = 0

            while (finalLaunchNumber < nbLaunchFinalFrame):  # Droit a 3 lances si strike ou spare -> 1 lance supplementaire
                print("DEBUT finalLaunchNumber", finalLaunchNumber)
                if ((len(frame_score) == 2) and ("X" not in frame_score) and (
                        "|" not in frame_score)):  # cas où on a fait ni strike ni spare
                    print("Dans conditio finalLaunchNumber", finalLaunchNumber)
                    print("Dans condition frame_score", frame_score)
                    finalLaunchNumber += 1
                    break

                print(f"\tLancé {finalLaunchNumber + 1} :")  # 1ER LANCE

                skittlesTouched = self.checkSkittlesInTen()
                if (skittlesTouched == 10):
                    finalLaunchNumber += 1
                    nbLaunchFinalFrame = 3  # Définis le nombre de lancés restants =2 si strike au premier lance. On n'a plus que 2 lancés
                    # print("nbLaunchFinalFrame", nbLaunchFinalFrame)
                    # print("finalLaunchNumber", finalLaunchNumber)
                    # print(f"\t\tVous avez fait un strike au lance {finalLaunchNumber + 1} de la derniere frame ! Vous avez encore {nbLaunchFinalFrame-1} lancés !")
                    print(f"\t\tVous avez fait un strike au lance {finalLaunchNumber + 1} de la derniere frame !" + (
                        f" Vous avez encore {nbLaunchFinalFrame - 1} lancés !" if finalLaunchNumber + 1 != 3 else ""))

                    frame_score.append("X")
                    continue  # passe à l'itération suivante pour éviter le finalLaunchNumber+1

                else:
                    # spare
                    counter += 1
                    print("counter", counter)

                    if (counter == 2):
                        print("ICI")
                        if (counter > 1) and (skittlesTouched + frame_score[counter - 2] == 10):
                            frame_score.append("|")
                            nbLaunchFinalFrame = 3
                        else:
                            frame_score.append(skittlesTouched)
                    else:
                        frame_score.append(skittlesTouched)

                    print("nbLaunchFinalFrameBBB", nbLaunchFinalFrame)
                    finalLaunchNumber += 1
                    print("finalLaunchNumberAAA", finalLaunchNumber)
                print("frame_score", frame_score)

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