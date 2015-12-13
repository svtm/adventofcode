
inputs = dict()

with open("inputs/DaySevenInput.txt") as file:
    for line in file:
        line = line.strip().split(" -> ")
        inputs[line[-1]] = line[0].split(" ")

def evalWire(wire):
    if wire.isdigit():
        return int(wire)

    expression = inputs[wire]
    if type(expression) == int:
        return expression

    if "AND" in expression:
        x = expression[0]
        y = expression[2]
        val = evalWire(x) & evalWire(y)
        inputs[wire] = val
        return val
    elif "OR" in expression:
        x = expression[0]
        y = expression[2]
        val = evalWire(x) | evalWire(y)
        inputs[wire] = val
        return val
    elif "NOT" in expression:
        x = expression[1]
        val = ~evalWire(x)
        inputs[wire] = val
        return val
    elif "LSHIFT" in expression:
        x = expression[0]
        y = expression[2]
        val = evalWire(x) << evalWire(y)
        inputs[wire] = val
        return val
    elif "RSHIFT" in expression:
        x = expression[0]
        y = expression[2]
        val = evalWire(x) >> evalWire(y)
        inputs[wire] = val
        return val
    else:
        if expression[0].isdigit():
            return int(expression[0])
        else:
            return evalWire(expression[0])

aValue = evalWire('a')
print(aValue)

## part 2:

## resetting wires:
with open("inputs/DaySevenInput.txt") as file:
    for line in file:
        line = line.strip().split(" -> ")
        inputs[line[-1]] = line[0].split(" ")

## putting value of a in b and reevaluating a
inputs['b'] = aValue

print(evalWire('a'))
