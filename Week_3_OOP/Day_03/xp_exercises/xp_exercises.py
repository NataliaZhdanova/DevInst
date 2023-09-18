# Exercise 1: Currencies
# Instructions
class Currency:
    def __init__(self, currency, amount) :
        self.currency = currency
        self.amount = amount

    def __str__(self) :
        return f"{self.amount} {self.currency}s"
    
    def __int__(self) :
        return self.amount

    def __repr__(self) :
        return f"{self.amount} {self.currency}s"

    def __add__(self, other_money) : # It returns a new object as the result of the addition operation.
        if isinstance(other_money, Currency) and self.currency == other_money.currency:
            return Currency(self.currency, self.amount + other_money.amount)
        elif isinstance(other_money, (int, float)) :
            return Currency(self.currency, self.amount + other_money)
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other_money.currency}>")

    def __iadd__(self, other) : # It modifies the original object in place to represent the result of the addition operation.
        if isinstance(other, (int, float)) :
            self.amount += other
            return self
        elif isinstance(other, Currency) and self.currency == other.currency :
            self.amount += other.amount
            return self
        else:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")


# Example usage
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)
int(c1)
repr(c1)

c1 + 5
c1 + c2

c1

c1 += 5
c1

c1 += c2
c1

c1 + c3


# Exercise 2: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

from funcy import func
print(func(2, 3))

# OR 
# from module_name import function_name as fn 
# OR
# import module_name as mn


# Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import random
import string

str_rand = str()
str_rand = "".join(random.choices(string.ascii_letters, k=5))
print(str_rand)



# Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

from datetime import date

def cur_date() :
    today = date.today()
    return today

print(cur_date())

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).


from datetime import datetime

def time_left_jan() :
    current_date = datetime.now()

    next_year = current_date.year + 1
    target_date = datetime(next_year, 1, 1)

    time_delta = target_date - current_date

    # Extract days, hours, minutes, and seconds
    days = time_delta.days
    seconds = time_delta.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_remaining = f"{days} days, {hours}:{minutes}:{seconds} hours"

    return time_remaining

# Display the result
print("Time remaining until January 1st of 2024:", time_left_jan())


# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

from datetime import datetime

def total_min_lived(birthdate) :
    birthdate_date = datetime.strptime(birthdate, "%d/%m/%Y")
    current_date = datetime.now()

    time_difference = current_date - birthdate_date

    minutes_lived = int(time_difference.total_seconds() / 60)

    return f"You have lived for {minutes_lived} minutes."


birthdate = "21/06/1979" 
info = total_min_lived(birthdate)
print(info)


# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, language_code. Use faker to populate them with fake data.

from faker import Faker

fake = Faker()
users_list = []

def add_user() :
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code()
    }
    users_list.append(user)


add_user()
add_user()
add_user()

for user in users_list:
    print(user)
