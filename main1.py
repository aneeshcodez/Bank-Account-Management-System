
class BankAccount:
    total_no_accounts = 0

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        BankAccount.total_no_accounts += 1

    def display_account_details(self):
        print(
            f"Name: {self.name}\n"
            f"Account No: {self.account_no}\n"
            f"Balance: ₹{self.balance}"
        )

    def deposit_money(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"Balance: ₹{self.balance}")
            print("Money deposited successfully")
        else:
            print("Enter a valid amount to deposit")

    def withdraw_money(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("Enter a valid amount to withdraw")
            return False

        if self.balance < withdraw_amount:
            print("Insufficient balance")
            return False

        self.balance -= withdraw_amount
        print(f"Balance: {self.balance}")
        print("Withdrawal successful")
        return True

    def check_balance(self):
        print(f"CURRENT BALANCE: {self.balance}")

    def __str__(self):
        '''
        Method __str__ should always return string, not print.
        Else we will get "__str__ returned non-string (type NoneType) error" in python
        Because the str fucntion,although is mostly used to print values but actually
        is designed to return a string,not to print one. In your class str function
        is calling the print directly while it is returning nothing ,
        that explains your error output.
        '''
        return f"Name: {self.name}\n Account No: {self.account_no}\n Balance: {self.balance}"

# Creating Objs for Class
account_1 = BankAccount("Ram", 101, 50)
account_1.display_account_details()
account_1.deposit_money(100)
account_1.withdraw_money(140)
account_1.check_balance()

class SavingsAccount(BankAccount):
    min_balance_required = 50

    def __init__(self, name, account_no, balance):
        super().__init__(name, account_no, balance)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < self.min_balance_required:
            raise ValueError(
                f"Minimum balance of ₹{self.min_balance_required} is required"
            )
        self._balance = new_balance

    def withdraw_money(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("Enter a valid amount to withdraw")
            return False

        if self.balance - withdraw_amount < self.min_balance_required:
            print(
                f"Withdrawal rejected. You must maintain "
                f"a minimum balance of ₹{self.min_balance_required}"
            )
            return False

        return super().withdraw_money(withdraw_amount)

    def __str__(self):
        return super().__str__()

# Testing SavingsAccount
sa_account_1 = SavingsAccount("Ram", 1011, 100)

sa_account_1.display_account_details()

print("\nWithdrawing ₹20:")
sa_account_1.withdraw_money(20)

print("\nWithdrawing ₹60:")
sa_account_1.withdraw_money(60)

print("\nWithdrawing ₹50:")
sa_account_1.withdraw_money(50)

print("\nFinal balance:")
sa_account_1.check_balance()

print(f"\nTotal accounts created: {BankAccount.total_no_accounts}")

print(sa_account_1)
print(account_1)

'''
i need a setter (you actually came up with this ,very good !)

'''