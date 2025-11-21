def get_employee_info(name, emp_id, department, salary):
    """
    Returns a formatted string containing employee information.
    """
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
if __name__ == "__main__":
    # Example usage
    print(get_employee_info("Harsha", "E101", "IT", 55000))
