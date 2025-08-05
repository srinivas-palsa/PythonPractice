### wrong permutation logic
from dataclasses import field

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# fact(int(input("Enter a factorial number: ")))
#
# def permutation(n,r):
#     return fact(n) // fact(n-r)
# permutation(5,2)





##RECURSION####

# def natural_nums_Sum(n):
#     if(n==1):
#         return 1
#     else:
#         return n + natural_nums_Sum(n-1)
#
# n = 5
# result = natural_nums_Sum(n)
# print(result)




########FILE HANDLING######

##Reading a file
# fileName = open("demo.txt", "r")
# data = fileName.read()
# print(data)
#
#
# ###Readind to specific characters
# file = open("demo.txt","r")
# data1 = file.read(10)
# print(data1)


#### Writing the data (Over wrights existing file text)

# file = open("demo.txt","w")
# file.write("This is Srinivas")  ### Over wrights
#
# file = open("demo.txt","r")
# print(file.read())
# file.close()



### Using append(a) to overcome overwriting of w


# file = open("demo.txt","a")
# file.write("I am from KPRIT")
# file = open("demo.txt", "r")
# print(file.read())





# import os

# os.remove("demo.txt")

# file = open("demo.txt","w")
# file.write("My name is Srinivas")
# file = open("demo.txt","r")
# print(file.read())

# os.rename("demo.txt","test.txt")




#####Problem

# file_name = open("practice.txt","w")
# file_name.write("Hi everyone.\nWe are learning File Handling I/O\nusing python\nI like programming in Python")
# file_name.close()
#
# file_name = open("practice.txt","r")
# data = file_name.read()
# replacing = data.replace("Python","JavaScript")
# print(replacing)
#
# file_name = open("practice.txt","w")
# file_name.write(replacing)
# file_name.close()
