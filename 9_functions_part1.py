#Function- function is group of related statements which performs some task
#These statements can be called multiple time without writing all code by just calling the name of function
#Functions are excecuted only when they are called
#It reduces repetition of code and enhance readability of program

#Here we are defining function1
#This is a simple function which only have one print statement
def function1():
    print("I am inside function1")

#Calling a function
function1()

#Arguments and return value- we can also pass arguments and return value from it
#Arguments are the values which are passed to function while calling it

def summ(num1, num2):
    return num1+num2

num3=summ(5,  7)
#Here num1 and num2 will store the value of 5 and 7 respectively
print(f"Summation is: {num3}")

#num4=summ(1, 2, 3)
#Above line will give error because we have only declared two variables for receving values inside function and we are passing 3 values
#So the number of arguments must be same for function and its calling statements

#To overcome this problem we can use *args
#*args is used when we are unaware about number of arguments that need to be passed


def summnew(*args):
    total = 0
    for i in args:
        total+=i

    return total

print("Calling summnew(1, 2, 3): ")
print(summnew(1, 2, 3))

print("Calling summnew(5, 6, 7, 8): ")
print(summnew(5, 6, 7, 8))

#So here we don't need to change in number of arguments and we can as many arguments as we want
#Keyword Arguments-its more like dictionary, we can pass values with some specified names for it.

def showdict(**kwargs):
    print(kwargs["name"])

showdict(name="Shweta", age=22)


#Default arguments- we can set the by default value of argument

def printmessage(name, msg="Welcome!"):
    print(f"Hii {name}, {msg}")

printmessage("Riya", "Thank you!")

#Here when we dont pass value for msg it will take it as Welcome! by default.
printmessage("Shweta")