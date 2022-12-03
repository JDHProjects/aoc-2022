from day_3 import part_1, part_2, str_to_sets, char_to_priority

testData = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

def test_str_to_sets():
    assert str_to_sets("abcdefghij") == ({'a','b','c','d','e'}, {'f','g','h','i','j'})

def test_char_to_priority():
    assert char_to_priority("a") == 1
    assert char_to_priority("z") == 26
    assert char_to_priority("A") == 27
    assert char_to_priority("Z") == 52

def test_part_1():
    assert part_1(testData) == 157

def test_part_2():
    assert part_2(testData) == 70