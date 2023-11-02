import price_info as price_info

def test_total_cost_shopping():
    test_total_cost = 38.8
    input_list = {'apple': 2, 'orange':3, 'pear' : 5, 'papaya': 1, 'pomegranate': 5}
    result = price_info.total_cost_shopping(input_list)
    assert (test_total_cost == result)

def test_cost_of_fruits():
    test_cost = 7.0
    result = price_info.cost_of_fruits('orange', 5)
    assert (test_cost == result)