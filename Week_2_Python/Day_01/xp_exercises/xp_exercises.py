# Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

#Solution EX 1:

print ("Hello world\n"*4)


# Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

#Solution EX 2:

result = (99 ** 3) * 8
print ('The result is: ', result)


# Exercise 3 : What Is The Output ?
# Instructions
# Predict the output of the following code snippets:
# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

#Solution EX 3:

5 < 3 - False
3 == 3 - True
3 == "3" - False
"3" > 3 - Incompatible
"Hello" == "hello" - False


# Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

#Solution EX 4:

computer_brand = "Lenovo"
print ('I have a ', computer_brand, ' computer.')


# Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

#Solution EX 5:

name = 'Natalia'
age = '44'
shoe_size = '38 EU'

info = "Hi, my name is " + name + ", I'm " + age + " years old, and my shoe size is " + shoe_size + "."
print (info)

# Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

#Solution EX 6:

a = input('Provide a random number \n')
b = input('Provide a random number \n')

if a > b :
    print ("Hello World")
else :
    print ("The condition is not met.")

# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

#Solution EX 7:

num = int (input("Provide a random number, and I'll check if it is odd or even: \n")) 
if (num % 2) == 0 :
    print ("The ", num, " number is even!")
else :
    print ("The ", num, " number is odd!")    



# Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

#Solution EX 8:

a = "Natalia"
b = str (input("What is your name?\n"))
if a == b :
    print("Hello, dear", b,"! I'm so glad that you are here,", b,"!")
else :
    print("You are not", a,"! Where is", a,"?!") 


# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

a = int (input("What is your height in inches?\n"))
b = a * 2.5
if b > 145 :
    print("Ok, you're tall enough to ride!")
else :
    print("Well, dear, you need to grow some more to ride.")