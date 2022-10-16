from my_def import PrintList

numbers = []
products = []
dict1 = {}  #Решил добавить словарь для тренировки навыка)

def DubleProduct(list_1, list_2, dict):
    i = 0
    while i < (int(len(list_1))/2):
        product = (list_1[i]*list_1[-(i+1)])
        list_2.append(product)
        dict1[f'Product of {list_1[i]} and {list_1[-(i+1)]}'] = product
        i += 1
    print(f'Products - {list_2}')
    print(f'Products in dictionary - {dict1}')

PrintList(numbers)
DubleProduct(numbers, products, dict1)
