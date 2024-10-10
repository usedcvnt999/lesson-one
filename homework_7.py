# Домашнее задание (5) первая часть

GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Fronted', 'Backend', 'IOS', 'Android', 'QA', 'UX/UI', 'PM'],
    'bag': {'fail', 'error', 'stack'}
}
print(GeekTech)

# 1 ) Удалить баг

# 2 ) Изменить адресс на нынешний - ( Имбраимова )

# 3 ) Добавить поле контакты и в него добавить номер телефона и инстаграмм аккаунт Гиктека +996557820078, @geeks_edu

# 4 ) Добавить/Расширить список актуальных курсов новыми курсами, которые вы знаете. Затем преобразовать этот список в set

# 5 ) Вывести словарь на экран с помощью цикла for с получением всех пар "ключ": значение


# 1 )
del GeekTech['bag']
print(GeekTech)

# 2 )
GeekTech['address'] = 'Имбраимова 175'

# 3 )
GeekTech.update({'socials': {
    'phone number': +996557820078,
    'instagram': '@geeks_edu'
}})
print(GeekTech)

# 4 )
GeekTech['courses'].append('C++')
GeekTech.update({'courses': set(GeekTech.pop('courses'))})
print(GeekTech)

# 5 )
for key, value in GeekTech.items():
    print(f'{key}: {value}')
