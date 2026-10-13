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
            # print("Withdrawn Successfully")
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
        if balance > SavingsAccount.min_balance_required:
            super().__init__(name, account_no, balance)
        else:
            raise ValueError("Balance cant be less than 50 rs.")

    #     self.name = name
    #     self.account_no = account_no
    #     self.sa_balance = sa_balance
    #
    #
    # @property
    # def balance(self):
    #     return self.sa_balance
    #
    # @balance.setter
    # def balance(self, new_balance):
    #     if new_balance >= SavingsAccount.min_balance_required:
    #         self.sa_balance = new_balance
    #     else:
    #         #print("Atleast 50 is required as the Minimum Balance")
    #         raise Exception("Atleast 50 is required as the Minimum Balance")

    # We are creating a withdrawal method for specifically saving's account
    def withdraw_money(self, withdraw_amount):

        balance_after_withdrawal = super().withdraw_money(withdraw_amount)
        balance_after_withdrawal = self.balance
        print(f"Balance amount after withdrawing : {balance_after_withdrawal} \nCurrent Withdrawal Successful")

sa_account_1 = SavingsAccount("Ram", 1011, 100)
sa_account_1.withdraw_money(60)

'''
1.over riding withdraw_money () method 
2. This method returns balance_after_withdrawal (This is from BankAccount class)
3. And this should be the Balance of Savings Account 
4. But Balance of Savings Accounts should not go below 50 Rs
5. So before we SET it, we have to validate the balance  
6. For Setting we need a Setter -> Go and read your notes

'''













