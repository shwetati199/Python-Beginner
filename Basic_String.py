# In this script, I will be showing how to create string, display, slicing and some method of string

# Create string

# Create string, You can also take input from user with help of input function
mystring="Hello, Shweta!"

# Displaying String
print(mystring)

# Slicing of String--> We can assume string as a characters array and by assuming so we can give index no from where we want to fetc to uptill where.
# This is a generic format of slicing mystring[start:end+1:skip]
# Note- mystring will print same thing as mystring[0:len(mystring)+1] because its the default value.

print(mystring[0:len(mystring)+1])

# We can also pass the character to skip as mystring[start:end+1:skip]
print(mystring[2:10:2])


# Negative slicing--> In this we take last character as -1 and from there we move on with negative increment(i.e -1, -2, -3, -4)

print(mystring[-7:-1])
print(mystring[-7:-1:2])

# Some important functions of string

# It returns true if string contains only alphabets (Note: inclusion of special characters returns false)
print(mystring.isalpha())

# It return the count of particular character
print(mystring.count('l'))

# It replace the string by new string
print(mystring.replace("Shweta", "Neha"))
