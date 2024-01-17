class BowlingGame:
    def __init__(self):
        # Initialisation de 10 manches pour une partie de bowling
        self.frames = [Frame() for _ in range(10)]
        self.currentFrameIndex = 0  # Index de la manche en cours

    def roll(self, pins):
        # Enregistre le nombre de quilles tombées dans la manche actuelle
        current_frame = self.frames[self.currentFrameIndex]
        current_frame.roll(pins)

        # Passe à la manche suivante si la manche actuelle est complète
        if self.currentFrameIndex < 9 and current_frame.is_complete():
            self.currentFrameIndex += 1

    '''def score(self):
        # Calcule le score total de la partie
        total_score = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            # Obtient les manches suivantes pour calculer les bonus de strike/spare
            next_frame = self.frames[i + 1] if i + 1 < len(self.frames) else None
            next_next_frame = self.frames[i + 2] if i + 2 < len(self.frames) else None
            total_score += frame.score(next_frame, next_next_frame)
        return total_score'''

    def score(self):
        total_score = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            frame_score = sum(frame.rolls)

            # Si c'est un strike, ajouter le score des deux prochains lancers.
            if frame.is_strike() and i < 9:  # Exclure la dernière frame
                frame_score += self.score_for_strike(i)

            # Si c'est un spare, ajouter le score du prochain lancer.
            elif frame.is_spare() and i < 9:  # Exclure la dernière frame
                frame_score += self.score_for_spare(i)

            total_score += frame_score

        return total_score

    def score_for_strike(self, frame_index):
        next_frame = self.frames[frame_index + 1]
        next_next_frame = self.frames[frame_index + 2] if frame_index + 1 < 9 else None
        bonus = sum(next_frame.rolls[:2])
        if next_frame.is_strike() and next_next_frame:
            bonus += next_next_frame.rolls[0]
        return bonus

    def score_for_spare(self, frame_index):
        next_frame = self.frames[frame_index + 1]
        return next_frame.rolls[0]

class Frame:
    def __init__(self):
        self.rolls = []  # Stocke les lancers de la manche
        self.complete = False  # Indique si la manche est complète

    def roll(self, pins):
        # Enregistre un lancer et vérifie si la manche est complète
        self.rolls.append(pins)
        if len(self.rolls) == 2 or self.rolls[0] == 10:
            self.complete = True

    def is_complete(self):
        # Special handling for the 10th frame
        if len(self.rolls) >= 3:
            return True
        if len(self.rolls) == 2 and self.rolls[0] != 10 and sum(self.rolls) < 10:
            return True
        return False

    def is_complete(self):
        # Vérifie si la manche est complète
        return self.complete

    def score(self, next_frame=None, next_next_frame=None):
        frame_score = sum(self.rolls)
        if self.is_strike():
            frame_score += sum(next_frame.first_two_rolls())
            if next_frame.is_strike() and next_next_frame:
                frame_score += next_next_frame.first_roll()
        elif self.is_spare():
            frame_score += next_frame.first_roll() if next_frame else 0
        return frame_score

    def is_strike(self):
        return self.rolls[0] == 10

    def is_spare(self):
        return sum(self.rolls) == 10

    def first_two_rolls(self):
        return self.rolls[:2]

    def first_roll(self):
        return self.rolls[0] if self.rolls else 0