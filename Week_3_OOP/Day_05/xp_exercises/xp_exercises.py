# Create a new file called anagram_checker.py which contains a class called AnagramChecker.

# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

# Note: None of the methods in the class should print anything.



class AnagramChecker :
    def __init__(self, word_list_file) :
        self.valid_words = set()
        with open(word_list_file, "r") as file :
            for line in file:
                self.valid_words.add(line.strip().lower())

    def is_valid_word(self, word) :
        return word.lower() in self.valid_words

    @staticmethod
    def is_anagram(word_1, word_2) :
        return sorted(word_1.lower()) == sorted(word_2.lower())

    def get_anagrams(self, word) :
        word = word.lower() 
        anagrams = [item for item in self.valid_words if self.is_anagram(word, item) and word != item]
        return anagrams


