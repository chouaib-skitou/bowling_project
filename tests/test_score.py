def calculer_score(frame_score_list):
    score_total = 0

    for frame_index in range(len(frame_score_list)):
        frame = frame_score_list[frame_index]

        # Pour les 9 premières frames
        if frame_index < 9:
            if frame[0] == "X":  # Strike
                score_total += 10
                # Ajout des scores des deux lancers suivants
                if frame_index+1 < len(frame_score_list):
                    next_frame = frame_score_list[frame_index + 1]
                    if next_frame[0] == "X":  # Prochain lancer est aussi un strike
                        score_total += 10
                        if frame_index+2 < len(frame_score_list):
                            if frame_score_list[frame_index + 2][0] == "X":
                                score_total += 10
                            else:
                                score_total += frame_score_list[frame_index + 2][0]
                    else:
                        score_total += sum(next_frame[:2])
            elif frame[1] == "|":  # Spare
                score_total += 10
                # Ajout du score du premier lancer de la frame suivante
                if frame_index+1 < len(frame_score_list):
                    score_total += frame_score_list[frame_index + 1][0]
            else:
                score_total += sum(frame[:2])
        else:  # Dernière frame
            frame_scores = [10 if x == "X" or x == "|" else x for x in frame]
            score_total += sum(frame_scores)

    return score_total
