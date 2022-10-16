limit = int(input('Введите, сколько чисел Фибоначчи от нуля вы хотите получить: '))

list5 = [-1, -1, 0, 1, 1]

def FibonachiPositive(list, limit):
    number1 = 1
    number2 = 1
    current = 0
    while current <= limit-3:
        number3 = number2 + number1
        number1 = number2
        number2 = number3
        list.append(number3)
        current += 1

def FibonachiNegative(list, limit):
    number1 = -1
    number2 = -1
    current = 0
    while current <= limit-3:
        number3 = number2 + number1
        number1 = number2
        number2 = number3
        list.insert(0, number3)
        current += 1

FibonachiPositive(list5, limit)
FibonachiNegative(list5, limit)
print(f'Для лимита равного {limit} ряд Фибоначчи выглядит следующим образом: \n{list5}')