# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.


from xp_exercises import AnagramChecker

def validate_word(word) :
    return word.isalpha() and len(word) > 0

def main() :
    print("Anagram Checker")
    anagram_checker = AnagramChecker("C:/Users/User/OneDrive/Documents/DevInst/Week_3_OOP/Day_05/xp_exercises/words.txt")

    while True :
        print("\nMenu:")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1" :
            my_word = input("Enter a word: ").strip()

            if validate_word(my_word) :
                anagrams = anagram_checker.get_anagrams(my_word)
                print("\nYOUR WORD:", f'"{my_word.upper()}"')
                print("This is a valid English word.")
                print("Anagrams for the word:", ", ".join(anagrams))
            else:
                print("\nError: Please enter a valid word with only letters.")
        elif choice == "2" :
            print("See you later, mate!")
            break
        else:
            print("Please select 1 or 2.")

if __name__ == "__main__" :
    main()



#     def get_anagrams(self, word) :
#         word = word.lower() 
#         anagrams = [item for item in self.valid_words if self.is_anagram(word, item) and word != item]
#         return anagrams


# anagram_checker = AnagramChecker("words.txt") 

# my_word = "meat"
# if anagram_checker.is_valid_word(my_word):
#     anagrams = anagram_checker.get_anagrams(my_word)
#     print(f"Anagrams for '{my_word}': {anagrams}")
# else:
#     print(f"'{my_word}' is not a valid word.")
