import pytest 
from employee import get_employee_info
def test_get_employee_info():
    name = "Harsha"
    emp_id = "E101"
    department = "IT"
    salary = 55000
    expected_output = (
        "Employee Name: Harsha\n"
        "Employee ID: E101\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    assert get_employee_info(name, emp_id, department, salary) == expected_output