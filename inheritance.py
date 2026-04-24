"""class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    
    def display(self):
        print(self.name,self.roll)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept

    def display(self):
        print(f"Name:{self.name},Salary{self.salary},dept:{self.dept}")

c=Manager("Vishal",50000,"IT")


class Animal:
    def eat():
        print("Animal eats")

class dog(Animal):
    def bark():
        print("dog barks")
    
d=dog()
d.barks

class Animal:
    def sound(self):
        print("Animal sound")

class dog(Animal):
    def sound(self):
        print("Meow")

d=dog()
d.sound()
"""

"""class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    
    def show(self):
        print(f"Name:{self.name}\nRoll:{self.roll}")

d=Student("Vishal",101)
d.show()
"""
"""class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language
    def display(self):
        print(f"Name:{self.name}\nSalary:{self.salary}\nLanguage:{self.language}")

d=Developer("Vishal",50000,"Python")
d.display()

class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")

b = B()

class Person:
    def __init__(self,name):
        self.name=name
class Studen(Person):
    def __init__(self,name):
        super().__init__(name)
        print(self.name)

s=Studen("Vishal")
"""
