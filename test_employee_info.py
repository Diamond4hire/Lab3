import employee_info


def test_age_range():
    result = []
    min_age=22
    max_age=31

    result = employee_info.get_employees_by_age_range(min_age,max_age)

    assert result == employee_info.employee_data[:3]

def test_average_salary():
    result = employee_info.calculate_average_salary()
    average = 361000/6

    assert result == average

def test_get_employee_by_dept():
    result = []
    department = "Sales"

    result = employee_info.get_employees_by_dept(department)
    employee_data_subset = [employee_info.employee_data[i] for i in [0, 5]]

    assert result == employee_data_subset