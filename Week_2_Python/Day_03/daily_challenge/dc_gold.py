# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

# user_input = input("Enter a text to encode or decode: ")
# to_do = input("Do you want to encode or decode it? Type 'encode' or 'decode'... ")
# shift = int(input("Specify a shift (a positive number): "))

def encode(user_input) :
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text_list = user_input.split(" ")
    encoded_list = []
    #print(text_list)
    for item in text_list :
        word = str()
        for index in range(0, len(item)) :
            if item[index] in alpha_upper :
                char_index = alpha_upper.index(item[index])
                if char_index + shift < len(alpha_upper):
                    new_char = alpha_upper[char_index + shift]
                else: 
                    new_char = alpha_upper[char_index + shift - len(alpha_upper)]
                word += new_char
            elif item[index] in alpha_lower :
                char_index = alpha_lower.index(item[index])
                if char_index + shift < len(alpha_lower):
                    new_char = alpha_lower[char_index + shift]
                else: 
                    new_char = alpha_lower[char_index + shift - len(alpha_lower)]
                word += new_char
            else :
                word += item[index]
        encoded_list.append(word)
    encoded_text = " ".join(encoded_list)
    print(f"Your encoded text is: '{encoded_text}'")

def decode(user_input) :
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text_list = user_input.split(" ")
    decoded_list = []
    #print(text_list)
    for item in text_list :
        word = str()
        for index in range(0, len(item)) :
            if item[index] in alpha_upper :
                char_index = alpha_upper.index(item[index])
                if char_index - shift >= 0:
                    new_char = alpha_upper[char_index - shift]
                else: 
                    new_char = alpha_upper[char_index - shift + len(alpha_upper)]
                word += new_char
            elif item[index] in alpha_lower :
                char_index = alpha_lower.index(item[index])
                if char_index - shift >= 0:
                    new_char = alpha_lower[char_index - shift]
                else: 
                    new_char = alpha_lower[char_index - shift + len(alpha_lower)]
                word += new_char
            else :
                word += item[index]
        decoded_list.append(word)
    decoded_text = " ".join(decoded_list)
    print(f"Your decoded text is: '{decoded_text}'")

user_input = input("Enter a text to encode or decode: \n")
to_do = input("Do you want to encode or decode it? Type 'encode' or 'decode': \n")
shift = int(input("Specify a shift (a positive number): \n"))

if to_do == "encode" :
    encode(user_input)
elif to_do == "decode":
    decode(user_input)


# shift = 6
# user_input = "Mary has a little lamb, white and fluffy, looking like a cloud of fur!"
# user_input = "Sgxe ngy g rozzrk rgsh, cnozk gtj lralle, ruuqotm roqk g iruaj ul lax!"
# decode(user_input)