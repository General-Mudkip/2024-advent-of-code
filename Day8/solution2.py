f = open("./input.txt", "r")
lines = f.readlines()

max_y = len(lines) 
max_x = len(lines[0]) - 1

antennae = []
unique_antinodes = []

def printMap(indices):
    print("\n\n\n\n")
    for i in range(len(lines)):
        for ii in range(len(lines[i])):
            if (i, ii) in indices:
                print("\033[91m\033[1m", "#", "\033[0m", sep="", end="")
            else:
                print(lines[i][ii], end="")

# Find all unique antennae
for i in range(len(lines)):
    for ii in range(len(lines[i].strip())):
        char = lines[i].strip()[ii]
        if char not in ["\n", "."]: 
            antennae.append((char, (i, ii)))

for ant1 in antennae:
    for ant2 in antennae:
        if ant1 != ant2 and ant1[0] == ant2[0]:
            y_diff = 0
            x_diff = 0

            anti_node = (ant1[1][0] + y_diff, ant1[1][1] + x_diff)

            # printMap([ant1[1], ant2[1], anti_node])
            # print([ant1[1], ant2[1], anti_node], x_diff, y_diff)

            counter = 0
            while anti_node[0] < max_y and anti_node[0] >= 0 and anti_node[1] >= 0 and anti_node[1] < max_x:
                print(y_diff, x_diff)
                if anti_node not in unique_antinodes:
                    unique_antinodes.append(anti_node)
                y_diff += ant1[1][0] - ant2[1][0]
                x_diff += ant1[1][1] - ant2[1][1]
                anti_node = (ant1[1][0] + y_diff, ant1[1][1] + x_diff)

printMap(unique_antinodes)
print(len(unique_antinodes))
