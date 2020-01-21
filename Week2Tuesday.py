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

# class Person:
#     def __init__(self, fname, lname, birthdate, adress, email):
#         self.fname = fname
#         self.lname = lname
#         self.birthdate = birthdate
#         self.adress = adress
#         self.email = email
#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year
#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1
#         return age
    

# sammy = Person("Sammy", "Kry", datetime.date(1998, 8,21), "123 Sesemy str.", "sammy@gmail.com")
# print(f"{sammy.fname} {sammy.lname}")

# age = sammy.age()
# print(age)

# Fucntion vs Class


# def greeting(name):
#     count = 0 
#     print(f"Hello {name}")
#     count += 1
# greeting("sammy")
# greeting("marin")
# greeting("sorina")

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.count = 0 
    
#     def greeting(self):
#         print(f"Hello {self.name}")
#         self.count += 1
#     def printCount(self):
#         print(self.count)

# alina = Person("Alina")

# alina.greeting()
# alina.greeting()
# alina.greeting()

# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         #self.other_person = other_person
#         print(f"Hello {other_person.name}, I am {self.name}")

# Sonny = Person("Sonny", "sonny@hotmail.com", "483-385-4948")
# Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# Sonny.greet(Jordan)
# Jordan.greet(Sonny)
# print(f"Hello Jordan, here is my info, {Sonny.name}, {Sonny.email}, {Sonny.phone}")
# print(f"Hello Sonny, here is my info, {Jordan.name}, {Jordan.email}, {Jordan.phone}")

# Inheritence
# Hello

class VString(str):
    def reverse(self, name):
        rstring = ' '
        for char in name:
            rstring = char + rstring
        return rstring

myString = VString("hello")
print(myString)

reversed_string = myString.reverse("Hello")
print(reversed_string)


