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

def create():
    student_code = int(input(f"Введите ID студента: "))
    students.update({student_code: {
        "Name": input(f"Введите имя студента: "),
        "Age": input(f"Введите возраст студента: "),
        "Subjects": [input(f"Введите два предмета студента\n Введите: ") for _ in range (0, 2)]
    }})

def search():
    student_name = input(f"Введите имя: ")
    for i in range(len(students) + 1):
        try:
            if students[i + 1]["Name"] == student_name:
                print(f"Студент имя которого вы искали под ID: ", i + 1)
                break
        except KeyError:
            print("Такого студента не существует :(")


def mass_delete():
    delete_tuple = [input(f"Введите ID студентов которых хотите удалить: ") for i in range(0, int(input(f"Введите количество ID: ")))]
    try:
        for i in range(len(delete_tuple)):
            delete_ID = delete_tuple.pop(0)
            del students[int(delete_ID)]
    except KeyError and ValueError:
        print("Такого студента не существует :(")

while True:
    print(students)
    user_input = int(input(f"Введите код функции которую хотите исполнить:\n "
                           f"1: Создать информацию о новом студенте\n "
                           f"2: Просмотреть информацию о студенте с определенным ID\n "
                           f"3: Изменить возраст студента по ID\n "
                           f"4: Добавить новый предмет для студента по его ID\n "
                           f"5: Удалить информацию о студенте по его ID\n "
                           f"6: Поиск студента по имени\n "
                           f"7: Массовое удаление студентов по ID\n "
                           f"8: Завершить программу \n"))
    if user_input == 1:
        create()
    elif user_input == 2:
        print(students[int(input(f"Введите ID студента информацию о котором хотите просмотреть: "))])
    elif user_input == 3:
        students[int(input(f"Введите ID студента: "))]["Age"] = input(f"Введите возраст на который хотите изменить: ")
    elif user_input == 4:
        students[int(input(f"Введите ID студента: "))]["Subjects"].append(input(f"Введите предмент который хотите добавить: "))
    elif user_input == 5:
        del students[int(input(f"Введите код студента которого хотите удалить: "))]
    elif user_input == 6:
        search()
    elif user_input == 7:
        mass_delete()
    elif user_input == 8:
        exit(0)
    else:
        print('Не корректное значение...')
