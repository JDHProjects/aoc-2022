from day_2 import part_1, part_2

testData = '''A Y
B X
C Z'''

def test_part_1():
    assert part_1(testData) == 15

def test_part_2():
    assert part_2(testData) == 12