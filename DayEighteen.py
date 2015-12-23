width = 6
height = 6
lights = list()

with open("test.txt") as file:
    for line in file:
        row = list()
        for ch in line.strip():
            row.append(ch == "#")
        lights.append(row)


def activeNeighbors(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0):
                nX = x + i
                nY = y + j
                if nX >= 0 and nY >= 0 and nX < width and nY < height and lights[nX][nY]:
                    count += 1
    return count
print(activeNeighbors(2, 3))

for steps in range(4):
    for row in lights:
        print(row)
    print()
    toggle = list()
    for x in range(width):
        for y in range(height):
            activeCount = activeNeighbors(x, y)
            if activeCount == 3 and not lights[x][y]:
                toggle.append((x, y))
            elif lights[x][y] and (activeCount > 2 or activeCount < 3):
                toggle.append((x, y))
    for spot in toggle:
        lights[spot[0]][spot[1]] = not lights[spot[0]][spot[1]]


activeLights = 0
for x in range(width):
    for y in range(height):
        if lights[x][y]:
            activeLights += 1
print(activeLights)
