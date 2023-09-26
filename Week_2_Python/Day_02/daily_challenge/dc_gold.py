# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !

from datetime import date

birth_date = input("What is your birth date (YYYY-MM-DD)? ")

birth = date.fromisoformat(birth_date)
today = date.today()
delta = today - birth
years = delta.days // 365
years_str = str(years)
year_last_num = int(years_str[-1])
if years == 53 :
    candles = "i" * (year_last_num + 3)
else: 
    candles = "i" * year_last_num 

print(f'''
       ___{candles}___
      |{" "*((year_last_num // 2) - 3)}:H:a:p:p:y:{" "*((year_last_num // 2) - 2)}|
    __|____{"_"*(year_last_num - 3)}______|__
   |^^^^^^^^{"^"*(year_last_num - 3)}^^^^^^^^|
   |{" "*((year_last_num // 2) - 3)}:B:i:r:t:h:d:a:y:{" "*((year_last_num // 2) - 2)}|
   |       {" "*(year_last_num - 3)}         |
   ~~~~~~~{"~"*(year_last_num - 3)}~~~~~~~~~~~    
      
    ''')

if birth.year % 4 == 0 :
    print(f'''
        ___{"i"*int(years_str[-1])}___
        |{" "*((int(years_str[-1]) // 2) - 3)}:H:a:p:p:y:{" "*((int(years_str[-1]) // 2) - 2)}|
        __|____{"_"*(int(years_str[-1]) - 3)}______|__
    |^^^^^^^^{"^"*(int(years_str[-1]) - 3)}^^^^^^^^|
    |{" "*((int(years_str[-1]) // 2) - 3)}:B:i:r:t:h:d:a:y:{" "*((int(years_str[-1]) // 2) - 2)}|
    |       {" "*(int(years_str[-1]) - 3)}         |
    ~~~~~~~{"~"*(int(years_str[-1]) - 3)}~~~~~~~~~~~    
        
        ''')