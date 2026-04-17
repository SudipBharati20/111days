#2. Multiple Inheritance
class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def display_employee_id(self):
        print(f"Employee ID: {self.employee_id}")
class TeachingAssistant(Student, Employee):
    def __init__(self, name, age, student_id, employee_id):
        Student.__init__(self, name, age, student_id)
        Employee.__init__(self, employee_id)

    def display(self):
        Student.display(self)
        Employee.display_employee_id(self)
ta = TeachingAssistant("Charlie", 22, "S54321", "E98765")
ta.display()