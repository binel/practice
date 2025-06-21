import sys 

input = sys.argv[1]

floor = 0
position = 0;
foundBasement = False;
for c in input: 
    position = position + 1;
    if c == '(':
        floor = floor + 1
    if c == ')':
        floor = floor - 1

    if floor < 0 and not foundBasement: 
        foundBasement = True
        print(f"basement position {position}")
print(f"final floor {floor}")