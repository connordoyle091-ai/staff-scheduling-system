import pytest

from src.employee import Employee, organize_employees
from src.shift import Shift, organize_shifts
from src.scheduler import (
    is_available,
    matching_qualifications,
    within_max_hours,
    has_shift_conflict,
    can_work_shift,
)


def test_shift_duration():
    shift = Shift(
        "Monday",
        9,
        13,
        2,
        {"lifeguard": 1}
    )

    assert shift.duration() == 4

def test_invalid_shift_day():
    with pytest.raises(ValueError):
        Shift(
            "Funday",
            9,
            13,
            2,
            {"lifeguard": 1}
        )


def test_invalid_shift_time():
    with pytest.raises(ValueError):
        Shift(
            "Monday",
            13,
            9,
            2,
            {"lifeguard": 1}
        )

def test_employee_is_available():
    availability = {
        "monday": [(9, 17)],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }

    employee = Employee(
        "Test Employee",
        ["lifeguard"],
        20,
        availability,
        []
    )

    shift = Shift(
        "Monday",
        10,
        14,
        2,
        {"lifeguard": 1}
    )

    assert is_available(employee, shift) is True
