from student import Student
class Teacher (Student):
    def __init__(self,name,age,school,subject):
        super().__init__(name,age,school)
        self.subject = subject
    def display_info(self):
        print(f"Hi, i Am {self.name}, And I'm {self.age} Years Old, I Am In The {self.school} School and My Favourite Subject Is {self.subject}")