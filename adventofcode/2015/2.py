import sys 

input = sys.argv[1]
totalPaper = 0
totalRibbon = 0
for line in input.splitlines():
    line = line.strip()
    split = line.split('x')
    length = int(split[0])
    width = int(split[1])
    height = int(split[2])
    dimensions = [length, width, height]
    dimensions = sorted(dimensions)
    sides = [length * width, length * height, width * height]
    sides = sorted(sides)
    totalPaper = totalPaper + (3 * sides[0]) + (2 * sides[1]) +(2 * sides[2])
    totalRibbon = totalRibbon + (dimensions[0] * 2) + (dimensions[1] * 2) + (dimensions[0] * dimensions[1] * dimensions[2])

print(f"Total paper: {totalPaper}\nTotal ribbon: {totalRibbon}")