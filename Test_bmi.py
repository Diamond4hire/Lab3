from Lab2 import bmi

print("Test_bmi")


def test_bmi_normal_weight():
    result = 0
    input_height = (1.7)
    input_weight = (58)

    result = bmi.calculate_bmi(input_height,input_weight)
    assert result == 0


def test_bmi_over_weight():
    result = 0
    input_height = (1.7)
    input_weight = (120)

    result = bmi.calculate_bmi(input_height,input_weight)
    assert result == 1



def test_bmi_under_weight():
    result = 0
    input_height = (1.7)
    input_weight = (5)

    result = bmi.calculate_bmi(input_height,input_weight)
    assert result == -1