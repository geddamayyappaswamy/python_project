import python_project.utils
def main():
    print("=== Simple Banking System ===")
    bank = BankingSystem()

    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Balance")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter account holder name: ")
            bank.create_account(name)
        elif choice == "2":
            acc = input("Enter account ID: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc, amount)
        elif choice == "3":
            acc = input("Enter account ID: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc, amount)
        elif choice == "4":
            acc = input("Enter account ID: ")
            bank.show_balance(acc)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
