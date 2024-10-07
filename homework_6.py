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
    student_code = input(f"Введите ID студента: ")
    students.update({student_code: {
        "Name": input(f"Введите имя студента: "),
        "Age": input(f"Введите возраст студента: "),
        "Subjects": [input(f"Введите два предмета студента\n Введите: ") for _ in range (0, 2)]
    }})
    print(students)

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
    delete_tuple = [input(f"Введите ID студентов которых хотите удалить: ") for i in
                    range(0, int(input(f"Введите количество ID: ")))]
    try:
        for i in range(len(delete_tuple)):
            delete_ID = delete_tuple.pop(0)
            del students[int(delete_ID)]
    except KeyError and ValueError:
        print("Такого студента не существует :(")
    print(students)

def user_menu(placeholder: int):
    user_input = int(input(placeholder))
    if user_input == 1:
        create()
    elif user_input == 2:
        print(students[int(input(f"Введите ID студента информацию о котором хотите просмотреть: "))])
    elif user_input == 3:
        students[int(input(f"Введите ID студента: "))]["Age"] = input(f"Введите возраст на который хотите изменить: ")
        print(students)
    elif user_input == 4:
        students[int(input(f"Введите ID студента: "))]["Subjects"].append(input(f"Введите предмент который хотите добавить: "))
        print(students)
    elif user_input == 5:
        del students[int(input(f"Введите код студента которого хотите удалить: "))]
        print(students)
    elif user_input == 6:
        search()
    elif user_input == 7:
        mass_delete()
    elif user_input == 8:
        exit(0)
    else:
        print('Не корректное значение...')


user_menu(f"Введите код функции которую хотите исполнить:\n 1: Создать информацию о новом студенте\n 2: Просмотреть информацию о студенте с определенным ID\n 3: Изменить возраст студента по ID\n 4: Добавить новый предмет для студента по его ID\n 5: Удалить информацию о студенте по его ID\n 6: Поиск студента по имени\n 7: Массовое удаление студентов по ID\n 8: Завершить программу \n")