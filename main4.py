# def f(x):
#     return x*x

# print(f(5))    ответ - 25





# def f(x):
#     return x*x

# print(type(f)) - запрос на тип функции - ответ: <class 'function'>





# def f(x):
#     return x*x

# a = f       - в переменную а вложили ссылку на функцию Ф
# print(f(5))




# def calk1(a, b):
#     return a+b

# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))

# math(calk2, 5, 45)





# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a,b: a + b

# math(calk1, 5, 45)







# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)






# Задача:
# 1. В списке хранятся числа. Нужно выбрать только четные числа
# и составить список пар (число; квадрат числа).

# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]



# Решение 1:
# data = [ 1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)


# Решение 2:
# def select(f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

# data = [ 1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)








# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)






# Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

# Решение

# Подсказка: имеется функция ".split(', ')", которая преобразует строку в список, указывается в ней разделитель.

# data = '15 156 96 3 5 8 52 5'
# print(data)
# data = data.split()
# print(data)


# data = '15 156 96 3 5 8 52 5'
# data = list(map(int, data.split()))
# print(data)








# функция "филтр"
# фильтруем значения, которые заканчиваются на 5
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)






# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close() # после запуска создался фаил "file.txt"


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n') # теперь в файле "file.txt" стерлись старые значения, записались текущие в 2 строки, т.к. поставили разделители

# print(56)




path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close() # выводит данные из файла "file.txt" в консоль