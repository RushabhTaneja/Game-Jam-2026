import turtle
import _tkninter
import time

# Setup screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0) # Fastest speed
t.hideturtle()
turtle.bgcolor("white")

# Define wheel properties
RADIUS = 150
NUM_SEGMENTS = 8
ANGLE = 360 / NUM_SEGMENTS

# Function to draw the wheel
def draw_wheel(rotation_angle):
    t.clear() # Clear previous drawings
    t.penup()
    t.goto(0, -RADIUS)
    t.pendown()
    t.color("black")
    t.circle(RADIUS) # Draw outer circle

    # Draw segments (simple coloring for visual effect)
    for i in range(NUM_SEGMENTS):
        start_angle = i * ANGLE + rotation_angle
        end_angle = (i + 1) * ANGLE + rotation_angle
        t.penup()
        t.goto(0, 0)
        t.setheading(start_angle)
        t.pendown()
        t.begin_fill()
        t.circle(RADIUS, ANGLE)
        t.goto(0, 0)
        t.end_fill()
        t.penup()

# Animation loop
angle_offset = 0
while True:
    draw_wheel(angle_offset)
    angle_offset += 5 # Increment angle for rotation
    if angle_offset > 360:
        angle_offset = 0
    time.sleep(0.05) # Control speed
