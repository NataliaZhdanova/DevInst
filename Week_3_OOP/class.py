def char_in_string(char, string) :
    number = string.count(char)
    print(number)

string = input("Provide a string: ")
char = input("Enter a character to count in this string: ")
char_in_string(char, string)