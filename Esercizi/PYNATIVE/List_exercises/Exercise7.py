'''Aggiungi un nuovo elemento all'elenco dopo un elemento specificato'''

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]


list1[2][2].append(7000)
print(list1)