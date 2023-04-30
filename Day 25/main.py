from turtle import Turtle, Screen
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("50_states.csv")
state_list = list(df["state"])

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(width=725, height=491)
screen.tracer(0)
screen.title("Name the States")

used_states = []
score = 0

while score < 50:
    inpt = str(screen.textinput(title=f"{score}/50 States Correct", prompt="Enter a state name: ")).title()
    if inpt == "Exit":
        states_to_learn = []
        for state in state_list:
            if state not in used_states:
                states_to_learn.append(state)

        df_learn = pd.DataFrame(states_to_learn)
        df_learn.to_csv("states_to_learn.csv", sep='\t')
        break
    if inpt in state_list and inpt not in used_states:
        score += 1
        s = Turtle()
        s.penup()
        state_data = df[df.state == inpt]

        s.goto(x=int(state_data.x), y=int(state_data.y))
        s.write(arg=inpt)
        used_states.append(inpt)

screen.exitonclick()
