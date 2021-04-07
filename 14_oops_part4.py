#Static Methods- they are used to create utility
#It is also bounded to class rather than objects but it can not access or modify class state
#To use static method we have to use @staticmethod decorator

class Student:

    course="IT"

    @staticmethod
    def print_details():
        print("Hii, I am a static methods")

Student.print_details()