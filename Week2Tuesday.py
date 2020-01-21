# Object Oriented Programming

# Terminology

# class Student:
#     properties(attributes):


# Inheritence - allows to inharet  functionallity and certain attributes
# from parent class.

# Object(parent)


# Onject(child)

# class Student:
#     def __init__(self, name, lname): #  A constructor will be called every time the Object is called.
#         self.name = name #       This will thell the func. that name is "Samiylo"
#         self.lname = lname
#     def greet(self):
#         print(f"Good Morning!")

# sammy = Student("Samiylo", "Kryshu")
# marin = Student("Marin", "Kryshu")

# print(sammy.name)
# shawnObject = Student()


#print(sammyObject.greet) # The period is called "Dot Opperator"



# class Greeting:
#     def say_hello(self):
#         print("Hello")

# Create a new Object for the greeting class
#newGreetingObj = Greeting()
#newGreetingObj.say_hello()   # This will refference to the class Greeting and call the method.

# Working with Constructors

# class Teacher:
#     def __init__(self):
#         print("constructor called")

# More Practice

# class Animal:
#     def __init__ (self, name):
#         self.name = name
# dog = Animal("dog")
#print(dog.name)

# Next Exercise

import datetime

class Person:
    def __init__(self, fname, lname, birthdate, adress, email):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.adress = adress
        self.email = email
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    

sammy = Person("Sammy", "Kry", datetime.date(1998, 8,21), "123 Sesemy str.", "sammy@gmail.com")
print(f"{sammy.fname} {sammy.lname}")

age = sammy.age()
print(age)

