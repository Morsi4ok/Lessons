"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на экран
все его атрибуты.
"""


class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"run{self.name}")

    def bark(self):
        print(f"bark{self.name}")


if __name__ == "__main__":
    dog = Dog(100, 100, "Bob", 10)
    dog.jump()
    dog.run()
    dog.bark()
    print(dog.name)
    print(dog.height)
    print(dog.age)
    print(dog.weight)
