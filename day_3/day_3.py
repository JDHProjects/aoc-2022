def str_to_sets(string):
    str_len = len(string)
    return (set(string[:str_len//2]),set(string[str_len//2:]))

def char_to_priority(char):
    int_val = ord(char)-64
    if int_val <= 26:
        return int_val + 26
    return int_val - 32

def part_1(data):
    total = 0
    for datum in data.split("\n"):
        (left, right) = str_to_sets(datum)
        for same in left.intersection(right):
            total += char_to_priority(same)
    return total

def part_2(data):
    total = 0
    count = 0
    running_set = set()
    for datum in data.split("\n"):
        count += 1
        if count == 1:
            running_set = set(datum)
        else:
            running_set = running_set.intersection(set(datum))   
        if count == 3:
            count = 0
            total += char_to_priority(running_set.pop())
            running_set = set()
        
    return total

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))