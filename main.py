class BankAccount:
    total_no_accounts = 0

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        BankAccount.total_no_accounts += 1

    def display_account_details(self):
        print(f'Name: {self.name}\n Account No : {self.account_no}\n Balance: {self.balance}')

    def deposit_money(self, deposit_amount):
        if (deposit_amount > 0):
            self.balance = self.balance + deposit_amount
            print(f'Balance : {self.balance}')
            print("Money Deposited Successfully")
        else:
            print("Enter a valid Amount to Deposit")

    def withdraw_money(self, withdraw_amount):
        if (withdraw_amount > 0 and self.balance >= withdraw_amount):
            self.balance = self.balance - withdraw_amount
            return self.balance
            print("Withdrawn Successfully")
        else:
            print("Enter a valid Amount to Withdraw")

    def check_balance(self):
        print(f'CURRENT BALANCE : {self.balance}')


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
        return self.balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= SavingsAccount.min_balance_required:
            self.balance = new_balance
        else:
            raise Exception("Atleast 50 is required as the Minimum Balance")

    # We are creating a withdrawal method for specifically saving's account
    def withdraw_money(self, withdraw_amount):

        balance_after_withdrawal = super().withdraw_money(self, withdraw_amount)

sa_account_1 = SavingsAccount("Ram", 1011, 100)














