# Given a “Matrix” string:

#     7ii
#     Tsx
#     h%?
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!


# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# A grid means that you could potentially break it into rows and columns,

# Matrix: A matrix is a two-dimensional array. It is a grid of numbers arranged in rows and columns.
# To reproduce the grid, the matrix should be a 2D list, not a string

# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix.

# Hints:
# Use
# ● lists for storing data
# ● Loops for going through the data
# ● if/else statements to check the data
# ● String for the output of the secret message

grid = [["7", "i", "i"], ["T", "s", "x"], ["h", "%", "?"], ["i", " ", "#"], ["s", "M", " "], ["$", "a", " "], ["#", "t", "%"], ["^", "r", "!"]]

def decipher() :
    selected_list = []
    for index in range(0, len(grid)) :
        row = grid[index]
        char = row[0]
        if char.isalpha() : 
            selected_list.append(char)
        else :
            selected_list.append(" ")

    for index in range(0, len(grid)) :
        row = grid[index]
        char = row[1]
        if char.isalpha() : 
            selected_list.append(char)
        else :
            selected_list.append(" ")

    for index in range(0, len(grid)) :
        row = grid[index]
        char = row[2]
        if char.isalpha() : 
            selected_list.append(char)
        else :
            selected_list.append(" ")
    joined_list = ''.join(selected_list)
    joined_list = joined_list.strip()
    print(joined_list)

decipher()