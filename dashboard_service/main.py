from fastapi import FastAPI, HTTPException
import requests

app_dashboard = FastAPI()

employee_service_url = "http://employee-service:8000"  # Assuming the URL where the Employee service is deployed

@app_dashboard.get("/dashboard/employee/{employee_id}")
def get_employee_from_dashboard(employee_id: str):
    response = requests.get(f"{employee_service_url}/employee/{employee_id}")
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Employee not found")
    elif response.status_code != 200:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return response.json()
