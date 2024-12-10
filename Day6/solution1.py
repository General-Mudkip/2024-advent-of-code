import time

f = open("./input.txt", "r")
map = f.readlines()

# y, x
position = (0,0)
orientation = "up"
isOut = False

visited_positions = []

max_x = len(map[0]) - 1
max_y = len(map) - 1

def replaceChar(original_string, index_to_replace, new_character):
    return original_string[:index_to_replace] + new_character + original_string[index_to_replace + 1:]

def printText(indices):
    print("\n\n\n\n")
    for i in range(len(map)):
        for ii in range(len(map[i])):
            if (i, ii) in visited_positions:
                print("\033[91m\033[1m", map[i][ii], "\033[0m", sep="", end="")
            else:
                print(map[i][ii], end="")

def isObstacle(new_pos):
    y = new_pos[0]
    x = new_pos[1]
    if map[y][x] == "#":
        return True
    else:
        return False

def addToVisited(new_pos):
    if new_pos not in visited_positions:
        visited_positions.append(new_pos)
        match orientation:
            case "up":
                map[new_pos[0]] = replaceChar(map[new_pos[0]], new_pos[1], "^")
            case "down":
                map[new_pos[0]] = replaceChar(map[new_pos[0]], new_pos[1], "v")
            case "right":
                map[new_pos[0]] = replaceChar(map[new_pos[0]], new_pos[1], ">")
            case "left":
                map[new_pos[0]] = replaceChar(map[new_pos[0]], new_pos[1], "<")

def move():
    global orientation, position, isOut
    match orientation:
        case "up":
            new_pos = (position[0] - 1, position[1])

            if (position[0] - 1 == -1):
                isOut = True
                return
            else:
                if isObstacle(new_pos):
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
                    orientation = "up"
                else:
                    addToVisited(new_pos)
                    position = new_pos


start = time.time()

for i in range(len(map)):
    for ii in range(len(map[i])):
        if map[i][ii] == "^":
            position = (i, ii)

while (not isOut):
    move()

end = time.time()
print(len(visited_positions))
print(end-start)
