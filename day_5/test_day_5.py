from day_5 import part_1, part_2, parse_data

testData = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

def test_parse_data():
    test_stack = {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}
    test_instructions = ["move 1 from 2 to 1","move 3 from 1 to 3","move 2 from 2 to 1","move 1 from 1 to 2"]
    assert parse_data(testData) == (test_stack, test_instructions)

def test_part_1():
    stack, instructions = parse_data(testData)
    assert part_1(stack, instructions) == "CMZ"

def test_part_2():
    stack, instructions = parse_data(testData)
    assert part_2(stack, instructions) == "MCD"