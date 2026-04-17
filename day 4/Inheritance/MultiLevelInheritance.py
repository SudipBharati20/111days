#3. Multilevel Inheritance
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic

    def display(self):
        super().display()
        print(f"Research Topic: {self.research_topic}")
grad_student = GraduateStudent("David", 25, "S67890", "Artificial Intelligence")
grad_student.display()