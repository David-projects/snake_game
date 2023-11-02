from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.shapesize(stretch_wid=20, stretch_len=100)
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.color("white")
        self.shapesize(stretch_wid=40, stretch_len=100)
        self.goto(0, 0)
        self.write(arg=f"Game Over: {self.score}", move=False, align=ALIGNMENT, font=FONT)