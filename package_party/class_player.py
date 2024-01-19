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

        self.initialize_player_score()


    def initialize_player_score(self):
        initial_frame = ["-", "-"]
        for i in range(party_manager.NUMER_OF_FRAME):
            self.list_of_party_score.append(initial_frame)

    def iterate_number_throw(self):
        # Last frame
        if self.num_current_frame == party_manager.NUMER_OF_FRAME - 1:
            if self.num_bowling_throw == 1:
                self.num_bowling_throw = 2
            if self.num_bowling_throw == 2:
                if ("X" in self.list_of_party_score[self.num_current_frame][self.num_bowling_throw]) \
                        or ("|" in self.list_of_party_score[self.num_current_frame][self.num_bowling_throw]):
                    self.num_bowling_throw = 3

        # All frames except last one
        else:
            if self.num_bowling_throw == 1:
                self.num_bowling_throw = 2
            elif self.num_bowling_throw == 2:
                self.num_bowling_throw = 1

    def add_new_frame_score(self, score):
        print
        self.list_of_party_score[self.num_current_frame][self.num_bowling_throw] = score
        self.iterate_number_throw()

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
            finalLaunchNumber = 0  # determine le nombre de lance effectue dans la derniere frame
            counter = 0
            while (finalLaunchNumber < nbLaunchFinalFrame):  # Droit a 3 lances si strike ou spare -> 1 lance supplementaire
                if ((len(frame_score) == 2) and ("X" not in frame_score) and (
                        "|" not in frame_score)):  # cas où on a fait ni strike ni spare
                    finalLaunchNumber += 1
                    counter += 1
                    break

                print(f"\tLancé {finalLaunchNumber + 1} :")  # 1ER LANCE

                skittlesTouched = self.checkSkittlesInTen()

                # if(counter == 1): #verifie la coherence au 2eme lance
                #    skittlesTouched = checkCoherentSkittlesLastFrame(skittlesTouched,frame_score, counter-1)

                if (skittlesTouched == 10):
                    finalLaunchNumber += 1
                    nbLaunchFinalFrame = 3  # Définis le nombre de lancés restants =2 si strike au premier lance. On n'a plus que 2 lancés
                    # print(f"\t\tVous avez fait un strike au lance {finalLaunchNumber + 1} de la derniere frame ! Vous avez encore {nbLaunchFinalFrame-1} lancés !")
                    print(f"\t\tVous avez fait un strike au lance {finalLaunchNumber} de la derniere frame !" + (
                        f" Vous avez encore {nbLaunchFinalFrame - 1} lancés !" if finalLaunchNumber + 1 != 3 else ""))

                    frame_score.append("X")
                    counter += 1
                    print("AJOUT DE COUNTER counter :", counter)
                    continue  # passe à l'itération suivante pour éviter le finalLaunchNumber+1

                else:
                    # spare
                    counter += 1
                    if (counter == 2):
                        print("frame_score[counter-2]", frame_score[counter - 2])

                        if (frame_score[0] == "X"):
                            frame_score.append(skittlesTouched)
                            print(f"\t\t Vous avez encore 1 lancer !")

                    if (e == 2):  # au 2eme lancer vérifie que c'est coherent avec le precedent
                        skittlesTouched = self.checkCoherentSkittlesLastFrame(skittlesTouched, frame_score, e - 1)
                        if (skittlesTouched == party_manager.NUMBER_OF_SKITTLES):
                            frame_score.append('X')
                            print(f"\t\tVous avez fait un strike au lance 3 de la derniere frame !")
                        elif (frame_score[e - 1] != "X"):  # cas du spare
                            if (frame_score[e - 1] + skittlesTouched == party_manager.NUMBER_OF_SKITTLES):  # cas du spare
                                frame_score.append("|")
                                print(f"\t\tVous avez fait un spare au lance 3 de la derniere frame !")
                        else:
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

    def checkCoherentSkittlesLastFrame(parSkittlesTouched, par_frame_score, counter):
        print("frame_score[counter-1]", par_frame_score[counter])
        while (parSkittlesTouched > 10 - par_frame_score[counter]):
            print(f"\t\tAu tour précédent vous avez renversé {par_frame_score[counter-1]} quilles :")
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


