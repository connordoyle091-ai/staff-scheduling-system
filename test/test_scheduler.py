import pytest

from src.employee import Employee, organize_employees
from src.shift import Shift, organize_shifts
from src.scheduler import (
    is_available,
    matching_qualifications,
    within_max_hours,
    has_shift_conflict,
    can_work_shift,
    assign_shift,
)


def test_shift_duration():
    shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    assert shift.duration() == 4

def test_invalid_shift_day():
    with pytest.raises(ValueError):
        Shift(
            "Funday",
            9,
            13,
            1,
            {"lifeguard": 1}
        )


def test_invalid_shift_time():
    with pytest.raises(ValueError):
        Shift(
            "Monday",
            13,
            9,
            1,
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
        1,
        {"lifeguard": 1}
    )

    assert is_available(employee, shift) is True

def make_availability(monday=None, tuesday=None):
    return {
        "monday": monday or [],
        "tuesday": tuesday or [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }
def test_start_and_end_time_cannot_be_equal():
    with pytest.raises(ValueError):
        Shift(
            "Monday",
            13,
            13,
            1,
            {"lifeguard": 1}
        )


def test_employee_is_not_available():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(monday=[(9, 12)]),
        []
    )

    shift = Shift(
        "Monday",
        11,
        15,
        1,
        {"lifeguard": 1}
    )

    assert is_available(employee, shift) is False


def test_split_availability():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(
            monday=[(9, 12), (14, 18)]
        ),
        []
    )

    shift = Shift(
        "Monday",
        14,
        17,
        1,
        {"lifeguard": 1}
    )

    assert is_available(employee, shift) is True


def test_shift_cannot_span_availability_gap():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(
            monday=[(9, 12), (14, 18)]
        ),
        []
    )

    shift = Shift(
        "Monday",
        11,
        15,
        1,
        {"lifeguard": 1}
    )

    assert is_available(employee, shift) is False


def test_matching_qualifications():
    employee = Employee(
        "Alex",
        ["lifeguard", "supervisor"],
        20,
        make_availability(),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        2,
        {
            "lifeguard": 1,
            "supervisor": 1
        }
    )

    assert matching_qualifications(employee, shift) == [
        "lifeguard",
        "supervisor"
    ]


def test_no_matching_qualifications():
    employee = Employee(
        "Connor",
        ["cashier"],
        20,
        make_availability(),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    assert matching_qualifications(employee, shift) == []


def test_employee_can_reach_exact_max_hours():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        8,
        make_availability(),
        []
    )

    existing_shift = Shift(
        "Tuesday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    employee.assigned_shifts.append(existing_shift)

    new_shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    assert within_max_hours(employee, new_shift) is True


def test_employee_cannot_exceed_max_hours():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        7,
        make_availability(),
        []
    )

    existing_shift = Shift(
        "Tuesday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    employee.assigned_shifts.append(existing_shift)

    new_shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    assert within_max_hours(employee, new_shift) is False


def test_overlapping_shifts_conflict():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(),
        []
    )

    existing_shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    new_shift = Shift(
        "Monday",
        12,
        16,
        1,
        {"lifeguard": 1}
    )

    employee.assigned_shifts.append(existing_shift)

    assert has_shift_conflict(employee, new_shift) is True


def test_back_to_back_shifts_do_not_conflict():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(),
        []
    )

    existing_shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    new_shift = Shift(
        "Monday",
        13,
        17,
        1,
        {"lifeguard": 1}
    )

    employee.assigned_shifts.append(existing_shift)

    assert has_shift_conflict(employee, new_shift) is False


def test_same_times_on_different_days_do_not_conflict():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(),
        []
    )

    existing_shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    new_shift = Shift(
        "Tuesday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    employee.assigned_shifts.append(existing_shift)

    assert has_shift_conflict(employee, new_shift) is False


def test_employee_can_work_valid_shift():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(monday=[(9, 17)]),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    assert can_work_shift(employee, shift) is True


def test_employee_cannot_work_without_required_qualification():
    employee = Employee(
        "Connor",
        ["cashier"],
        20,
        make_availability(monday=[(9, 17)]),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    assert can_work_shift(employee, shift) is False


def test_employee_cannot_work_when_unavailable():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    assert can_work_shift(employee, shift) is False


def test_assign_valid_shift():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(monday=[(9, 17)]),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    result = assign_shift(employee, shift)

    assert result is True
    assert shift in employee.assigned_shifts
    assert employee.hours_worked() == 4


def test_invalid_shift_is_not_assigned():
    employee = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    result = assign_shift(employee, shift)

    assert result is False
    assert shift not in employee.assigned_shifts
    assert employee.hours_worked() == 0
    
def test_qualification_count_must_equal_required_workers():
    with pytest.raises(ValueError):
        Shift(
            "Monday",
            9,
            13,
            3,
            {
                "lifeguard": 2
            }
        )
