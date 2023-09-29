# Write a program to reverse the sentence wordwise.

sentence = input("Provide a sentence: ")
#sentence = "You have entered a wrong domain"
word_list = sentence.split(" ")
word_list_reversed = word_list[::-1]
reversed_sentence = " ".join(word_list_reversed)
print(f"Reversed sentence is: '{reversed_sentence}'.")