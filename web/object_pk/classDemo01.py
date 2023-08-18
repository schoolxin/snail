# -*- coding:utf-8 -*-
# @FileName  :classDemo01.py
# @Time      :2023/6/29 19:08
# @Author    :dzz
# @Function  :


class Animal:
    def __init__(self):
        pass
    def say(self):
        print("动物叫")

class Sheep(Animal):
    def say(self):
        print("羊在咩咩叫")

class Dog(Animal):
    def say(self):
        print("狗在汪汪叫")

class Cat(Animal):
    def say(self):
        print("猫在叫")

class NoAnimal():
    def say(self):
        print("NO猫在叫")

def animal_say(ani):
    ani.say()


if __name__ == "__main__":
    dog = Dog()
    an = Animal()
    an1 = NoAnimal()
    animal_say(an1)
    cat = Cat()
    animal_say(cat)
    print(isinstance(dog,Animal))
    print(isinstance(an,Dog))
