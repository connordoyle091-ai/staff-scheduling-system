class Shift:
    def __init__(self, day, start_time, end_time, required_workers, required_qualifications):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.required_workers = required_workers
        self.required_qualifications = required_qualifications
def organize_shifts(shifts):
    organized_shifts = {"monday": [],
                        "tuesday": [],
                        "wednesday": [],
                        "thursday": [],
                        "friday": [],
                        "saturday": [],
                        "sunday": []}
    for shift in shifts:
        required_personnel = {}
        for x in shift.required_qualifications:
            if x not in required_personnel:
                required_personnel[x] = 1
            else:
                required_personnel[x] += 1
        organized_shifts[shift.day.lower()].append({"start time": shift.start_time, "end time": shift.end_time, "required workers": shift.required_workers, "required personnel": required_personnel})
    return organized_shifts

    
                        
