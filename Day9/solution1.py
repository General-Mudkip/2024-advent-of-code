f = open("./test.txt", "r")
lines = f.readlines()

disk_map = lines[0].strip()

block_string = []

def map_has_free_space():
    has_encountered_dot = False
    dot_index = 0
    for i in range(len(block_string)):
        if block_string[i] == "." and not has_encountered_dot:
            has_encountered_dot = True
            dot_index = i
        if block_string[i] != "." and has_encountered_dot:
            return True, dot_index
    else:
        return False, dot_index

def find_last_element():
    for i in reversed(range(len(block_string))):
        if block_string[i] != ".":
            return i
    
    return 0

block_index = -1
for i in range(len(disk_map)):
    char = disk_map[i]
    if i % 2 == 0:
        block_index += 1
        for i in range(int(char)):
            block_string.append(str(block_index))
    else:
        for i in range(int(char)):
            block_string.append(".")

count = 0
while True:
    count += 1
    print(count, "/", len(disk_map))
    b, dot_index = map_has_free_space()
    if not b:
        break
    else:
        block_string[dot_index] = block_string[find_last_element()]
        block_string[find_last_element()] = "."


sum = 0
for i in range(len(block_string)):
    if block_string[i] == ".":
        break
    sum += i * int(block_string[i])
print(sum)
