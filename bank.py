class BankAccount:
    def __init__(self,name,balance,secret):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    def check_balance(self):
        print("Checking balance!")

        secret = input("Input your password: ")

        if secret == self.__secret:
            print(f"Hello :{self.name}")
            print(f"Your Balance is: {self.__balance}")
        else:
            print("Sorry your password is incorrect")

    def withdraw(self):
        print("User is withdrawing")
        secret = input("Input ur password: ")
        print(f"ur balance is{self.balance}")

        if secret == self.__secret:
            amount = float(input("Input your amount"))
            remain = self.__balance - amount

            if remain < 0:
                print("Your balance is insufficient")
            else:
                self.balance = remain
                print("withdraw succsessfully...")
                print(f"Your reamining balance is: {self.__balance}")
        else:
                print("we dont know you.")

    def deposit(self):
        print("==Deposit ur money==")
        secret = input("Input ur password: ")

        if secret == self.__secret:
            amount = float(input("Input your amount here: "))
            self.__balance += amount
            print("Deposit successful!!")
            print(f"Your new balance is now: {self.__balance}")
        else:
            print("Your password is incorrect.")

class SavingAccount(BankAccount):
        def calculate_interest(self):
            print("Calculate interest")
            SavingAccount.__balance += 10
            print(f"Your balance is now: {self._BankAccount__balance}")

class StudentbankAccount(BankAccount):
     def withdraw(self): 
        print ("===Student is withdrawing===")
        secret = input("Input your password: ")
        
        if secret == self._BankAccount__secret:
            amount = float(input("Input your amount: "))

            if amount > 500:
                print("Student accoount can't withdraw more than 500$")
            else:
                remain = self._BankAccount__balance - amount

                if remain < 0:
                    print("Your balance is not enough to withdraw")
                else: 
                    self._BankAccount__balance = remain
                    print("Withdraw succesful...")
                    print(f"Your remaining balance is: {self._BankAccount__balance}")
        else: 
            print("We don't know you.")

# PremiumSaving inherit from SavingAccount
class PremiumSaving(SavingAccount):

    # override deposit method (2% bonus every deposit)
    def deposit(self):
        print("==== Premium Deposit ====")
        secret = input("Input your secret number: ")

        if secret == self._BankAccount__secret:
            amount = float(input("Input deposit amount: "))

            bonus = amount * 0.02   # 2% bonus
            total = amount + bonus

            self._BankAccount__balance += total

            print(f"You received 2% bonus: {bonus}$")
            print(f"Your new balance is: {self._BankAccount__balance}")
        else:
            print("Sorry we don't know you.")


# BusinessAccount inherit from BankAccount
class BusinessAccount(BankAccount):

    def take_loan(self):
        print("==== Business Loan ====")
        secret = input("Input your password number: ")

        if secret == self._BankAccount__secret:
            loan = float(input("Input loan amount: "))
            self._BankAccount__balance += loan
            print(f"Loan approved. Your new balance is: {self._BankAccount__balance}")
        else:
            print("Access denied.")
             

Sathya = BankAccount(name="Sathya", balance=500, secret="2244")


Sathya = StudentbankAccount(name="Sathya", balance=500, secret="2244")
Sathya.withdraw()
Sathya.deposit()

Sathya = BusinessAccount(name="Sathya", balance=500, secret="2244")
Sathya.take_loan()