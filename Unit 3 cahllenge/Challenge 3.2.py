class Student:
  def __init__(self, name, roll_no, cgpa):
     self.name = name
     self.roll_no = roll_no
     self.cgpa = cgpa
    
def sort_students(student_list):
    sorted_students=sorted(student_list,                       key=lambda                          student:                           student.cgpa,                        reverse=True)

    return sorted_students

students=[Student("student1", "001", 7.0),
         Student("student2", "002", 8.0), 
         Student("student3", "003", 6.0),
         Student("student4", "004", 9.0),
         Student("student5", "005", 9.8),
         ]

sorted_students=sort_students(students)

for student in sorted_students:
  print("Name:{} Roll_no:{} CGPA:{}".format(student.name,student.roll_no,student.cgpa))