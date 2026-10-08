# Shopping Cart using Functions
cart = {}  # item name -> {"price": float, "qty": int}


def add_item():
    name = input("Item name: ").strip().lower()
    try:
        price = float(input("Price: ₹"))
        qty = int(input("Quantity: "))
    except ValueError:
        print("Invalid price or quantity.")
        return
    if price <= 0 or qty <= 0:
        print("Price and quantity must be positive.")
        return
    if name in cart:
        cart[name]["qty"] += qty
        cart[name]["price"] = price
    else:
        cart[name] = {"price": price, "qty": qty}
    print(f"Added {qty} x {name}.")


def remove_item():
    name = input("Item to remove: ").strip().lower()
    if name in cart:
        del cart[name]
        print(f"Removed {name}.")
    else:
        print("Item not found in cart.")


def calculate_total():
    total = 0
    for item in cart.values():
        total += item["price"] * item["qty"]
    return total


def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print(f"\n{'Item':<15}{'Price':>10}{'Qty':>6}{'Subtotal':>12}")
    for name, d in cart.items():
        print(f"{name:<15}{d['price']:>10.2f}{d['qty']:>6}{d['price'] * d['qty']:>12.2f}")
    print(f"Total: ₹{calculate_total():.2f}")


def checkout():
    if not cart:
        print("Cart is empty. Nothing to checkout.")
        return False
    view_cart()
    print("Thank you for shopping! Checkout complete.")
    cart.clear()
    return True


while True:
    print("\n--- SHOPPING CART ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        if checkout():
            break
    elif choice == "5":
        print("Exiting without checkout.")
        break
    else:
        print("Invalid choice.")
