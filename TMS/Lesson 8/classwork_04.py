"""
Оформить предыдущую задачу в виде программы, вынести функцию в отдельный файл, добавить комментарии с описанием.
"""
from func import prime_numbers
# выводит в порядке возрастания все простые числа,
# расположенные между n и m (включая сами числа n и m), а также количество x этих чисел.

if __name__ == "__main__":
    n = int(input("Enter N:"))
    m = int(input("Enter M:"))

    result = prime_numbers(n, m)
    print(result, len(result))
