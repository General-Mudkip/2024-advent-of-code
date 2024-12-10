import math

f = open("./input.txt", "r")
f2 = open("./input2.txt", "r")
rules = f.readlines()
updates = f2.readlines()

ruleList = []
for rule in rules:
    ruleList.append((int(rule.split("|")[0]), int(rule.split("|")[1])))

correct = []
for update in updates:
    incorrectOrder = False
    for rule in ruleList:
        rule1Present = False
        rule1Index = -1
        rule2Present = False
        rule2Index = -1

        for i in range(len(update.split(","))):
            page = int(update.split(",")[i])
            if rule[0] == page:
                rule1Index = i
                rule1Present = True
            if rule[1] == page:
                rule2Index = i
                rule2Present = True

        if rule1Present and rule2Present:
            if (rule1Index > rule2Index):
                incorrectOrder = True

    if not incorrectOrder:
        correct.append(update)

sum = 0
for c in correct:
    lis = c.split(",")
    middle = math.floor(len(lis) / 2)
    sum += int(lis[middle])

print(sum)
