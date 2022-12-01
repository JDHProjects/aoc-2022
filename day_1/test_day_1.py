from main import find_max_cal, find_top_3_cal

testData = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

def test_part_1():
    assert find_max_cal(testData) == 24000

def test_part_2():
    assert find_top_3_cal(testData) == 45000
