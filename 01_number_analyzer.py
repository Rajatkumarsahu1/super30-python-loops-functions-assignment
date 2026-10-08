# Number Analyzer using for loop
n = int(input("Enter N: "))
even_count = odd_count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "is Even")
        even_count += 1
    else:
        print(i, "is Odd")
        odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
