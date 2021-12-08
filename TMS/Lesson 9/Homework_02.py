"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает
марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""
from Homework_01 import Car

if __name__ == "__main__":
    fast_car = Car("Mercedes", "E500", 2000, 0)
    while fast_car.speed < 100:
        fast_car.increase_speed()
    fast_car.current_speed()
