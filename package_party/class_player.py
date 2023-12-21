import party_manager


class Player:
    id = -1
    name = ""
    current_frame = 0
    total_score = 0
    list_of_score = [[], []]

    def __init__(self, id, name):
        self.id = id
        self.name = "player" + id


    # The function to call at the start of player's frame
    # Should end at the end of the frame
    def next_turn(self, current_frame):
        return

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