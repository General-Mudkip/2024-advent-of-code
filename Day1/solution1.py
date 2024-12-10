f = open("./input1.txt", "r")
lines = f.readlines()

list1 = []
list2 = []

for line in lines:
    splitLine = line.split()
    list1.append(int(splitLine[0]))
    list2.append(int(splitLine[1]))

list1.sort()
list2.sort()

sum = 0;
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)
