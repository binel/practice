import sys

def updatePosition(xpos, ypos, char):
    if c == '>':
        xpos += 1
    if c == '<':
        xpos -= 1
    if c == '^':
        ypos += 1
    if c == "v":
        ypos -= 1
    
    return xpos, ypos

useRoboSanta = True 
santaTurn = True

input = sys.argv[1]

xpos, ypos = 0, 0
xpos2, ypos2 = 0, 0
positions = {(xpos, ypos)}

for c in input: 
    if useRoboSanta and not santaTurn:
        santaTurn = True
        xpos2, ypos2 = updatePosition(xpos2, ypos2, c)
        positions.add((xpos2, ypos2))
    else: 
        santaTurn = False
        xpos, ypos = updatePosition(xpos, ypos, c)
        positions.add((xpos, ypos))

print(len(positions))
