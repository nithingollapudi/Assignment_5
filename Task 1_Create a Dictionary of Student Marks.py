student_marks = {'Rahul':90,'Bobby':80,'Rithvik':75,'Satwik':95,'Venkat':0}
student_name= (input("Enter the student's name:"))
if student_name in student_marks:
    print(f"{student_name} marks:{student_marks[student_name]}")
else:
    print("student not found")