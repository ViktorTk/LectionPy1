# Создание списка
# list_1 = [] # - создали пустой список
# list_1 = list() # - также создали пустой список
# list_1 = [1, 2, 3, 8]
# print(list_1) # - выведет весь список

# for i in list_1: # - выводит каждый элемент списка на новую строку
#     print(i)

# print(len(list_1)) # - выводит количество элементов в списке

# print(list_1[3]) # - выводит элемент под нужным номером (нумерация начинается с 0)

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # - дополнили список еще одним элементом
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1) # - создали пустой список, после чего добавляли в него элементы в количестве 5 единиц



# Удаление последнего элемента списка.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]


# Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]


# Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]



# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])               # 1
# print(list_1[1])               # 2
# print(list_1[len(list_1)-1])   # 10
# print(list_1[-5])              # 6
# print(list_1[:])               # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])              # [1, 2]
# print(list_1[len(list_1)-2:])  # [9, 10]
# print(list_1[2:9])             # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])           # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6])             # [1, 7]



# Создание кортежа (неизменяемого списка)

# t = ()

# print(type(t))

# t = (1, )
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a,b,c = v

# print(a, b, c)


# t = [1, 2, 3, 5]


# for i in range(len(t)):
#     print(t[i])


# t[0] = 2

# print(t)



# Словари
# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])



# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = 'l←l'
# print(dictionary['left']) # l←l
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k, v) in directionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →




# Создание "множеств"

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue', 'gray}
# colors.remove('red')
# print(colors) # {'green', 'blue', 'gray}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue', 'gray}
# colors.clear() # { }
# print(colors) # set()



# Операции со множествами в Python

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                               # c = {1, 2, 3, 5, 8}
# u = a.union(b)                             # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)                      # i = {8, 2, 5}
# dl = a.difference(b)                       # dl = {1, 3}
# dr = b.difference(a)                       # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}



# Создание "замороженного" множества

a = {1, 8, 6}

b = frozenset(a)

print(b)










