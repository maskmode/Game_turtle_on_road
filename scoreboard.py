from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.up()
        self.goto(-280, 260)
        self.upd_score()


    def upd_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def hlevel(self):
        self.level += 1
        self.upd_score()

    def game_over(self):
        self.goto(-90, 0)
        self.write("GAME OVER", align="left", font=FONT)




