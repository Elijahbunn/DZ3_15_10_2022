from my_def import PrintList2

list3 = []


def FindDiff(list):
    my_max = 0
    my_min = list[0] % 1
    i = 0
    while i < int(len(list)):
        current = list[i] % 1
        if current > my_max:
            my_max = round(current, 5)
        elif current < my_max and current < my_min and current != 0:
            my_min = round(current, 5)
        i += 1
    print(f'Max is {my_max}')
    print(f'Min is {my_min}')
    diff = my_max - my_min
    print(f'Difference is {diff}')


PrintList2(list3)
FindDiff(list3)
