class Shift:
    def __init__(self, day, start_time, end_time, required_workers,):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.required_workers = required_workers
def organize_shifts(shifts):
    organized_shifts = {"monday": [],
                        "tuesday": [],
                        "wednesday": [],
                        "thursday": [],
                        "friday": [],
                        "saturday": [],
                        "sunday": []}
    for shift in shifts:
        organized_shifts[shift.day.lower()].append({"start time": shift.start_time, "end time": shift.end_time, "required workers": shift.required_workers})
    return organized_shifts
    
                        
