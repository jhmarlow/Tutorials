# url: https://www.tutorialspoint.com/python/python_classes_objects.htm

# class basics
class Employee:
    'common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total employee count %d") % Employee.empCount

    def displayEmployee(self):
        print("Name :", self.name, ", Salary : ", self.salary)

emp1 = Employee("zara", "2000")
emp2 = Employee("manni", "5000")
emp1.age = 7

emp1.displayEmployee()
print("Total Employee %d" % Employee.empCount)

# inheriting attributes
class Parent:
    'parent class'
    parentAttr = 100
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)

class Child(Parent):
    'child class'
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")

c = Child() # instanciate child
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

Child.__doc__

issubclass(Child, Parent)
isinstance(c, Child)

# overiding methods
class Par:
    def myMethod(self):
        print("Calling parent method")

class Chi(Par):
    def myMethod(self):
        print("Calling child method")

p = Par()
p.myMethod()

c = Chi()
c.myMethod()

# overloading 
class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def __str__(self):
        return("Vector (%d, %d)" %(self.a, self.b))

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(1,5)
v2 = Vector(-1, 2)
print(v1+v2)

# data hiding
class JustCounter:
    secretCount = 0

    def count(self):
        self.secretCount += 1
        print(self.secretCount)

counter = JustCounter()
counter.count()
counter.count()
# cant see as secret 
# print(counter.__secretCount)

