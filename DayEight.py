## not finished

def code_and_string_len(line):
    code = 0
    for ch in line:
        code += 1
    print(line)
    line = line.replace('\"', '')
    print(line)
    return code, len(line)

stringLen = 0
codeLen = 0
with open("inputs/DayEightInput.txt") as file:
    for line in file:
        print(line)
        for ch in line:
            codeLen += 1
        line = line.replace('\"', '')
        stringLen += len(line)

print("Codelength - stringlength = " + str(codeLen - stringLen))
