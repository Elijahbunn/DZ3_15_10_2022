number = int(input('Enter number: '))
number2 = []

def Tranformation(number, list):
    while number > 1:
        list.append(int(round(number%2)))
        number = int(number / 2)
    number_dv = 0
    i = 1
    while i < int(len(list)):
        number_dv += list[i]*(10**i)
        i += 1
    number_dv += 1*(10**i) + 1
    print(f'Данное число в двоичной системе = {number_dv}')

Tranformation(number, number2)