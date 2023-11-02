import employee_info as employee

test_employee_data = [
    {"name": "John", "age": 40, "department": "Sales", "salary": 62500},
    {"name": "Jane", "age": 38, "department": "Marketing", "salary": 63000},
    {"name": "Mary", "age": 41, "department": "Marketing", "salary": 55000},
    {"name": "Chloe",  "age": 39, "department": "Engineering", "salary": 69000},
    {"name": "Mike", "age": 34, "department": "Engineering", "salary": 57000},
    {"name": "Peter", "age": 46, "department": "Sales", "salary": 61500}
]

def test_calculate_average_salary():
    test_value = 61333.33
    result = employee.calculate_average_salary(test_employee_data)
    assert (test_value == result)

def test_get_employees_by_age_range():
    test_arr = [{'name': 'John', 'age': 40, 'department': 'Sales', 'salary': 62500},
                {'name': 'Mary', 'age': 41, 'department': 'Marketing', 'salary': 55000}]
    test_lower_range_value = 39
    test_upper_range_value = 44
    result = employee.get_employees_by_age_range(test_employee_data, test_lower_range_value, test_upper_range_value)
    assert (test_arr == result)

def test_get_employees_by_dept():
    test_arr = [{'name': 'Chloe', 'age': 39, 'department': 'Engineering', 'salary': 69000},
                {'name': 'Mike', 'age': 34, 'department': 'Engineering', 'salary': 57000}]

    result = employee.get_employees_by_dept(test_employee_data, "Engineering")

    assert (test_arr == result)

