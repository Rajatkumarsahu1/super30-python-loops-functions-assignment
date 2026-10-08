# Sum and Average Without sum()
numbers = [10, 20, 30, 40, 50]

total = 0
count = 0
for num in numbers:
    total += num
    count += 1

average = total / count if count else 0
print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
