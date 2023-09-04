no_dup = list()
word_list = list()
new_word = str()
word = input("Provide a string of characters: \n")

for x in word :
    word_list.append(x)

no_dup = list(dict.fromkeys(word_list))

new_word = ("").join(no_dup)
print(new_word)


