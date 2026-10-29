from ortools.sat.python import cp_model

def generate_schedule(employees, shifts):
    model = cp_model.CpModel()
    assigned = {}
    for x in range(len(employees)):
        for y in range(len(shifts)):
            assigned[x, y] = model.new_bool_var(f"Assigned_{x}_{y}")
    for y in range(len(shifts)):
        model.add(sum(assigned[x,y] for x in range(len(employees))) == shifts[y].required_workers)
