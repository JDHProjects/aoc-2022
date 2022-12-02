#1=rock
#2=paper
#3=scissors
part_1_lookup = [[4,8,3],[1,5,9],[7,2,6]]
part_2_lookup = [[3,4,8],[1,5,9],[2,6,7]]
translator = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0, #lose
    'Y': 1, #draw
    'Z': 2  #win
    }


def total_score(data,lookup):
    score = 0
    data_list = data_to_list(data)
    for inputs in data_list:
        score += lookup[translator[inputs[0]]][translator[inputs[1]]]
    return score 

def data_to_list(data):
    return [x.split(" ") for x in data.split("\n")]

def part_1(data):
    return total_score(data, part_1_lookup)

def part_2(data):
    return total_score(data, part_2_lookup)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))