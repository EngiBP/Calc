import json

print('''
    Список доступных математических операций:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')


def get_text():
    with open('posts.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        count = 1
        result = []
        for i in data['response']['items']:
            if i['text']:
                result.append(str(count) + ' Сообщение:\n' + i['text'])
                count += 1

    return result


def calculate():
    permissions: str = input('Введите необходимую математическую операцию:')
    a = float(input('Введите число а: '))
    b = float(input('Введите число b: '))

    if permissions == '+':
        print(a + b)

    elif permissions == '-':
        print(a - b)

    elif permissions == '*':
        print(a * b)

    elif permissions == '/':
        print(a / b)

    else:
        print('Error: Неверный знак операции')


calculate()
