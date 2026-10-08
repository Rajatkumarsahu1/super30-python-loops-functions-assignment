# Reusable Number Analysis Function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def analyze_number(number):
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    parity = "Even" if number % 2 == 0 else "Odd"
    prime = "Prime" if is_prime(number) else "Not Prime"
    return sign, parity, prime


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    sign, parity, prime = analyze_number(num)
    print(f"{num} is {sign}, {parity}, and {prime}.")
