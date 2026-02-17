import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




df = pd.read_csv("50_states.csv")

guessed_states = []
all_states = df.state.str.lower().to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states name?")

    if answer_state is None:
        continue

    if answer_state == "exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break

    if answer_state.lower() in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_row = df[df.state.str.lower() == answer_state.lower()]
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

    if len(guessed_states) == 50:
        break



