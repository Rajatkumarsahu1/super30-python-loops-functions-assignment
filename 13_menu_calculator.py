# Menu-Driven Calculator
while True:
    print("\n--- CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "6":
        print("Goodbye!")
        break
    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number.")
        continue

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", a / b)
    elif choice == "5":
        if b == 0:
            print("Error: Modulus by zero is not allowed.")
        else:
            print("Result:", a % b)
