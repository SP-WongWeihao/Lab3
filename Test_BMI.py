import Lab2.bmi as bmi

def test_under_weight():
    height = 1.6
    weight = 40
    under_weight_retval = -1
    testval = bmi.calculate_bmi(height, weight)
    assert (testval == under_weight_retval)

def test_normal_weight():
    height = 1.5
    weight = 50
    normal_weight_retval = 0
    testval = bmi.calculate_bmi(height, weight)
    assert (testval == normal_weight_retval)

def test_over_weight():
    height = 1.4
    weight = 60
    over_weight_retval = 1
    testval = bmi.calculate_bmi(height, weight)
    assert (testval == over_weight_retval)
