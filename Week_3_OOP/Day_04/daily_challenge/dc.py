# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.



# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.

class Text :
    def __init__(self, text) :
        self.text = text

    def word_frequency(self, word) :
        words_list = self.text.split()
        frequency = words_list.count(word)
        return frequency

    def most_common_word(self) :
        words_list = self.text.split()

        if not words_list :
            return "Text is empty."

        word_counts_dict = {}
        for item in words_list :
            word_counts_dict[item] = word_counts_dict.get(item, 0) + 1

        most_common = max(word_counts_dict, key=word_counts_dict.get)
        return most_common

    def unique_words(self) :
        words_list = self.text.split()
        unique_words = set(words_list)
        return list(unique_words)
    
    @classmethod
    def from_file(cls, filename) :
        with open(filename, "r") as file:
            file_text = file.read()
        return cls(file_text)

# text = "A good book would sometimes cost as much as a good house."
# text_analyzer = Text(text)


# word_freq = "good"
# frequency = text_analyzer.word_frequency(word_freq)
# print(f"The word '{word_freq}' appears {frequency} times in the text.")

# common_word = text_analyzer.most_common_word()
# print(f"The most common word in the text is '{common_word}'.")

# unique_words_list = text_analyzer.unique_words()
# print("Unique words in the text are:", unique_words_list)



# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
# Implement a classmethod that returns a Text instance but with a text file:
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
# Now, use the provided the_stranger.txt file and try using the class you created above.

# text_inst = Text.from_file("C:/Users/User/OneDrive/Documents/DevInst/Week_3_OOP/Day_04/daily_challenge/the_stranger.txt")
# common_word = text_inst.most_common_word()
# print(f"The most common word in the text is '{common_word}'.")

# unique_words_list = text_inst.unique_words()
# print("Unique words in the text are:", unique_words_list)

# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.

import string
from nltk.corpus import stopwords
import re

class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punct(self):
        translator = str.maketrans('', '', string.punctuation)
        text_no_punct = self.text.translate(translator)
        return text_no_punct

    def remove_stopwords(self):
        import nltk
        nltk.download('stopwords')
        english_stopwords = set(stopwords.words("english"))     

        words_list = self.text.split()

        filtered_words = [word for word in words_list if word.lower() not in english_stopwords]

        text_no_stopwords = " ".join(filtered_words)
        return text_no_stopwords

    def remove_spec_char(self):
        text_no_spec_chars = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return text_no_spec_chars


text_mod = TextModification.from_file("C:/Users/User/OneDrive/Documents/DevInst/Week_3_OOP/Day_04/daily_challenge/the_stranger.txt")

# print("Text without punctuation:", text_mod.remove_punct())

print("Text without stopwords:", text_mod.remove_stopwords())

# print("Text without special characters:", text_mod.remove_spec_char())
