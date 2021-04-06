#Class methods- class method changes the property of class or class variables
#We have to @classmethod decorator to define class method
#It receives cls as implicit first argument, just like instance method receives self
#Using cls we can access class variable
#We don't need to create instance of class to use class method

class Student:

    course="CSE"

    @classmethod
    def change_course(cls, newcourse):
        print(f"Class name is: {cls}")
        cls.course=newcourse

print(f"Course Name: {Student.course}")

#We can change class variable by using class method
Student.change_course("IT")
print(f"New Course Name: {Student.course}")
