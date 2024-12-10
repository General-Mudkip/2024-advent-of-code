from itertools import product

f = open("./input.txt", "r")
lines = f.readlines()

operator_array = ["add", "mul", "conc"]

def get_ops(n):
    return list(product(operator_array, repeat=n))

total_sum = 0
for j in range(len(lines)):
    split_line = lines[j].split(":")
    final_value = int(split_line[0])
    the_values = split_line[1].strip().split(" ")

    is_evaluable = False

    ops = get_ops(len(the_values) - 1)

    for i in range(len(ops)):
        sum = int(the_values[0])
        for ii in range(len(ops[i])):
            copied_values = the_values.copy()
            current_operator = ops[i][ii]
            arg2 = int(copied_values[ii + 1])

            if (current_operator == "add"):
                sum += arg2
            elif (current_operator == "mul"):
                sum *= arg2
            elif (current_operator == "conc"):
                sum = int(str(sum) + copied_values[ii + 1])

        if sum == final_value:
            is_evaluable = True

    if (is_evaluable):
        total_sum += final_value

print(total_sum)
