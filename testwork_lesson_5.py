# the_boys = {
#     'name': 'The Boys',
#     'releaseDate': 'July 26, 2019',
#     'mainActor': {
#         'Homelander': 'Antony Starr',
#         'AnnieJanuary': 'Erin Moriarty',
#         'BillyButcher': 'Karl Urban',
#         'HughieCampbell': 'Jack Quaid',
#     },
#     'episodes': 32
# }
#
# print(f' Сериал {the_boys['name']}, был выпущен {the_boys['releaseDate']} года.\n В главных ролях {the_boys['mainActor']}.\n В {the_boys['name']} {the_boys['episodes']} эпизодов или серий')
from math import expm1

students = {
    1: {
        "Name": "Maksim",
        "Age": 45,
        "Subjects": ["Algebra", "Physics"]
    },
    2: {
        "Name": "Eugen",
        "Age": 17,
        "Subjects": ["History", "Biology"]
    }
}



delete_tuple = [input(f"Введите ID студентов которых хотите удалить: ") for i in range (0, int(input(f"Введите количество ID: ")))]
try:
    for i in range(len(delete_tuple)):
        delete_ID = delete_tuple.pop(0)
        del students[int(delete_ID)]
except KeyError:
    print("Такого студента не существует :(")
print(students)
