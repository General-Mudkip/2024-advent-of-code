f = open("./input1.txt", "r")
lines = f.readlines()

list1 = []
list2 = []

for line in lines:
    splitLine = line.split()
    list1.append(int(splitLine[0]))
    list2.append(int(splitLine[1]))

similarityScore = 0
for i in range(len(list1)):
    totalCount = 0
    for ii in range(len(list2)):
        if (list1[i] == list2[ii]):
            totalCount += 1
    similarityScore += list1[i] * totalCount

print(similarityScore)
