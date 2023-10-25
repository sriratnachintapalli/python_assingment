class Student:
    student_name = 'chintapalli sriratna'
    student_age= '22'
    student_grade = 'A' 
    def display():
        print(f'Student name: {Student.student_name}\nStudent age: {Student.student_age}\nStudent grade: {Student.student_grade}')
print("Original attributes and their values of the Student class:")
Student.display()
