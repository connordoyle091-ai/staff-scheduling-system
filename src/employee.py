class Employee:
    def __init__(self,name, qualifications, max_hours, availability):
        self.name = name
        self.qualifications = qualifications
        self.max_hours = max_hours
        self.availability = availability
def organize_employees(employee_info):
    employees_organized = {}
    for i, employee_instance,  in enumerate(employee_info):
        employees_organized[f"Employee {i + 1}"] = {"name": employee_instance.name,
                                                "qualifications": employee_instance.qualifications,
                                                "max hours": employee_instance.max_hours,
                                                "availability": employee_instance.availability}
    return employees_organized
