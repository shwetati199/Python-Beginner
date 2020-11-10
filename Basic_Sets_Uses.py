# Sets in python represents mathematical notion of sets
# Sets are unordered so we can't access item with index number
# We can add or remove item but can't change item so item in sets are immutable but set is mutable.
# Repetition of elements are not allowed.

# Creating a set

# First way- by using set function and adding elements with help of add function of set or you can directly pass list of elements into set function.
myset1= set([0, 56, 79, 22])
myset1.add(1)
myset1.add(2)
myset1.add(3)
print(myset1)

# Second way- by using curly braces -> {} .
myset2= {3, 4, 5}
print(myset2)

# Note - If you want to create an empty set you need to use set(), if you will use {} it will create an empty dictionary since they both uses {}.
# By using add function we can add one argument at a time but if you want to add multiple elements you can use update function

myset1.update([5, 6, 7, 9], [6, 99, 100])
print(myset1)

# Union
unionset=myset1.union(myset2)
print(unionset)

# Intersection
interset=myset1.intersection(myset2)
print(interset)

# Removing item
myset1.remove(99)
print(myset1)