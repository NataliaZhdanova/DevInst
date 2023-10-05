# What You Will Create
# Use python to create a Hangman game.
# The 'print_hangman' function draws the "hangman" figure accordint to the number of wrong attempts.

def print_hangman(wrong_attempts) :
    matrix = [
        (" ", "_", "_", "_", "_"),
        (" ", " ", "O", " ", "|"),
        (" ", " ", "O", "/", "|"),
        (" ", " ", "|", " ", "|"),
        (" ", "/", "|", " ", "|"),
        (" ", "/", "|", "\\", "|"),
        (" ", "/", " ", " ", "|"),
        (" ", "/", " ", "\\", "|")
    ]
    if wrong_attempts == 1:
        row_01 = "".join(matrix[0])
        row_02 = "".join(matrix[1])
        print(f"{row_01}\n {row_02}")
    elif wrong_attempts == 2 :
        row_01 = "".join(matrix[0])
        row_02 = "".join(matrix[1])
        row_03 = "".join(matrix[3])
        print(f"{row_01}\n {row_02}\n {row_03}")
    elif wrong_attempts == 3 :
        row_01 = "".join(matrix[0])
        row_02 = "".join(matrix[1])
        row_03 = "".join(matrix[4])
        print(f"{row_01}\n {row_02}\n {row_03}")
    elif wrong_attempts == 4 :
        row_01 = "".join(matrix[0])
        row_02 = "".join(matrix[1])
        row_03 = "".join(matrix[5])
        print(f"{row_01}\n {row_02}\n {row_03}")
    elif wrong_attempts == 5 :
        row_01 = "".join(matrix[0])
        row_02 = "".join(matrix[1])
        row_03 = "".join(matrix[5])
        row_04 = "".join(matrix[6])
        print(f"{row_01}\n {row_02}\n {row_03}\n {row_04}")
    elif wrong_attempts == 6 :
        row_01 = "".join(matrix[0])
        row_02 = "".join(matrix[1])
        row_03 = "".join(matrix[5])
        row_04 = "".join(matrix[7])
        print(f"{row_01}\n {row_02}\n {row_03}\n {row_04}")
    elif wrong_attempts == 7 :
        row_01 = "".join(matrix[0])
        row_02 = "".join(matrix[2])
        row_03 = "".join(matrix[5])
        row_04 = "".join(matrix[7])
        print(f"{row_01}\n {row_02}\n {row_03}\n {row_04}")
        print(f"Ooops, you lost the game!")


# The 'get_words_from_file' function extracts words from the specified file, puts them into the list, 
# then - creates another list containing only long enough words (to make the game more interesting), and finally, returns this list.

def get_words_from_file(file_name) :
    long_words = []
    with open(file_name, "r") as file :
        words_list = file.read().split()
        for item in words_list :
            if len(item) >= 7 :
                long_words.append(item)

    return long_words

# The 'get_random_word' function:
# 1. Generates a random number to use it as an index of the "long_words" list
# 2. Gets a word with this random index from the list 
# 3. Changes the word to the lower case
# 4. Creates a dictionary, where keys are indexes of chars in the word, and values - are chars themselves
# 5. Returns the dictionary

def get_random_word(long_words) :
    import random
    random_index = random.randint(0, len(long_words))
    random_word = long_words[random_index]
    nc_word = random_word.lower()
    word_dict = dict()
    for index in range(0, len(nc_word)):
        word_dict[index] = nc_word[index]
    return word_dict


# The 'play' function:
# 1. Generates a random number to use it as an index of the "long_words" list
# 2. Gets a word with this random index from the list 
# 3. Changes the word to the lower case
# 4. Creates a dictionary, where keys are indexes of chars in the word, and values - are chars themselves

def play(word_dict) :

# 1. Creates a counter of wrong attempts
      wrong_attempts = 0

# 2. Creates a copy of the word dictionary to use for guesses
      guess_dict = word_dict.copy()

# 3. In this new dictionary, changes all values to "*" 
      for key in guess_dict.keys() :
            guess_dict[key] = "*"

# 4. Creates two lists from values of both dictionaries - to get independent access to those values 
      star_list = list(guess_dict.values())
      char_list = list(word_dict.values())
      print(f"The word to guess is: {''.join(star_list)}")   

# 5. Creates a 'while' loop with two conditions, where both of them must be True for the loop to continue working 
# The loop stops working either when the user makes a 7th unsuccessful guess attempt,   
# or when the "guessed word" string becomes the same as the "initial word" string
      
      while (''.join(star_list) != ''.join(char_list)) and (wrong_attempts < 7):
            user_char = input("Guess a letter: ")

# 6. Creates an 'if' loop to check if the provided char is in the word
            if user_char in char_list:

# 7. Creates a list of indexes for char occurrences in the word
                  indexes = []
                  for index in range(0, len(char_list)):
                        if user_char == char_list[index]:
                              indexes.append(index)

# 8. Uses the list of indexes to update the "guesses" dictionary and the "guesses" list of values
                  for item in indexes:
                        guess_dict[item] = word_dict[item]
                        star_list[item] = word_dict[item]

# 9. Prints the string with guessed chars                  
                  print("".join(list(guess_dict.values())))
            
# 10. If the provided char is not in the word, increments the value of the 'wrong_attempts' counter and prints the corresponding hangman state       
            else :
                  wrong_attempts +=1
                  print_hangman(wrong_attempts)

# 11. Outputs the word that the user needed to guess      
      print(f"The word was: {''.join(char_list)}")

# The 'game" function provides a file with words and arranges all other functions for gaming
def game() :
    file_name = 'words.txt'    
    play(get_random_word(get_words_from_file(file_name)))

game()
        

# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.
