from day_4 import part_1, part_2, parse_str, within, overlap

testData = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

def test_str_to_sets():
    assert parse_str("2-4,6-8") == ((2,4),(6,8))

def test_within():
    assert within("2-4,6-8") == False
    assert within("2-8,3-7") == True
    assert within("3-7,2-8") == True

def test_overlap():
    assert overlap("2-4,6-8") == False
    assert overlap("2-8,3-7") == True
    assert overlap("2-6,6-8") == True

def test_part_1():
    assert part_1(testData) == 2

def test_part_2():
    assert part_2(testData) == 4