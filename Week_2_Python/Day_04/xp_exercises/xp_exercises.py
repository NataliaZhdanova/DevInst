# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

#Solution EX 1:

def display_message() :
    print("In this course, we're learning full stack coding!")


display_message()

# Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

#Solution EX 2:



def favorite_book() :
    book_title = input("What is the title of your favorite book? \n")
    print(f"Your favorite book is '{book_title}'!")

favorite_book()

# or:

book_title = input("What is the title of your favorite book? \n")

def favorite_book(title) :
    print(f"Your favorite book is '{title}'!")

favorite_book(book_title)


# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

#Solution EX 3:

def describe_city(city_name, country = "Israel") :
    print(f"{city_name} is in {country}!")

describe_city("Moscow", "Russia")
describe_city("Moscow")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

#Solution EX 4:

number = int(input("Provide a number from the range 1 - 100: \n"))

def random_num() :
    number = int(input("Provide a number from the range 1 - 100: \n"))
    import random
    r_num = random.randint(1,100)
    if number == r_num :
        print("Success!")
    else :
        print(f"Failure! Your number is {number} and my number is {r_num}!")     

random_num()

# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

#Solution EX 5:

def make_shirt() :
    size = input("What is the size of the shirt? \n")
    message = input("What message should we print on the shirt? \n")
    print(f"Ok! The size of the shirt is {size} and the message to be printed is '{message}'!")

make_shirt()

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.

def make_shirt(size = "L", message = "I love Python!") :
    size_question = input("Would you like to provide the shirt size? \n")
    if size_question.lower() == "yes" :
        size = input("What is the size of the shirt? \n")
        message_question = input("Would you like to provide the message? \n")
        if message_question.lower() == "yes" :
            message = input("What message should we print on the shirt? \n")
            print(f"Ok! The size of the shirt is {size} and the message to be printed is '{message}'!")
        else :
            print(f"Ok! The size of the shirt is {size} and the message to be printed is '{message}'!")
    else :
        message_question = input("Would you like to provide the message? \n")
        if message_question.lower() == "yes" :
            message = input("What message should we print on the shirt? \n")
            print(f"Ok! The size of the shirt is {size} and the message to be printed is '{message}'!")
        else :
            print(f"Ok! The size of the shirt is {size} and the message to be printed is '{message}'!")


make_shirt()

# Make a large shirt with the default message

make_shirt()

# Make medium shirt with the default message

make_shirt("M")

# Make a shirt of any size with a different message.

make_shirt("S", "I love JS!")

# Bonus: Call the function make_shirt() using keyword arguments.

make_shirt(message = "I love JS!", size = "M")

# Exercise 6 : Magicians
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

#Solution EX 6:

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians() :
    for name in magician_names :
        print(name)

def make_great() :
    for index in range(0,3) :
        magician_names[index] = "The great " + magician_names[index]

make_great()
show_magicians()


# Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

#Solution EX 7:

def get_random_temp() :
    import random
    r_grad = random.randint(-10,40)
    return r_grad
    
def main() :
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0 :
        print("Brrr, that's freezing! Wear some extra layers today!")
    elif temp in range(0, 16) :
        print("Quite chilly! Don't forget your coat!")
    elif temp in range(16, 24) :
        print("Just perfect!")
    elif temp in range(24, 33) :
        print("Pretty hot today!")
    elif temp in range(33, 41) :
        print("Welcome to Hell, dear!")

main()

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

def get_random_temp(season) :
    import random
    if season == "winter":
        r_grad = random.randint(-10,17)
    elif season == "spring":
        r_grad = random.randint(17,33)
    elif season == "summer":
        r_grad = random.randint(23,43)
    elif season == "autumn":
        r_grad = random.randint(15,33)
    return r_grad

def main() :
    season = input("What season is outside?\n")
    season = season.lower()
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0 :
        print("Brrr, that's freezing! Wear some extra layers today!")
    elif temp in range(0, 16) :
        print("Quite chilly! Don't forget your coat!")
    elif temp in range(16, 24) :
        print("Just perfect!")
    elif temp in range(24, 33) :
        print("Pretty hot today!")
    elif temp in range(33, 43) :
        print("Welcome to Hell, dear!")

main()


# Bonus: Give the temperature as a floating-point number instead of an integer.

def get_random_temp(season) :
    import random
    if season == "winter":
        r_grad = round(random.uniform(-10,17), 2)
    elif season == "spring":
        r_grad = round(random.uniform(17,33), 2)
    elif season == "summer":
        r_grad = round(random.uniform(23,43), 2)
    elif season == "autumn":
        r_grad = round(random.uniform(15,33), 2)
    return r_grad

def main() :
    season = input("What season is outside?\n")
    season = season.lower()
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    temp = int(temp)
    if temp < 0 :
        print("Brrr, that's freezing! Wear some extra layers today!")
    elif temp in range(0, 16) :
        print("Quite chilly! Don't forget your coat!")
    elif temp in range(16, 24) :
        print("Just perfect!")
    elif temp in range(24, 33) :
        print("Pretty hot today!")
    elif temp in range(33, 43) :
        print("Welcome to Hell, dear!")

main()

# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

def main() :
    month = int(input("What is the number of the current month?\n"))
    if month == 12 :
        season = "winter"
    elif month in range (1,3) :
        season = "winter"
    elif month in range (3,6) :
        season = "spring"
    elif month in range (6,9) :
        season = "summer"
    elif month in range (9,12) :
        season = "autumn"
    temp = get_random_temp(season)
    print(f"It's {season}! The temperature right now is {temp} degrees Celsius.")
    temp = int(temp)
    if temp < 0 :
        print("Brrr, that's freezing! Wear some extra layers today!")
    elif temp in range(0, 16) :
        print("Quite chilly! Don't forget your coat!")
    elif temp in range(16, 24) :
        print("Just perfect!")
    elif temp in range(24, 33) :
        print("Pretty hot today!")
    elif temp in range(33, 43) :
        print("Welcome to Hell, dear!")

main()

# Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# There is an array of dictionaries, containing those questions and answers

data = [
     {
         "question": "What is Baby Yoda's real name?",
         "answer": "Grogu"
     },
     {
         "question": "Where did Obi-Wan take Luke after his birth?",
         "answer": "Tatooine"
     },
     {
         "question": "What year did the first Star Wars movie come out?",
         "answer": "1977"
     },
     {
         "question": "Who built C-3PO?",
         "answer": "Anakin Skywalker"
     },
     {
         "question": "Anakin Skywalker grew up to be who?",
         "answer": "Darth Vader"
     },
     {
         "question": "What species is Chewbacca?",
         "answer": "Wookiee"
     }
]

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers

#Solution EX 8:

def quizzer() :
    correct = 0
    incorrect = 0
    quest_dic = dict()
    incorrect_list = []
    print("Welcome to our Star Wars quiz! \n")
    for index in range(0,6) :
        quest_dic = data[index]
        print(quest_dic["question"])
        user_answer = input("Your answer is: ")
        user_answer = user_answer.title()
        if user_answer == quest_dic["answer"] :
            correct += 1
        else :
            incorrect +=1
            incorrect_list.append(user_answer)
            quest_dic["user answer"] = user_answer
            data[index] = quest_dic
    return (correct, incorrect)

# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

def results() :
    correct_num, incorrect_num = quizzer()
    print(f"\nYou gave {correct_num} correct answers and {incorrect_num} wrong answers!\n")
    for index in range(0,6) :
        quest_dic = data[index]
        if "user answer" in quest_dic :
            print(f"For this question: '{quest_dic['question']}' the correct answer was '{quest_dic['answer']}', and your answer was '{quest_dic['user answer']}'. \n")
    if incorrect_num >= 3 :
        print("Please, take the quiz again!")
results()       




