import re

f = open("./input.txt", "r")
lines = f.readlines()

currentSequence = []

sum = 0
mulActive = True
for char in lines[0]:
    if len(currentSequence) == 0 and char == "m" or char == "d":
        currentSequence.append(char)

    elif len(currentSequence) == 1:
        if (currentSequence[0] == "m" and char == "u"):
            currentSequence.append("u")
        elif (currentSequence[0] == "d" and char == "o"):
            currentSequence.append("o")
        else: currentSequence = []

    elif len(currentSequence) == 2:
        if (currentSequence[1] == "u" and char == "l"):
            currentSequence.append("l")

        elif currentSequence[1] == "o": 
            if char == "(":
                currentSequence.append("(")
            elif char == "n":
                currentSequence.append("n")

        else: currentSequence = []

    elif len(currentSequence) == 3: 
        if (currentSequence[2] == "l" and char == "("):
            currentSequence.append("(")
        elif (currentSequence[2] == "(" and char == ")"):
            currentSequence.append(")")
        elif (currentSequence[2] == "n" and char == "'"):
            currentSequence.append("'")
        else: currentSequence = []

    elif len(currentSequence) == 4 and currentSequence[3] == "'":
        if char == "t":
            currentSequence.append("t")
        else: currentSequence = []

    elif len(currentSequence) == 5 and currentSequence[4] == "t" :
        if char == "(":
            currentSequence.append("(")
        else: currentSequence = []

    elif len(currentSequence) == 6 and currentSequence[5] == "(" :
        if char == ")":
            currentSequence.append(")")
        else: currentSequence = []

    elif len(currentSequence) > 3 and not currentSequence.__contains__(")"):
        if char in [")", ",", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            currentSequence.append(char)
        else:
            print("Invalid character encountered: ", char, "".join(currentSequence))
            currentSequence = []

    if (currentSequence.__contains__(")")):
        sequenceString = "".join(currentSequence)

        if sequenceString == "do()":
            # print(sequenceString)
            mulActive = True
        elif sequenceString == "don't()":
            # print(sequenceString)
            mulActive = False
        else:
            pattern = r"\((.*?)\)"
            numberString: str = re.findall(pattern, sequenceString)[0]
            splitString = numberString.split(",")
            if (len(splitString) == 2):
                # print(mulActive, splitString, sequenceString, sum)
                if mulActive == True:
                    sum += int(splitString[0]) * int(splitString[1])
        currentSequence = []

print(sum)
