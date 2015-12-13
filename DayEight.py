import re

count = 0
encoded = 0
with open("inputs/DayEightInput.txt") as file:
    data = file.read()
    for line in data.splitlines():
        count += len(eval(line))
        encoded += len(re.escape(line)) + 2 # + 2 for quotation marks
    char = len(data.replace("\n", ""))
print("Part 1: " + str(char-count))
print("Part 2: " + str(encoded-char))
