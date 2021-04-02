#Loop- repetition of some statements for particular condtion and time
#While loop- here we will use while keyword, this loop should continue till condtion inside while loop is true

print("While example")
i=1

while i<=5:
    print(i)
    i+=1


#Continue statement- using this we can skip statements written after continue for particular value without breaking loop,
#so basically it will go back again on the starting point of loop
print("Continue example")
i=10

while i<=50:

    i+=10
    if i==30:
         continue
    print(i)

#Else - we can also use else with while loop, it will execute once the condition inside while loop becomes false

i=1

while i<5:
    print(i)
    i+=1

else:
    print(f"I is now: {i}")