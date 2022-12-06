from day_6 import part_1, part_2

test_data_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test_data_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_data_3 = "nppdvjthqldpwncqszvftbrmjlhg"
test_data_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_data_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def test_part_1():
    assert part_1(test_data_1) == 7
    assert part_1(test_data_2) == 5
    assert part_1(test_data_3) == 6
    assert part_1(test_data_4) == 10
    assert part_1(test_data_5) == 11

def test_part_2():
    assert part_2(test_data_1) == 19
    assert part_2(test_data_2) == 23
    assert part_2(test_data_3) == 23
    assert part_2(test_data_4) == 29
    assert part_2(test_data_5) == 26