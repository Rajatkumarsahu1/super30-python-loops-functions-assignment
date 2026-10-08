# ATM Withdrawal Simulator using while
balance = 10000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Current balance: ₹{balance}")
    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: ₹"))
            if amount > 0:
                balance += amount
                print(f"Deposited ₹{amount}. New balance: ₹{balance}")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid amount.")
    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                print("Amount must be positive.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Withdrew ₹{amount}. New balance: ₹{balance}")
        except ValueError:
            print("Invalid amount.")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
