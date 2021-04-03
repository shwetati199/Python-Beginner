#Here we will see anonymous function and some built-in function
#Anonymous Function- They don't have names that's why they are called as anonymous, also known as lambda function
#They are basically one line function or we can say that they can solve only one line expression

def addition(a, b):
    return a+b
#Here addition is simple function which just takes two inputs, sums them and returns the result.

add = lambda a, b:a+b

value1 = addition(3, 4)
value2 = add(3, 4)

print(f"value1: {value1}")
print(f"value2: {value2}")

#Here addition and add both are giving same value on same input but add is lambda function
#We can also use lambda function as below
value3 =(lambda a, b:a-b)(5, 1)
print(f"value3: {value3}")

#Map - it basically maps a function for all given iterable
#So basically one function is applied for list of inputs with help of map function

mylist=[1, 2, 3, 4, 5]

def add_one(val):
    return val+1
#Here if we want to execute showme for given list of names then we can do this by:

for i in mylist:
    print(add_one(i))

#We can do the same thing by using map function

print("Using map function")
x=map(add_one, mylist)

#Note- map function returns address, so we need to convert it into list
print(list(x))

#Filter- it filters list of elements with help of some function, if function returns true for given element then it will be in output else not.

def check_even(val):
    return val%2==0

newlist=filter(check_even, mylist)

#Note- filter function also return address so we need to convert it into list.

print(f"Original List: {mylist}")
print("Even from List:", end=" ")
print(list(newlist))

#Reduce- it reduces an iterable to single value, it uses mathematical concept of folding or reduction
#So it converts list of elements into single value by doing some operations on it.
#For using reduce we need to import it from functools

from functools import reduce

def sum(a, b):
    return a+b
total=reduce(sum, [1, 2, 3])

print(total)