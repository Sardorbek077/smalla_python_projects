# with open('weather_data.csv') as data_file:
#     data = data_file.readline()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#         print(row[1])
#
#     temperature.pop(0)
#     print(temperature)

#
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# # data_temp = data['temp']
# # print(data_temp)
#
# # temp_list= data['temp'].to_list()
# # ave_temp = sum(temp_list)/len(temp_list)
# # print(ave_temp)
# #
# # print(data['temp'].max())
# #
# # print(data[data.temp == data.temp.max()])
# # Monday = data[data.day == 'Monday']
# # monday_temp = Monday.temp
# # print((monday_temp * 1.8)+32)
#
# data_dict = {
#     'cars': ['volvo', 'bmw', 'fiat', 'toyoto'],
#     'year': ['2000', '2020', '2030', '2000']
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('cars')
# print(data.cars)
#
# import pandas
#
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250103.csv')
# gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
# red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])
# print(gray_squirrels)
# print(black_squirrels)
# print(red_squirrels)
#
# data_dict = {
#     'Fur Color': ['Gray', 'Cinnamon', 'Black'],
#     'Count': [gray_squirrels, red_squirrels, black_squirrels]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv('squirrel_count.csv')


import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data['state'].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 States Correct',
                                    prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('States to learn.csv')
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t_states = turtle.Turtle()
        t_states.hideturtle()
        t_states.penup()
        state_data = data[data.state == answer_state]
        t_states.goto(state_data.x.item(), state_data.y.item())
        t_states.write(state_data.state.item())


screen.exitonclick()
