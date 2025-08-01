#Pattern 1

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",  end=" ")
#     print()


#pattern 2

# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

#########   OR   ###########

# n=int(input("Enter number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()



# pattern 3

# n=int(input("Enter num of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()



# pattern 4

# n=int(input("Enter num of rows: "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()


# pattern 5
n=int(input("Enter no of rows: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

