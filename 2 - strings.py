text_1 = "Hello, my name is \"Mousaab Labrassi\"" # string (str)

# Strings Methods
print(text_1.upper()) # convert all characters to uppercase
print(text_1.lower()) # convert all characters to lowercase
print(text_1.capitalize()) # convert the first character to uppercase
print(text_1.title()) # convert the first character of each word to uppercase
print(text_1.swapcase()) # convert uppercase to lowercase and vice versa
print("mousaab".islower()) # check if all characters are lowercase
print("MOUSAAB".isupper()) # check if all characters are uppercase
print("Mousaab".istitle()) # check if the first character is uppercase
print(len(text_1)) # get the length of the string
print(text_1[0]) # get the first character
print(text_1[-1]) # get the last character
print(text_1.index("M")) # get the index of the first occurrence of the character
print(text_1.replace("Mousaab", "Moussaab")) # replace the first string with the second string