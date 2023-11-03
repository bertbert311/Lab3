import employee_info
def test_get_employees_by_age_range():
    result = [{'age':23, 'department':"Marketing", 'name':"Mary", 'salary':56000}]
    employee = employee_info.get_employees_by_age_range(22,25)
    assert employee == result

def test_calculate_average_salary():
    result = float(60166.67)
    salary = employee_info.calculate_average_salary()
    assert result == float(format(salary,".2f"))

def test_get_employees_by_dept():
    result = [{"name" :'John',"age": 30, "department": "Sales", "salary": 50000}, {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    employee_by_dept = employee_info.get_employees_by_dept("Sales")
    assert result == employee_by_dept
