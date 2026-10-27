class Employee:
    def __init__(self,name, qualifications, max_hours):
        self.name = name
        self.qualifications = qualifications
        self.max_hours = max_hours
def organize_employees(employee_info, start=1):
    employees_organized = {}
    for i, employee_instance,  in enumerate(employee_info):
        if employee_instance not in employees_organized:
            employees_organized[f"Employee {i + 1}"] = {"name": employee_instance.name,
                                                    "qualifications": employee_instance.qualifications,
                                                    "max hours": employee_instance.max_hours}
    return employees_organized
