class BankAccount:

    bank_name = "First National Dojo"
    
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


checking = BankAccount(0.01, 100).deposit(100).deposit(150).deposit(275).withdraw(556).yield_interest().display_account_info()
savings = BankAccount(0.02, 500).deposit(223).deposit(556).withdraw(357).withdraw(45).withdraw(100).withdraw(9).yield_interest().display_account_info()





    # bank_name = "First National Dojo"
    # all_accounts = []
    # def __init__(self, int_rate, balance):
    #     pass
    #     self.int_rate = int_rate
    #     self.balance = balance
    #     BankAccount.all_accounts.append(self)

    # @classmethod
    # def change_bank_name(cls,name):
    #     cls.bank_name = name

    # @classmethod
    # def all_balances(cls):
    #     sum = 0

    #     for account in cls.all_accounts:
    #         sum += account.balance
    #     return sum

    # def withdraw(self, amount):

    #     if BankAccount.can_withdraw(self.balance,amount):
    #         self.balance -= amount
    #     else:
    #         print("Insufficient Funds")
    #     return self

    # @staticmethod
    # def can_withdraw(balance, amount):
    #     if (balance - amount) < 0:
    #         return False
    #     else:
    #         return True