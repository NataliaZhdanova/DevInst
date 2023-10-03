# Exercise 1 : What’s Your Name ?
# Instructions
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

def get_full_name(first_name, last_name, middle_name='') :
    if middle_name == '':
        print(f"{first_name.capitalize()} {last_name.capitalize()}")
    else :
        print(f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}")

first_name = input("Provide the first name: ")
middle_name = input("Provide the middle name (or press enter if there is no middle name): ")
last_name = input("Provide the last name: ")

get_full_name(first_name, last_name, middle_name)


# Exercise 2 : From English To Morse
# Instructions
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.

eng_morse_dict = {
    "A" : "._",
    "B" : "_...",
    "C" : "_._.",
    "D" : "_..",
    "E" : ".",
    "F" : ".._.",
    "G" : "__.",
    "H" : "....",
    "I" : "..",
    "J" : ".___",
    "K" : "_._",
    "L" : "._..",
    "M" : "__",
    "N" : "_.",
    "O" : "___",
    "P" : ".__.",
    "Q" : "__._",
    "R" : "._.",
    "S" : "...",
    "T" : "_",
    "U" : ".._",
    "V" : "..._",
    "W" : ".__",
    "X" : "_.._",
    "Y" : "_.__",
    "Z" : "__..",
    "." : "._._._",
    "," : "__..__",
    "?" : "..__.."
}

def text_to_morse() :
    text = input("Provide a text to convert into the morse sequence: ")
#   text = "Mary has a little lamb. It is white and fluffy."
    all_cap = text.upper()
    word_list = all_cap.split(" ")
    morse_list = []
    for item in word_list :
        morse_word = str()
        for index in range(0,len(item)) :
            morse_word += eng_morse_dict[item[index]] + " "
        morse_list.append(morse_word)
        
    print("/ ".join(morse_list))

def morse_to_text() :
  morse = input("Provide a morse sequence to convert into the text: ")
  morse_eng_dict = {}
  for key,value in eng_morse_dict.items() :
          morse_eng_dict[value] = key
# morse = ".. / ._.. ___ ..._ . / __ _.__ / ... .__ . . _ / _.. ___ __. / ... .__. ___ _ ._._._"
  morse_list = morse.split(" / ")
  word_list = []
  for item in morse_list :
      item_letters_list = item.split(" ")
      eng_word = str()
      for index in range(0, len(item_letters_list)) :
          eng_word += morse_eng_dict[item_letters_list[index]]
      word_list.append(eng_word)
  sentence = " ".join(word_list)
  all_normal = sentence.lower()
  print(all_normal.capitalize())

conversion = input("What would you like to do - convert text to morse (1) or morse to text (2): ")
if conversion == "1" :
    text_to_morse()
else: 
    morse_to_text()

# Exercise 3 : Box Of Stars
# Instructions
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

def box_printer(*args) :
    print("******************")
    for index in range(len(args)) :
        print(f"* {args[index]}{' ' * (15 - len(args[index]))}*")
    print("******************")

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

# Exercise 4
# Analyse this code before executing it. What is the purpose of this code? - sorting a list in the ascending order
def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)