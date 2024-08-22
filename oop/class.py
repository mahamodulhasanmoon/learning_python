class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

import datetime

x = datetime.datetime.now()
print(x)

x = abs(-7.25)

print(x)


import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))