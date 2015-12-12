import json, pprint

rawdata = open("inputs/DayTwelveInput.txt").read()

data = json.loads(rawdata)


def handleItem(item):
    num = 0
    if type(item) is int:
        num = item
    elif type(item) is dict:
        for value in item.values():
            val = handleItem(value)
            if type(val) is str:
                num = 0
                break
            else:
                num += val
    elif type(item) is list:
        for value in item:
            val = handleItem(value)
            if type(val) is int:
                num += val
    elif type(item) is str:
        if item == "red":
            num = "red"
    return num

sumnumbers = 0            
for key, value in data.items():
    sumnumbers += handleItem(value)

print(str(sumnumbers))
