# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers
# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False

# A Perfect Number N is defined as any positive integer where the sum of its divisors minus the number itself equals the number. 

user_number = int(input("Enter a positive number: "))
sum_div = 0
for number in range(1, user_number + 1) :
    if user_number % number == 0 :
        sum_div += number

if sum_div - user_number == user_number :
    print(f"Congrats, {user_number} is a perfect number!")
else :
    print(f"Sorry, {user_number} is not a perfect number!")