#create a txt file and write the following data
#The txt file contains students id,name and marks of a  module
#ID001, hero, 85
#ID002, zero, 78
#ID003, gunda, 92

with open("students.txt", "w") as file:
    file.write("ID001, hero, 85\n")
    file.write("ID002, zero, 78\n")
    file.write("ID003, gunda, 92\n")