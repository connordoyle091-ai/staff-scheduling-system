class Shift:
    valid_days = {
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    }

    def __init__(
        self,
        day,
        start_time,
        end_time,
        required_workers,
        required_qualifications
    ):
        if day.lower() not in self.valid_days:
            raise ValueError("Invalid shift day")

        if end_time <= start_time:
            raise ValueError("Shift end time must be after start time")
        if sum(required_qualifications.values()) != required_workers:
            raise ValueError("Required number of qualifications must be equal to the number of workers")

        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.required_workers = required_workers
        self.required_qualifications = required_qualifications
    def duration(self):
        return self.end_time - self.start_time
def organize_shifts(shifts):
    organized_shifts = {"monday": [],
                        "tuesday": [],
                        "wednesday": [],
                        "thursday": [],
                        "friday": [],
                        "saturday": [],
                        "sunday": []}
    for shift in shifts:
        organized_shifts[shift.day.lower()].append({"start time": shift.start_time, "end time": shift.end_time, "required workers": shift.required_workers, "required personnel": shift.required_qualifications})
    return organized_shifts

    
                        
