import time

f = open("./test3.txt", "r")
lines = f.readlines()

disk_map = lines[0].strip()

block_string = []

def find_block():
    current_block_number = -1
    block_index_array = []

    for i in range(last_block_index - 1, -1, -1):
        if block_string[i] != ".":
            if current_block_number != -1:
                if current_block_number != block_string[i]:
                    return block_index_array
                else:
                    block_index_array.append(i)
            else:
                block_index_array.append(i)
                current_block_number = block_string[i]
    return []
    

block_index = -1
highest_id = 0
for i in range(len(disk_map)):
    char = disk_map[i]
    if i % 2 == 0:
        block_index += 1
        highest_id = i
        for i in range(int(char)):
            block_string.append(str(block_index))
    else:
        for i in range(int(char)):
            block_string.append(".")

last_block_index = len(block_string)

start = time.time()
for i in range(20):
    start_time = time.time()
    # print("pre find_block:", time.time() - start_time)
    curr_block = find_block()
    # print("find_block:", time.time() - start_time)
    curr_id = 0
    if len(curr_block) > 0:
        curr_id = block_string[curr_block[0]]

    current_free_slot = []
    slot = []
    for i in range(len(block_string)):
        if block_string[i] == ".":
            current_free_slot.append(i)
        else:
            if len(current_free_slot) >= len(curr_block):
                slot = current_free_slot
                break
            else:
                current_free_slot = []

    if len(slot) == 0 or slot[0] > curr_block[0]:
        if len(curr_block) > 0:
            last_block_index = curr_block[-1]
    # print("find slot:", time.time() - start_time)

    if len(curr_block) > 0 and len(slot) > 0 and slot[0] < curr_block[0]:
        last_block_index = curr_block[-1] + 1
        for i in range(len(curr_block)):
            block_string[slot[i]] = block_string[curr_block[i]]
            block_string[curr_block[i]] = "."

    # print("finished:", time.time() - start_time)

sum = 0
for i in range(len(block_string)):
    if block_string[i] != ".":
        sum += i * int(block_string[i])
print(sum)
print(block_string)
print(time.time() - start, "seconds")
