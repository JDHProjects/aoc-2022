import copy 

def parse_data(data):
    split_data = data.split("\n\n")
    stack_data = split_data[0].split("\n")
    stack_width = 1 + len(stack_data[-1]) // 4
    
    stack_dict = {}
    for x in range(0, stack_width):
        stack_dict[int(stack_data[-1][1 + (x * 4)])] = []
    for y in range(len(stack_data)-2, -1, -1):
        for x in range(0, stack_width):
            current_value = stack_data[y][1 + (x * 4)]
            if ' ' != current_value:
                stack_dict[x+1].append(current_value)
    return (stack_dict, split_data[1].split("\n"))

def part_1(stack, instructions):
    for instruction in instructions:
        inst_list = instruction.split(" ")
        stack_from = int(inst_list[3])
        stack_to = int(inst_list[5])
        for i in range(int(inst_list[1])):
            stack[stack_to].append(stack[stack_from].pop(-1))
    
    stack_out = ""
    for pile in stack:
        stack_out += stack[pile][-1]
    return stack_out

def part_2(stack, instructions):
    for instruction in instructions:
        inst_list = instruction.split(" ")
        stack_from = int(inst_list[3])
        stack_to = int(inst_list[5])
        stack_move = int(inst_list[1])
        stack[stack_to] += stack[stack_from][-stack_move:]
        stack[stack_from] = stack[stack_from][:-stack_move]
        
    stack_out = ""
    for pile in stack:
        stack_out += stack[pile][-1]
    return stack_out

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        stack, instructions = parse_data(input_file.read())
    print(part_1(copy.deepcopy(stack), instructions))
    print(part_2(copy.deepcopy(stack), instructions))