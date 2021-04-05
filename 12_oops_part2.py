#Class variable vs instance variable
#Class variable - they are property of class means they are common for all objects
#Instance variable- they are property of objects, unique for each objects

class Student:

    course="IT"

    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno

#Here course will be common for all students so we can make them as class variable
#But name and rollno will be unique for all student, so it will be instance variable

Shweta=Student("Shweta", 1)
Riya=Student("Riya",2)

print(Shweta.name)
print(Shweta.rollno)
print(Shweta.course)

#Now if we will change course by IT to CSE from Shweta object then it will not be changed by other objects
Shweta.course="CSE"

print(f"Shweta's course:{Shweta.course}")
print(f"Riya's course:{Riya.course}")

#So any changes done by objects will not reflect in class variable for other objects
#To change the course for all objects we can change it by using class name

Student.course="Mech"

print(f"Shweta's course:{Shweta.course}")
print(f"Riya's course:{Riya.course}")