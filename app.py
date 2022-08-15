# Create a class with Managers (attrs: first, last, email, loc)
# Create an Employees subclass
# Create a method that will display Manager first, last, email, and location
# Create a method that will display Employees first, last, email, and location
# Set Manager pay
# Get Manager pay



class Managers:
    def __init__(self, first, last, email, location):
        self.first = first
        self.last = last
        self.email = email
        self.location = location


class Employees(Managers):
    def __init__(self, first, last, email, location, age):
        super().__init__(first, last, email, location)
        self.age = age


manager1 = ("Oscar", "Caicedo", "oscarcaicedo@epsilon.com", "Chicago, IL")
manager2 = ("Jose", "Armas", "JoseArmas@epsilon.com", "Chicago, IL")

emp1 = ("Carlos", "Minero", "Cminero1@yahoo.com", 28)


print(manager1)
print(manager2)
print(emp1)
