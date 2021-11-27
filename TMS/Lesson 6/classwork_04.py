import random

"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту, в случае
положительного ответа  - вытягивать случайную карту. Игра заканчивается если игрок отказывается брать карту,
либо сумма его карт больше 21-го.
"""


def main():
    b = ''
    h = 0
    while b != 'no' and h <= 21:
        g = list1(library1)
        h += g
        b = input(f"u have now: {h}, more/no? ")
    if h > 21:
        print("u lose")
    else:
        print(f"u have {h}")

def list1(c):
    a = random.choice(c)
    if a == "J":
        g = 2
    elif a == "D":
        g = 3
    elif a == "K":
        g = 4
    elif a == "A":
        g = int(input("1 или 11? "))
    else:
        g = a
    return g


if __name__ == "__main__":
    library1 = (6, 7, 8, 9, 10, "J", "D", "K", "A")
    print(main())
