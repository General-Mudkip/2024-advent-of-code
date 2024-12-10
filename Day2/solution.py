f = open("./input.txt", "r")
lines = f.readlines()

sum = 1000

for report in lines:
    levels = report.split()

    old_diff = 0

    for i in range(len(levels) - 1):
        diff = int(levels[i]) - int(levels [i + 1])
        if abs(diff) > 3 or diff == 0 or diff * old_diff < 0:
            sum -= 1
            break
        else:
            old_diff = diff

print(sum)
