class Factory:
    a=12
    def hello():
        print("hello")
print("hola")
obj1=Factory()
print(obj1.a)
Factory.hello()
class Animal:
    a=12
    def show():
        print("hola")
class Person(Animal):
    pass
print(Person.a)
class Animal:
    def __init__(self,name):
        self.name=name
        def show(self):
            print(f"your name is {self.name}")
class Person(Animal):
    def hello(self):
        print("your name is {self.name}")
        pass
obj1=Person("akarsh")
obj1.hello()

