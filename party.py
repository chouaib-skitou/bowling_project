nbFrame = 5
currentScore = 0
nbLaunch = 2
frame_score_list = []

def checkSkittlesInTen():
    skittlesTouched = int(input("\t\tIndiquez le nombre de quilles renversées :"))
    while (skittlesTouched > 10 or skittlesTouched < 0):  # Empêche les valeurs incohérentes
        skittlesTouched = int(input("\t\tVeuillez renseigner un nombre entre 0 et 10 :"))
    return skittlesTouched

def checkCoherentSkittles(parSkittlesTouched, par_frame_score):
    while (parSkittlesTouched > 10 - par_frame_score[0]):
        print(f"\t\tAu tour précédent vous avez renversé {par_frame_score[0]} quilles :")
        parSkittlesTouched = int(input("\t\tVeuillez renseigner un nombre cohérent :"))
    return parSkittlesTouched

def checkSpare(par_frame_score, parSkittlesTouched):
    if (par_frame_score[0] + parSkittlesTouched == 10):
        print(f"\t\tVous avez fait un spare ! On passe à la frame suivante !")
        par_frame_score.append("|")
    else:
        par_frame_score.append(skittlesTouched)


#contrary to usual strike check, since we are in the last frame, we keep playing
def checkStrikeLastFrame(par_frame_score, parSkittlesTouched):
    if (parSkittlesTouched == 10):  # En cas de strike
        print(f"\t\tVous avez fait un strike ! On passe à la frame suivante !")
        par_frame_score.append("X")
    else:
        par_frame_score.append(parSkittlesTouched)



for frameNumber in range(nbFrame):
    print("frame_score_list : ", frame_score_list)
    print(f"Frame {frameNumber+1} :")
    frame_score = [] #stock le nombre de quilles renversées pour
    print("frameNumber", frameNumber)
    if (frameNumber == nbFrame - 1): #LE DERNIERE FRAME
        for launchNumber in range(nbLaunch+1): #Droit a 3 lances si strike ou spare -> lanc supplementaire

            print(f"\tLancé {launchNumber + 1} :")  # 1ER LANCE

            if (launchNumber == 0):  # 1ER LANCE
                print("nbLaunch", nbLaunch)
                skittlesTouched = checkSkittlesInTen()  # Nombre de quilles entre 0 et 10

                if (skittlesTouched == 10):  # En cas de strike
                    print(f"\t\tVous avez fait un strike à la première partie de la dernière frame ! Vous avez le droit à encore 2 lancés !")
                    nbLaunch += 1
                    frame_score.append("X")
                else:
                    frame_score.append(skittlesTouched)

            else:
                #TEMPORAIRE : SI STRIKE AVANT
                skittlesTouched = checkSkittlesInTen()
                frame_score.append(skittlesTouched)
                #pas de check de coherence car toutes tombées
                #checkSpare(frame_score, skittlesTouched)  # Vérifie si on fait un spare
                #skittlesTouched = checkCoherentSkittles(skittlesTouched, frame_score)
                print(frame_score)


                #checkStrikeLastFrame(frame_score, skittlesTouched)


    else:
        for launchNumber in range(nbLaunch):
            print(f"\tLancé {launchNumber + 1} :") #1ER LANCE

            if (launchNumber == 0):  #1ER LANCE
                skittlesTouched = checkSkittlesInTen() #Nombre de quilles entre 0 et 10

                if(skittlesTouched == 10): #En cas de strike
                    print(f"\t\tVous avez fait un strike ! On passe à la frame suivante !")
                    frame_score.append("X")
                    frame_score.append("")
                    break
                else:
                    frame_score.append(skittlesTouched)

            if(launchNumber == 1): #2EME LANCE
                skittlesTouched = checkSkittlesInTen() #Nombre de quilles entre 0 et 10
                skittlesTouched = checkCoherentSkittles(skittlesTouched, frame_score) #Nombre de quilles coherent avec lance precedent
                checkSpare(frame_score, skittlesTouched) #Vérifie si on fait un spare

    frame_score_list.append(frame_score)


print(frame_score_list)
       # if (skittlesTouched == 10):
        #    print("Vous avez fait un strike ! ")



