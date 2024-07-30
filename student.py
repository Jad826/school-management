from person import Person
class Student (Person):
    def __init__(self,name, age,school):
        super().__init__(name, age)
        self.school = school
    def display_info(self):
        print(f"name: {self.name}age: {self.age} school : {self.school}")