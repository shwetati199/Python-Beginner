#Here we will use If else
#Basically if else is used whenever there is condition to certain task like I will do homework if I will get chocolate else I will play

#Enter yes to give chocolate else no
getChoco=input("Please give me chocolate!")

if getChoco=="yes":
    print("I will do my homework")
else:
    print("I am going to play")

#We can also have multiple outcomes of certain condtions like If a number is equal to nnumber or less or greater than it
#Here we will comapre given number with 100

num=int(input("Please enter a number!"))

if num<100:
    print("Number is less than 100")
elif num==100:
    print("Number is equal to 100")
else:
    print("Number is larger than 100")