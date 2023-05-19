# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# a = sum_numbers(5, 'qwert')
# print(a)






# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q','e', 'l'))
# print(sum_str('q','e', 'l', 'r', 'f'))




# ИМПОРТИРОВАНИЕ ИЗ ДРУГОГО ФАЙЛА

# import modulL3
# print(modulL3.max1(5, 9))


# from modulL3 import max1
# print(max1(10, 9))



# ЧТОБЫ ИМПОРТИРОВАТЬ ВСЕ ФУНКЦИИ ИЗ ФАЙЛА - НУЖНО ПОСТАВИТЬ *

# from modulL3 import *
# print(max1(10, 9))




#ЧТОБЫ ПЕРЕИМЕНОВАТЬ НАЗВАНИЕ ИМПОРТИРОВАННОЙ ФУНКЦИИ ИЗ ФАЙЛА

# import modulL3 as m1

# print(m1.max1(10, 9))




# ЗАДАЧА ПО РЕКУРСИИ, пример: НЕОБХОДИМО ВЫВЕСТИ n-ПЕРВЫХ ЧЛЕНОВ ПОСЛЕДОВАТЕЛЬНОСТИ ФИБОНАЧЧИ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)





# ЗАДАЧА ПО СОРТИРОВКЕ, пример:
# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой должен отгадать.
# Перебор чисел из варитантов (больше 100? - нет, больше 75? - да, больше 87? - нет, больше 78? - нет, больше 77? - нет => ответ 76)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greather = [i for i in array[1:] if i > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greather)

# print(quick_sort([10, 5, 2]))    





def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list1)
print(list1)

    





