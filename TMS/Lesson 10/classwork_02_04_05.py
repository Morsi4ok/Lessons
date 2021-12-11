"""
Ex.2
Переопределить магические методы сложения, вычитания, умножения на число.
"""
from __future__ import annotations
from classwork_01_03 import MyTime


class MyTimeMath(MyTime):
    def __add__(self, other: MyTimeMath) -> MyTimeMath:
        seconds = self.seconds + other.seconds
        minutes_offset = 0
        if seconds > 60:
            minutes_offset = seconds // 60
            seconds %= 60
        minutes = self.minutes + other.minutes + minutes_offset
        hour_offset = 0
        if minutes > 60:
            hour_offset = minutes // 60
            minutes %= 60
        hour = self.hours + other.hours + hour_offset
        return MyTimeMath(hour, minutes, seconds)

    def __sub__(self, other: MyTimeMath) -> MyTimeMath:
        seconds = self.seconds - other.seconds
        minutes_offset = 0
        if seconds < 0:
            minutes_offset = abs(seconds) // 60
            seconds = abs(seconds) % 60
        minutes = self.minutes - other.minutes - minutes_offset
        hour_offset = 0
        if minutes < 0:
            hour_offset = abs(minutes) // 60
            minutes = abs(minutes) % 60
        hour = self.hours - other.hours - hour_offset
        return MyTimeMath(hour, minutes, seconds)

    # Ex.4
    # Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.
    def __mul__(self, multiplier: int) -> MyTimeMath:
        seconds = self.seconds * multiplier
        minutes_offset = 0
        if seconds > 60:
            minutes_offset = seconds // 60
            seconds %= 60
        minutes = self.minutes * multiplier + minutes_offset
        hour_offset = 0
        if minutes > 60:
            hour_offset = minutes // 60
            minutes %= 60
        hour = self.hours * multiplier + hour_offset
        return MyTimeMath(hour, minutes, seconds)


if __name__ == "__main__":
    my_time_1 = MyTimeMath(2, 50, 40)
    my_time_2 = MyTimeMath(1, 32, 27)
    print(my_time_1 + my_time_2)
    print(my_time_1 - my_time_2)
    print(my_time_1 * 2)
    # Ex.5
    # Создать второй объект класса MyTime, найти разницу с первым, добавить к нему 7 часов и 45 минут,
    # вывести на печать результат.
    my_time_3 = my_time_1 - my_time_2 + MyTimeMath(7, 55, 0)
    print(my_time_3)
