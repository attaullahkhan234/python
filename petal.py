import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Petal Design")

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "lime","cyan", "violet", "pink", "white"]

for i in range(36):
    t.color(colors[i % len(colors)])
    t.begin_fill()
    for j in range(2):
        t.circle(100, 60)
        t.left(120)
    t.end_fill()
    t.left(10)



t.penup()
t.goto(0, -10)
t.pendown()

t.color("yellow")
t.dot(40)

turtle.done()