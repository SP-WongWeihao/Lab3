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

def test_bubble_above_ten_num():
    MORE_THAN_TEN_NUMBERS_RETVAL = 1
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == MORE_THAN_TEN_NUMBERS_RETVAL)

def test_bubble_no_num():
    ZERO_NUMBERS_RETVAL = 0
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == ZERO_NUMBERS_RETVAL)

def test_bubble_not_integers():
    NOT_INTEGER_RETVAL = 2
    input_arr = [1.23, 4.4, 0.2]
    result = (Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING))
    assert (result == NOT_INTEGER_RETVAL)
