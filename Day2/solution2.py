f = open("./input.txt", "r")
lines = f.readlines()

sum = 0

for report in lines:
    levels = report.split()
    tolerance = 0
    safe = True

    old_diff = 0 
    for i in range(len(levels) - 1):
        diff = int(levels[i]) - int(levels[i+1])

        if abs(diff) > 3 or diff == 0 or diff * old_diff < 0:
            safe = False
            break

        old_diff = diff

    isSafeWithPopped = False
    if not safe:
        for i in range(len(levels)):
            shortenedList = levels.copy()
            shortenedList.pop(i)
            old_diff = 0
            count = 0

            for i in range(len(shortenedList) - 1):
                diff = int(shortenedList[i]) - int(shortenedList[i+1])

                if abs(diff) > 3 or diff == 0 or diff * old_diff < 0:
                    count += 1

                old_diff = diff

            if count == 0:
                isSafeWithPopped = True


    if safe or isSafeWithPopped:
        sum += 1
    else:
        print(report)

print(sum)
