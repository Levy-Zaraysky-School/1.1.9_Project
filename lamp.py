import turtle
import time

turtle.speed(5)
turtle.fillcolor("Grey")
#turtle.hideturtle()
turtle.pencolor("Grey")
turtle.hideturtle()

turtle.up()
turtle.goto(175, -200)
turtle.down()

turtle.begin_fill() # Base
turtle.goto (160,-150)
turtle.goto(140,-150)
turtle.goto(125, -200)
turtle.goto(175, -200)
turtle.end_fill()

turtle.up()
turtle.goto(156,-150)
turtle.down()

turtle.begin_fill() # Pole
turtle.goto(156,0)
turtle.goto(144,0)
turtle.goto(144,-150)
turtle.end_fill()

turtle.up()
turtle.goto(144,0)
turtle.down()

turtle.pencolor("Black") # For outline

# Light Base
turtle.goto(130,40)
turtle.goto(170,40)
turtle.goto(156,0)

turtle.up()
turtle.goto(130,40)
turtle.down()

turtle.speed(0)
turtle.pencolor("Grey")

turtle.begin_fill() # Glass
turtle.goto(150,60)
turtle.goto(170,40)
turtle.goto(130,40)
turtle.end_fill()

turtle.speed(1)
turtle.up()
turtle.goto(150,0)
turtle.goto(149,0)
turtle.down()
turtle.goto(149,10)
turtle.goto(151,10)
turtle.goto(151,0)

turtle.begin_fill()
turtle.up()
turtle.goto(150,10)
turtle.down()
turtle.circle(8)
turtle.fillcolor("Yellow")
turtle.end_fill()

turtle.speed(0)

# for i in range(10):
#     time.sleep(0.5)
#     turtle.fillcolor("Yellow")
#     turtle.end_fill()
#     time.sleep(0.5)
#     turtle.undo()
#     turtle.begin_fill()
#     turtle.up()
#     turtle.goto(150, 10)
#     turtle.down()
#     turtle.circle(8)

# turtle.done()