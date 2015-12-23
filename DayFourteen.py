class Reindeer:
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest

    def distance(self, seconds):
        dist = 0
        while seconds > 0:
            if seconds < self.time:
                dist += self.speed * seconds
                return dist
            else:
                dist += self.speed * self.time
            seconds -= (self.time + self.rest)
        return dist

deer = []
with open("inputs/DayFourteenInput.txt") as file:
    for line in file:
        line = line.split(" ")
        name = line[0]
        speed = int(line[3])
        time = int(line[6])
        rest = int(line[-2])
        deer.append(Reindeer(name, speed, time, rest))

winner = ("", 0)
for reindeer in deer:
    dist = reindeer.distance(2503)
    if dist > winner[1]:
        winner = (reindeer.name, dist)

print(winner)
        
