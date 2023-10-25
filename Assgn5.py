class Employee:
    # Class variable to keep track of all employees and their total salary
    all_employees = []
    total_salary = 0

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        # Add the employee to the list of all employees
        Employee.all_employees.append(self)
        # Update the total salary of all employees
        Employee.total_salary += salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            # Update the total salary for all employees
            Employee.total_salary += (new_salary - self.salary)
            self.salary = new_salary
        else:
            print("Invalid salary value. Salary not updated.")

    @classmethod
    def average_salary(cls):
        if len(cls.all_employees) > 0:
            return cls.total_salary / len(cls.all_employees)
        else:
            return 0

# Create some employee instances
employee1 = Employee("Sri", 101, 50000)
employee2 = Employee("Jhanu", 102, 60000)
employee3 = Employee("Riya", 103, 75000)

# Get and set salaries
print("Employee 1's current salary:", employee1.get_salary())
employee1.set_salary(55000)
print("Employee 1's updated salary:", employee1.get_salary())

# Calculate the average salary of all employees
average_salary = Employee.average_salary()
print("Average Salary of All Employees:", average_salary)

