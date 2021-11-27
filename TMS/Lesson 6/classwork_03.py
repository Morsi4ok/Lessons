import random

"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт, где на первом месте 
номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""


def list1(c):
    a = random.choice(c)
    return a


def list2(h):
    b = random.choice(h)
    return b


if __name__ == "__main__":
    library1 = (6, 7, 8, 9, 10, "J", "D", "K", "A")
    library2 = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    print(list1(library1), list2(library2))
