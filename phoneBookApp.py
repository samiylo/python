import pickle

print(
    """
    Electronic Phone Book
    =====================
    Look up an entry: 1
    Set an entry: 2
    Delete an entry: 3
    List all entries: 4
    Quit: 5
    """)

contacts = {}

while True:
    userAction = int(input("What do you want to do (1-5)? "))

    if userAction != [1,2,3,4,5]:
        print("Please enter a number 1 - 5.")

    if userAction == 1:
        name = input("Who are you looking for? ")
        info = contacts.get(name)
        print(info)

    if userAction == 2:
        name = input("What is the name? ")
        number = input("What is the number? ")

        contacts[str(name)] = number
        print(contacts)

    if userAction == 3:
        name = input("Who would you like to delete? ")
        del contacts[name]
        print(f"{name} has neen deleted!")

    if userAction == 4:
        print(contacts)

    if userAction == 5:
        break