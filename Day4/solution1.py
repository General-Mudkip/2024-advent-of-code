f = open("./input.txt", "r")
lines = f.readlines()

def printText(indices):
    print("\n\n\n\n")
    for i in range(len(lines)):
        for ii in range(len(lines[i])):
            if (i, ii) in indices:
                print("\033[91m\033[1m", lines[i][ii], "\033[0m", sep="", end="")
            else:
                print(lines[i][ii], end="")

sum = 0
for i in range(len(lines)):
    line = lines[i]

    for ii in range(len(line) - 4):
        straightLine = []
        indices = []
        for iii in range(ii, ii+4):
            indices.append((i, iii))
            straightLine.append(line[iii])

        printText(indices)

        joinedString = "".join(straightLine)
        if joinedString == "XMAS" or joinedString == "SAMX":
            print("Added one!")
            sum += 1

        if (i < (len(lines) - 3)):
            diagonalLine = []
            indices = []
            for iv in range(4):
                indices.append((i + iv, ii + iv))
                diagonalLine.append(lines[i + iv][ii + iv])
            # printText(indices)

            joinedDiagonal = "".join(diagonalLine)
            if joinedDiagonal == "XMAS" or joinedDiagonal == "SAMX":
                print("Added one!")
                sum += 1

        if (i > 2):
            diagonalLine = []
            indices = []
            for iv in range(4):
                indices.append((i-iv, ii + iv))
                diagonalLine.append(lines[i - iv][ii + iv])
            # printText(indices)

            joinedDiagonal = "".join(diagonalLine)
            if joinedDiagonal == "XMAS" or joinedDiagonal == "SAMX":
                print("Added one!")
                sum += 1

for i in range(len(lines) - 3):
    print("Line ", i + 1)

    line = lines[i]

    for ii in range(len(line)):
        verticalLine = []
        indices = []
        for iii in range(4):
            indices.append((i + iii, ii))
            verticalLine.append(lines[i + iii][ii])

        joinedVertical = "".join(verticalLine)
        
        if (joinedVertical == "XMAS" or joinedVertical == "SAMX"):
            sum += 1

        # printText(indices)

print(sum)
