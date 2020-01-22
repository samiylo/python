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
            print(f"{account.fname}, {account.lname}, {account.atype}, {account.status}")


def main():
    wellsfargo = Bank("Wells Fargo", "123 seesemy")
    action = 1

    while action != 6:
        print("1: Create account.")
        print("6: Exit application")

        action = int(input("Welcome! What would you like to do today? "))

        if (action == 1):
            fname = input("What is the first nane? ")
            mname = input("What is the middle name? ")
            lname = input("What is the last name? ")
            atype = input("What type of account woudld you like to open? Checking or Savings? ")
            deposit = int(input("How much would you like to deposit? "))

            wellsfargo.new_account(fname, mname, lanme, atype, deposit, "Open")
        elif (action == 6):
            break




