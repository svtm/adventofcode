width = 1000
height = 1000

#lights = [[False]*width for i in range(height)]
lights = [[0]*width for i in range(height)]

def toggle(fromX, fromY, toX, toY):
    for i in range(fromX, toX+1):
        for j in range(fromY, toY+1):
           # lights[i][j] = not lights[i][j]
           lights[i][j] += 2

def setLights(fromX, fromY, toX, toY, state):
    for i in range(fromX, toX+1):
        for j in range(fromY, toY+1):
#            lights[i][j] = state
            if not state and lights[i][j] > 0:
                lights[i][j] -= 1
            elif state:
                lights[i][j] += 1
            
def printLights():
    for i in range(0, width):
        for j in range(0, height):
            print(lights[i][j], end="\t")
        print()

def countLights():
    count = 0
    for i in range(0, width):
        for j in range(0, height):
            count += lights[i][j]
    return count

def readStrings():
    with open("DaySixInput.txt") as file:
        for line in file:
            instr = line.split(" ")
            if (instr[0] == "toggle"):
                fromCoords = instr[1].split(",")
                toCoords = instr[3].split(",")
                toggle(int(fromCoords[0]), int(fromCoords[1]), int(toCoords[0]), int(toCoords[1]))
            else:
                state = True if (instr[1] == "on") else False
                fromCoords = instr[2].split(",")
                toCoords = instr[4].split(",")
                setLights(int(fromCoords[0]), int(fromCoords[1]), int(toCoords[0]), int(toCoords[1]), state)
    print(countLights())  
