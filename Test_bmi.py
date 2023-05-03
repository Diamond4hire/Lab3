from Lab2 import bmi

print("Test_bmi")


def test_bmi_normal_weight():
    test = 0
    if 18.5 <= bmi.result[1] <= 25.0:
        assert 18.5 <= bmi.result[1] <= 25.0 and bmi.result[0] == 0
    else:
        print("passed, not in range")
        assert test == 0


def test_bmi_over_weight():
    test = 0
    if bmi.result[1] > 25:
        assert bmi.result[1] > 25 and bmi.result[0] == 0
    else:
        print("passed, not in range")
        assert test == 0


def test_bmi_under_weight():
    test = 0
    if bmi.result[1] < 18.5:
        assert bmi.result[1] < 18.5 and bmi.result[0] == 0
    else:
        print("passed, not in range")
        assert test == 0
