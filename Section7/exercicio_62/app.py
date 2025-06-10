class Bank_account:
    def __init__ (self, client_name, balance):
        self.client_name = client_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}."
        else:
            return "Invalid amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid amount. Please enter a positive number."

    def transfer(self, amount, destination_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            destination_account.balance += amount
            return f"Transferred {amount} to {destination_account.client_name}. New balance: {self.balance}."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid amount. Please enter a positive number."

client_1 = Bank_account("Alice", 1000)
print(client_1.deposit(200))
print(client_1.balance)
print(client_1.withdraw(1500))