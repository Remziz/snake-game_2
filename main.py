from turtle import *
from random import randint
import time
h = Turtle()
d = Turtle()
c = Turtle()
h.color('green')
h.shape('turtle')
h.pensize(2)
d.color('blue')
d.shape('turtle')
d.pensize(2)
c.color('red')
c.shape('turtle')
c.pensize(2)
# Определи функцию rand_move(), переносящую черепашку в случайную точку
def rand_move_c(c):
    c.up()
    c.goto(randint(-200, 200), randint(-200, 200))
    c.down()
def rand_move_d(d):
    d.up()
    d.goto(randint(-200, 200), randint(-200, 200))
    d.down()
def rand_move_h(h):
    h.up()
    h.goto(randint(-200, 200), randint(-200, 200))
    h.down()
# Определи функцию-обработчик catch(x, y), которая обработает клик по черепашке
# (успешные клики копятся в свойстве t.points)
def catch_c(x, y):
    c.write('A!', font = ('Arial', 14, 'normal'))
    rand_move_c(c)
def catch_d(x, y):
    d.write('A!', font = ('Arial', 14, 'normal'))
    rand_move_d(d)
def catch_h(x, y):
    h.write('A!', font = ('Arial', 14, 'normal'))
    rand_move_h(h)
h.left(120)
d.right(90)
c.right(30)
while c.xcor() <= 150 and c.ycor() >= -150 and d.xcor() <= 150 and d.ycor() >= -150 and h.xcor() <= 150 and h.ycor() >= -150:
    time.sleep(0.7)
    h.forward(10)
    c.forward(10)
    d.forward(10)
    h.onclick(catch_h)
    d.onclick(catch_d)
    c.onclick(catch_c)
c.color('green')
c.write('Goodbye', font =('Arial', 16, 'bold'))
c.hideturtle()
d.clear()
h.clear()
exitonclick()