def incr_string(string, pos):
    char = ord(string[pos])
    char += 1
    if (char > ord('z')):
        char = ord('a')
        string = string[:pos] + chr(char) + string[pos+1:]
        return incr_string(string, pos-1)
    string = string[:pos]+chr(char)+string[pos + 1:]
    return string

badchars = ["i", "o", "l"]
def valid_password(string):
    i = 0
    straight = False
    pairs = set()
    while i < len(string):
        if string[i] in badchars:
            return False
        if i+1 < len(string) and string[i+1] == string[i]:
            pairs.add(string[i])
            i += 1
            continue
        charval = ord(string[i])
        if i+2 < len(string) and ord(string[i+1]) == charval+1 and ord(string[i+2]) == charval+2:
            straight = True
            i += 2
        else:
            i += 1
    return straight and len(pairs) > 1
            
password = "vzbxkghb"

while not valid_password(password):
    password = incr_string(password, len(password)-1)
print(password)

#part2: do it again
password = incr_string(password, len(password)-1)
while not valid_password(password):
    password = incr_string(password, len(password)-1)
print(password)
        
