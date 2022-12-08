from timeit import timeit

def search(x, data):
    buffer = data[:x-1]
    for i in range(x-1,len(data)):
        if len(buffer) >= x:
            buffer = buffer[1-x:]
        buffer+=data[i]
        if len(set(buffer)) == x:
            return i+1
    return -1

def faster_search(x, data):
    last = 0
    occ_index = {'a':-1,'b':-1,'c':-1,'d':-1,'e':-1,'f':-1,'g':-1,'h':-1,'i':-1,'j':-1,'k':-1,'l':-1,'m':-1,'n':-1,'o':-1,'p':-1,'q':-1,'r':-1,'s':-1,'t':-1,'u':-1,'v':-1,'w':-1,'x':-1,'y':-1,'z':-1}
    for i in range (0, len(data)):
        if i - last == x:
            return i
        if (occ_index[data[i]] >= last):
            last = occ_index[data[i]] + 1
        occ_index[data[i]] = i
    return -1

def part_1(data):
    return search(4, data)

def part_1_fast(data):
    return faster_search(4, data)

def part_2(data):
    return search(14, data)

def part_2_fast(data):
    return faster_search(14, data)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()
    print(timeit(lambda: part_1(input_data), number=10000))
    print(timeit(lambda: part_1_fast(input_data), number=10000))
    print(timeit(lambda: part_2(input_data), number=10000))
    print(timeit(lambda: part_2_fast(input_data), number=10000))