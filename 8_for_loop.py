#For loop- it is used mostly to loop over a sequence
#It works more like iterator method

namelist=["Shweta","Riya", "Priya", "Supriya"]
print("Namelist: ")
for name in namelist:
    print(name)

#For loop don't require indexing variable to get set.
#For loop over String
print("For loop for string")
for i in "Shweta":
    print(i)

#Break Statemnets- this is used to break the innermost loop whenever the given condition is true

evennums=[2, 4, 6, 8, 9, 10, 12, 13, 15, 16]

#Ex- we want to only print even numbers from this list and if odd numbers encounter more than two time we have to Print that
# "2 Odds found" and need to break the loop
#Here we will use continue and break to do the given task.

oddcount=0

for i in evennums:
    if i%2!=0:
        oddcount+=1
        if(oddcount==2):
            print("2 Odds found")
            break
        continue
    print(i)

#Nested for loops: we can have loop inside loop and this is called as nested for loop
# For example- if we want to print pattern we can use nested loop

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()
