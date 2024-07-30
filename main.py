import person
from teacher import Teacher
name = input("Enter The Name Of The Student : ")
age = int(input("Enter The Age Of The Studet : "))
school = input("Enter The School Of The Student : ")
subject = input("Enter The Favourite Subject Of The Student : ")
t = Teacher(name, age, school,subject)
t.display_info()