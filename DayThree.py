
def getKey(char, curr_x, curr_y):      
    if (char == '^'):
        curr_y += 1
    elif (char == 'v'):
        curr_y -= 1
    elif (char == '<'):
        curr_x -= 1
    elif (char == '>'):
        curr_x += 1

    return str(curr_x)+":"+str(curr_y), curr_x, curr_y

x = 0
y = 0
roboX = x
roboY = y

houses = dict({str(x)+":"+str(y): 2})
robo = False
with open("DayThreeInput.txt") as file:
    for line in file:
        for word in line:
            for ch in word:
                key = ""
                if (robo):
                    key, roboX, roboY = getKey(ch, roboX, roboY)
                else:
                    key, x, y = getKey(ch, x, y)

                if (key in houses):
                    houses[key] += 1
                else:
                    houses[key] = 1
                robo = not robo

houseCount = 0
for house in houses:
    houseCount += 1

print(houseCount)


