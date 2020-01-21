### Homework for Week 2: Tuesday

# Sonny and Jordan

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        #print(self.friends)

    def greet(self, other_person):
        self.greeting_count += 1
        print(f"Hello {other_person.name}, I am {self.name}")
    
    def print_contact_info(self):
        print(f"{self.name}'s' email: {self.email}, {self.name}'s phone: {self.phone}")

    def add_friend(self,fname):
        self.friends.append(fname)
        #print(self.friends[0].phone)
    
    def num_friends(self):
        print(len(self.friends))



Sonny = Person("Sonny", "sonny@hotmail.com", "483-385-4948",)
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456",)
Sonny.greet(Jordan)
Sonny.add_friend(Jordan)
print(Sonny.greeting_count)

Sonny.num_friends()

#Sonny.friends.append(Jordan)

# print(Sonny.friends[0].phone)

#Sonny.greet(Jordan)
#Jordan.greet(Sonny)

# print(f"Hello Jordan, here is my info, {Sonny.name}, {Sonny.email}, {Sonny.phone}")
# print(f"Hello Sonny, here is my info, {Jordan.name}, {Jordan.email}, {Jordan.phone}")
#Sonny.print_contact_info()


### Make your own class

# Make yout own Class (Vehicle)

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print(f'Make > {self.make}, Model > {self.model}, and Year {self.year}.')

# car = Vehicle('Toyota', 'Camry', 2019)

# car.print_info()
