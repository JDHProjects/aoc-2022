def search(x, data):
    buffer = data[:x-1]
    
    for i in range(x-1,len(data)):
        
        if len(buffer) >= x:
            buffer = buffer[1-x:]
        buffer+=data[i]
        if len(set(buffer)) == x:
            return i+1
    return -1

def part_1(data):
    return search(4, data)

def part_2(data):
    return search(14, data)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))