# tests/test_dashboard.py
from pact import Consumer, Provider

# Define Consumer and Provider
consumer = Consumer("Dashboard")
provider = Provider("Employee")

# Define Pact for each API endpoint
with consumer:
    with provider:
        # Define contract for creating employee
        (consumer
         .upon_receiving("A request to create an employee")
         .with_request(method="POST", path="/employee/create")
         .will_respond_with(200, body={"message": "Employee created successfully"}))

        # Define contract for updating employee
        (consumer
         .upon_receiving("A request to update an employee")
         .with_request(method="PUT", path="/employee/update/123")
         .will_respond_with(200, body={"message": "Employee updated successfully"}))

        # Define contract for getting employee
        (consumer
         .upon_receiving("A request to get an employee")
         .with_request(method="GET", path="/employee/123")
         .will_respond_with(200, body={"employee_id": "123", "name": "John Doe"}))

# Verify that Consumer contract is a subset of Provider contract
# Run this test before any changes to the Provider APIs to ensure backward compatibility
(Consumer("Dashboard")
 .has_pact_with(Provider("Employee"))
 .verify())
