import math
import pygame as pg
from pygame.math import Vector2
import turtle

size = 30
speed = 6

spoke1 = turtle.Turtle()
spoke2 = turtle.Turtle()
spoke3 = turtle.Turtle()
spoke4 = turtle.Turtle()
spokes = [spoke1,spoke2,spoke3,spoke4]

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

while True:
 for spoke in spokes:
  spoke.left(speed)

turtle.done()
