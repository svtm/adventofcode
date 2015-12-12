import hashlib


def dayFour(string, zeroes):
    zeroString = ""
    for i in range (0, zeroes):
        zeroString += "0"

    testString = string.encode('utf-8')
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    hashString = m.hexdigest()
    if hashString[0:zeroes] == zeroString:
        return string

    count = 0
    while True:
        testString = string + str(count)
        m = hashlib.md5()
        m.update(testString.encode('utf-8'))
        hashString = m.hexdigest()
        if hashString[0:zeroes] == zeroString:
            return testString, hashString, count
        count += 1
