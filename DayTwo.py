totalPaperArea = 0;
totalRibbonLength = 0;
with open("DayTwoInput.txt") as file:
    for line in file:
        dims = line.split('x')
        dims = [int(i) for i in dims]
        areas = [dims[0]*dims[1], dims[1]*dims[2], dims[0]*dims[2]]
        for side in areas:
            totalPaperArea += 2*side
        totalPaperArea += min(areas)
        dims.sort()
        totalRibbonLength += 2 * dims[0] + 2 * dims[1] + dims[0]*dims[1]*dims[2]

print(totalPaperArea)
print(totalRibbonLength)
        
