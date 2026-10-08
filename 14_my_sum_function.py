# Create Your Own sum() Function
def my_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("my_sum:", my_sum(data))
    print("Empty list:", my_sum([10,20,30,40,50]))
