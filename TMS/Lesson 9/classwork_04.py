"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать Dog и Cat от класса Animal и
Удалить в дочерних классах те методы, которые имеются у родительского класса. Создать объект каждого класса и
вызвать все его методы.
"""


class Animal:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f'jump {self.name}')

    def run(self):
        print(f'run {self.name}')

    def change_name(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def bark(self):
        print(f'bark {self.name}')


class Cat(Animal):
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def meow(self):
        print(f'meow {self.name}')


if __name__ == '__main__':
    dog = Dog(100, 100, "Bob", 10)
    dog.jump()
    dog.run()
    dog.bark()
    dog.change_name("Sam")
    print(dog.name)
    print(dog.height)
    print(dog.age)
    print(dog.weight)

    cat = Cat(50, 70, "Sofi", 20)
    cat.jump()
    cat.run()
    cat.meow()
    cat.change_name("Mary")
    print(cat.name)
    print(cat.height)
    print(cat.age)
    print(cat.weight)
