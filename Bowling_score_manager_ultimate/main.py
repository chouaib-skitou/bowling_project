import tkinter as tk

# Bowling scoring logic would go here
def calculate_frame_scores(rolls):
    frame_scores = []
    roll_index = 0
    frame = 0
    while frame < 10 and roll_index < len(rolls):
        frame_score = 0
        if rolls[roll_index] == 10:  # Strike
            frame_score = 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
            roll_index += 1
        elif roll_index + 1 < len(rolls) and rolls[roll_index] + rolls[roll_index + 1] == 10:  # Spare
            frame_score = 10 + rolls[roll_index + 2]
            roll_index += 2
        elif roll_index + 1 < len(rolls):  # Open frame
            frame_score = rolls[roll_index] + rolls[roll_index + 1]
            roll_index += 2
        else:  # Not enough rolls left to calculate a frame score
            break
        
        frame_scores.append(frame_score)
        frame += 1

        # Handling the 10th frame: If we're on the last frame, add any extra rolls
        if frame == 10:
            while roll_index < len(rolls):
                frame_scores[-1] += rolls[roll_index]
                roll_index += 1
    
    return frame_scores




class BowlingScoreGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bowling Score Calculator")
        self.geometry("800x600")  # Adjust the size as needed

        # Buttons for pin entry
        button_style = {
            'bg': '#4CAF50',  # Background color
            'fg': '#FFFFFF',  # Foreground (text) color
            'font': ('Helvetica', 12, 'bold'),  # Font type, size, and style
            'borderwidth': 2,  # Border width
            'relief': 'raised',  # Border style
            'padx': 10,  # Padding in x direction
            'pady': 5  # Padding in y direction
        }

        self.pin_buttons_frame = tk.Frame(self)
        self.pin_buttons_frame.pack()
        for pin in range(11):  # 0 to 10 pins
            btn = tk.Button(self.pin_buttons_frame, text=str(pin), command=lambda p=pin: self.enter_pins(p), **button_style)
            btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Display for frame scores
        self.frame_scores = [tk.StringVar() for _ in range(10)]
        self.frames_frame = tk.Frame(self)
        self.frames_frame.pack()
        for i, var in enumerate(self.frame_scores):
            tk.Label(self.frames_frame, textvariable=var).grid(row=0, column=i)

        # Labels for Hdcp Score and Max Possible
        self.hdcp_score_var = tk.StringVar()
        self.max_possible_var = tk.StringVar()
        tk.Label(self, textvariable=self.hdcp_score_var).pack()
        tk.Label(self, textvariable=self.max_possible_var).pack()

        self.rolls = []  # Stores the rolls

    def enter_pins(self, pins):
        self.rolls.append(pins)
        self.update_scores()

    def update_scores(self):
        # Here we would calculate the frame scores, the handicap score, and the max possible score
        frame_scores = calculate_frame_scores(self.rolls)
        for var, score in zip(self.frame_scores, frame_scores):
            var.set(score)
        # Update Hdcp and Max Possible labels
        self.hdcp_score_var.set("Hdcp Score: TBD")  # Replace TBD with actual calculation
        self.max_possible_var.set("Max Possible: TBD")  # Replace TBD with actual calculation

if __name__ == "__main__":
    app = BowlingScoreGUI()
    app.mainloop()
