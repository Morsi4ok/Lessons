# Дан список my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], выведите все элементы, которые меньше 5.
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
end_list = []
for x in my_list:
    if x < 5 in my_list:
        end_list.append(x)
print(end_list)

# Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
# Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево
line = input()
line1 = line[::-1]
if line == line1:
    print("палиндром")
else:
    print("не палиндром")


# Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
# которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.

# xor_cipher
def main():
    code = "Hello, I'm from RB"
    key = "94klsdnlkm"
    a = shifr_code(code)
    b = shifr_key(key)
    first_part = xor_cipher(a, b)
    print(first_part)


def shifr_code(code):
    code = list(code)
    a = []
    z = 0
    while z < len(code):
        p = ord(code[z])  # ord преобразует символ в код
        a.append(p)
        z += 1
    return a


def shifr_key(key):
    key = list(key)
    b = []
    x = 0
    while x < len(key):
        p = ord(key[x])
        b.append(p)
        x += 1
    return b


def xor_cipher(a, b):
    c = []
    for i, u in zip(a, b):  # zip объединяет 2 списка вместе
        c.append(chr(i ^ u))  # chr преобразует код в символ
    return c


main()

# xor_uncipher аналогично шифровке, по типу обратного переноса
num1 = 'a'  # допустим строка
num2 = 'b'  # ключ
num3 = chr(ord(num1) ^ ord(num2))  # шифр через ^ между строкой и ключом
num4 = chr(ord(num3) ^ ord(num2))  # получение строки из num1


# Пока через "три версты писал первую половину" и думал как 2-ую сделать, наткнулся на простенькое решение этой задачи
# И уже из головы все идеи до этого испарились и лишь этот сидит
def xor_cipher(string, key):
    encrypt_string = ''
    for char in string:
        encrypt_string += chr(ord(char) ^ key)

    return encrypt_string
# для расшифровки будет аналогичная функция
# если ввести результат введённой функции,то расшифрует в исходную
# в целом немного подккоректировал именно для запуска
def main():
    string = "5a4asdf"
    key = "gasa4fasdf"
    d = xor_cipher(string, key)


def xor_cipher(string, key):
    encrypt_string = ''
    for s, k in zip(string, key):
        encrypt_string += chr(ord(s) ^ ord(k))

    return encrypt_string


main()
