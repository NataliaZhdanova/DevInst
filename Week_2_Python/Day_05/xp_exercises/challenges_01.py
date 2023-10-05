# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

def insert_item(string, item, index) :
      list = string.split(", ")
      list.insert(index, item)
      new_string = ", ".join(list)
      print(new_string)

string = input("Provide a list of items using a comma as a delimiter: ")
item = input("Provide an item you want to insert into this list: ")
index = int(input("Provide a number for a position of this new item in the list: "))
insert_item(string, item, index)

# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

def count_spaces(string) :
      spaces = string.count(" ")
      print(f"There are {spaces} spaces in this string.")

string = input("Provide a string: ")
count_spaces(string)

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

def calculate(string) :
      number_upper = 0
      number_lower = 0
      for char in string :
            if char.isupper() == True :
                  number_upper += 1
            elif char.islower() == True :
                  number_lower +=1
      print(f"The number of upper-case characters is: {number_upper}")
      print(f"The number of lower-case characters is: {number_lower}")

string = input("Provide a string: ")
calculate(string)

# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

#     >>>my_sum([1,5,4,2])
#     >>>12

def my_sum(string) :
      list = string.split(", ")
      sum = 0
      for item in list:
            sum += int(item)
      print(f"The sum of the provided numbers is: {sum}")

string = input("Provide a list of numbers using a comma as a delimiter: ")
my_sum(string)

# Exercise 5
# Instructions
# Write a function to find the max number in a list

#     >>>find_max([0,1,3,50])
#     >>>50

def find_max(string) :
    list = string.split(", ")
    list.sort()
    max = list[-1]
    print(f"The max number is: {max}")

string = input("Provide a list of numbers using a comma as a delimiter: ")
find_max(string)

# Exercise 6
# Instructions
# Write a function that returns factorial of a number

#     >>>factorial(4)
#     >>>24

def factorial(number) :
      result = 1
      for mult in range(1, number + 1) :
            result = result * mult
      print(f"The factorial of the number {number} is {result}")

number = int(input("Provide a number to calculate its factorial: "))
factorial(number)            

# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

#     >>>list_count(['a','a','t','o'],'a')
#     >>>2

def list_count(list, element) :
      counter = 0
      for index in range(0, len(list)) :
            if list[index] == element :
                  counter += 1
      print(f"The element appears {counter} times in the list.")

list_count(['a','a','t','o'],'a')

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>norm([1,2,2])
#     >>>3

def norm(list) :
      import math
      sum = 0
      for element in list:
            sum += element * element
      
      print(f"L2-norm of the list = {round(math.sqrt(sum), 2)}")

norm([1,2,2,6])

# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

#     >>>is_mono([7,6,5,5,2,0])
#     >>>True

#     >>>is_mono([2,3,3,3])
#     >>>True

#     >>>is_mono([1,2,0,4])
#     >>>False

def is_mono(list) :
      check_list = []
      for index in range(0, len(list) - 1) :
            if list[0] < list[-1] :
                  if list[index + 1] >= list[index] :
                        check_list.append("True")
                  else: 
                        check_list.append("False")
            elif list[0] > list[-1] :
                  if list[index + 1] <= list[index] :
                        check_list.append("True")
                  else :
                        check_list.append("False")
      
      if 'False' in check_list :
            print("False")
      else: 
            print("True")

is_mono([7,6,5,5,2,0])
is_mono([2,3,3,3])
is_mono([1,2,0,4])

# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

def longest(list) :
      length_dict = dict()
      for index in range(0, len(list)) :
            length_dict[len(list[index])] = index
      
      max_key = max(length_dict.keys())
      
      longest_word_index = length_dict[max_key]
      print(f"The longest word is '{list[longest_word_index]}'.")

list = ['Mary', 'loves', 'communism', 'and', 'owns', 'a', 'little', 'lamb.']
longest(list)


# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def separator(list) :
      int_list = []
      str_list = []
      for index in range(0, len(list)) :
            if type(list[index]) == int :
                  int_list.append(list[index])
            else :
                  str_list.append(list[index])

      print(int_list)
      print(str_list)

list = ['Mary', 11, 'loves', 'communism', 36, 'and', 1, 'owns', 'a', 'little', 192, 'lamb.']
separator(list)


# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

#     >>>is_palindrome('radar')
#     >>>True

#     >>>is_palindrome('John)
#     >>>False

def is_palindrome(string) :
      rev_string = string[::-1]
      if rev_string == string :
            print("True")
      else :
            print("False")

is_palindrome('radar')
is_palindrome('John')

# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3

def sum_over_k(sentence, k) :
      sentence_list = sentence.split(" ")
      word_list = []
      for element in sentence_list :
            if len(element) > k :
                  word_list.append(element)
      
      print(len(word_list))

sentence = 'Do or do not there is no try'
k=2
sum_over_k(sentence,k)


# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3

def dict_avg(dictionary) :
      sum_values = sum(dictionary.values())
      average = sum_values / len(dictionary.values())
      print(f"The average value in a dictionary is: {round(average, 2)}")

dict_avg({'a': 1,'b':2,'c':8,'d': 1})


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

#     >>>common_div(10,20)
#     >>>[2,5,10]

def common_div(num_01, num_02) :
      div_list = []
      for number in range(1, min(num_01, num_02) + 1) :
            if num_01 % number == num_02 % number == 0 :
                  div_list.append(number)

      print(div_list)

common_div(10,20)

# Exercise 16
# Instructions
# Write a function that test if a number is prime:

#     >>>is_prime(11)
#     >>>True

def is_prime(number) :
      div_list = []
      for item in range(1, number + 1) :
            if number % item == 0 :
                  div_list.append(number)

      if len(div_list) == 2:
            print("The number is prime!")
      else :
            print("The number is not prime!")

is_prime(11)
is_prime(5)
is_prime(22)
is_prime(1989)


# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]

def weird_print(string) :
      list = string.split(", ")
      final_list = []
      for index in range (0, len(list), 2) :
            if int(list[index]) % 2 == 0 :
                  final_list.append(list[index])
      
      print(f"The initial list: {list}")
      print(f"The list of even values with even indexes: {final_list}")

string = input("Provide a list of numbers using a comma as a delimiter: ")
weird_print(string)

# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2

def type_count(**kwargs) :
      int_num = 0
      str_val = 0
      float_num = 0
      bool_val = 0
      for value in kwargs.values() :
            if type(value) == int :
                  int_num += 1
            elif type(value) == float :
                  float_num += 1
            elif type(value) == bool :
                  bool_val += 1
            elif type(value) == str :
                  str_val += 1
      
      print(f"The following types were used: int - {int_num} times, str - {str_val} times, float - {float_num} times, and bool - {bool_val} times.")  

type_count(a = 1, b = 'string', c = 1.0, d = True, e = False,  f = "another string", g = 22, h = True)


# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def split_func(string, split_char) :
      split_dict = dict()
      split_list = []
      index_list = []
      key = 0
      start = 0
      for element in string :
            split_dict[key] = element
            key += 1

      for index in range(0, len(string)) :
            if split_dict[index] == split_char :
                  index_list.append(index)

      print(index_list)

      for index_num in index_list :
            split_list.append(string[start:index_num])
            start = index_num +1
            if index_num == index_list[-1]:
                  split_list.append(string[(index_num + 1):])

      print(split_list)

string = "Mary has a little lamb, white and fluffy, looking like a cloud."
split_char = " "
split_func(string, split_char)


# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"

def into_pass(string) :
      num = len(string)
      print("Your password is: " + "*" * num)

string = input("Enter a password: ")
into_pass(string)