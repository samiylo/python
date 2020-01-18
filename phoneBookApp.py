import pickle
import os.path
import time

if os.path.isfile('contacts.pickle'):
    with open('contacts.pickle', 'rb') as fh:
        contacts = pickle.load(fh)

else:
    contacts = {}


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


while True:
    userAction = int(input(print(
    """
    Electronic Phone Book
    =====================
    Look up an entry: 1
    Set an entry: 2
    Delete an entry: 3
    List all entries: 4
    Quit: 5
    What do you want to do (1-5)? 
    """)))
    

    # if userAction != [1,2,3,4,5]:
    #     print("Please enter a number 1 - 5.")

    if userAction == 1:
        name = input("Who are you looking for? ")
        info = contacts.get(name)
        print(f'Name: {name}\nPhone Number: {info}.')

    elif userAction == 2:
        name = input("What is the name? ")
        number = input("What is the phone number? ")

        contacts[name] = number
        print(contacts)

    elif userAction == 3:
        name = input("Who would you like to delete? ")
        del contacts[name]
        print(f"{name} has been deleted!")

    elif userAction == 4:
        print(contacts)

    elif userAction == 5:
        with open('contacts.pickle', 'wb') as fh:
            pickle.dump(contacts, fh)
        time.sleep(.1)
        print("-")
        time.sleep(.1)
        print("--")
        time.sleep(.1)
        print("---")
        time.sleep(.1)
        print("----")
        time.sleep(.1)
        print("-----")
        time.sleep(.1)
        print("File saved. Bye!")
        break
    
    else:
        print("Please use input 1 - 5. ")