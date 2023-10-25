class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, my name is {self.name}."

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and I am {self.gender}."

class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and I am a {self.gender} student in the {self.course} course."

class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and I am a {self.gender} teacher. I teach {self.subject}."

# Create a Person, Student, and Teacher
person1 = Person("sri", 30, "female")
student1 = Student("gowthm", 20, "male", "Computer Science")
teacher1 = Teacher("ram", 40, "male", "Mathematics")

# Greet and introduce each of them
print(person1.greet())
print(person1.introduce())
print("\n" + student1.greet())
print(student1.introduce())
print("\n" + teacher1.greet())
print(teacher1.introduce())

