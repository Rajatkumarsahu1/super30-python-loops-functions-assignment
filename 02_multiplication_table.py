# Multiplication Table Generator
n = int(input("Enter a number: "))

print(f"\nTable of {n} (1 to 10):")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Modified: user supplies the ending range
end = int(input("\nEnter the ending range: "))
print(f"\nTable of {n} (1 to {end}):")
for i in range(1, end + 1):
    print(f"{n} x {i} = {n * i}")
