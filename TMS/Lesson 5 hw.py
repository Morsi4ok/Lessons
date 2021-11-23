# Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
# В результате ее работы на печать выводятся значения переданных переменных, но только если они не равны None.
# Получим, например, следующее сообщение: Переданы аргументы: var1 = 2, var3 = 10.
def three_args(**kwargs):
    a = []
    result = str()
    for key, value in kwargs.items():
        if value != None:
            a.append(f'{key} = {value}')
        result = ', '.join(a)
    return result


h = three_args(var1=2, var2='hello', var3=None)
print(f"Переданы аргументы: {h}")


