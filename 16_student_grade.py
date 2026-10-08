# Student Grade Function
# Grading rules: A >= 90, B >= 75, C >= 60, D >= 40, else Fail
# A student also fails if any subject is below 40.
def calculate_grade(marks):
    if len(marks) != 5:
        raise ValueError("Exactly 5 subject marks are required.")
    for m in marks:
        if m < 0 or m > 100:
            raise ValueError(f"Invalid marks: {m}. Marks must be between 0 and 100.")

    total = 0
    for m in marks:
        total += m
    percentage = total / len(marks)

    if min(marks) < 40:
        grade = "Fail"
    elif percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"
    return total, percentage, grade


if __name__ == "__main__":
    marks = []
    for i in range(1, 6):
        while True:
            try:
                m = float(input(f"Enter marks for subject {i}: "))
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total, percentage, grade = calculate_grade(marks)
    print(f"Total: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
