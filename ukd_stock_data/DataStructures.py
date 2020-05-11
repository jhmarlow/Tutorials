# Python Object Oriented Programming
# 'Class' (Employee variables the same across all instances
# 'Instance' (emp_X) variables can be different


# -------Create class --------
class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# call 'self.raise_amount' means that you can change amount for each instance
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Create a class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# ------ Data input -----

emp_1 = Employee('Jacob', 'Marlow', 50000)
emp_2 = Employee('James', 'Barlow', 60000)

emp_str_1 = 'john-doe-70000'
emp_str_2 = 'steve-smith-50000'
emp_str_3 = 'jane-doe-60000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)

# ----- Call methods ---------------

# call data
print(emp_1.email)

# call method
print(emp_2.fullname())

# apply method
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# call all instance info
print(emp_1.__dict__)

# call all class info
print(Employee.__dict__)

# print raise amount (change instance)
emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)

# print raise amount (change in class method)
Employee.set_raise_amount(1.07)

print(Employee.raise_amount)
print(emp_1.raise_amount)

# Number of employees
print(Employee.num_of_employees)

# Static method
import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))