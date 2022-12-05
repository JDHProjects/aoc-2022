def parse_str(string):
    split_str = string.split(",")
    first = split_str[0].split("-")
    second = split_str[1].split("-")
    return (int(first[0]),int(first[1])), (int(second[0]),int(second[1]))

def within(data):
    values = parse_str(data) 
    if values[0][0] <= values[1][0] and values[0][1] >= values[1][1]:
        return True
    if values[1][0] <= values[0][0] and values[1][1] >= values[0][1]:
        return True
    return False

def overlap(data):
    values = parse_str(data)
    if values[0][0] <= values[1][0] and values[0][1] >= values[1][0]:
        return True
    if values[0][0] <= values[1][1] and values[0][1] >= values[1][1]:
        return True
    if values[1][0] <= values[0][0] and values[1][1] >= values[0][0]:
        return True
    if values[1][0] <= values[0][1] and values[1][1] >= values[0][1]:
        return True
    return False

def part_1(data):
    count = 0
    for datum in data.split("\n"):
        if within(datum):
            count += 1
    return count 

def part_2(data):
    count = 0
    for datum in data.split("\n"):
        if overlap(datum):
            count += 1
    return count 

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))