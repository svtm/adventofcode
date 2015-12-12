##number = str(1)
##
##for i in range(0, 10):
##    print(number)
##    j = 0
##    nextNumber = ""
##    while j < len(number):
##        char = number[j]
##        count = 1
##        k = j+1
##        while (k < len(number) and number[k] == char):
##            count += 1
##            k += 1
##        nextNumber += str(count)+char
##        j = k
##    number = nextNumber 

def lookandsay(number):
    result = ""

    repeat = number[0]
    number = number[1:]+" "
    count = 1

    for nextnum in number:
        if nextnum != repeat:
            result += str(count)+repeat
            count = 1
            repeat = nextnum
        else:
            count += 1
    return result

number = str(1113222113)
for i in range(0, 50):
    number = lookandsay(number)
print(len(number))
