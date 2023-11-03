from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.shapesize(stretch_wid=20, stretch_len=100)
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.color("white")
    #     self.shapesize(stretch_wid=40, stretch_len=100)
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over: {self.score}", move=False, align=ALIGNMENT, font=FONT)