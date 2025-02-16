student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data_dict_from_pandas = pandas.read_csv('nato_phonetic_alphabet.csv')

letter = data_dict_from_pandas['letter'].to_list()
code = data_dict_from_pandas['code'].to_list()
new_data_dict = zip(letter, code)
new_data_dict = dict(new_data_dict)
# print(new_data_dict)

# Another way of creating dict from csv_file
data_dict_from_pandas = {row.letter:row.code for (index, row) in data_dict_from_pandas.iterrows()}
# print(new_data)

user_input = input('Please write your name: ').upper()
for i in user_input:
    print(i, new_data_dict[i], end=', ')