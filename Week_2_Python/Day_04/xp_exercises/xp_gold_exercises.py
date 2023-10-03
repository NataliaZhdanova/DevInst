# Exercise 1 : When Will I Retire ?
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).

def get_age(date_of_birth):
    import datetime
    cur_date = datetime.datetime.today()
    bd_date = datetime.datetime.strptime(date_of_birth, '%Y/%m/%d')
    age_years = (cur_date - bd_date) // 365
    age_str = str(age_years)
    age_years_int = int(age_str[:2])
    return age_years_int


# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.

def can_retire(gender, date_of_birth):
    age = get_age(date_of_birth)
    if gender == "n" :
        print("You're immortal, you'll work forever!")
    elif gender == "f" :
        if age >= 62 :
            print("You can retire!")
        else :
            print("You have to work a bit more before you can retire!")
    elif gender == "m" :
        if age >= 67:
            print("You can retire!")
        else :
            print("You have to work a bit more before you can retire!")


gender = input("What is your gender (enter 'm', 'f', or 'n')? ")
date_of_birth = input("What is your date of birth (use YYYY/MM/DD format)? ")
can_retire(gender, date_of_birth)


# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.


# Exercise 2 : Sum
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

def sum_int(string_num) :
    result = 0
    for mult in range(1, 5) :
        integer = int(string_num * mult)
        result += integer
    print(result)

string_num = input("Enter a positive number: ")
sum_int(string_num)

# Hint: treating our number as a int or a str at different points in our code may be helpful


# Exercise 3 : Double Dice
# Instructions
# Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.

def throw_dice():
    import random
    integer = random.randint(1, 7)
    return integer

# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the dice in total. In the example above, it should return 3.

def throw_until_doubles() :
    flag = True
    attempts = 0
    while flag == True :
        num_1 = throw_dice()
        num_2 = throw_dice()
        attempts += 1
        if num_1 == num_2 :
            flag = False
    return attempts

# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls 
# (in other words, how many throws it took until doubles were thrown, each time) in a collection. 
# (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).

def main() : 
    throw = 0
    attempts_list = []
    while throw <= 100 :
        attempts = throw_until_doubles()
        throw += 1
        attempts_list.append(attempts)
    print(f"Total throws: {sum(attempts_list)}")
    print(f"Average throws to reach doubles: {round(sum(attempts_list) / len(attempts_list), 2)}")

main()


# After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
# Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
# For example:

# If the results of the throws were as follows (your code would do 100 doubles, not just 3):
# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)

# Then my output would show something like this:
# Total throws: 8
# Average throws to reach doubles: 2.67.

