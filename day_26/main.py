import random

students = ['ALI', 'VALI', 'HUSAN', 'ANVAR']
students_scores = {name:random.randint(10, 100) for name in students}
passed_students = {name:grade for name, grade in students_scores.items() if grade>50}

all_students_scores = {
    "students": students,
    "scores": [random.randint(50, 100) for i in range(1,5)]
}
#
# dict_from_two_values_of_dict = {}
# first_value =[]
# second_value = []
# num = 0
# for score in all_students_scores.values():
#
#     if num == 1:
#         second_value = score
#
#     else:
#         for name in all_students_scores.values():
#             first_value = name
#             break
#
#     num += 1
#
# dict_from_two_lists= zip(first_value, second_value)
# print(dict(dict_from_two_lists))
