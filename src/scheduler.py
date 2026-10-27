from employee import Employee, organize_employees
from shift import Shift, organize_shifts
# availability check
def is_available(employee, shift):
    day = shift.day.lower()
    for start, end in employee.availability[day]:
        if shift.start_time >= start and shift.end_time <= end:
            return True
    return False


# employee availability
connor_availability = {
    "monday": [(9, 17)],
    "tuesday": [(13, 21)],
    "wednesday": [],
    "thursday": [(9, 17)],
    "friday": [(9, 13)],
    "saturday": [],
    "sunday": []
}
alex_availability = {
    "monday": [],
    "tuesday": [(7, 14)],
    "wednesday": [(8, 13)],
    "thursday": [],
    "friday": [(9, 13)],
    "saturday": [],
    "sunday": [(12, 18)]
}
# employee info
employees_general_info = [
    Employee("Connor", ["lifeguard"], 20, connor_availability),
    Employee("Alex", ["lifeguard", "supervisor"], 15, alex_availability),
]
shifts = [
    Shift("Monday", 9, 13, 3, {
    "lifeguard": 2,
    "supervisor": 1
}),
    Shift("Monday", 10, 13, 4, {"lifeguard": 2,
        "supervisor": 2
    })
]

employees_organized = organize_employees(employees_general_info)
#print(employees_organized)
shifts_organized = organize_shifts(shifts)
print(shifts_organized)
print(is_available(employees_general_info[0], shifts[0]))
