#3. Create a class ‘Employee’ and add salary and increment properties to it.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_increment(self, increment):
        self.salary += increment

    def display(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")
employee = Employee("John Doe", 50000)
employee.display()
employee.apply_increment(5000)
employee.display()