import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_str():
    false = 0
    result = 0
    input_arr = ["a", 1, 3, "b" , "c" , 1]

    if false == all(ele.isdigit() for ele in input_arr):
        result = 2

    assert(result == 2)

def test_bubble_sort_excess():
    result = 0
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if len(input_arr) >= 10:
        result = 1

    assert(result == 1)
