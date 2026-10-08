# Password Retry System
PASSWORD = "python@123"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    entered = input("Enter password: ")
    if entered == PASSWORD:
        print("Access Granted")
        break
    attempts += 1
    remaining = MAX_ATTEMPTS - attempts
    if remaining > 0:
        print(f"Incorrect password. {remaining} attempt(s) left.")
else:
    print("Account Locked")
