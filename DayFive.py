naughty = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]
def checkNice(string):
    for badstring in naughty:
        if string.find(badstring) != -1:
            return False
    vowelCount = 0
    doubleLetter = False
    prevChar = ""
    for ch in string:
        if ch in vowels:
            vowelCount += 1
        if ch == prevChar:
            doubleLetter = True
        prevChar = ch

    return (doubleLetter and (vowelCount >= 3))

def checkNice2(string):
    pair = False
    sandwich = False
    for i in range(0, len(string)-2):
        if (not pair and (string.find(string[i:i+2], i+2) != -1)):
            pair = True
        if string[i+2] == string[i]:
            sandwich = True
        if (sandwich and pair):
            return True
    return False

def checkStrings():
    nice1Count = 0
    nice2Count = 0
    with open("inputs/DayFiveInput.txt") as file:
        for line in file:
            if checkNice(line):
                nice1Count += 1
            if checkNice2(line):
                nice2Count += 1
    return nice1Count, nice2Count
