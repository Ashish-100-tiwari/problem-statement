# employee_service/main.py
from fastapi import FastAPI, HTTPException

app_employee = FastAPI()

# Employee database (mock)
employees_db = {}

@app_employee.post("/employee/create")
def create_employee(employee_id: str, name: str):
    if employee_id in employees_db:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    employees_db[employee_id] = {"name": name}
    return {"message": "Employee created successfully"}

@app_employee.put("/employee/update/{employee_id}")
def update_employee(employee_id: str, name: str):
    if employee_id not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found")
    employees_db[employee_id]["name"] = name
    return {"message": "Employee updated successfully"}

@app_employee.get("/employee/{employee_id}")
def get_employee(employee_id: str):
    if employee_id not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees_db[employee_id]
