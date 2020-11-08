# Here we will find how to make basic calculator in python
# User are supposed to choose operations and enter data on which operations should be performed
# Description of line will be above the statement

print("Welcome to Calculator Program!")

# input function used to take input from user and shows string passed in the function on screen
op = input("Enter Operation to be performed")

# input function returns value of type string so we need to convert it into number using int function
num1=int(input("Enter first number"))

num2=int(input("Enter second number"))

# Now we will use simple if elif statement to print the result
# if operator(op) values matches to user input it will go into that if or elif section, if nothing matched it will show incorrect input by user


if op=='+':
    print("Output is: ", num1+num2)
elif op=='-':
    print("Output is: ", num1-num2)
elif op=='*':
    print("Output is: ", num1*num2)
elif op=='/':
    print("Output is: ", num1/num2)
elif op=='%':
    print("Output is: ", num1%num2)
else:
    print("Incorrect input by user")