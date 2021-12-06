"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих
элементов этой последовательности равны друг другу и что это за элемент.
Т.е. если программе на вход подать последовательность [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5],
то на печать программа должна вывести числа 4 и 3, где 4 - повторяющийся элемент, 3 - количество повторений
"""

counter = 0
my_list = [3, 5, 4, 2, 4, 5, 5, 6, 3, 7, 7, 7, 7, 2, 8, 9, 5, 0]
digit = int()
most_repetitions = 0
most_rep_element = int()
for i in my_list:
    if i != 0:  # 0 не является натуральным, поэтому по условию стоит в конце для завершения цикла
        if i == digit:
            counter += 1
            if counter > most_repetitions and digit > most_rep_element:
                most_repetitions = counter
                most_rep_element = digit
        else:
            counter = 0
            digit = i
            counter += 1
    else:
        break
print(f'''Наибольшее количество повторений: {most_repetitions}
Повторяющийся элемент: {most_rep_element}''')
