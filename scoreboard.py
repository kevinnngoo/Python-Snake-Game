from turtle import Turtle
from snake import Snake
from food import Food
import time

ALIGNMENT = "CENTER"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #self.high_score = 0
        #write the high score to data.txt
        #read the high score from data.txt
        with open("data.txt") as data:
           self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()

        # if snake.head.distance(food) < 15:
        #     food.refresh()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()