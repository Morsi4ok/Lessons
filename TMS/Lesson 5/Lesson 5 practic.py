# Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
# Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.


def names(name):
    result_of_name = f"Hello, {name}"
    return result_of_name


my_list = ["Victor", "Anton", "Pavel", "Nikita", "Alexandr"]
for name in my_list:
    result = names(name)
    print(result)


# Создать функцию, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них.

def numbers(*args):
    a = 0
    for n in args:
        a += n
    b = max(args)
    print(a)
    print(b)


numbers(1, 2, 3, 6, 54, 62, 34, 5, 62, 3)

# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент func_type.
# В зависимости от func_type вернуть минимальное либо максимальное значение. Написать программу в виде трех функций.
def function(*args, **kwargs):
    for key, value in kwargs.items():
        if value == "max":
            print(max(args))
        elif value == "min":
            print(min(args))
        else:
            print("Вы ввели не min и не max")


a = function(1, 2, 3, 4, 5, 6, func_type=input("min or max?"))

# Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона,
# к которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".

def month_to_season(month):
    season_numbers = {(12, 1, 2): 'Зима', (3, 4, 5): 'Весна', (6, 7, 8): 'Лето', (9, 10, 11): 'Осень'}
    season = 0
    for key, value in season_numbers.items():
        if month in key:
            season = value
            break
    return season


month = int(input("Введите номер месяца: "))
print(month_to_season(month))
