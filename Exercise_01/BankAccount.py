class Account: 
    def __init__(self, Name, Balance):
        self.Name = Name
        self.Balance = Balance

    def BankAcc(account_name, starting_balance):
        Name = account_name
        Balance = starting_balance

    def Deposit(self,amount):
       self.Balance += amount

    def Withdraw(self,amount):
        self.Balance -= amount

    def get_balance(self):
        return self.Name + " has a balance of $" + str(self.Balance)