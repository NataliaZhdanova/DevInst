# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****

matrix = [
    (0, 0, 1, 0, 0),
    (0, 1, 1, 1, 0),
    (1, 1, 1, 1, 1)
]

for index in range(0, len(matrix)) :
    for num_ind in range(0, len(matrix[index])) :
        if matrix[index][num_ind] == 0:
            print(" ",end = "")
        else :
            print("*", end = "")
    print("")

# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****

matrix = [
    (0, 0, 0, 0, 1),
    (0, 0, 0, 1, 1),
    (0, 0, 1, 1, 1),
    (0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1)
]

for index in range(0, len(matrix)) :
    for num_ind in range(0, len(matrix[index])) :
        if matrix[index][num_ind] == 0:
            print(" ",end = "")
        else :
            print("*", end = "")
    print("")


# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *
matrix = [
    (1, 0, 0, 0, 0),
    (1, 1, 0, 0, 0),
    (1, 1, 1, 0, 0),
    (1, 1, 1, 1, 0),
    (1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1),
    (0, 1, 1, 1, 1),
    (0, 0, 1, 1, 1),
    (0, 0, 0, 1, 1),
    (0, 0, 0, 0, 1)
]

for index in range(0, len(matrix)) :
    for num_ind in range(0, len(matrix[index])) :
        if matrix[index][num_ind] == 0:
            print(" ",end = "")
        else :
            print("*", end = "")
    print("")

# Exercise 2
# Instructions
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233]                                             # assigning a value to the list variable
for i in range(len(my_list) - 1):                                           # creating a sequence of values to iterate upon (i in range(0, 4))
    minimum = i                                                             # assigning a value from the iterable to the variable (0)
    for j in range( i + 1, len(my_list)):                                   # creating a sequence of values to iterate upon (j in range(1, 5))
        if(my_list[j] < my_list[minimum]):                                  # comparing the next list value with the "minimum" value 
            minimum = j                                                     # if the next list value is smaller than the list value with [minimum] index, change the "minimum" value to the index of next list value
            if(minimum != i):                                               # if the new "minimum" is not equal to the old "minimum"
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # switch places of list values with old and new "minimum" indexes
print(my_list)

