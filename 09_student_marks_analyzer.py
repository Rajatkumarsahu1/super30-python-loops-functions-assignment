# Student Marks Analyzer
marks = [78, 45, 32, 90, 67, 39, 55, 88]
PASS_MARK = 40

highest = lowest = marks[0]
total = 0
passed = failed = 0

for m in marks:
    total += m
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    if m >= PASS_MARK:
        passed += 1
    else:
        failed += 1

print("Marks:", marks)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", round(total / len(marks), 2))
print("Passed:", passed)
print("Failed:", failed)
