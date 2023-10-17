"""Turtle Tutorial Lesson"""

__author__ = "730651920"

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()
i: int = 0
leo.speed(50)
leo.penup()
leo.goto(-150,-75)
leo.pendown()
leo.pencolor("pink")
leo.fillcolor(44, 229, 217)


leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

side_length: int = 300 
bob.speed(50)
bob.penup()
bob.goto(-150,-75)
bob.pendown()
j: int = 0
while (j < 35):
    side_length *= .95
    bob.forward(side_length)
    bob.left(121.5)
    j = j + 1
bob.hideturtle()    



done()