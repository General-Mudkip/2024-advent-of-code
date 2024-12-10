import time

f = open("./input.txt", "r")
map = f.readlines()

# y, x

def replaceChar(original_string, index_to_replace, new_character):
    return original_string[:index_to_replace] + new_character + original_string[index_to_replace + 1:]

def printMap(indices):
    print("\n\n\n\n")
    for i in range(len(map)):
        for ii in range(len(map[i])):
            if (i, ii) in indices:
                print("\033[91m\033[1m", new_map[i][ii], "\033[0m", sep="", end="")
            else:
                print(new_map[i][ii], end="")

def isObstacle(new_pos):
    y = new_pos[0]
    x = new_pos[1]
    if new_map[y][x] == "#":
        return True
    else:
        return False

def addToVisited(new_pos):
    if new_pos not in visited_positions:
        visited_positions.append(new_pos)
        match orientation:
            case "up":
                new_map[new_pos[0]] = replaceChar(new_map[new_pos[0]], new_pos[1], "^")
            case "down":
                new_map[new_pos[0]] = replaceChar(new_map[new_pos[0]], new_pos[1], "v")
            case "right":
                new_map[new_pos[0]] = replaceChar(new_map[new_pos[0]], new_pos[1], ">")
            case "left":
                new_map[new_pos[0]] = replaceChar(new_map[new_pos[0]], new_pos[1], "<")

def move():
    global orientation, position, isOut, infLoop
    match orientation:
        case "up":
            new_pos = (position[0] - 1, position[1])

            if (position[0] - 1 == -1):
                isOut = True
                return
            else:
                if isObstacle(new_pos):
                    if (new_pos in up_change_orientation_positions):
                        infLoop = True
                    up_change_orientation_positions.append(new_pos)
                    orientation = "right"
                else:
                    position = new_pos
                    addToVisited(new_pos)

        case "down":
            new_pos = (position[0] + 1, position[1])

            if (position[0] + 1 > max_y):
                isOut = True
                return
            else:
                if isObstacle(new_pos):
                    if (new_pos in down_change_orientation_positions):
                        infLoop = True
                    down_change_orientation_positions.append(new_pos)
                    orientation = "left"
                else:
                    addToVisited(new_pos)
                    position = new_pos

        case "right":
            new_pos = (position[0], position[1] + 1)

            if (position[1] + 1 > max_x):
                isOut = True
                return
            else:
                if isObstacle(new_pos):
                    if (new_pos in right_change_orientation_positions):
                        infLoop = True
                    right_change_orientation_positions.append(new_pos)
                    orientation = "down"
                else:
                    addToVisited(new_pos)
                    position = new_pos

        case "left":
            new_pos = (position[0], position[1] - 1)

            if (position[1] - 1 == -1):
                isOut = True
                return
            else:
                if isObstacle(new_pos):
                    if (new_pos in right_change_orientation_positions):
                        infLoop = True
                    right_change_orientation_positions.append(new_pos)
                    orientation = "up"
                else:
                    addToVisited(new_pos)
                    position = new_pos


start = time.time()

total_loops = 0
position_count =len(map) * len(map[0]) 
count = 0
for p_i in range(len(map)):
    for p_ii in range(len(map[p_i])):
        count += 1
        new_map = map.copy()

        if count % 10 == 0 and count != 0:
            print(total_loops, count, "/", position_count, " || Time: ", time.time() - start, " || Estimated: ", time.time() - start +  ((time.time() - start) / count) * (position_count - count))

        if new_map[p_i][p_ii] != "^" and new_map[p_i][p_ii] != "#":
            # new_map[p_i] = replaceChar(new_map[p_i], p_ii, "#")
            pass
        else:
            continue

        position = (0,0)
        orientation = "up"
        isOut = False
        infLoop = False

        visited_positions = []
        up_change_orientation_positions = []
        down_change_orientation_positions = []
        right_change_orientation_positions = []
        left_change_orientation_positions = []

        max_x = len(map[0]) - 1
        max_y = len(map) - 1
        for i in range(len(map)):
            for ii in range(len(map[i])):
                if map[i][ii] == "^":
                    position = (i, ii)

        while (not isOut):
            if (infLoop):
                print(position)
                total_loops += 1
                break
            move()
        print(visited_positions)

end = time.time()
print(end-start)
print(total_loops)
