f = open("./test.txt", "r")
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
for i in range(len(lines)-2):
    line = lines[i]
    for ii in range(len(line)-3):
        indices = []
        elements = []
        for iii in range(3):
            rowOfElements = []
            for iv in range(3):
                rowOfElements.append(lines[i + iii][iv + ii])
                indices.append((i + iii, iv + ii))
            elements.append(rowOfElements)
        printText(indices)
        firstDiag = elements[0][0] + elements[1][1] + elements[2][2]
        secondDiag = elements[0][2] + elements[1][1] + elements[2][0]

        if (firstDiag == "MAS" or firstDiag == "SAM") and (secondDiag == "MAS" or secondDiag == "SAM"):
            sum += 1

print(sum)
