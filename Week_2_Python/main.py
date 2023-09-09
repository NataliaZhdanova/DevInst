def longest_word() :
    sentence = input("Provide a sentence to find the longest word in it: \n")
    sentence_to_list = sentence.split(" ")
    longest_word = max(sentence_to_list, key = len)
    print(f"The longest word is: '{longest_word}'")

longest_word()