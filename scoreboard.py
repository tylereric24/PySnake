from turtle import *
from food import Food
from snake import Snake
import random

ALIGNMENT = "center"
FONT = ("Comic Sans", 24, "bold")


class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Current Score: {self.score} ", align=ALIGNMENT,font=FONT)
        
    def update_score(self):
        self.write(f"Current Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score % 10 == 0:
            colormode(255)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.color(r, g, b)
            self.clear()
            self.update_score()
        else:
            self.clear()
            self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"💀💀GAME OVER💀💀\nYOUR FINAL SCORE: {self.score} ", align=ALIGNMENT, font=FONT)

        
