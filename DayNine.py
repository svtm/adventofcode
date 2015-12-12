from queue import *
from itertools import *

towns = set()
edges = dict()

def distance(origin, destination):
    key = origin + "-" + destination;
    if (key in edges.keys()):
        return edges[key]
    else:
        return -1



with open("DayNineInput.txt") as file:
    for line in file:
        cities, dist = line.split(" = ")
        origin, destination = cities.split(" to ")

        towns.add(origin)
        towns.add(destination)

        edges[origin+"-"+destination] = int(dist)
        edges[destination+"-"+origin] = int(dist)


routes = permutations(towns, len(towns))
bestpath = 999999
worstpath = 0

for route in routes:
    pathFailed = False
    path = 0
    pathString ="\n"
    for i in range(0, len(route)-1):
        dist = distance(route[i], route[i+1])
        pathString += route[i]+"-"
        if (dist < 0):
            print(pathString+"!-"+route[i+1])
            pathFailed = True
            break
        path += dist
    if (not pathFailed):
        if (path < bestpath):
            bestpath = path
        if (path > worstpath):
            worstpath = path

print(str(bestpath) + ", " + str(worstpath))



