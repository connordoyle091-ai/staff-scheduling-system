from ortools.sat.python import cp_model
model = cp_model.CpModel()
def generate_schedule(employees, shifts):
    assigned = {}
    for x in range(len(employees)):
        for y in range(len(shifts)):
            assigned[x, y] = model.new_bool_var(f"Assigned_{x}_{y}")
    
