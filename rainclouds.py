import turtle as trtl
import time

painter = trtl.Turtle()
painter.color("grey")
painter.speed(0)
painter.hideturtle()

# Create the turtle named painter
painter = trtl.Turtle()

painter.speed(0)

# Function to draw a cloud at a given position
def draw_cloud(x, y, scale=1.0):
    def draw_circle(painter, cx, cy, radius):
        painter.penup()
        painter.goto(cx, cy - radius)
        painter.pendown()
        painter.begin_fill()
        painter.circle(radius)
        painter.end_fill()

    # Cloud made of overlapping circles
    draw_circle(painter, x - 20 * scale, y, 15 * scale)
    draw_circle(painter, x, y, 20 * scale)
    draw_circle(painter, x + 20 * scale, y, 15 * scale)
    draw_circle(painter, x - 10 * scale, y + 15 * scale, 12 * scale)
    draw_circle(painter, x + 10 * scale, y + 15 * scale, 12 * scale)


# Draw 6 clouds with varying sizes and positions
draw_cloud(-150, 150, 0.9)  # small
draw_cloud(-30, 140, 1.2)  # a little bigger
draw_cloud(50, 130, 1.0)  # medium
draw_cloud(160, 150, 0.8)  # smaller
draw_cloud(100, 90, 1.3)  # slightly bigger
draw_cloud(-80, 100, 1.0)  # medium

painter.speed(0)

painter.penup()
painter.goto(100, 100)
painter.pendown()
painter.color("silver")
painter.begin_fill()
painter.circle(50)

painter.end_fill()
painter.color("black")
draw_cloud(100, 85, 1.3)  # slightly bigger

painter.penup()
painter.goto(100, 120)
painter.pendown()
painter.color("grey")
painter.begin_fill()
painter.circle(5)

painter.end_fill()

painter.penup()
painter.goto(110, 140)
painter.pendown()
painter.color("grey")
painter.begin_fill()
painter.circle(3)

painter.end_fill()

painter.penup()
painter.goto(80, 170)
painter.pendown()
painter.color("grey")
painter.begin_fill()
painter.circle(6)

painter.end_fill()

painter.penup()
painter.goto(130, 170)
painter.pendown()
painter.color("grey")
painter.begin_fill()
painter.circle(2)

painter.end_fill()

painter.penup()
painter.goto(130, 170)
painter.pendown()
painter.color("grey")
painter.begin_fill()
painter.circle(2)

painter.end_fill()
painter.penup()
painter.goto(30, 170)
painter.pendown()
painter.color("gold")

painter.begin_fill()
for _ in range(5):
    painter.forward(10)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-20, 150)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(8)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(140, 110)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(11)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-30, 110)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(7)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-60, 100)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(10)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(50, 180)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(5)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(40, 90)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(13)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-60, 90)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(4)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-80, 100)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(15)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-100, 180)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(5)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-85, 190)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(3)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-150, 190)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(6)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-160, 120)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(7)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-170, 110)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(5)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-180, 185)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(10)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-180, 170)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(2)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(190, 170)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(8)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(180, 150)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(7)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-150, 150)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(8)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-130, 150)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(5)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-100, 150)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(4)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(-80, 140)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(10)
    painter.right(144)
painter.end_fill()

painter.penup()
painter.goto(100, 80)
painter.pendown()

painter.begin_fill()
for _ in range(5):
    painter.forward(6)
    painter.right(144)
painter.end_fill()

painter.hideturtle()

import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.tracer(0)

# Setup pen
pen = turtle.Turtle()
pen.hideturtle()
pen.color("blue")
pen.speed(0)

# Raindrops: spread across a wide band, but shifted lower
# Instead of -200..200, use -100..150 (lower overall)
drops = [[random.randint(-300, 300), random.randint(-100, 150)] for _ in range(250)]


def update():
    pen.clear()
    for d in drops:
        # draw drop
        pen.up()
        pen.goto(d[0], d[1])
        pen.down()
        pen.setheading(-90)
        pen.forward(10)
        pen.up()

        # move downward
        d[1] -= 15

        # reset when below bottom
        if d[1] < -200:
            d[0], d[1] = random.randint(-300, 300), random.randint(-100, 150)

    screen.update()
    screen.ontimer(update, 100)


# Start animation
update()
# turtle.done()

wn = trtl.Screen()
print(wn.window_height(), wn.window_width())
wn.mainloop()













