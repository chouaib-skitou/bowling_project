
def calculate_score(frame_score_list):
    total_score = 0

    for i, frame in enumerate(frame_score_list):
        # Handling the second-to-last frame
        if i == len(frame_score_list) - 2:
            total_score += calculate_frame_score(frame, frame_score_list[i+1])

        # Handling the last frame
        elif i == len(frame_score_list) - 1:
            total_score += sum(frame)

        # Handling all other frames
        else:
            if frame[0] == "X":  # Strike
                total_score += 10 + sum_of_next_two_rolls(frame_score_list, i)
            elif "|" in frame:  # Spare
                total_score += 10 + frame_score_list[i+1][0]
            else:  # Regular throws
                total_score += sum(frame)

    return total_score

def sum_of_next_two_rolls(frames, index):
    next_two_rolls = []
    for frame in frames[index+1:index+3]:
        next_two_rolls.extend(frame)
    return sum(next_two_rolls[:2])

def calculate_frame_score(current_frame, next_frame):
    frame_score = 0
    if current_frame[0] == "X":  # Strike in the second-to-last frame
        frame_score = 10
        if next_frame[0] == "X":
            frame_score += 10 + (10 if next_frame[1] == "X" else next_frame[1])
        elif "|" in next_frame:  # Spare after strike
            frame_score += 10
        else:
            frame_score += sum(next_frame)
    elif "|" in current_frame:  # Spare in the second-to-last frame
        frame_score = 10 + (10 if next_frame[0] == "X" else next_frame[0])
    else:  # Regular throws
        frame_score = sum(current_frame)
    return frame_score



def test_last_frame_scenarios():
    frame_score_list = []
    currentScore = 0

    # Helper function to simulate rolling and updating frame scores
    def roll_and_update(frame_scores, skittles):
        frame_scores.append(skittles)
        frame_score_list.append(frame_scores)

    # Test for the last frame with a strike
    frame_scores_strike = []
    for _ in range(9):  # First 9 frames are all zeros
        roll_and_update([0, 0], 0)
    roll_and_update(frame_scores_strike, 10)  # Strike in the last frame
    roll_and_update(frame_scores_strike, 3)   # Extra roll 1
    roll_and_update(frame_scores_strike, 4)   # Extra roll 2
    score_strike = calculate_score(frame_score_list)  # Implement a function to calculate the score

    frame_score_list.clear()  # Clearing for next test

    # Test for the last frame with a spare
    frame_scores_spare = []
    for _ in range(9):  # First 9 frames are all zeros
        roll_and_update([0, 0], 0)
    roll_and_update(frame_scores_spare, 5)   # First roll in the last frame
    roll_and_update(frame_scores_spare, 5)   # Spare in the last frame
    roll_and_update(frame_scores_spare, 4)   # Extra roll
    score_spare = calculate_score(frame_score_list)

    frame_score_list.clear()  # Clearing for next test

    # Test for the last frame without strike or spare
    frame_scores_normal = []
    for _ in range(9):  # First 9 frames are all zeros
        roll_and_update([0, 0], 0)
    roll_and_update(frame_scores_normal, 3)  # First roll in the last frame
    roll_and_update(frame_scores_normal, 4)  # Second roll in the last frame
    score_normal = calculate_score(frame_score_list)

    # Verify expected scores for each scenario
    assert score_strike == 17  # 10 (strike) + 3 + 4
    assert score_spare == 14   # 5 + 5 (spare) + 4
    assert score_normal == 7   # 3 + 4
