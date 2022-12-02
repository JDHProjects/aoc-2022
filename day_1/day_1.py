def find_max_cal(data):
    return max(sum_data(data))

def sum_data(data):
    data_list = data.split("\n\n")

    return list(map(lambda a: sum([int(x) for x in a.split("\n")]), data_list))

def find_top_3_cal(data):
    data_list=sorted(sum_data(data))
    return sum(data_list[-3:])

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()
    print(find_max_cal(input_data))
    print(find_top_3_cal(input_data))