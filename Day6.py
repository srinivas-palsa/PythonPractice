##########DICTIONARY###########



# mydict = {
#     "name" : "Srinivas",
#     "age" : 21,
#     "isStudent" : True
# }
# mydict = {
#     "college" : "KPRIT" ##Here this dictionary is overwriting 1st dictionary as this dictionary is also declared as the 1st dictionary
# }
# print(mydict)


# mydict = {
#     "name" : "Srinivas",
#     "age" : 21,
#     "isStudent" : True
# }
# mydict["name"]= "Srinu"  ##Changing the value of name from Srinivas to Srinu
# print(mydict)


# mydict = {
#     "name" : "Srinivas",
#     "age" : 21,
#     "isStudent" : True
# }
# mydict["OK"] = "Nothing"  ## Adding a new key value but it is a wrong way to update (Still executes)
# print(mydict)


#
# mydict = {
#     "name" : "Srinivas",
#     "age" : 21,
#     "isStudent" : True
# }
# print(mydict.items())  ## Whole dictionary becomes as a list and each key and value returns in tuples
# print(mydict)



# mydict = {
#     "name" : "Srinivas",
#     "age" : 21,
#     "isStudent" : True
# }
# # print(mydict.get("name"))  ## Returns the name value only
# print(mydict.get("nam")) ##Key error but shows error only in this line as None and executes everything except this...
#                          ## if i dont us get method then whole code will stop executing(Shows Key error)
#
# print("CODE ENDS")



###PROBLEM 1###
#
# myDict = {
#     "table" : ["a piece of furniture", "list of facts and figures"], ##We can give multiple values to a key by using list
#     "cat" : "a small animal"
# }
# print(myDict)


###PROBLEM 2###
##OWN ANSWER###

# student_marks = {
#     "maths" : int(input("Enter maths marks: ")),
#     "science" : int(input("Enter science marks: ")),
#     "social" : int(input("Enter social marks: "))
# }
# print(student_marks)



# student_marks = {
#     "subject1" = int(input("Enter sub1 marks: ")),
#     "sub2" = int(input("Enter sub2 marks: ")),
#     "sub3" = int(input("Enter sub3 marks: "))


# student_marks = {}
# for i in range(1,4):
#     sub = input(f"Enter name of subject {i}: "),
#     marks = int(input(f"Enter marks of subject {sub}: "))
#     student_marks.update({sub:marks})
# print(student_marks)



###PROBLEM 3### key 1-10 and value square of number

# myDict = {}
# for i in range(1,11):
#     key = i
#     value = i*i
#     myDict.update({key:value})
# print(myDict)













#########FUNCTIONS###############

# def flenth(list):
#     print(len(list))
# flenth([1,23,4,5,67,8])
# flenth([1,23,4,5,67,8,34,4])


# def length(myList):
#     print(myList)
# length([234,556,6,7,7,8,8,])

# def elements(myList):
#     for i in myList:
#         print(i, end=" ")
# elements([1,2,3,4,5,6,7,9,10])



###UDS TO INR#####
def convert(usd):
    inr = int(input("Enter inr: "))
    total= inr*usd
    print(total)
convert(80)