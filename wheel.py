import math
import pygame as pg
from pygame.math import Vector2
import turtle
import random

size = 20
speed = 20
spinning = False

spoke1 = turtle.Turtle()
spoke2 = turtle.Turtle()
spoke3 = turtle.Turtle()
spoke4 = turtle.Turtle()
spokes = [spoke1,spoke2,spoke3,spoke4]

turtle.register_shape("C:/Users/jml67/Game-Jam-2026/assets/blue_circle-ezgif.com-resize.gif")
turtle.register_shape("assets/red_square-ezgif.com-resize.gif")
turtle.register_shape("assets/yello_triangle-ezgif.com-resize.gif")

gif_shapes = ["C:/Users/jml67/Game-Jam-2026/assets/blue_circle-ezgif.com-resize.gif", "assets/red_square-ezgif.com-resize.gif", "assets/yello_triangle-ezgif.com-resize.gif"]

def generate_sequence():
    return [random.choice(gif_shapes) for _ in range(4)]

_ = 0
for spoke in spokes:
 spoke.speed(0)
 spoke.shape('square')
 spoke.shapesize(stretch_wid=size,stretch_len=1)
 spoke.left(45*_)
 _ += 1

rim = turtle.Pen()
rim.width(20)
rim.speed(0)
rim.up()
rim.forward(size*10)
rim.down()
rim.left(90)


rim.circle(size*10)

sequence_turtles = []

def setup_sequence_display():

    start_x = 50
    start_y = -200

    for i in range(4):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.goto(start_x + i * 40, start_y)
        sequence_turtles.append(t)

def display_sequence(seq):
    for i, gif in enumerate(seq):
        t = sequence_turtles[i]
        t.shape(gif)
        t.shapesize(stretch_wid=size, stretch_len=1)
        t.showturtle()

setup_sequence_display()
current_sequence = generate_sequence()
display_sequence(current_sequence)

def toggle_spin():
    global spinning
    spinning = not spinning

turtle.onscreenclick(lambda x, y: toggle_spin())

def update():
    if spinning:
        for spoke in spokes:
            spoke.left(speed)
    turtle.update()
    turtle.ontimer(update, 16)

update()

turtle.done()
