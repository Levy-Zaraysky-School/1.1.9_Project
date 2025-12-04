import turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
Pai = turtle.Turtle()
Pai.hideturtle()
Pai.speed(0)
Pai.color("gray")
Pai.pensize(1)
Pai_width = 6000
Pai_height = 120
y_offset = -200
Pai.penup()
Pai.goto(-Pai_width/2, y_offset)
Pai.pendown()
Pai.begin_fill()
for _ in range(2):
    Pai.forward(Pai_width)
    Pai.left(90)
    Pai.forward(Pai_height)
    Pai.left(90)
Pai.end_fill()
line = turtle.Turtle()
line.hideturtle()
line.speed(0)
line.color("white")
line.pensize(6)
dash_length = 30
gap_length = 20
num_dashes = int(Pai_width / (dash_length + gap_length))
start_x = -Pai_width/2 + 10
center_y = y_offset + Pai_height/2
line.penup()
line.goto(start_x, center_y)
line.setheading(0)
for _ in range(num_dashes):
    line.pendown()
    line.forward(dash_length)
    line.penup()
    line.forward(gap_length)
grass = turtle.Turtle()
grass.color("green")
grass.pensize(1)
grass.speed(0)
Pai_width = 6000
Pai_height = 120
y_offset = -300
grass.penup()
grass.goto(-Pai_width/2, y_offset)
grass.pendown()
grass.begin_fill()
for _ in range(2):
    grass.forward(Pai_width)
    grass.left(90)
    grass.forward(Pai_height)
    grass.left(90)
grass.end_fill()