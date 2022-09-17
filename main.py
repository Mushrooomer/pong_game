from turtle import Screen, Turtle
from paddle import Paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()











screen.exitonclick()