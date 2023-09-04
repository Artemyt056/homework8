from pprint import pprint
from decimal import Decimal

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
students['Добродько Антон'] = {
        'Пошта': 'Antonio@gmail.com',
        'Вік': 19,
        'Номер телефону': '+38098415891',
        'Середній бал': 65
}

key, value, *other = students
total_score = 0
list_of_students = []

for key, value in students.items():
    if students[key]['Середній бал'] > 90:
        list_of_students.append([key, students[key]['Середній бал']])

    total_score += students[key]['Середній бал']
print(list(list_of_students))
for key in students:
    if not students[key]['Номер телефону']:
        students[key]['Номер телефону'] = '+38049123421'

if students:
    final_score = Decimal(total_score / len(students)).quantize(Decimal('0.01'))
    print('Середній бал групи', final_score)

pprint(students)

