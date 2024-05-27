# Напишите функцию flatten_and_sort, которая принимает двумерый массив (список списков) array,
# и возвращает "плоский" список со всеми числами в порядке возрастания result_list
# Например (Ввод --> Вывод) :
#
# [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]] -->  [1, 2, 3, 4, 5, 6, 7, 8, 9]


def flatten_and_sort(array):
    result_list = []
    while array > []:
        result_list = result_list + array[0]
        del array[0]
    result_list = sorted(result_list)
    return result_list

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]],
    [[], []],
    [[], [1]],
    [[1, 3, 5], [100], [2, 4, 6]]
]

test_data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9], [], [1], [1, 2, 3, 4, 5, 6, 100]
]


for i, d in enumerate(data):
    assert flatten_and_sort(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
print('\n            Задание 2')
s = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [1], [1, 2, 3, 4, 5, 6, 100]]
result_list = []
while s > []:
    result_list = result_list + s[0]
    del s[0]
result_list = sorted(result_list)
print(result_list)
