def PrintList(list):
    i = 0
    leng = int(input('Enter length of list: '))
    while i < leng:
        list.append(int(input(f'Enter number {i+1} for list: ')))
        i += 1
    print(f'Current list: {list}')

def PrintList2(list):
    i = 0
    leng = int(input('Enter length of list: '))
    while i < leng:
        list.append(float(input(f'Enter number {i+1} for list: ')))
        i += 1
    print(f'Current list: {list}')