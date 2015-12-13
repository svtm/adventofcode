from itertools import permutations

people = set()
values = {}
with open("inputs/DayThirteenInput.txt") as file:
    for line in file:
        line = line.rstrip("\n.").split(" ")
        if line[2] == "lose":
            val = -int(line[3])
        else:
            val = int(line[3])
        values[(line[0], line[-1])] = val
        people.add(line[0])
        people.add(line[-1])

res = {}
for perm in permutations(people):
    happiness = 0
    for pair in zip(perm, perm[1:]):
        happiness += values[pair]
    for pair in zip(perm[::-1], perm[-2::-1]):
        happiness += values[pair]

    happiness += values[(perm[0], perm[-1])]
    happiness += values[(perm[-1], perm[0])]

    res[perm] = happiness

print(max(res.values()))
