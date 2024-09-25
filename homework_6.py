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
        "Subjects": []
    }})
    first_subject = input(f"Введите два предмета студента\n Первый предмет: ")
    second_subject = input(f"Второй предмет: ")
    students[student_code]["Subjects"].append(first_subject)
    students[student_code]["Subjects"].append(second_subject)
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
        exit(0)
    else:
        print('Не корректное значение...')

user_menu(f"Введите код функции которую хотите исполнить:\n 1: Создать информацию о новом студенте\n 2: Просмотреть информацию о студенте с определенным ID\n 3: Изменить возраст студента по ID\n 4: Добавить новый предмет для студента по его ID\n 5: Удалить информацию о студенте по его ID\n 6: Завершить программу \n")