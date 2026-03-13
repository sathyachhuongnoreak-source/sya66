class BankAccount:
    def __init__(self, name, balance, secret):
        self.name = name
        self._balance = balance
        self._secret = secret

    def verify(self, secret):
        return self._secret == secret

    def withdraw(self, amount):
        if amount > self._balance:
            print("Balance is not enough")
            return
        self._balance -= amount
        print("Withdraw successfully!")
        print(f"Your remaining balance is {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print("Deposit Successfully!")
        print(f"Your remaining balance is {self._balance}")

    def check_balance(self):
        print(f"Hello {self.name}. Your remaining balance is {self._balance}")

    def transfer(self, receiver, amount):

        if amount > self._balance:
            print("You dont have enough balance to transfer") 
            return
        self.withdraw(amount)
        receiver.deposit(amount)

print("Transaction successfully.")


class SavingAccount(BankAccount):
    def calculate_interest(self):
        self._balance += 10
        print("Interest Received: 10$")
        print(f"Your remaining balance is {self._balance}")


class StudentAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 100:
            print("You can't withdraw more than 100$")
            return
        super().withdraw(amount)


class BusinessAccount(BankAccount):
    def take_loan(self, amount):
        print("You took loan successfully!")
        self._balance += amount
        print(f"Thank you! Your balance now is {self._balance}")


accounts = {}
current_user = None

while True:
    print('''
=== ATM System ===
Choose Menu
1. CREATE ACCOUNT
2. LOGIN
3. CHECK BALANCE
4. WITHDRAW
5. DEPOSIT
6. TRANSFER
7. LOGOUT
''')

    choice = input("Select Menu: ")

    if choice == "1":
        name = input("Input account name: ")
        if name in accounts:
            print("Account name already exists.")
            continue

        balance = float(input("Input initial balance: "))
        secret = input("Input your secret: ")

        acc = BankAccount(name, balance, secret)
        accounts[name] = acc

        print("Bank Account is created successfully!")

    elif choice == "2":
        name = input("Input account name: ")
        secret = input("Input secret PIN: ")

        if name in accounts and accounts[name].verify(secret):
            print("")
            print(f"Login success! Welcome {name}!")
            print("")
            current_user = accounts[name]
            continue

        print("Invalid account name or secret")

    elif choice == "3":
        if current_user is None:
            print("Please login first!!")
            continue
        current_user.check_balance()

    elif choice == "4":
        if current_user is None:
            print("Please login first")
            continue
        amount = float(input("Input amount: "))
        current_user.withdraw(amount)
    elif choice == "5":
        if current_user is None:
            print("Please login first")
            continue
        amount = float(input("Input amount to deposit: "))
        current_user.deposit(amount)
    elif choice =="6":
        if current_user is None:
            print("please login first")
            continue

        receiver_name = input("Input receiver:  ")
        if receiver_name not in accounts:
            print("Receiver doesn't exist")
            continue

        amount = float(input(f"input ammount to transfer to {receiver_name}:  "))
        current_user.transfer(accounts[receiver_name],amount)
    elif choice == "7":
        current_user = None
        print("logout success!!")
