# Create a class with Managers (attrs: first, last, email, loc)
# Create an Employees subclass
# Create a method that will display Manager first, last, email, and location
# Create a method that will display Employees first, last, email, and location
# Set Manager pay
# Get Manager pay



# class Managers:
#     def __init__(self, first, last, email, location):
#         self.first = first
#         self.last = last
#         self.email = email
#         self.location = location


# class Employees(Managers):
#     def __init__(self, first, last, email, location, age):
#         super().__init__(first, last, email, location)
#         self.age = age


# manager1 = ("Oscar", "Caicedo", "oscarcaicedo@epsilon.com", "Chicago, IL")
# manager2 = ("Jose", "Armas", "JoseArmas@epsilon.com", "Chicago, IL")

# emp1 = ("Carlos", "Minero", "Cminero1@yahoo.com", 28)


# print(manager1)
# print(manager2)
# print(emp1)


# from abc import ABC, abstractmethod

# class Employee(ABC):
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'

#     @abstractmethod
#     def get_salary(self):
#         pass

# class FulltimeEmployee(Employee):
#     def __init__(self, first_name, last_name, salary): #Instance attributes from original and new ones.
#         super().__init__(first_name, last_name) # Instances attributes of the OG class
#         self.salary = salary
    
#     def get_salary(self):
#         return self.salary
    
# class HourlyEmployee(Employee):
#     def __init__(self, first_name, last_name, worked_hours, rate):
#         super().__init__(first_name, last_name)
#         self.worked_hours = worked_hours
#         self.rate = rate
    
#     def get_salary(self):
#         return self.worked_hours * self.rate

# class Payroll:
#     def __init__(self):
#         self.employee_list = []

#     def add(self, employee):
#         self.employee_list.append(employee)
    
#     def print(self):
#         for e in self.employee_list:
#             print(f"{e.full_name} \t ${e.get_salary()}")


# payroll = Payroll()

# payroll.add(FulltimeEmployee('John', 'Doe', 6000))
# payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
# payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
# payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
# payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

# payroll.print()
