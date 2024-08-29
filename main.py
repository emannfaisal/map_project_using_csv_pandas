import turtle
import pandas
import csv

screen=turtle.Screen()
screen.setup(500,500)
screen.title("guess the states")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
state_x_coords = states.x.to_list()
state_y_coords = states.y.to_list()
guessed_states = []
missing_states = []
guess_state = 0
while len(guessed_states)<len(states_list):
    guess = screen.textinput("Guess the state","enter a name (or 'exit' or 'quit')").strip().capitalize()
    if guess.lower() == 'exit':
        for i in range(0,len(states_list)):
            for j in range(0,len(guessed_states)):
                if states_list[i] not in guessed_states[j]:
                    missing_states.append(states_list[i])
        with open('missing_states.csv',mode = 'w',newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(missing_states)
        break
    if guess in states_list and guess not in guessed_states:
        guessed_states.append(guess)
        index = states_list.index(guess)
        x = state_x_coords[index]
        y = state_y_coords[index]
        turtle.goto(x,y)
        turtle.write("guess",align='left',font=('Arial',10,'bold'))



if len(guessed_states) == len(states_list):
    turtle.goto(0,250)
    turtle.write("Congratulations! You guessed all states!",align="left",font=('Arial',10,'Normal'))
screen.exitonclick()


