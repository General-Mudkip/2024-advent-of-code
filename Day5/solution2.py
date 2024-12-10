import math

f = open("./input.txt", "r")
f2 = open("./input2.txt", "r")
rules = f.readlines()
updates = f2.readlines()

def checkIfCorrect(laArray):
    incorrectOrder = False
    for rule in ruleList:
        rule1Present = False
        rule1Index = -1
        rule2Present = False
        rule2Index = -1

        for i in range(len(laArray)):
            page = int(laArray[i])
            if rule[0] == page:
                rule1Index = i
                rule1Present = True
            if rule[1] == page:
                rule2Index = i
                rule2Present = True

        if rule1Present and rule2Present:
            if (rule1Index > rule2Index):
                swapVal = laArray[rule1Index]
                laArray[rule1Index] = laArray[rule2Index]
                laArray[rule2Index] = swapVal
                print(rule1Index, rule2Index, laArray[rule1Index], laArray[rule2Index])
                incorrectOrder = True

    if incorrectOrder:
        return False, laArray
    else:
        return True, laArray

ruleList = []
for rule in rules:
    ruleList.append((int(rule.split("|")[0]), int(rule.split("|")[1])))

correct = []
for update in updates:
    incorrectOrder = False

    updateArray = update.split(",")
    for rule in ruleList:
        rule1Present = False
        rule1Index = -1
        rule2Present = False
        rule2Index = -1


        for i in range(len(updateArray)):
            page = int(updateArray[i])
            if rule[0] == page:
                rule1Index = i
                rule1Present = True
            if rule[1] == page:
                rule2Index = i
                rule2Present = True

        if rule1Present and rule2Present:
            if (rule1Index > rule2Index):
                incorrectOrder = True

    if incorrectOrder:
        correct.append(updateArray)

sum = 0
for c in correct:
    print("\n\n\nNew array, ", c)
    isC, array = checkIfCorrect(c)
    while not isC:
        print(isC, array)
        isC, array = checkIfCorrect(array)
    print(isC, array)
    middle = math.floor(len(c) / 2)
    sum += int(c[middle])

print(sum)
