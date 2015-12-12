floor = 0;
position = 0;
with open("DayOneRoute.txt") as file:
        for word in file:
                for ch in word:
                    position += 1;
                    if (ch =='('):
                        floor += 1
                    
                    elif (ch == ')'):
                        floor -= 1

                    if (floor < 0):
                        print(position)
                        break
                        

print(floor)
