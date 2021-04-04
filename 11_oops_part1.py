#OOPS- Object Oriented Programming is a style of programming based on concepts of classes and objects
#In oops we solve the problems by using object.
#Object- Object is a real entity which have two properties 1- attributes 2-Behaviour
#Class- it's a logical entity or we can say blueprint for class or collection of objects.
#Example for class- A class name Dog, it presents all categories of dogs
#Example for object- An object of class Dog named Baxter(dog name) which have all attributes and behaviour(Methods) of Dog class.
#We can also say that object is specific and class is general category.

#Defintion of class

print("---Class Dog---")
class Dog:
    pass

#Creating object
Baxter=Dog()

#We can also set name of dog or other properties
Baxter.name="Baxter"
Baxter.eye_color="brown"
Baxter.weight=20

#Printing the details of Baxter

print(f"Name: {Baxter.name}")
print(f"Eye Color: {Baxter.eye_color}")
print(f"Weight: {Baxter.weight}")

#Note- here attributes of Baxter such as name,eye_color, weight are the properties of baxter itself because it's not defiend inside class
#If we want to create attributes of class then we can also do this with help of init method
#We can also creates methods as per our requirement such as showdetails() for printing details of class

print("---Class Dog1---")
class Dog1:

    #init is constructor of class, it is called by default when object is created
    #self is default parameter of this function which refers to the paticular object which is calling it.

    def __init__(self, name, eye_color, weight):
        self.name=name
        self.eye_color=eye_color
        self.weight=weight

    #This function will print attributes of class
    #Functions are also called as behaviour of class

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Eye Color: {self.eye_color}")
        print(f"Weight: {self.weight}")

#Here init function will be called automatically
Ace = Dog1("Ace", "Black", 15)

#Calling show_details function
Ace.show_details()