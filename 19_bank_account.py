# Bank Account Mini Application
balance = 0.0
history = []


def deposit(amount):
    global balance
    if amount <= 0:
        print("Deposit must be positive.")
        return
    balance += amount
    history.append(f"Deposited ₹{amount:.2f}")
    print(f"Deposited ₹{amount:.2f}.")


def withdraw(amount):
    global balance
    if amount <= 0:
        print("Withdrawal must be positive.")
    elif amount > balance:
        print("Insufficient balance. Withdrawal denied.")
    else:
        balance -= amount
        history.append(f"Withdrew ₹{amount:.2f}")
        print(f"Withdrew ₹{amount:.2f}.")


def check_balance():
    print(f"Current balance: ₹{balance:.2f}")


def transaction_history():
    if not history:
        print("No transactions yet.")
        return
    for i, t in enumerate(history, 1):
        print(f"{i}. {t}")


while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice in ("1", "2"):
        try:
            amt = float(input("Enter amount: ₹"))
        except ValueError:
            print("Invalid amount.")
            continue
        deposit(amt) if choice == "1" else withdraw(amt)
    elif choice == "3":
        check_balance()
    elif choice == "4":
        transaction_history()
    elif choice == "5":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice.")
