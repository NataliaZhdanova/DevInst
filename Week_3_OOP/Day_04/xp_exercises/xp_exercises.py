# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# Download the word list
# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

import random

def get_words_from_file(file_name) :
    with open(file_name, "r") as file :
        words_list = file.read().split()
    return words_list

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
# Take the random words and create a sentence (using a python method), the sentence should be lower case.


def get_random_sentence(words_list, length) :
    if length < 2 or length > 20 :
        raise ValueError("Sentence length should be between 2 and 20 words.")
    
    random_words = random.sample(words_list, length)
    random_sentence = " ".join(random_words).lower()
    return random_sentence

# Create a function called main which will:
# Print a message explaining what the program does.
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

def main() :
    print("This is a random sentence generator!")
    try :
        length = int(input("Provide the sentence length (2-20 words): "))
#        length = 30
        if 2 <= length <= 20 :
            words_list = get_words_from_file("C:/Users/User/OneDrive/Documents/DevInst/Week_3_OOP/Day_04/xp_exercises/words.txt")      
            sentence = get_random_sentence(words_list, length)
            print(f"Random sentence: {sentence}.")
        else :
            print("Sentence length should be between 2 and 20 words.")
    except ValueError :
        print("Please, enter a valid number between 2 and 20.")

if __name__ == "__main__" :
    main()



# Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data_dict = json.loads(sampleJson)

salary = data_dict["company"]["employee"]["payable"]["salary"]

data_dict["company"]["employee"]["birth_date"] = "1979-11-11"


with open("changed_data.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Salary:", salary)
print("Changed JSON Data:")
print(json.dumps(data_dict, indent=4))

# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
