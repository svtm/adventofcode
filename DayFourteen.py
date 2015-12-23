class Reindeer:
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest
        self.currentRest = 0
        self.currentTime = time
        self.dist = 0
        self.points = 0

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

    def move_for_second(self):
        if self.currentTime > 0:
            self.dist += self.speed
            self.currentTime -= 1
            if self.currentTime == 0:
                self.currentRest = self.rest
        elif self.currentRest > 0:
            self.currentRest -= 1
            if self.currentRest == 0:
                self.currentTime = self.time
        return self.dist

    def give_point(self):
        self.points += 1

    def __str__(self):
        return self.name + ": " + str(self.points)
            
            

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

## part 2
totalDist = dict()
for i in range(2503):
    for reindeer in deer:
        totalDist[reindeer.name] = reindeer.move_for_second()
    lead = max(totalDist.values())
    for reindeer in deer:
        if reindeer.dist == lead:
            reindeer.give_point()

for reindeer in deer:
    print(reindeer)
    
        
