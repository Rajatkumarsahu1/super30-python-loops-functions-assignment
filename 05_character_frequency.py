# Character Frequency Counter
text = input("Enter a string: ")

freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch, count in freq.items():
    print(f"'{ch}' occurs {count} time(s)")
