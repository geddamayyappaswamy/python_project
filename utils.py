import uuid

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0.0):
        account_id = str(uuid.uuid4())[:8]  # short unique ID
        self.accounts[account_id] = {
            "name": name,
            "balance": balance
        }
        print(f"Account created for {name}. ID: {account_id}, Balance: ₹{balance:.2f}")

    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            print("Account not found.")
            return
        self.accounts[account_id]["balance"] += amount
        print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.accounts[account_id]['balance']:.2f}")

    def withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            print("Account not found.")
            return
        if self.accounts[account_id]["balance"] < amount:
            print("Insufficient funds.")
            return
        self.accounts[account_id]["balance"] -= amount
        print(f"Withdrawn ₹{amount:.2f}. New balance: ₹{self.accounts[account_id]['balance']:.2f}")

    def show_balance(self, account_id):
        if account_id not in self.accounts:
            print("Account not found.")
            return
        acc = self.accounts[account_id]
        print(f"Account: {account_id} | Holder: {acc['name']} | Balance: ₹{acc['balance']:.2f}")
