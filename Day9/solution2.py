f = open("./test3.txt", "r")
lines = f.readlines()

disk_map = lines[0].strip()

block_string = []
unplaceable_ids = []
placed_ids = []

def map_has_free_space():
    dot_in_numbers = False
    has_encountered_dot = False
    free_spaces = [] # Array of arrays: (indexes)

    current_free_slot = []
    for i in range(len(block_string)):
        if block_string[i] == ".":
            has_encountered_dot = True
            current_free_slot.append(i)
        if block_string[i] != "." and has_encountered_dot:
            dot_in_numbers = True
            if current_free_slot != []:
                free_spaces.append(current_free_slot)
            current_free_slot = []

    if dot_in_numbers:
        return True, free_spaces
    else:
        return False, free_spaces

def find_block():
    current_block_number = -1
    block_index_array = []

    for i in reversed(range(len(block_string))):
        if block_string[i] != "." and block_string[i] not in unplaceable_ids and not block_string[i] in placed_ids:
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

while (len(placed_ids) + len(unplaceable_ids)) <= (highest_id / 2):
    b, free_slots = map_has_free_space()
    if not b:
        break
    else:
        curr_block = find_block()
        curr_id = 0
        if len(curr_block) > 0:
            curr_id = block_string[curr_block[0]]
        is_placed = False
        for slot in free_slots:
            if len(curr_block) > 0 and len(slot) >= len(curr_block) and slot[0] < curr_block[0]:
                is_placed = True
                for i in range(len(curr_block)):
                    block_string[slot[i]] = block_string[curr_block[i]]
                    block_string[curr_block[i]] = "."
        if not is_placed:
            unplaceable_ids.append(curr_id)
        else:
            placed_ids.append(curr_id)

sum = 0
for i in range(len(block_string)):
    if block_string[i] != ".":
        sum += i * int(block_string[i])
print(block_string)
print(sum)
