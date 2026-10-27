from employee import Employee, organize_employees
from shift import Shift, organize_shifts

employees_general_info = [
    Employee("Connor", ["lifeguard"], 20),
    Employee("Alex", ["lifeguard", "supervisor"], 15),
]

shifts = [
    Shift("Monday", 9, 13, 2),
]

employees_organized = organize_employees(employees_general_info)
print(employees_organized)
shifts_organized = organize_shifts(shifts)
print(shifts_organized)
