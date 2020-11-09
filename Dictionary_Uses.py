# Dictionary - is basically a key-value pair, indexed and changeable(mutable) (i.e. {key: value})
# Keys are unique within the dictionary

mydict1={'animal':'tiger', 'car':'maruti', 'car': 'maruti'}
print(mydict1)

# We can access particular element by its key
print(mydict1['animal'])

# Insert in dictionary
mydict1['book']='python'
print(mydict1)

# Deletion
del mydict1['book']
print(mydict1)

# Accessing dictionary within dictionary
mydict2={'food':'chole-bhature', 'sweets':{'first':'pepsi', 'second': 'halwa', 'third':'ice-cream'}}
print(mydict2['sweets']['third'])

del mydict2['sweets']['third']
print(mydict2)

# Creating copy of dictionary

copydict = mydict2.copy()
print(copydict)

# Even if you delete original dictionary then also new dictionary will be there
del mydict2
print(copydict)

# Returns all keys
print(copydict.keys())

# Returns all items
print(copydict.items())
