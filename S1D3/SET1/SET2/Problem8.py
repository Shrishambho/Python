employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_data = {employee: defaults for employee in employees}

print(employee_data)
