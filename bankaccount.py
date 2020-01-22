class AccountHolder:
    def __init__(self, fname, mname, lname, atype, balance, status):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.atype = atype
        self.balance = balance
        self.status = status
    

class Bank:
    def __init__(self, name, adress):
        self.accounts = []
        self.name = name
        self.adress = adress

    def new_account(self, fname, mname, lname, atype, balance, status):
        if balance >= 100:
            temp  = AccountHolder(fname, mname, lname, atype, balance, status)
            self.accounts.append(temp)
            return print(f"A {atype} account successfully created for {fname} {lname} with a balance of {balance}")
        else:
            return print(f"Insufficiant funds to create account. Please deposit a minimum of 100$.")#return of insufficiant deposit ammount
    def show_members(self):
        for account in self.accounts:
            print(f"{account.fname}, {account.lname}, {account.atype}, {account.balance}")
    
    def transfer_money(self, your_name, recipient, ammount):
        for accounts in self.accounts:
            if accounts.fname == your_name:
                accounts.balance -= ammount
                print(f"{ammount} has been withdrawn from {your_name}'s account")

        for accounts in self.accounts:
            if accounts.fname == recipient:
                accounts.balance += ammount
                print(f"{ammount} has been added to {recipient}'s account.")
    
    def withdraw (self, your_name, ammount):
        for accounts in self.accounts:
            balance = accounts.balance
            if accounts.fname == your_name:
                accounts.balance -= ammount
                print(f"{ammount} has been withdrawn from {your_name}'s account")
                print(f"{balance} is the new ballance in {your_name}'s account.")
            else:
                return print("This is not a valid account name.")



        
            


def main():
    wellsfargo = Bank("Wells Fargo", "123 seesemy")
    action = 1

    while action != 6:
        print("1: Create account.")
        print("2: Print all accounts.")
        print("3: Transfer money.")
        print("4: Withdraw money.")
        print("6: Exit application")

        action = int(input("Welcome! What would you like to do today? "))

        if (action == 1):
            fname = input("What is the first name? ")
            mname = input("What is the middle name? ")
            lname = input("What is the last name? ")
            atype = input("What type of account woudld you like to open? Checking or Savings? ")
            deposit = int(input("How much would you like to deposit? "))

            response = wellsfargo.new_account(fname, mname, lname, atype, deposit, "Open")
            print(response)
        elif (action == 2):
            wellsfargo.show_members()
        
        elif (action == 3):
            your_name = input("What is your first name?" )
            recipient = input("What is the recipients first name?" )
            ammount = int(input("What ammount would you like to transfer? "))
            wellsfargo.transfer_money(your_name, recipient, ammount)

        elif (action == 4):
            your_name = input("What is your name? ")
            ammount = int(input("What ammount would you like to withdraw? "))
            wellsfargo.withdraw(your_name, ammount)
            

        else: 
            break

main()


