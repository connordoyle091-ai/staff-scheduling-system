from src.employee import Employee
from src.shift import Shift
from src.scheduler import assign_shift


connor_availability = {
    "monday": [(9, 17)],
    "tuesday": [(13, 21)],
    "wednesday": [],
    "thursday": [(9, 17)],
    "friday": [(9, 13)],
    "saturday": [],
    "sunday": []
}

employee = Employee(
    "Connor",
    ["lifeguard"],
    20,
    connor_availability,
    []
)

shift = Shift(
    "Monday",
    9,
    13,
    1,
    {"lifeguard": 1}
)

assign_shift(employee, shift)

print(employee.assigned_shifts)
