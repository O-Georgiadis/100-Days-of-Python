from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower().strip()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-230, y_positions[turtle_index])

def evaluate_winner():
    for turtle in screen.turtles():
        if turtle.xcor() > 230:
             return turtle

while not evaluate_winner():
    for turtle in screen.turtles():
        turtle.forward(random.randint(0, 10))
        eval = evaluate_winner()
        if eval:
            break


if eval.color()[0] == user_bet:
    print(f"You've won! The {eval.color()[0]} turtle is the winner!")
else:
    print(f"You've lost! The {eval.color()[0]} turtle is the winner!")

screen.exitonclick()