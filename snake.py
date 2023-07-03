from turtle import *
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
corvals = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    

    
    
    


    def __init__(self):
        self.my_turtles = []
        self.create_snake()
        self.head = self.my_turtles[0]

        
    def create_snake(self):
        for x in corvals:
            self.add_snake(x)




    def move(self):
        for turtle in range(len(self.my_turtles) -1, 0, -1):
            new_x = self.my_turtles[turtle - 1].xcor()
            new_y = self.my_turtles[turtle - 1].ycor()
            self.my_turtles[turtle].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.my_turtles[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.my_turtles[0].setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
         self.my_turtles[0].setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.my_turtles[0].setheading(0)

    def add_snake(self, x):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(x)
        self.my_turtles.append(new_turtle)
    
    def grow(self):
        self.add_snake(self.my_turtles[-1].position())