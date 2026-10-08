# Find Maximum and Minimum Without max() / min()
numbers = [45, 12, 89, 3, 67, 24]

largest = smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
