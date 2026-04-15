#read the data and store it in a 2D list or dictionary
#use read function to read the txt file and convert the required dat according.
def read():
    students = []
    with open("students.txt", "r") as file:
        for line in file:
            student_data = line.strip().split(", ")
            students.append(student_data)
    return students
