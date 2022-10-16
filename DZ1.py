from my_def import PrintList

list1 = []

def SearchSum(list):
    i = 1
    sum = 0
    while i < int(len(list)):
        sum += list[i]
        i += 2
    print(f'Sum = {sum}')

PrintList(list1)
SearchSum(list1)
