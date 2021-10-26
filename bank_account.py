class BankAccount:

    bank_name = "First National Dojo"
    balance = 0

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: ${self.balance})
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= int_rate
        return self




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