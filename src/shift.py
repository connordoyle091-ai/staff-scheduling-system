class Shift:
    def __init__(self, day, start_time, end_time, required_workers, required_qualifications):
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

    
                        
