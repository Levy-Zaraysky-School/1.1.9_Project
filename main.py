import turtle
import time

painter = turtle.Turtle()

print(turtle.window_height())
print(turtle.window_width())

painter.speed(1)

painter.up()
painter.goto(375, -450)

painter.down()

painter.goto(375, 0)

turtle.done()