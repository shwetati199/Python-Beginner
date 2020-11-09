# Date : 09-11-2020
# Here we will create list of subjects
# List is collection of items which is ordered and changeable(Also called mutable)
# (Note- in python index of list starts from 0 rather than 1)
subject = ['Python', 'Java', 'PHP', 'Javascript', 'Node Js']

# Printing list
print(subject)

# Slicing in list
print(subject[1:4])
print(subject[-5:-1])

# Important functions

# reverse function reverses the original list instead of creating new one

subject.reverse()
print(subject)

# Append function use to add data at end
subject.append('HTML')
print(subject)

# pop - it removes one item from end also return same
val= subject.pop()
print(val)
print(subject)

# remove - it remove item with the given name
subject.remove('PHP')
print(subject)


# Tuples - collection of items which are not changeable(also called immutable)
mytup=(15, 11, 16, 2, 4, 5, 20, 50)

print(mytup)

#Slicing
print(mytup[0:5])
print(mytup[0:len(mytup):2])
print(mytup[-5:-1])

# Create tuple with one item


# If you have only one element in tuple and you are writing code like below then it will be assigned as number not tuple
mytup1=(1)
print(type(mytup1))
print(mytup1)

# You have to add an extra comma at end
mytup2=(1, )
print(type(mytup2))
print(mytup2)

# You can't delete item from tuple but you can delete whole tuple itself
del mytup2

# Below line will give error
# print(mytup2)
print(max(mytup))

# Conversion of list into tuple
numlist=[1, 2, 3]
numtuple=tuple(numlist)
print(numlist)
print(numtuple)

# Conversion of tuple into list
mytup3=("Hi", "how", "are", "you", " ?")
mylist=list(mytup3)
print(mytup3)
print(mylist)