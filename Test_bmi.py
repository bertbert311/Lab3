import Lab2.bmi as bmi

def test_bmi_normal_weight():

    assert(0 == bmi.calculate_bmi(weight=57,height=1.73))

def test_bmi_overweight():

    assert(1 == bmi.calculate_bmi(weight=80,height=1.73))

def test_bmi_underweight():

    assert(-1 == bmi.calculate_bmi(weight=50,height=1.73))