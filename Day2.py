#SUM OF TWO NUMBERS
from operator import countOf

# a= int(input("Enter a number: "))
# b= int(input("Enter another number: "))
# print(f"Sum of {a} and {b} is {a+b}")



#Write a program to input a side & print its area

# side= int(input("Enter the side: "))
# area = side*side
# print("Area = ",area)


##Average of 2 floating point numbers

# x = float(input("Enter a decimal number: "))
# y = float(input("Enter another decimal number: "))
# average= (x+y)/2
# print(f"Average is:{average}")


###Finding Greater number (Bool)

# a=int(input("Give a number: "))
# b=int(input("Give another number: "))
# print(a>b)


##printing name and its length & finding and counting a letter

# name= input("Enter your name: ")
# print(name)
# print("length of your name is: ",len(name))
# print("First occurance of a is: ",name.find("a"))
# print("a is repeating: ",name.count("a"),"times")

# # x= input("name: ")
# # counting = input("Alphabet you want to count: ")
# # print(x.count(counting))


###First and last letters are same or not

# name=input("Enter your name: ").lower()
# x=name[0]
# y=name[-1]
# print(x is y) # 'is' can be used in place of ==


##PALINDROME

# originalWord=input("Enter a name: ")
# reversedWord=name[::-1]
# print(originalWord==reversedWord)


##CONDITIONAL STATEMENT
## odd , even

# num= int(input("Enter a number: "))
# if(num%2==0):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


##Username format checker

# username= input("Enter the username: ")
# if(" " in username):
#     print("username is invalid")
# elif(len(username)>4):7
#     print("username is accepted")
# else:
#     print("username is too short")


###PERSONAL GA CHESHNA

# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))
# x=a,b,c
# max=0
# for i in x:
#     if max<i:
#         max=i
# print(max)

# a=int(input("Enter a number: "))
# b=int(input("Enter b number: "))
# c=int(input("Enter c number: "))
# if (a>b and a>c):
#     print(f"{a} is big")
# elif (b>a and b>c):
#     print(f"{b} is big")
# else:
#     print(f"{c} is big")